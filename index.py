from extension.app import TwinkleTwinkleCuteSansWorld
from kiki_random import random_key
from string import ascii_letters, digits
app = TwinkleTwinkleCuteSansWorld()

@app.r('/api/login', methods = ['POST'])
@app.need_data
def login(data):
    username, pswd = data['id'], data['pswd']
    if app.userdb[username]['password'] != pswd: return app.res({'error': 'password or id wrong'}, 403)
    return app.res(app.userdb[username]['token'])

@app.r('/api/join', methods = ['POST'])
@app.need_data
def join(data):
    username, pswd = data['id'], data['pswd']
    if username in app.userdb.keys(): return app.res({'error': 'id already used'}, 400)
    token = random_key(strings = ascii_letters + digits)

    app.userdb[username] =  {
        'name': username,
        'pswd': pswd,
        'token': token
    }

    return app.res({'token': token})

app.run_web()