import requests  # Импорт библиотеки Requests
from bs4 import BeautifulSoup
import pyperclip


print ('Ссылка на страницу:')
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
name_tovar = soup.find('h1').text
image_tovar = soup.find(class_='featured-area').find('img').get('data-src')
print (url)
print (image_tovar)
print (name_tovar)
pyperclip.copy('<hr style="margin-top:20px; margin-bottom:20px;" class="divider divider-solid"> <div '
               'class="row"><div class="col-md-4"><center><img src="' + image_tovar + '" rel="nofollow"></center> </div> <div class="col-md-8"><a href="' + url + '" target="_blank"><h3>' + name_tovar + '</h3><!--noindex-->' + '<!--/noindex--><br><a href="' + url + '" target="_blank" class="shortc-button medium green "><span class="fa" aria-hidden="true"></span> <span class="shortc-button" style="color: white;">Посмотреть варианты подарков</span></a></div></div><hr style="margin-top:20px; margin-bottom:20px;" class="divider divider-solid">')

