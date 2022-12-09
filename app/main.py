from fastapi import FastAPI
from app.repository.QueryRepositoy import QueryRepository

app = FastAPI()
repository = QueryRepository()


@app.get("/api/get_max_duration/{year}/{platform}/{measure}")
async def get_max_duration(year, platform, measure):
    result = repository.get_max_duration(year, platform, measure)
    if result is None:
        return "no hay resultados"
    return {"titulo": result[0]}


@app.get("/api/get_count_platform/{platform}/")
async def get_count_platform(platform):
    result = repository.get_count_platform(platform)
    if result is None:
        return "no hay resultados"
    return {"platform": result[0],
            "movie": result[1],
            "tvshow": result[2]}


@app.get("/api/get_listedin/{genre}/")
async def get_listedin(genre):
    result = repository.get_listedin(genre)
    if result is None:
        return "no hay resultados"
    return {"platform": result[0],
            "cantidad": result[1]}


@app.get("/api/get_actor/{platform}/{year}")
async def get_actor(platform, year):
    result = repository.get_actor(platform, year)
    if result is None:
        return "no hay resultados"
    return {"platform": result[0],
            "cantidad": result[1],
            "actores": result[2]}
