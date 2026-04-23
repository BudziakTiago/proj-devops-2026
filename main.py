from fastapi import FastAPI
import requests
import os

app = FastAPI()

animes = []

headers = {
    "Authorization": os.environ.get('MAL_AUTHORIZATION') 
}

params = {
    "fields": "anime_title, my_list_status",
    "offset": 0,
    "limit": 5
}

@app.get("/")
async def root():
    
    response = requests.get(
        "https://api.myanimelist.net/v2/users/@me/animelist",
        headers=headers,
        params=params
    )

    animeList = response.json()['data']

    for index, anime in enumerate(animeList):
        index += 2
        animeID = anime['node']['id']
        url = f"https://api.myanimelist.net/v2/anime/{animeID}"

        searchAnimeDetails = requests.get(
            url,
            headers={"X-MAL-CLIENT-ID": os.environ.get('MAL_CLIENT_ID')},
            params={"fields":"genres, alternative_titles"}
        )

        score = anime['node']['my_list_status']['score']
        status = anime['node']['my_list_status']['status']

        animeDetails = searchAnimeDetails.json()
        animeGenres = animeDetails['genres']

        title = animeDetails['alternative_titles']['en']

        line1 = f"Anime: {title} / Status: {status.capitalize()} / Score: {score}"
        line2 = ", ".join(genres['name'] for genres in animeGenres)

        lines = f"{line1} / Genres: {line2}"

        animes.append(lines)

    return animes
