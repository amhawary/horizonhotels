
import mysql.connector
from mysql.connector import errorcode



def get_connection():
    try:
        conn = mysql.connector.connect(host='localhost',                               
                              user='root',
                              password='password',
                              database='amin2alhawary_prj')
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('User name or Password is not working')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(err)                        
    else:
        return conn   