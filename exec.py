import requests
from bs4 import BeautifulSoup
import re

page = 1

while page <= 157:
    url = "http://world.kbs.co.kr/service/program_listenagain.htm?page=" + str(page) + "&lang=e&procode=parkofd&segcode="
    print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    mp3 = soup.select('a.download')

    if mp3 is not None:
        for el in mp3:
            href = el.get('href')
            href = href.strip()
            #http://world.kbs.co.kr/"down.htm?inpage_id=61369&Type=MP3
            hostname = "http://world.kbs.co.kr/"
            furl = hostname + href
            r = requests.get(furl)
            d = r.headers['content-disposition']
            fname = re.findall("filename=(.+)", d)[0]

            open(fname, "wb").write(r.content)
            print(fname)

    page += 1

    