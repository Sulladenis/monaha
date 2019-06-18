import requests
import os
from bs4 import BeautifulSoup
from django.core.files.images import File
from django.conf import settings
from blog.models import BlogPhoto, Blog

path_temp = os.path.join(settings.BASE_DIR, 'temp')

url_list = []
def get_urls_pagelist(url_page):
    soup = BeautifulSoup(requests.get(url_page).text, "html.parser")
    urls = soup.find_all('h1', class_='title')
    url = [url.find('a').get('href') for url in urls]
    return url

def upload_file(img_url, file_name):
    r = requests.get(img_url)
    with open(os.path.join(path_temp, file_name), 'wb') as f:
        f.write(r.content)
    print('в папку temp переданно фото {}'.format(file_name))

def add_data(post, file_name):
    img = BlogPhoto.objects.create(post = post)
    with open(os.path.join(path_temp, file_name), 'rb') as f:
        myfile = File(f)
        img.photo.save(name=file_name, content=myfile)
    print('к посту {} \nдобавлен файл: {} \nurl: {}'.format(img.post.title, img.photo.name, img.photo.url))

for i in range(5, 0, -1): # --> url_list
    url_l = 'http://monaha.ru/blog/' + str(i)
    print(url_l)
    url_list.extend(get_urls_pagelist(url_l))

for url in url_list:
    soup = BeautifulSoup(requests.get('http://monaha.ru' + url).text, "html.parser")
    block = soup.find("div", {"id": "system"})
    main_img = block.find('div', class_="pos-media").find('img')['src']
    slideshow = block.find('div', class_="wk-slideshow")

    if slideshow != None:
        img = slideshow.find('img')['src']
        all_img = slideshow.find_all('img')
        list_img = [x.get('data-src') for x in all_img]
        list_img[0] = img
    else:
        img = block.find('div', class_="pos-content").find_all('img')
        list_img = [x['src'] for x in img]

    list_img.append(main_img)
    title = block.find('h1', class_="title").text.strip()
    text = block.find('div', class_="pos-content").text.strip()
    date = block.find('p', class_="meta").text.replace('.', ' ').split(' ')[2:5]
    date = '{} {} {}'.format(date[0], date[1], date[2])

    def add_data_db(list_img):
        post = Blog.objects.create(title=title, text=text, date=date)
        print('Создана запись - {} добавленны данные {}, {}'.format(post, title, date))

        for url in list_img:
            if not url.startswith('http'):
                url = 'http://monaha.ru'+ url
            file_name = url.split('/')[-1]
            upload_file(url, file_name)
            add_data(post, file_name)
            os.remove(os.path.join(path_temp, file_name))
            print('фото из папки temp {} удалленно'.format(file_name))

    add_data_db(list_img)
# import blog.utils 
