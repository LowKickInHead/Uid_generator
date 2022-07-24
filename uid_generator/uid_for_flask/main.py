import my_module
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()


class Main(Resource):
    def get(self):
        new = my_module.uid_generate()
        return new


api.add_resource(Main, "/api/main")
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host="127.0.0.1")
