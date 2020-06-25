from flask import Flask, render_template
import os
import random

app = Flask(__name__)

#TODO
#some subroutine here

@app.route("/")
def index():
	return render_template("index.html", url=url)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

