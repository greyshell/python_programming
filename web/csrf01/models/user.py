from mysql_db import MySQLdb

import traceback


class User:

    def __init__(self, details):
        self.id = details[0]
        self.username = details[1]
        self.name = details[3]
        self.age = details[4]

    def save(self):
        db = MySQLdb()
        cursor = db.conn.cursor()
        rows = None
        try:
            user_input = (self.age, self.id)  # pass the input in the form of a tuple
            query = "UPDATE tbl_users SET age = %s WHERE id = %s"
            cursor.execute(query, user_input)
            db.conn.commit()
            cursor.close()
            if cursor.rowcount != 0:
                return True, cursor.rowcount
            return False, cursor.rowcount

        except Exception as e:
            print(e)
            traceback.print_exc()
            cursor.close()
            db.conn.close()
            return False, e

    @staticmethod
    def get_user(username, password):
        # creating the cursor
        db = MySQLdb()
        cursor = db.conn.cursor()
        rows = None
        try:
            user_input = (username, password)  # pass the input in the form of a tuple
            query = "SELECT * FROM tbl_users WHERE username = %s AND password = %s"
            cursor.execute(query, user_input)
            rows = cursor.fetchall()
            cursor.close()
            print(rows)
            return User(rows[0])

        except Exception as e:
            print(e)
            traceback.print_exc()
            cursor.close()
            db.conn.close()
            return None

    @staticmethod
    def logged_user(user_id):
        # creating the cursor
        db = MySQLdb()
        cursor = db.conn.cursor()
        rows = None
        try:
            user_input = (user_id,)  # pass the input in the form of a tuple
            query = "SELECT * FROM tbl_users WHERE id = %s"
            cursor.execute(query, user_input)
            rows = cursor.fetchall()
            cursor.close()
            print(rows)
            print(user_id)
            return User(rows[0])

        except Exception as e:
            print(e)
            traceback.print_exc()
            cursor.close()
            db.conn.close()
            return None
