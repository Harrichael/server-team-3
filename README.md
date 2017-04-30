# Chat Client: Server Team 3 #

This is the server component of Team 3's Chat Client for CS3100, SP2017 at Missouri S&T.

## Clone the Repo ##
```
git clone git@github.com:renodubois/server-team-3.git
cd server-team-3
git submodule update --init
```

## Run the Server ##
```
python3 server/
```

## Update the Client Pages ##
```
cd server/lib/ChatBareBones2
git checkout master
git pull
```

The ChatBareBones2 directory is the client team's repo, so the two git commands above operate on the client team's repo. You can make direct changes here and push them.

## Troubleshooting ##

### Unrecognized Python Command ###
You need to make sure you are running the correct command for Python3. For most linux installs, this is "python3". For Windows, it could be python.exe. You may need to install Python3 or add the installation path to your Windows environment variables. After updating these variables, you will need a freshly opened terminal.

### No Module Named lib.bottle.bottle ###
You need to initialize the submodules. See the instructions for cloning the repo. Notice that the submodule command must be ran in the top directory of the repo.
