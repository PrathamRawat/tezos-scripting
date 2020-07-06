import sqlite3

DATABASE_PATH = "./node_database.db"
database = None
cursor = None


def setup_database():
    global database
    database = sqlite3.connect(DATABASE_PATH)  # opens existing file or it makes new one if it does not exit
    global cursor
    cursor = database.cursor()
    command = """CREATE TABLE IF NOT EXISTS 'nodes' (
        name INTEGER PRIMARY KEY,
        rpc_port INTEGER,
        exposition_port INTEGER,
        conseil_port INTEGER,
        arronax_port INTEGER,
        network VARCHAR,
        status VARCHAR 
        );"""
    cursor.execute(command)
    database.commit()


def get_all_nodes():
    command = """SELECT name FROM 'nodes';"""
    cursor.execute(command)
    return cursor.fetchall()


def result_to_dict(data):
    output = dict()
    output['name'] = data[0]
    output['rpc_port'] = data[1]
    output['exposition_port'] = data[2]
    output['conseil_port'] = data[3]
    output['arronax_port'] = data[4]
    output['network'] = data[5]
    output['status'] = data[6]
    return output


def get_node_data(name):
    command = """SELECT * FROM 'nodes' WHERE nodes.name="{}";""".format(name)
    cursor.execute(command)
    return result_to_dict(cursor.fetchone())


def add_node(data):
    command = """INSERT INTO 'users' VALUES ({}, {}, {}, {}, {}, "{}", "{}");""".format(
        data["name"],
        data["rpc_port"],
        data['exposition_port'],
        data["conseil_port"],
        data["arronax_port"],
        data["network"],
        data["status"]
    )
    cursor.execute(command)
    database.commit()


def update_status(name, status):
    command = """UPDATE nodes SET nodes.status={} WHERE nodes.name={};""".format(status, name)
    cursor.execute(command)
    database.commit()


def get_max_port():
    command = """SELECT MAX(arronax_port) FROM 'nodes';"""
    cursor.execute(command)
    if not cursor.fetchone()[0]:
        return 42069
    return cursor.fetchone()[0]
