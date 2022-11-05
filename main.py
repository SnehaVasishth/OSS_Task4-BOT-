import os
import json

from flask import Flask, render_template, send_from_directory

app = Flask(
    __name__,
    static_url_path='/static',
    template_folder='./'
)




@app.route("/")
def home():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(
        host='localhost',
        port=5050,
        debug=True
    )



