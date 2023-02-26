import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = r"C:\Users\Vishwajeet Kumbhar\OneDrive\Desktop\PYTHON\class103\PRO-C103-Student-Boilerplate-main"
to_dir = r"C:\Users\Vishwajeet Kumbhar\OneDrive\Desktop\PYTHON\class103\PRO-C103-Student-Boilerplate-main"



# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
       print("A file is created")
    
    def on_deleted(self,event):
        print("A file is deleted")

    def on_modified(self,event):
        print("A file is modified")

    def on_moved(self,event):
        print("A file is moved")


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


while True:
    time.sleep(2)
    print("running...")

    