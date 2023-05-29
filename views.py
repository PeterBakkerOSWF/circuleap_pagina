from flask import Blueprint, render_template, request, jsonify, url_for
from calculate import results, pr, de, sa, asset

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route('score')
def score():
    return render_template("score_team.html", results=results, development=de, production=pr, sales=sa, asset=asset)


@views.route("profile")
def profile():
    return render_template("profile.html")


@views.route("/json")
def get_json():
    return jsonify({'name': 'tim', 'çoolness':10})

@views.route(("data"))
def get_data():
    data = request.json
    return jsonify(data)


@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views/get_json"))
