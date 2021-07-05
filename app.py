from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

# Parser
status_put_args = reqparse.RequestParser()
status_put_args.add_argument("uid", type=str, help="Name of the client (Default: MAC address)")
status_put_args.add_argument("ip-address", type=str, help="IP address of the client")
status_put_args.add_argument("history", type=str, help="IP address of the client")

# Data
clients_status = {}


def abort_if_client_id_doesnt_exist(uid: str):
    if uid not in clients_status:
        abort(404, message="Client ID is not valid.")


def abort_if_client_id_exist(uid: str):
    if uid in clients_status:
        abort(404, message="Client ID already exists/")


class Status(Resource):

    def get(self, uid: str):
        abort_if_client_id_doesnt_exist(uid)
        return clients_status[uid]

    def post(self, uid: str):
        abort_if_client_id_exist(uid)
        args = status_put_args.parse_args()
        clients_status[uid] = args
        return clients_status[uid], 201

    def put(self, uid: str):
        args = status_put_args.parse_args()
        clients_status[uid] = args
        return clients_status[uid], 201

    def delete(self, uid: str):
        abort_if_client_id_doesnt_exist(uid)
        del clients_status[uid]
        return '', 204


api.add_resource(Status, "/status/<string:uid>")

# class Table(Resource):
# @app.route('/', methods=['GET'])
# def table_api():
#  r = request.get('??')
# data = json.loads(r.content)
# return render_template("table.html", headers=headers, data=data)


# api.add_resource(Table)

if __name__ == '__main__':
    app.run(debug=True)
