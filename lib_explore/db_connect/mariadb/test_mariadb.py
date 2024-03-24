#!/usr/bin/env python3

# author: greyshell

import os
import json
import keyring
from core_concepts.db_connect.mariadb import CONSTANTS
import mariadb


def db_config():
    # if any of these fields are None then docker env is not set
    if (os.environ.get("MARIADB_USER") is None) or \
            (os.environ.get("MARIADB_ROOT_PASSWORD") is None) or \
            (os.environ.get("MARIADB_DATABASE") is None) or \
            (os.environ.get("MARIADB_PORT") is None) or \
            (os.environ.get("MARIADB_HOST") is None):
        print(f"Get the db config params from CONSTANT.py and keyring")
        # if credentials are not found in the env then pick up from keyring
        creds = json.loads(keyring.get_password(CONSTANTS.KEYRING_SERVICE_NAME, CONSTANTS.KEYRING_USERNAME))
        user = list(creds.keys())[0]
        password = list(creds.values())[0]

        return {'user': user,
                'password': password,
                'database': CONSTANTS.MARIADB_DB,
                'port': CONSTANTS.MARIADB_PORT,
                'host': CONSTANTS.MARIADB_HOST
                }

    print(f"Get the db config params from docker env")

    return {'user': os.environ.get("MARIADB_USER"),
            'password': os.environ.get("MARIADB_ROOT_PASSWORD"),
            'database': os.environ.get("MARIADB_DATABASE"),
            'port': int(os.environ.get("MARIADB_PORT")),
            'host': os.environ.get("MARIADB_HOST")
            }


def safe_exec(conn, user):
    cur = conn.cursor()

    try:
        params = (user,)  # pass the input in the form of a tuple
        query = "SELECT comment, user FROM tbl_post01 WHERE user = %s"

        cur.execute(query, params)
        rows = cur.fetchall()
        return rows

    except mariadb.Error as e:
        print(f"Error: {e}")

    finally:
        cur.close()


def unsafe_exec(conn, user):
    cur = conn.cursor()

    try:
        query = f"SELECT comment, user FROM tbl_post01 WHERE user = '{user}'"
        cur.execute(query)
        rows = cur.fetchall()
        return rows

    except mariadb.Error as e:
        print(f"Error: {e}")

    finally:
        cur.close()


if __name__ == '__main__':
    config = db_config()
    db_conn = mariadb.connect(**config)

    user_input = "tom"  # "O'a"

    print(f"Result from safe exec:")
    for row in safe_exec(db_conn, user_input):
        print(f"{row}")

    print(f"Result from unsafe exec:")
    for row in unsafe_exec(db_conn, user_input):
        print(f"{row}")

    db_conn.close()


