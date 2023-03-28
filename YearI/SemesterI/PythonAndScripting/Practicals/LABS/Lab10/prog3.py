from PIL.ExifTags import TAGS
from PIL import Image
from datetime import datetime

current_time = datetime.now()
print("LAB 10 Shubhang Gupta " + str(current_time))

file = 'Canon_40D.jpg'
image = Image.open(file)
image.show()

exif_table={}
for k, v in image.getexif().items():
    tag=TAGS.get(k)
    exif_table[tag]=v

for key, value in exif_table.items(): print(f'{key} : {value}')

