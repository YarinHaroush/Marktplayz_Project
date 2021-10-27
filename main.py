from api import app
import uvicorn

from db_handler import init_games_table, init_players_table, init_watchers_table

if __name__ == "__main__":
    init_games_table()
    init_players_table()
    init_watchers_table()
    uvicorn.run(app, host="0.0.0.0", port=8080)
