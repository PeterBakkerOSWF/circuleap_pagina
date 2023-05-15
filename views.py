from flask import Blueprint, render_template, request, jsonify, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@app.route('/score')
def score():
	return render_template('score_team.html', results = ["results", 1])


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
