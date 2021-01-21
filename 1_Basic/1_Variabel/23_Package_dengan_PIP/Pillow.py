from PIL import Image

im = Image.open("foto.jpg")
print ('format file: ', im.format)
print ('format file: ', im.size)
print ('format file: ', im.mode)

im.show()