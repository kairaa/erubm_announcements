from bs4 import BeautifulSoup
import requests


def get_full_text(full_text_link):
    full_text_page = requests.get(full_text_link).text
    full_text_soup = BeautifulSoup(full_text_page, 'lxml')
    entry_content = full_text_soup.find('div', class_="entry-content border-1px p-20 pr-10")
    mt_10 = entry_content.find('div', class_="mt-10")
    return mt_10.text


url = "https://bm.erciyes.edu.tr/?Duyurular"

page = requests.get(url).text

soup = BeautifulSoup(page, 'lxml')

h5_tag = soup.findAll('h5')

announcement_list = []
summaryID = len(h5_tag) - 1

for i in range(10):
    summary = h5_tag[i].a.text
    link = "https://bm.erciyes.edu.tr/?DuyuruID=" + str(summaryID)

    info = {
        "summary": summary,
        "link": link,
        "full_text": get_full_text(link)
    }
    summaryID -= 1
    announcement_list.append(info)

print('\n'.join(map(str, announcement_list)))
