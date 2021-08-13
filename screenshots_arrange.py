import os
import time
import shutil


def make_and_copy():
    print("Please enter the path to your screenchots folder")
    path = str(input())
    t = time.time()
    current_file = "/old_ss_time(" + str(t) + ")"
    os.mkdir(path + "/old_ss_time(" + str(t) + ")")
    all_files = os.listdir(path)
    for x in all_files:
        if x != current_file:
            shutil.move(path + "/" + x, path + current_file)
    return path, current_file[1:]
