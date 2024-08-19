from rembg import remove
from PIL import Image

#Importa a imagem original
img = Image.open('c:\Users\david\Downloads\20230625_132020.jpg')

#Remove fundo da imagem
img_without_back = remove(img)

#|Salva a imagem sem fundo
img_without_back.save('img_without_back.png')