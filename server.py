from lib.aniLink import animeLink
from flask import Flask, render_template, request, jsonify
from aniForm import aniForm
from colorama import Fore, Back
import time
import random
import binascii
import threading

app = Flask(__name__)
app.secret_key = binascii.hexlify(str(random.random()).encode("utf-8"))
anime = animeLink()


def getData(website, keyword):
    anime.search(keyword)
    if website == "animesave":
        anime.website("animesave")
    elif website == "meguminime":
        anime.website("meguminime")
    elif website == "drivenime":
        anime.website("drivenime")
    elif website == "bakacan":
        anime.website("bakacan")
    elif website == "meownime":
        anime.website("meownime")
    elif website == "wibudesu":
        anime.website("wibudesu")
    elif website == "kusonime":
        anime.website("kusonime")
    elif website == "awbatch":
        anime.website("awbatch")
    elif website == "meowbatch":
        anime.website("meowbatch")
    else:
        listSite = [
            "animesave",
            "meguminime",
            "drivenime",
            "bakacan",
            "meownime",
            "wibudesu",
            "kusonime",
            "awbatch",
            "meowbatch",
        ]
        threads = list()
        for site in listSite:
            t = threading.Thread(target=anime.website, args=(site,))
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    return anime.result


@app.before_request
def bef():
    for a in anime.result:
        anime.result[a].clear()


@app.route("/", methods=["POST", "GET"])
def vIndex():
    form = aniForm(csrf_disabled=False)
    context = {
        "form": form,
    }
    if request.method == "POST":
        if form.validate_on_submit():
            data = getData(website=form.listSite.data, keyword=form.keyword.data)
            waktu = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
            context["data"] = data
            for site in data:
                if len(data[site]) >= 1:
                    for b in data[site]:
                        if "error" in b:
                            print("{bRed}[{website}][{time}] {log}{bReset}".format(
                                website=site, time=waktu, log=b["error"], bRed=Back.RED, bReset=Back.RESET)
                            )
                        else:
                            print("{fYellow}[{website}]{fReset}{fGreen}[{time}]{fReset} {log}".format(
                                website=site, time=waktu, log=b["title"], fGreen=Fore.GREEN, fYellow=Fore.YELLOW, fReset=Fore.RESET)
                            )
            return render_template("index.html", **context)
        else:
            return render_template("index.html", **context)
    else:
        return render_template("index.html", **context)


@app.route("/api/v1", methods=["POST"])
def api():
    if request.method == "POST":
        website = request.form["website"]
        keyword = request.form["keyword"]
        result = getData(website, keyword)
        return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
