# db.py - Functions related to the database.

# Library Imports
import mysql.connector
from mysql.connector import errorcode


# Connect to our database
def db_connect(user, pwd, host, db):
    """Connects to a database

        Keyword Arguments:
        user -- username for the database
        pwd -- password for that username
        host -- hostname for the database
        db -- database to select
    """
    config = {
        'user': user,
        'password': pwd,
        'host': host,
        'database': db
    }
    try:
        db = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        return db


def get_user(db, username):
    """Grabs a user given a username

        Keyword Arguments:
        db -- mysql.connector object connected to the database
        username -- username of the user you're searching for
    """
    cursor = db.cursor()
    query = "SELECT * FROM user WHERE username='{}'".format(username)
    cursor.execute(query)
    result = []
    for obj in cursor:
        result.append(obj)
    cursor.close()
    return result


def create_user(db, params):
    """Creates a user with given parameters

    Keyword Arguments:
    db -- mysql.connector object that contains the DB connection
    params -- dictionary containing the following params:
        username - required
        password - required
        email - optional
        fname - optional
        lname - optional
        bio - optional
        gender - optional
    """
    # Create a cursor object to run queries.
    cursor = db.cursor()
    # We need to create our query string using given params.
    query = 'INSERT INTO user ('
    # Add in the fields they are wanting to specify.
    for i, items in enumerate(params.items()):
        # Check for last iteration
        if i == len(params) - 1:
            query += '{}) VALUES ('.format(items[0])
        else:
            query += '{}, '.format(items[0])
    # Add in the values they have specified.
    for i, items in enumerate(params.items()):
        # Check for last iteration
        if i == len(params) - 1:
            query += '"{}")'.format(items[1])
        else:
            query += '"{}", '.format(items[1])
    cursor.execute(query)
    cursor.close()


def modify_user(db, params):
    """Modifies an existing user's info

        Keyword Arguments:
        db -- mysql.connector object that contains the DB connection
        params -- dictionary containing any of the following params:
            username
            password
            email
            fname
            lname
            bio
            gender
    """
    # TODO: Make sure foreign keys don't get borked by this function
    pass


def get_all_users(db):
    pass


def get_channel(db, name):
    pass


def modify_channel(db, params):
    pass


def blacklist_user(db, channel, username, duration):
    pass


def modify_admin(channel, username, modify):
    pass


# Included head_admins
def get_admins(channel):
    pass


# TODO: Message retrieval

def send_message(channel, body):
    pass


def send_private_message(channel, body):
    pass