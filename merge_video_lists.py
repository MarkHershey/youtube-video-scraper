import os
import json
from pathlib import Path

from authorised_channels import authorised_channels


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
    total_video_count = 0

    authorised_video_lst = dict()
    authorised_video_count = 0

    channel_lst = dict()
    total_channel_count = 0
    authorised_channel_count = len(authorised_channels.keys())

    for index, filename in enumerate(os.listdir(FOLDER_PATH)):
        # if filename[-5:] == ".json" and filename[:10] == "video_lst_":
        # if filename[-5:] == ".json" and filename[:18] == "channel_video_lst_":
        if filename[-5:] == ".json":
            filepath = FOLDER_PATH / filename

            with filepath.open() as file:
                # load the sub list
                video_lst_tmp = json.load(file)
                for id, content in video_lst_tmp.items():

                    channelTitle = content["channelTitle"]
                    channelId = content["channelId"]

                    if id in video_lst:
                        pass
                    else:
                        video_lst[id] = content
                        total_video_count += 1

                        if channelId in authorised_channels.keys():
                            authorised_video_lst[id] = content
                            authorised_video_count += 1

                        if channelId in channel_lst:
                            channel_lst[channelId]["downloaded_video_count"] += 1
                        else:
                            total_channel_count += 1
                            channel_lst[channelId] = {
                                "channelTitle": channelTitle,
                                "channelId": channelId,
                                "downloaded_video_count": 1,
                                "authorised": False,
                            }

    # print channels and video count
    sorted_ids = sorted(
        channel_lst.keys(),
        key=lambda x: channel_lst[x]["downloaded_video_count"],
        reverse=True,
    )
    print("\nchannelTitle: downloaded_video_count\n")
    for id in sorted_ids:
        print(
            f"{channel_lst[id]['channelTitle']}: {channel_lst[id]['downloaded_video_count']}"
        )

    # write to json files
    merged_video_lst_fp = FOLDER_PATH / "merged_list" / "merged_video_lst.json"
    channels_lst_fp = FOLDER_PATH / "merged_list" / "channels_lst.json"
    authorised_video_lst_fp = FOLDER_PATH / "merged_list" / "authorised_video_lst.json"

    with merged_video_lst_fp.open(mode="w") as output:
        json.dump(video_lst, output, indent=4)

    with channels_lst_fp.open(mode="w") as output:
        json.dump(channel_lst, output, indent=4)

    with authorised_video_lst_fp.open(mode="w") as output:
        json.dump(authorised_video_lst, output, indent=4)

    print("\n\n\n\n>>>>>>>>")
    print(f"total_video_count: {total_video_count}")
    print(f"authorised_video_count: {authorised_video_count}")
    print(f"total_channel_count: {total_channel_count}")
    print(f"authorised_channel_count: {authorised_channel_count}")


if __name__ == "__main__":
    # merge()
    merge("/Users/mark/Documents/CODE/youtube-video-scraper/video_lists", True)
