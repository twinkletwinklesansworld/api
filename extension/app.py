from flask import Flask, request, jsonify
from json import dumps
from database.jsondatabase import JsonDatabase

class TwinkleTwinkleCuteSansWorld(Flask):
    def __init__(self):
        super().__init__(__name__)

        self.r = self.route
        self.e = self.errorhandler

        self.req = request
        self.userdb = JsonDatabase('database/users.json')
        self.postdb = JsonDatabase('database/posts.json')

    def main(self, function):
        def wrap(*args, **kwargs):
            auth = str(self.req.headers['Auth']).split()
            if self.userdb[auth[0]]['token'] == auth[1]: userdata = self.userdb[auth[0]]
            else: return {'error': 'invalid token'}
            try: res = function(userdata,  *args, **kwargs)
            except Exception as e: return self.res({'error': str(e)}, 500)  
            return res
        return wrap

    def need_data(self, function):
        def wrap(*args, **kwargs):
            data = dict(self.req.form)
            try: res = function(data, *args, **kwargs)
            except Exception as e: return self.res({'error': str(e)}, 500)
            return res
        return wrap
    
    def res(self, *args):
        if len(args) == 1: return args[0], 200, {'ContentType': 'application/json'}
        elif len(args) == 2: return args[0], int(args[1]), {'ContentType': 'application/json'}
        elif len(args) == 3: return args[0], int(args[1]), dict(args[2])

    def run_web(self, host = '0.0.0.0', port = 5000, debug = True): return self.run(host = host, port = port, debug = debug)