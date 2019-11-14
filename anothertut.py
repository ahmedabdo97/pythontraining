import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://www.desktopbackground.org/p/2013/05/08/573004_epic-wallpapers-hd-1080p-hd-553-seo-wallpapers_1920x1080_h.jpg")
print("status code", r.status_code)

image = Image.open(BytesIO(r.content))

path = "./image.jpg"

print(image.size, image.format, image.mode)
path = "./image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("cannot save images")