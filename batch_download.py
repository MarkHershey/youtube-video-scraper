# Requirements:
#   youtube-dl (pip install youtube_dl)
#   aria2c (optional)

import subprocess
import json
import os

cwd = os.path.dirname(os.path.abspath(__file__))


def download(video_lst: list, aria=False, threads="8", debug=False):

    # Clear cache for youtube-dl
    # Enable this when you encounter some error with youtube-dl
    if debug:
        subprocess.call(
            ["youtube-dl", "--rm-cache-dir",]
        )

    for index, video in enumerate(video_lst.values()):
        id = video["id"]
        url = video["url"]
        title = video["title"]

        template = cwd + "/videos/%(id)s.%(ext)s"

        print(f"\n---------------<Video: {index + 1} >---------------")
        if aria:
            subprocess.call(
                [
                    "youtube-dl",
                    "-o",
                    template,
                    "-f",
                    "best[ext=mp4][height<=1080]/best[height<=1080]",
                    "--external-downloader",
                    "aria2c",
                    "--external-downloader-args",
                    "-x" + threads,
                    url,
                ]
            )
        else:
            subprocess.call(
                ["youtube-dl", "-o", template, "-f", "best[ext=mp4]/best", url,]
            )


if __name__ == "__main__":
    with open("test.json", "r") as file:
        video_lst = json.load(file)

    # call download
    download(video_lst, aria=True, debug=False)
