from typing import List
import requests
from bs4 import BeautifulSoup
import re

page = 1
filecount = 0

while page <= 157:
    url = "https://world.kbs.co.kr/service/program_playlist_list.htm?page="+ str(page) +"&lang=e&procode=parkofd&bbs=parkofd_playlist"
    print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    pl = soup.select('a.ga_Program_playlist_tit')
    if pl is not None:
        for el in pl:
            href = el.get('href')
            href = href.strip()
            href = href[1:]
            #http://world.kbs.co.kr/service/program_playlist_view.htm?lang=e&procode=parkofd&bbs=parkofd_playlist&no=44568
            hostname = "https://world.kbs.co.kr/service"
            furl = hostname + href
            res = requests.get(furl)
            soup = BeautifulSoup(res.content, 'html.parser')
            date = soup.select('section.comp_board_view div.title_area h1')[0].text.strip()
            dateformat = date[2:-6] + date[5:-3] + date[8:]
            content = soup.select('div.body_txt.fr-view p')
            filename = 'elena' + dateformat + '.txt'
            print('w:' + filename)
            f = open(filename,'w')

            for c in content:
               f.write(c.text.strip() + '\r\n')

            f.close()
            filecount += 1

    page += 1
    
print(filecount)
    