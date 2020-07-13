#!/usr/bin/env python3

# author: greyshell

from mysql_db import MySQLdb


class TblPost02:
    def __init__(self):
        self.db = MySQLdb()

    def unsafe_insert_query(self, comment, pin, age, user):
        # create the cursor
        cursor = self.db.conn.cursor()
        rows = None
        try:
            query = f"INSERT tbl_post02 (comment, pin, age, user) VALUES ('{comment}', {pin}, {age}, '{user}')"
            cursor.execute(query)
            self.db.conn.commit()
            cursor.close()

            if cursor.rowcount != 0:
                return True, cursor.rowcount
            return False, cursor.rowcount

        except Exception as e:
            cursor.close()
            self.db.conn.close()
            return False, e

    def safe_select_query(self):
        # create the cursor
        cursor = self.db.conn.cursor()
        rows = None
        try:
            query = "SELECT comment, pin, age, user FROM tbl_post02 WHERE user = 'anonymous'"
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return True, rows

        except Exception as e:
            print(e)
            cursor.close()
            self.db.conn.close()
            return False, e
