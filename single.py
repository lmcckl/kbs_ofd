import requests
from bs4 import BeautifulSoup
import re


print('Enter date: YYYY-MM-DD')
sdate = input()

url = "http://world.kbs.co.kr/service/program_listenagain.htm?lang=e&procode=parkofd&segcode=&broad_date=" + str(sdate)
print(url)
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
mp3 = soup.select('a.download')

if mp3 is not None:
    for el in mp3:
        href = el.get('href')
        href = href.strip()
        hostname = "http://world.kbs.co.kr/"
        furl = hostname + href
        r = requests.get(furl)
        d = r.headers['content-disposition']
        fname = re.findall("filename=(.+)", d)[0]

        open(fname, "wb").write(r.content)
        print(fname)

    