import screenshots_arrange
import upload_screenshot
import os
import png_to_jpg
import time
import shutil

(path, current_file) = screenshots_arrange.make_and_copy()
print(path, current_file)

upload_screenshot.login()

while True:
    all_files = os.listdir(path)
    if len(all_files) > 1:
        for x in all_files:
            if x != current_file:
                if x[-4:] == ".png":
                    time.sleep(4)
                    png_to_jpg.convert_to_jpg(path, x)
                    #png_to_jpg.delete_image(path, x)
                    print(path, x)
                    time.sleep(2)
                if x[-4:] == ".jpg":
                    print(path + "/" + x)
                    upload_screenshot.upload(path+"/"+x)
                    shutil.move(path + "/" + x+".REMOVE_ME", path +"/"+ current_file)
                    time.sleep(5)

print(all_files)
