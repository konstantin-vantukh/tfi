from flask import Flask
from flask_restful import Api, Resource, reqparse
import werkzeug
import os
import tf

app = Flask(__name__)
api = Api(app)


class RequestHandler(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self):
        message_get = 'usage: curl [IP address]:5000 -X PUT -H "multipart/form-data"' + \
            '-F "uploading=@[file]"'
        return {"message": message_get}, 200

    def put(self):
        self.parser.add_argument("uploading",
                                 type=werkzeug.datastructures.FileStorage,
                                 location="files"
                                 )
        args = self.parser.parse_args()
        if args is None:
            return {"message": "no args detected."}, 400
        uploading = args.get("uploading")
        if uploading is None:
            return {"message": "args detected, but file name is null."}, 400
        text = uploading.read().decode('utf-8')
        chars = len(text)
        response = {
            "filename": uploading.filename,
            "chars": chars,
            "keywords": tf.tf(text)
        }
        return response, 201


api.add_resource(RequestHandler, "/")

if __name__ == "__main__":
    app.run(debug=True)
