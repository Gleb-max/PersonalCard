import json
from random import choice
from flask import Flask, render_template, url_for


MEMBERS_INFO = "templates/members.json"


app = Flask(__name__)


@app.route("/member")
def random_member():
    with open(MEMBERS_INFO) as json_file:
        member = choice(json.load(json_file)["members"])
    member["professions"] = ", ".join(sorted(member["professions"]))
    params = {
        "title": "Личная карточка",
        "member": member,
    }
    return render_template("member.html", **params)


if __name__ == "__main__":
    app.config['SECRET_KEY'] = "SECRET_KEY"
    app.run(port=8080, host="127.0.0.1")
