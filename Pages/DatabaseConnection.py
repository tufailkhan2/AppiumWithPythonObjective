import pymysql
from basePackage.baseClass import BaseClass


class DatabaseConnection(BaseClass):
    def __init__(self):
        self.driver = BaseClass.get_driver()

    db_connection = pymysql.connect(
        host='mysql_host',
        user='mysql_user',
        password='mysql_password',
        database='mysql_database',
        port=3306  # Port needed for database
    )
    cursor = db_connection.cursor()

    table_query = '''
        Select * from Table_Name;
    '''
    cursor.execute(table_query)
    db_connection.commit()

    # Close the database connection when done
    cursor.close()
    db_connection.close()
