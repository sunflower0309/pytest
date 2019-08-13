import requests
import bs4
import sys
if __name__ == '__main__':
    server='http://www.diyibanzhu6.xyz'

    def getchapterpages(target):
        text=[]
        req = requests.get(url=target)
        bf = bs4.BeautifulSoup(req.text)
        url = bf.find_all('center', class_='chapterPages')
        urls=url[0].find_all('a')
        for each in range(len(urls)):
            x='_'+(str)(each+1)
            tar=target[:-5]+x+'.html'
            print(tar)
            text.append(download(tar))
        return text

    def download(target):
        req = requests.get(url=target)
        bf = bs4.BeautifulSoup(req.text)
        text1 = bf.find_all('div', class_='page-content font-large')
        te=text1[0].text.replace('<br/>' * 2, '')
        return te.replace('\xa0','\n')

    def getchapter(target):
        chapter=[]
        req2 = requests.get(url=target)
        bf2 = bs4.BeautifulSoup(req2.text)
        text2 = bf2.find_all('ul', class_='list')
        no_li = text2[1].find_all('a')
        for each in no_li:
            chapter.append(server + each.get('href'))
        return chapter


    def writer(path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.writelines(text)
            f.write('\n\n')

    chapters=getchapter('http://www.diyibanzhu6.xyz/12/12430/')
    for ark in chapters:
        text=getchapterpages(ark)
        for i in text:
            writer(r'C:\Users\Administrator\Downloads\明日方舟.txt', i)
