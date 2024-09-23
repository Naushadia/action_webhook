from flask import Blueprint, json, request
from ..extensions import client

webhook = Blueprint("Webhook", __name__, url_prefix="/webhook")


@webhook.route("/receiver", methods=["POST"])
def receiver():
    collection = client.db["webhook_store"]
    data = request.get_json()
    extracted_data = {
        "request_id": data["head_commit"]["id"],
        "author": data["head_commit"]["author"]["name"],
        "action": data["action"],
        "from_branch": data["pull_request"]["head"]["ref"],
        "to_branch": data["pull_request"]["base"]["ref"],
        "timestamp": data["pull_request"]["created_at"],
    }

    collection.insert_one(extracted_data)
    return {}, 200
