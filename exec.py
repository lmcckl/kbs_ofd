import requests
from bs4 import BeautifulSoup
import command

page = 1
while page < 2:
    url = "http://world.kbs.co.kr/service/program_listenagain.htm?page=" + str(page) + "&lang=e&procode=parkofd&segcode="
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    mp3 = soup.select('a.download')

    if mp3 is not None:
        for el in mp3:
            href = el.get('href')
            href = href.strip()
            #http://world.kbs.co.kr/down.htm?inpage_id=61369&Type=MP3
            cmd = "wget http://world.kbs.co.kr" + href
            r = command.run([cmd])
            page += 1
    else:
        page = 999999
    
    