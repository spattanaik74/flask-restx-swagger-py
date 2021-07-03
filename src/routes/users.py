from flask import jsonify
from flask_restx import Resource, fields
from src.namespace import user_api
from src.instance.flask_app import api
from src.instance.config import mycol
from src.instance.flask_app import app


app.config['SWAGGER_UI_JSONEDITOR'] = True

resource_field = api.model('Resource', {'name': fields.String,
                                        'place': fields.String})

@user_api.route("/User_info")
class UserInfo(Resource):
    def get(self):
        """
        GET request endpoints
        :return:
        """
        output = []
        for i in mycol.find():
            output.append({"name": i["name"], "place": i["place"]})
        return jsonify(output)
    @api.expect(resource_field)
    def post(self):
        """
        POST request endpoints
        :return:
        """
        new_data = api.payload
        new_db = mycol.insert(new_data)
        return jsonify(str(new_db))



    def put(self):
        """
        PUT request endpoints
        :return:
        """

    def delete(self):
        """
        DELETE request endpoints
        :return:
        """