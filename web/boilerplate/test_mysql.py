#!/usr/bin/env python3

# author: greyshell
# description: test mysql db connection
# note: start the mysql service -> service mysql start

from mysql_db import MySQLdb


class TestMySQL:
    """ setup MySQL database connection """

    def __init__(self):
        self.db = MySQLdb()

    def safe_select_all_query(self):
        """
        SELECT * FROM tbl_post01;
        :return:
        """
        # creating cursor
        cursor = self.db.conn.cursor()
        rows = None
        try:
            query = "SELECT * FROM tbl_post01"
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return True, rows

        except Exception as e:
            print(e)
            cursor.close()
            return False, e

    def unsafe_select_query(self, user):
        # create the cursor
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
            query = "SELECT comment, city, age, user FROM tbl_post03 WHERE user = %s"
            cursor.execute(query, user_input)
            rows = cursor.fetchall()
            cursor.close()
            return True, rows

        except Exception as e:
            print(e)
            cursor.close()
            self.db.conn.close()
            return False, e


def main():
    mysql = TestMySQL()

    # select all rows
    return_type, rows = mysql.safe_select_all_query()
    if len(rows) == 0:  # when no row is found it returns the empty list [] -> but empty list is not None
        print(f"[+] no row is found")
    else:
        # display the result
        for row in rows:
            print(row)  # rows -> list but row -> tuple

    # vulnerable for SQLi
    print("")
    return_type, rows = mysql.unsafe_select_query(user='jack')
    if len(rows) == 0:  # when no row is found it returns the empty list [] -> but empty list is not None
        print(f"[+] no row is found")
    else:
        # display the result
        for row in rows:
            print(row)

    # SQLi fix
    print("")
    return_type, rows = mysql.safe_select_query(user='admin')
    if len(rows) == 0:  # when no row is found it returns the empty list [] -> but empty list is not None
        print(f"[+] no row is found")
    else:
        # display the result
        for row in rows:
            print(row)

    # end of main()


if __name__ == "__main__":
    main()
    # end of main
