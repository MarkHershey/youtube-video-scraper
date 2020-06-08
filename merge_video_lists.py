import os
import json
from pathlib import Path


def merge(folder: str = "", debug: bool = False):

    cwd = Path.cwd()

    if folder == "":
        FOLDER_PATH = cwd
        print(f"Path: {FOLDER_PATH}")
    else:
        FOLDER_PATH = Path(folder)
        if FOLDER_PATH.is_dir():
            print(f"Path: {FOLDER_PATH}")
        else:
            print("Invalid Path")
            return

    video_lst = dict()
    video_count = 0
    debug = False

    for dirpath, dirnames, filenames in os.walk(FOLDER_PATH, topdown=True):
        if debug:
            print("-------------------------------------------------------------------")
            print(f"Current directory: {dirpath}")
            print(f"# sub-directories: {len(dirnames)}")
            print(f"# files in current directory: {len(filenames)}\n")

        for index, filename in enumerate(filenames):
            # if filename[-5:] == ".json" and filename[:10] == "video_lst_":
            # if filename[-5:] == ".json" and filename[:18] == "channel_video_lst_":
            if filename[-5:] == ".json":
                print(os.path.join(dirpath, filename))
                with open(os.path.join(dirpath, filename), "r") as file:
                    video_lst_tmp = json.load(file)
                    for id, content in video_lst_tmp.items():
                        if id in video_lst:
                            pass
                        else:
                            video_lst[id] = content
                            video_count += 1
                            print(video_count)

    with open("merged_video_lst.json", "w") as output:
        json.dump(video_lst, output, indent=4)


if __name__ == "__main__":
    # merge()
    merge("/Users/mark/Documents/CODE/youtube-video-scraper/video_lists", True)
