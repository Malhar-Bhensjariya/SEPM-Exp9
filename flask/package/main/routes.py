from flask import Blueprint, jsonify, request, session

main_bp = Blueprint('main_bp', __name__)
@main_bp.route("/", methods=["POST"])
def home():
    return jsonify("Hi from flask server")