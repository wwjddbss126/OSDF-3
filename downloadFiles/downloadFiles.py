import urllib.request, wget, os
from bs4 import BeautifulSoup
 
url = 'http://www.digitalforensics.or.kr/'
req = urllib.request.Request(url + 'images/')
code = urllib.request.urlopen(url + 'images/').read()
soup = BeautifulSoup(code, 'html.parser')
fileList = []

def createFolder(dir):
    if not os.path.exists(dir):
            os.makedirs(dir)
    
def func():
    createFolder(os.getcwd() + './downloaded/')
    for link in soup.find_all('a'):
        fileList.append(link.get('href'))

    for i in range(1, len(fileList)):
        downloadUrl = url + fileList[i]
        wget.download(downloadUrl, './downloaded/'+str((downloadUrl.split('/'))[-1]))

if __name__ == '__main__':
    func()