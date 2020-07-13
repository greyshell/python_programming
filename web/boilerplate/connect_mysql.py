#!/usr/bin/env python3

# author: greyshell
# description: setup mysql db connection
# note: start the mysql service -> service mysql start

import mysql.connector
import keyring


class ConnectMySQL:
    """ setup MySQL database connection """

    def __init__(self):
        self.conn = None

    def create_connection(self):
        """
        create a database connection for MySQL database
        :return: connection object or None
        """
        try:
            # pick database credentials from keyring
            self.conn = mysql.connector.connect(user=keyring.get_password('mysql', 'user'),
                                                password=keyring.get_password('mysql', 'password'),
                                                host='localhost',
                                                database='vulnapp')

        except mysql.connector.Error as err:
            print(err)
            exit(0)

        return self.conn

    def demo_select_all_statement(self):
        """
        SELECT * FROM tbl_post01;
        :return:
        """
        # creating cursor
        cursor = self.conn.cursor()
        rows = None
        try:
            query = "SELECT * FROM tbl_post01"
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()

        except Exception as e:
            print(e)
            cursor.close()
            self.conn.close()
            exit(0)

        return rows

    def demo_select_statement_bad_usage(self, user):
        """
        SELECT comment FROM tbl_post01 WHERE user = 'tom';
        :param user: string
        :return:
        """
        # creating cursor
        cursor = self.conn.cursor()
        rows = None
        try:
            query = "SELECT user_comment, user_name FROM tbl_post01 WHERE user_name = '" + str(user) + "'"
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()

        except Exception as e:
            print(e)
            cursor.close()
            self.conn.close()
            exit(0)

        return rows

    def demo_select_statement_good_usage(self, user):
        """
        SELECT comment FROM tbl_post01 WHERE user = 'tom';
        :param user: string
        :return:
        """
        # creating cursor
        cursor = self.conn.cursor()
        rows = None
        try:
            user_input = (user,)  # pass the input in the form of a tuple
            query = "SELECT user_comment, user_name FROM tbl_post01 WHERE user_name = %s"
            cursor.execute(query, user_input)
            rows = cursor.fetchall()
            cursor.close()

        except Exception as e:
            print(e)
            cursor.close()
            self.conn.close()
            exit(0)

        return rows


def main():
    db_mysql = ConnectMySQL()
    db_conn = db_mysql.create_connection()

    # select all rows
    rows = db_mysql.demo_select_all_statement()
    if len(rows) == 0:  # when no row is found it returns the empty list [] -> but empty list is not None
        print(f"[+] no row is found")
    else:
        # display the result
        for row in rows:
            print(row)  # rows -> list but row -> tuple

    # vulnerable for SQLi
    print("")
    rows = db_mysql.demo_select_statement_bad_usage(user='amit')
    if len(rows) == 0:  # when no row is found it returns the empty list [] -> but empty list is not None
        print(f"[+] no row is found")
    else:
        # display the result
        for row in rows:
            print(row)

    # SQLi fix
    print("")
    rows = db_mysql.demo_select_statement_good_usage(user='amit')
    if len(rows) == 0:  # when no row is found it returns the empty list [] -> but empty list is not None
        print(f"[+] no row is found")
    else:
        # display the result
        for row in rows:
            print(row)

    # # closing the database connection, preventing application dos attack
    db_conn.close()
    print("[+] finished execution..")

    # end of main()


if __name__ == "__main__":
    main()
    # end of main
