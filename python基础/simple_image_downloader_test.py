

import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt 




url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
response = requests.get(url)
##图片的二进制文本
img = response.content
image = Image.open(BytesIO(img))
plt.imshow(image)
