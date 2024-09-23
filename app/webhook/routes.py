from flask import Blueprint, json, request
from ..extensions import client

webhook = Blueprint("Webhook", __name__, url_prefix="/webhook")


@webhook.route("/receiver", methods=["POST"])
def receiver():
    collection = client.db["webhook_store"]
    data = request.get_json()
    print(data)
    collection.insert_one(data)
    return {}, 200
