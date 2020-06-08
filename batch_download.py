# Requirements:
#   youtube-dl (pip install youtube_dl)
#   aria2c (optional)

import subprocess
import json
import os
from pathlib import Path


def download(
    video_lst: dict,
    aria: bool = False,
    threads: int = 8,
    output_path: str = "cwd",
    clear_cache: bool = False,
):

    # Clear cache for youtube-dl
    # Enable this when you encounter some error with youtube-dl
    if clear_cache:
        subprocess.call(
            ["youtube-dl", "--rm-cache-dir",]
        )

    if isinstance(threads, int):
        threads = str(threads)
    elif isinstance(threads, str) and threads.isdigit():
        try:
            threads = int(threads)
            threads = str(threads)
        except:
            print("threads should be a integer")
            return
    else:
        return

    if output_path == "cwd":
        base_path = str(Path.cwd())
    else:
        base_path = Path(output_path)
        if base_path.is_dir():
            base_path = str(base_path)
        else:
            print("Invalid output_path")
            return

    for index, video in enumerate(video_lst.values()):
        id = video["id"]
        url = video["url"]
        title = video["title"]

        template = base_path + "/videos/%(id)s.%(ext)s"

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
    with open("merged_video_lst_from_six_channels.json", "r") as file:
        video_lst = json.load(file)

    # call download
    download(video_lst, aria=True, output_path="/Volumes/MARK_HFS+_2T/UROP/verified")
