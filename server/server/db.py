# db.py - Functions related to the database.

# Library Imports
from pymongo import MongoClient
from time import time


# Connect to our database
def db_connect():
    """Connects to a database
    """
    # TODO: Support authentication
    try:
        # This will connect to a localhost:27017 instance of MongoDB
        client = MongoClient()
    except Exception as e:
        # TODO: Error handling
        print('Oh no! {}'.format(e))
    else:
        client = client.server
        return client


def get_user(client, username):
    """Grabs a user given a username

    Keyword Arguments:
    client -- MongoClient object connected to the database
    username -- username of the user you're searching for
    Returns:
    dict containing the user, if no match then returns None.
    """
    return client.users.find_one({'username': username})


def create_user(client, params):
    """Creates a user with given parameters

    Keyword Arguments:
    client -- mysql.connector object that contains the DB connection
    params -- dictionary containing the following params:
        username - required
        password - required
        email - required
    """
    # We need to check and see if that username already exists.
    # If we find one, exit and inform them that the username is already taken.
    if get_user(client, params['username']):
        return 400
    # Next check for a duplicate email.
    elif client.users.find_one({'email': params['email']}):
        return 400
    # If no conflicts, add it.
    else:
        client.users.insert_one(params)
        return 201


def modify_user(client, username, params):
    """Modifies an existing user's info

    Keyword Arguments:
    client -- mysql.connector object that contains the DB connection
    params -- dictionary containing any of the following params:
        password
        fname
        lname
        bio
        gender
    """
    user = get_user(client, username)
    if user:
        client.users.update_one({'_id': user['_id']}, {'$set': params})
        return 200
    else:
        # User wasn't found.
        return 404


def get_all_users(client):
    users = []
    for user in client.users.find_many({}):
        users.append(user)
    return users


def get_channel(client, name):
    return client.channels.find_one({'name': name})


def create_channel(client, name, admin_name):
    if get_channel(client, name):
        # channel with that name already exists
        return 409
    else:
        params = {
            'name': name,
            'head_admin': admin_name,
            'blacklist': []
        }
        client.channels.insert_one(params)
        return 201


def modify_channel(client, name, params):
    chan = get_channel(client, name)
    if chan:
        client.channels.update_one({'_id': chan['_id']}, {'$set': params})
        return 200
    else:
        # User wasn't found.
        return 404


def blacklist_user(client, channel, username, duration):
    # Make sure this is an actual user.
    if not get_user(client, username):
        return 400
    # Found will be a helper variable to detirmine if we found the entry or not
    found = False
    # First, grab the existing blacklist for that channel.
    chan = client.channels.find_one({'name': channel})
    blacklist = chan['blacklist']
    # Check to see if the user exists in there currently.
    for entry in blacklist:
        # This means the user is already in there
        if entry['username'] == username:
            found = True
            entry['finish-time'] += duration
    if not found:
        # This means we didn't find one, so need to create a new entry.
        finish_time = int(time()) + duration
        blacklist.append({'username': username, 'finish-time': finish_time})
    # Now, let's return our blacklist back to the DB.
    client.channels.update_one({'_id': chan['_id']},
                               {'$set': {'blacklist': blacklist}})
    return 200


def remove_user_blacklist(client, channel, username):
    found = False
    # Grab the current blacklist.
    chan = client.channels.find_one({'name': channel})
    blacklist = chan['blacklist']
    for entry in blacklist[:]:
        if entry['username'] == username:
            found = True
            blacklist.remove(entry)
    if not found:
        # User wasn't blacklisted in the first place
        # TODO: What status code for this???
        return 400
    client.channels.update_one({'_id': chan['_id']},
                               {'$set': {'blacklist': blacklist}})
    return 200


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

# TODO: Replace (update) personal block lists

# TODO: Insert & grab PM Boxes, alphabetically sorted