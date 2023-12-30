import sys
sys.path.insert( 0 ,"./utils")

from flask import Flask
from flask import render_template,request,send_file,redirect

from script import Download

app = Flask(__name__)


@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        url = request.form["url"]
        video = Download(url)
        return send_file(video.download(),as_attachment=True)
    return render_template("index.html")

# @app.route("/download/<url>")
# def get_video(url):
    


if __name__ == "__main__":
    app.run(debug=True)
    print("Hosted")
