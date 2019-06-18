
p = requests.get(img)
out = open("...\img.jpg", "wb")

out.write(p.content)
out.close()

# Запись картинки в Базу Данных
with open('blog\картинка.jpg', 'rb') as f:
    myfile = File(f)
    myfile.write('Hello World')
    img = OldBlogPhoto.objects.create(photo=myfile, name='third')


>>> with open(r'media\oldphoto\temp\img.jpg', 'wb') as fw:
...     myfile = File(fw)
...     myfile.write(p.content)
        img = OldBlogPhoto.objects.create(photo=myfile, name='fourth')

user1=User(name='abc')
user1.pic.save('abc.png', File(open('/tmp/pic.png', 'rb')))

import requests
import shutil

r = requests.get(settings.STATICMAP_URL.format(**data), stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f) 


from PIL import Image
from StringIO import StringIO

r = requests.get('https://example.com/image.jpg')
i = Image.open(StringIO(r.content))