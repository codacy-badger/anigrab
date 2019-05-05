import os, threading, time
from flask import Blueprint, render_template, request
from ..forms.aniForm import aniForm
from ..libs.anigrab import Anigrab
from colorama import Fore, Back

bweb = Blueprint("web",
                 __name__,
                 static_folder=os.path.join(os.getcwd(), "src/static"),
                 template_folder=os.path.join(os.getcwd(), "src/template"))
anime = Anigrab()


def getData(website, keyword):
    for a in anime.result:
        anime.result[a].clear()
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
            t = threading.Thread(target=anime.website, args=(site, ))
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    return anime.result


@bweb.route("/", methods=["POST", "GET"])
def index():
    form = aniForm()
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
                            print(f"{Back.RED}[{site}][{waktu}] {b.get('error')}{Back.RESET}")
                        else:
                            print(
                                f"{Fore.YELLOW}[{site}]{Fore.RESET}{Fore.GREEN}[{waktu}]{Fore.RESET} {b.get('title')}"
                            )
    return render_template("index.html", **context)
