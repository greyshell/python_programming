#!/usr/bin/env python3

# author: greyshell

from mysql_db import MySQLdb


class TblPost01:
    def __init__(self):
        self.db = MySQLdb()

    def unsafe_select_query(self, user):
        # creating the cursor
        cursor = self.db.conn.cursor()
        rows = None
        try:
            query = f"SELECT comment, user FROM tbl_post01 WHERE user = '{user}'"
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return True, rows

        except Exception as e:
            cursor.close()
            self.db.conn.close()
            return False, e

    def safe_select_query(self, user):
        # creating the cursor
        cursor = self.db.conn.cursor()
        rows = None
        try:
            user_input = (user,)  # pass the input in the form of a tuple
            query = "SELECT comment, user FROM tbl_post01 WHERE user = %s"
            cursor.execute(query, user_input)
            rows = cursor.fetchall()
            cursor.close()
            return True, rows

        except Exception as e:
            print(e)
            cursor.close()
            self.db.conn.close()
            return False, e
