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

You may need to substitute "python3" for the appropriate command on your system. You can also optionally turn on e-mail verification:

```
python3 server/ --verify_email TRUE
```

To see what options the server was started with, perform a GET on /api/server/hello.

## Update the Client Pages ##
```
cd server/lib/ChatBareBones2
git checkout master
git pull
```

The ChatBareBones2 directory is the client team's repo, so the two git commands above operate on the client team's repo. You can make direct changes here and push them.

The client repo will have an html, js, css, and img file. The files within them are automatically routed to localhost:8000/client/<path/to/fileName.ending> with the exception that html files are routed to localhost:8000/<path/to/fileName>.

## Troubleshooting ##

### Unrecognized Python Command ###
You need to make sure you are running the correct command for Python3. For most linux installs, this is "python3". For Windows, it could be python.exe. You may need to install Python3 or add the installation path to your Windows environment variables. After updating these variables, you will need a freshly opened terminal.

### No Module Named lib.bottle.bottle ###
You need to initialize the submodules. See the instructions for cloning the repo. Notice that the submodule command must be ran in the top directory of the repo.

### No Module Named server.server_run ###
You are trying to run the server with a version of Python 2. This server is written in Python 3 and it fails on this import because importing changed slightly between python versions.
