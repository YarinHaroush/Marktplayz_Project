import sqlite3

con = sqlite3.connect('server.db', check_same_thread=False)


def init_games_table():
    """
    Create Table of Games.
    :return: None
    """
    con.execute("CREATE TABLE games (id INTEGER PRIMARY KEY, Title VARCHAR(255), Platform VARCHAR(255))")
    con.execute("insert into games values (1, 'Fifa21', 'Sony')")
    con.execute("insert into games values (2, 'Fortnite', 'Xbox')")
    con.execute("insert into games values (3, 'GTA_San_Andreas', 'PC')")
    con.execute("insert into games values (4, 'Mortal_Combat', 'Sony')")
    con.execute("insert into games values (5, 'Maple_Story', 'PC')")
    con.execute("insert into games values (6, 'WWE', 'Sony')")
    con.commit()


def init_players_table():
    """
    Create Table of Players.
    :return: None
    """
    con.execute("CREATE TABLE players (id INTEGER, Games VARCHAR(255), Created_date Date)")
    con.execute("insert into players values (1, 'Fifa21', '2021-04-22 10:00:00')")
    con.execute("insert into players values (1, 'Fortnite', '2021-01-22 10:00:00')")
    con.execute("insert into players values (1, 'WWE', '2021-04-26 10:00:00')")
    con.execute("insert into players values (2, 'GTA_San_Andreas', '2016-07-12 10:00:00')")
    con.execute("insert into players values (2, 'Maple_Story', '2016-07-12 10:00:00')")
    con.execute("insert into players values (3, 'Mortal_Combat', '2012-03-09 10:00:00')")


def init_watchers_table():
    """
    Create Table of Watchers.
    :return: None
    """
    con.execute("CREATE TABLE watchers (id INTEGER, Name VARCHAR(255))")
    con.execute("insert into watchers values (1, 'Avi')")
    con.execute("insert into watchers values (1, 'Gil')")
    con.execute("insert into watchers values (2, 'Dolev')")
    con.execute("insert into watchers values (3, 'Rotem')")



def get_all_games():
    """
    Displays the entire table of games.
    :return: All the results that exist in the table.
    """
    query = con.execute("select * from games")
    results = query.fetchall()
    return results


def get_insert_game(title, platform):
    """
    Insert game using Title & Platform.
    :param title:
    :param platform:
    :return: None
    """
    con.execute(f"insert into games (Title, Platform) values ('{title}', '{platform}')")
    con.commit()
    return "Inserted successfully"


def get_delete_game(game_id):
    """
    Delete game using ID.
    :param game_id:
    :return: None
    """
    con.execute(f"delete from games where id = {game_id}")
    con.commit()
    return "Deleted successfully"


def get_update_game(game_id, title, platform):
    """
    Update game using ID & Title & Platform.
    :param game_id:
    :param title:
    :param platform:
    :return: None
    """
    con.execute(f"update games set (Title, Platform) = ('{title}', '{platform}') where id = {game_id}")
    con.commit()
    return "Updated successfully"


def get_all_player():
    """
    Displays the entire table of players.
    :return: All the results that exist in the table.
    """
    query_player = con.execute("select * from players")
    results_player = query_player.fetchall()
    return results_player


def get_insert_player(player_id, games, date):
    """
    Insert player using ID & Games & Created_date.
    :param player_id:
    :param games:
    :param date:
    :return: None
    """
    con.execute(f"insert into players (id ,Games, Created_date) values ('{player_id}', '{games}', '{date}')")
    con.commit()
    return "Inserted successfully"


def get_delete_player(player_id):
    """
    Delete player using ID.
    :param player_id: Player's ID
    :return: None
    """
    con.execute(f"delete from players where id = {player_id}")
    con.commit()
    return "Deleted successfully"


def get_update_player(player_id, games, date):
    """
    Update player using ID & Games & Created_date.
    :param player_id:
    :param games:
    :param date:
    :return: None
    """
    con.execute(f"update players set (Games, Created_date) = ('{games}', '{date}') where id = {player_id}")
    con.commit()
    return "Updated successfully"


def get_game_by_id(game_id):
    """
    Displays the entire table of game using ID.
    :param game_id:
    :return: All the results that exist in the table using ID.
    """
    query = con.execute(f"select * from games where id = {game_id}")
    results = query.fetchall()
    return results


def get_players_at_created_date(created_date):
    """
    Displays the player's ID by the date entered.
    :param created_date:
    :return: ID of the player according to the date entered.
    """
    query = con.execute(f"select ID from players where Created_date = '{created_date}'")
    con.commit()
    results = query.fetchall()
    return results


def get_all_watchers():
    """
    Displays the entire table of watchers.
    :return: All the results that exist in the table.
    """
    query = con.execute("select * from watchers")
    results = query.fetchall()
    return results


def get_watchers_handler(watcher_id):
    """
    Displays watcher names by ID.
    :param watcher_id:
    :return: all watcher names according Specific ID.
    """
    query = con.execute(f"select name from watchers where id = '{watcher_id}'")
    con.commit()
    results = query.fetchall()
    return results