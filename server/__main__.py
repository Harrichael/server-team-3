
import argparse

from server.server_run import run

def arg_bool(text):
    if text.upper() == 'TRUE' or text.upper() == 'YES' or text.upper() == 'ON':
        return True
    return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Server 3 Startup Script')
    parser.add_argument('-u', '--host', default='localhost')
    parser.add_argument('-p', '--port', type=int, default=8000)
    parser.add_argument('-d', '--debug', type=bool, default=True)
    parser.add_argument('-e', '--verify_email', type=arg_bool, default=False)

    args = parser.parse_args()
    
    run( host=args.host,
         port=args.port,
         debug=args.debug,
         config=args,
       )
