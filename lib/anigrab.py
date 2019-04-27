import requests
from bs4 import BeautifulSoup

__author__ = "M Nabil Adani"
__github__ = "https://github.com/nabil48/"
__date_create__ = "10/10/2018 02:48 AM"
__date_modife__ = "26/04/2019 01:27 PM"


class Anigrab:
    result = {
        "animesave": [],
        "meguminime": [],
        "drivenime": [],
        "bakacan": [],
        "meownime": [],
        "wibudesu": [],
        "kusonime": [],
        "awbatch": [],
        "meowbatch": []
    }
    url = {
        "animesave": "http://www.animesave.com/",
        "meguminime": "http://meguminime.com/",
        "drivenime": "https://drivenime.com/",
        "bakacan": "http://bakacan.id/",
        "meownime": "http://meownime.com/",
        "wibudesu": "https://wibudesu.com/",
        "kusonime": "https://kusonime.com/",
        "awbatch": "http://awbatch.in/",
        "meowbatch": "http://meowbatch.com"
    }
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    }

    def _request(self, website):
        result = requests.get(self.url.get(website),
                              params=self.query.get(website),
                              headers=self.header)
        return result

    def search(self, keyword):
        self.query = {
            "animesave": {
                "s": keyword
            },
            "meguminime": {
                "s": keyword
            },
            "drivenime": {
                "s": keyword
            },
            "bakacan": {
                "s": keyword,
                "post_type": "anime"
            },
            "meownime": {
                "s": keyword,
                "submit": "Search"
            },
            "wibudesu": {
                "s": keyword,
                "post_type": "post"
            },
            "kusonime": {
                "s": keyword,
                "post_type": "post"
            },
            "awbatch": {
                "s": keyword
            },
            "meowbatch": {
                "s": keyword
            }
        }

    def website(self, site=None):
        """
        list site
            1.animesave
            2.meguminime
            3.drivenime
            4.bakacan
            5.meownime
            6.wibudesu
            7.kusonime
            8.awbatch
            9.meowbatch
        """
        if site == "animesave":
            try:
                soup = BeautifulSoup(self._request(site).text, "lxml")
                div = soup.find("div", attrs={"class": "allgreen"})
                link = div.find_all("a")
                data = dict()
                for a in link:
                    data["link"] = a.get("href")
                    data["title"] = a.get("title")
                    self.result["animesave"].append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                self.result["animesave"].append(data)

        elif site == "meguminime":
            try:
                soup = BeautifulSoup(self._request(site).text, "lxml")
                div = soup.find("div", attrs={"class": "pst"})
                link = div.find_all("h2")
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a.get("href")
                    data["title"] = h2.a.get("title")
                    self.result["meguminime"].append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                self.result["meguminime"].append(data)

        elif site == "drivenime":
            try:
                soup = BeautifulSoup(self._request(site).text, "lxml")
                div = soup.find("div", attrs={"id": "content_box"})
                link = div.find_all("h2")
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a.get("href")
                    data["title"] = h2.a.get("title")
                    self.result["drivenime"].append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                self.result["drivenime"].append(data)

        elif site == "bakacan":
            try:
                soup = BeautifulSoup(self._request(site).text, "lxml")
                div = soup.find("div", attrs={"class", "vinsmokebody"})
                link = div.find_all("h2")
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a.get("href")
                    data["title"] = h2.a.get("title")
                    self.result["bakacan"].append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                self.result["bakacan"].append(data)

        elif site == "meownime":
            try:
                soup = BeautifulSoup(self._request(site).text, "lxml")
                div = soup.find("div", attrs={"class": "site-main"})
                link = div.find_all("h1", attrs={"class": "entry-title"})
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a.get("href")
                    data["title"] = h2.a.text
                    self.result["meownime"].append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                self.result["meownime"].append(data)

        elif site == "wibudesu":
            try:
                soup = BeautifulSoup(self._request(site).text, "lxml")
                div = soup.find("div", attrs={"class": "rseries"})
                link = div.find_all("h2")
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a.get("href")
                    data["title"] = h2.a.get("title")
                    self.result["wibudesu"].append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                self.result["wibudesu"].append(data)

        elif site == "kusonime":
            try:
                soup = BeautifulSoup(self._request(site).text, "lxml")
                div = soup.find("div", attrs={"class": "rseries"})
                link = div.find_all("h2")
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a.get("href")
                    data["title"] = h2.a.get("title")
                    self.result["kusonime"].append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                self.result["kusonime"].append(data)

        elif site == "awbatch":
            try:
                soup = BeautifulSoup(self._request(site).text, "lxml")
                div = soup.find("div", attrs={"class": "konten-tengah"})
                link = div.find_all("h2")
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a.get("href")
                    data["title"] = h2.a.get("title")
                    self.result["awbatch"].append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                self.result["awbatch"].append(data)

        elif site == "meowbatch":
            try:
                soup = BeautifulSoup(self._request(site).text, "lxml")
                div = soup.find("div", attrs={"class": "post-content-container"})
                link = div.find_all("a", attrs={"class": "post-title"})
                data = dict()
                for url in link:
                    data["link"] = url.get("href")
                    data["title"] = url.h4.text.strip()
                    self.result["meowbatch"].append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                self.result["meowbatch"].append(data)
