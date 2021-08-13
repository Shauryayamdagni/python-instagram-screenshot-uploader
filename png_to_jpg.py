from PIL import Image
import os


def convert_to_jpg(path, image):
    img_png = Image.open(path + "/" + image)
    rgb_img = img_png.convert("RGB")
    rgb_img.save(path + "/" + image[0:-4] + ".jpg")
    delete_image(path,image)

def delete_image(path, image):
    os.remove(path + "/" + image)

#convert_to_jpg("/home/shaurya/Desktop/testing/", "Screenshot.png")
#delete_image("/home/shaurya/Desktop/testing/", "Screenshot.png")
