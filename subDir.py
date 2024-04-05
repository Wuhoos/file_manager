import os
import shutil

from main import imgDir, docDir, otherDir, sourceDir

dir = sourceDir

#optimized version
'''
def orginize_dir(dir):
    extensions = {item.split('.')[-1] for item in os.listdir(dir) if os.path.isfile(os.path.join(dir, item))}
    for extension in extensions:
        if not os.path.exists(os.path.join(dir, extension)):
            os.mkdir(os.path.join(dir, extension))

def move_file(dir):
    for item in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, item)):
            file_extension = item.split('.')[-1]
            shutil.move(os.path.join(dir, item),os.path.join(dir, file_extension, item))


def orginize(imgDir, docDir, otherDir):
    orginize_dir(imgDir)
    orginize_dir(docDir)
    orginize_dir(otherDir)

    move_file(imgDir)
    move_file(docDir)
    move_file(otherDir)
'''



imgExtensions = {item.split('.')[-1] for item in os.listdir(imgDir) if os.path.isfile(os.path.join(imgDir, item))}
docExtensions = {item.split('.')[-1] for item in os.listdir(docDir) if os.path.isfile(os.path.join(docDir, item))}
othersExtensions = {item.split('.')[-1] for item in os.listdir(otherDir) if os.path.isfile(os.path.join(otherDir, item))}

#imgExtensions
#create folder for each ext. type

for extension in imgExtensions:
    if not os.path.exists(os.path.join(imgDir, extension)):
        os.mkdir(os.path.join(imgDir, extension))

#move files
for item in os.listdir(imgDir):
    if os.path.isfile(os.path.join(imgDir, item)):
        file_extension = item.split('.')[-1]
        shutil.move(os.path.join(imgDir, item), os.path.join(imgDir, file_extension, item))

#docExtensions
for extension in docExtensions:
    if not os.path.exists(os.path.join(docDir, extension)):
        os.mkdir(os.path.join(docDir, extension))

for item in os.listdir(docDir):
    if os.path.isfile(os.path.join(docDir, item)):
        file_extension = item.split('.')[-1]
        shutil.move(os.path.join(docDir, item), os.path.join(docDir, file_extension, item))
        

#otherExtension
for extension in othersExtensions:
    if not os.path.exists(os.path.join(otherDir, extension)):
        os.mkdir(os.path.join(otherDir, extension))

for item in os.listdir(otherDir):
    if os.path.isfile(os.path.join(otherDir, item)):
        file_extension = item.split('.')[-1]
        shutil.move(os.path.join(otherDir, item), os.path.join(otherDir, file_extension, item))
