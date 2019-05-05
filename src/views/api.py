from flask import Blueprint, jsonify, request
from .web import getData

bapi = Blueprint("api", __name__)


@bapi.route("/v1", methods=["POST", "GET"])
def vone():
    if request.method == "POST":
        result = getData(**request.form.to_dict())
        return jsonify(result)
    return jsonify({"message": "API Message"})

