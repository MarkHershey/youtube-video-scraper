import os
import json


def main():
    FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
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
            if filename[-5:] == ".json" and filename[:10] == "video_lst_":
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
    main()
