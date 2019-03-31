#!/usr/bin/python

# author: greyshell
# description: setup database connection

import mysql.connector
from decouple import config


class ConnectMySQL:
    """ setup MySQL database connection """

    def create_connection(self):
        """
        create a database connection to the MySQL database
        :return: connection object or None
        """
        try:
            # pick database configurations from .env
            conn = mysql.connector.connect(user=config('mysql_user'),
                                           password=config('mysql_password'),
                                           host=config('mysql_host'),
                                           database=config('mysql_database'))
            return conn

        except mysql.connector.Error as err:
            print err
            return None

    def select_book_by_id(self, conn, book_id, fix):
        """
        SQLi in where clause: select a book by id
        :param conn: database connection object
        :param book_id: number, primary key
        :param fix: bool (True or False)
        :return: a two dimension list or None
        """
        # creating cursor
        cursor = conn.cursor()
        rows = None
        try:
            # branching the code based on the fix
            if fix is True:
                # white list validation: regex and length
                # use parametrised query
                # query = "SELECT * FROM auth_permission WHERE id = %s_list" % book_id
                temp_book_id = (book_id,)
                query = 'SELECT * FROM auth_permission WHERE id = ?' + temp_book_id
            else:
                # query = "SELECT * FROM auth_permission where id =" + str(book_id)
                query = "SELECT host FROM user where user = '" + str('offsec') + "'"

            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()

        # except mysql.connector.Error as err:
        #     print err
        except Exception as e:
            print e

        finally:
            # closing connection
            cursor.close()
            conn.close()
            return rows


def main():
    db_mysql = ConnectMySQL()
    db_conn = db_mysql.create_connection()
    # db_conn.close()

    if db_conn is None:
        msg = "error in connection"
        print msg
        exit(0)

    rows = db_mysql.select_book_by_id(db_conn, 1, fix=False)
    if rows is None:
        msg = "error in execution"
        print msg
        exit(0)

    # display the result
    for row in rows:
        print row

    print "[+] execution finished with graceful error handling .."

    # end of main()


if __name__ == "__main__":
    main()
    # end of main
