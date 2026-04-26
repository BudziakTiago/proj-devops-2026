from fastapi import FastAPI
import requests
import os

app = FastAPI()

headers = {
    "Authorization": os.environ.get('MAL_AUTHORIZATION') 
}

def getUserStatistics():
    userInformation = requests.get(
        "https://api.myanimelist.net/v2/users/@me",
        headers=headers,
        params={ "fields": "anime_statistics" }
    )

    userInfo = userInformation.json()['anime_statistics']

    return userInfo['num_items_watching']

def getUserAnimeList():
    response = requests.get(
        "https://api.myanimelist.net/v2/users/@me/animelist",
        headers=headers,
        params={ "status": "watching", "fields": "anime_title, my_list_status", "offset": 0, "limit": getUserStatistics() }
    )

    return response.json()['data']

def getAnimeDetails(url):
    searchAnimeDetails = requests.get(
        url,
        headers={"X-MAL-CLIENT-ID": os.environ.get('MAL_CLIENT_ID')},
        params={"fields":"genres, alternative_titles"}
    )

    return searchAnimeDetails.json()

@app.get("/")
async def root():
    animes = []
    animeList = getUserAnimeList()

    for index, anime in enumerate(animeList):
        animeID = anime['node']['id']
        score = anime['node']['my_list_status']['score']
        status = anime['node']['my_list_status']['status']

        url = f"https://api.myanimelist.net/v2/anime/{animeID}"
        animeDetails = getAnimeDetails(url)
        animeGenres = animeDetails['genres']

        title = f"Title JP (EN): {animeDetails['alternative_titles']['ja']} ({animeDetails['alternative_titles']['en']})"

        line1 = f"Anime: {title} / Status: {status.capitalize()} / Score: {score}"
        line2 = ", ".join(genres['name'] for genres in animeGenres)

        lines = f"{line1} / Genres: {line2}"

        animes.append(lines)

    return animes
