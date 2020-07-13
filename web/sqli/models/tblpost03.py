#!/usr/bin/env python3

# author: greyshell

from mysql_db import MySQLdb


class TblPost03:
    def __init__(self):
        self.db = MySQLdb()

    def unsafe_insert_query(self, comment, city, age, user):
        # create the cursor
        cursor = self.db.conn.cursor()
        rows = None
        try:
            query = f"INSERT tbl_post03 (comment, city, age, user) VALUES ('{comment}', '{city}', {age}, '{user}')"
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
            query = "SELECT comment, city, age, user FROM tbl_post03 WHERE user LIKE 'anonymous%'"
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return True, rows

        except Exception as e:
            print(e)
            cursor.close()
            self.db.conn.close()
            return False, e
