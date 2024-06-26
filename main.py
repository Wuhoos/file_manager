from os import scandir, rename
import os
from os.path import splitext, exists, join
from shutil import move

import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sourceDir = '/Users/david/Downloads'
docDir = '/Users/david/Downloads/docs'
imgDir = '/Users/david/Downloads/img'
zipDir = '/Users/david/Downloads/zipFile'
otherDir = '/Users/david/Downloads/other'

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi",
                    ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", 
                    ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", 
                    ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", 
                    ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", 
                    ".svg", ".svgz", ".ai", ".eps", ".ico", '.mov', '.m4a', '.mp4']

document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

other_extensions = ['.dmg', '.ttf', '.db', '.iso', '.exe', '.ics']


def newName(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        print(f'this is the {name}')
        counter += 1
    return name


def moveFile(dest, entry, name):
    if exists(f"{dest}/{name}"):
        uniqueName = newName(dest, name)
        oldName = join(dest, uniqueName)
        new_name = join(dest, uniqueName)
        rename(oldName, new_name)
    move(entry, dest)

class MoveHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(sourceDir) as downloads:
            for download in downloads:
                name = download.name
                self.checkDocFile(download, name)
                self.checkImgFile(download, name)
                self.checkZipFile(download, name)
                self.checkOtherFile(download, name)

    def checkDocFile(self, entry, name):
        for document_extension in document_extensions:
            if name.endswith(document_extension) or name.endswith(document_extension.upper()):
                moveFile(docDir, entry.path, name)
                logging.info(f"Moved doc File: {name}")

    def checkImgFile(self, entry, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                moveFile(imgDir, entry.path, name)
                logging.info(f"Moved img File: {name}")

    def checkZipFile(self, entry, name):
        if name.endswith('.zip'):
            moveFile(zipDir, entry.path, name)
            logging.info(f'Moved zip file: {name}')

    def checkOtherFile(self, entry, name):
        for other_extension in other_extensions:
            if name.endswith(other_extension):
                moveFile(otherDir, entry.path, name)
                logging.info(f'Moved other\' file: {name}')
        


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sourceDir
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
