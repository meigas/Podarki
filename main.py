import requests  # Импорт библиотеки Requests
from bs4 import BeautifulSoup
import pyperclip


# Основная функция
   # URL страницы
print ('Ссылка на страницу:')
url = input()
   # Получаем страницу
r = requests.get(url)
   #7usd = float(74.1)
   # Открываем файл
soup = BeautifulSoup(r.text, 'html.parser')
#print (soup)
name_tovar = soup.find('h1').text
#description_tovar = soup.find(property='og:description').get('content')
#image_tovar = soup.find(id='dynamicImage_image_picture').find('img').get('src')
image_tovar = soup.find(class_='featured-area').find('img').get('data-src')
print (url)
print (image_tovar)
print (name_tovar)
# print (description_tovar)
# print (url)
# pyperclip.copy (name_tovar)
#pyperclip.copy('<hr style="margin-top:20px; margin-bottom:20px;" class="divider divider-solid"> <div
# class="content-column one_fourth"><div style="padding-right:25px;"> <center><img src="' + image_tovar + '" rel="nofollow"></center> </div></div> <div class="content-column three_fourth last_column"><h3>' + name_tovar + '</h3><div class="clear1"></div><!--noindex-->' + description_tovar + '<!--/noindex--><br><a href="' + url + '" target="_blank" class="shortc-button medium green "><span class="fa" aria-hidden="true"></span> <span class="shortc-button" style="color: white;">Перейти в Microsoft Store</span></a></div><hr style="margin-top:20px; margin-bottom:20px;" class="divider divider-solid">')

