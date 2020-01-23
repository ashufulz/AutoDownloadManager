# Only for Windows

import os, shutil
from os import path
import time, datetime

source = 'C:\\Users\\username\\Downloads'              # Source directory
img_dir = 'H:\\DM\\Image'                # Paths to different directories
vid_dir = 'H:\\DM\\Video'
song_dir = 'H:\\DM\\Song'
text_dir = 'H:\\DM\\Text'

aext = (".mp3", ".wav")                                     # Audio extensions
iext = (".jpg", ".jpeg", ".png", ".bmp")                    # Image extensions
text = (".doc", ".docx", ".odt", ".pdf", ".rtf", ".txt", ".tex", ".wks", ".wps", ".wpd")            # Text extensions
vext = (".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv", ".m2ts", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv")    # Video extensions


def main():

    # --- Text ---
    files = [i for i in os.listdir(source) if i.endswith(text)]             # Any file with provided Text extensions
    for f in files:
        if not os.path.exists(text_dir):                                    # Will check if the directory exists
            os.makedirs(text_dir)                                           # Else it will create new one

        try:
            shutil.move(path.join(source, f), text_dir)                     # To copy use 'shutil.copy'
            print("Text moved successfully to ["+text_dir+"]")

        except shutil.SameFileError:
            print("Source and destination represents the same file.")

        except PermissionError:
            print("Permission denied.")

        except:
            print("Error occurred while copying file.")


    # --- Image ---
    files = [i for i in os.listdir(source) if i.endswith(iext)]
    for f in files:
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)

        try:
            shutil.move(path.join(source, f), img_dir)
            print("Image moved successfully to ["+img_dir+"]")

        except shutil.SameFileError:
            print("Source and destination represents the same file.")

        except PermissionError:
            print("Permission denied.")

        except:
            print("Error occurred while copying file.")


    # --- Audio ---
    files = [i for i in os.listdir(source) if i.endswith(aext)]
    for f in files:
        if not os.path.exists(song_dir):
            os.makedirs(song_dir)

        try:
            shutil.move(path.join(source, f), song_dir)
            print("Audio moved successfully to ["+song_dir+"]")

        except shutil.SameFileError:
            print("Source and destination represents the same file.")

        except PermissionError:
            print("Permission denied.")

        except:
            print("Error occurred while copying file.")


    # --- Video ---
    files = [i for i in os.listdir(source) if i.endswith(vext)]
    for f in files:
        if not os.path.exists(vid_dir):
            os.makedirs(vid_dir)

        try:
            shutil.move(path.join(source, f), vid_dir)
            print("Video moved successfully to ["+vid_dir+"]")

        except shutil.SameFileError:
            print("Source and destination represents the same file.")

        except PermissionError:
            print("Permission denied.")

        except:
            print("Error occurred while copying file.")


while True:
    now = datetime.datetime.now()
    today = now.strftime("%d%b-%H%M")

    main()
    print('--- Updated at: ' + today + ' ---')
    time.sleep(300)                                         # Will run the code every 5 minutes

