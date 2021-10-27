from fastapi import FastAPI

from db_handler import get_all_games, get_insert_game, get_update_game, get_delete_game, get_all_player,\
    get_insert_player, get_update_player, get_delete_player, get_players_at_created_date, get_all_watchers, get_watchers_handler

app = FastAPI()


@app.get("/")
def read_root_endpoint():
    return {"message": "Hello World"}


@app.get("/games")
def get_games_endpoint():
    return get_all_games()


@app.post("/games")
def add_game_endpoint(title: str, platform: str):
    return get_insert_game(title, platform)


@app.put("/games")
def update_game_endpoint(game_id: int, title: str, platform: str):
    return get_update_game(game_id, title, platform)


@app.delete("/games")
def delete_game_endpoint(game_id: int):
    return get_delete_game(game_id)


@app.get("/players")
def get_players_endpoint():
    return get_all_player()


@app.post("/players")
def add_players_endpoint(player_id: int, games: str, date: str):
    return get_insert_player(player_id, games, date)


@app.put("/players")
def update_players_endpoint(player_id: int, games: str, date: str):
    return get_update_player(player_id, games, date)


@app.delete("/players")
def delete_players_endpoint(player_id: int):
    return get_delete_player(player_id)


@app.get("/players/{created_date}")
def get_players_at_created_date_endpoint(created_date: str):
    return get_players_at_created_date(created_date)


@app.get("/watchers")
def get_watchers_endpoint():
    return get_all_watchers()


@app.get("/watchers/{watcher_id}")
def get_watchers_handler_endpoint(watcher_id: int):
    return get_watchers_handler(watcher_id)