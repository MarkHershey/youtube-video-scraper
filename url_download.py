import subprocess
import sys

cwd = os.path.dirname(os.path.abspath(__file__))
template = cwd + "/videos/%(id)s.%(ext)s"

video_link, threads = sys.argv[1]

subprocess.call(
    [
        "youtube-dl",
        "-o",
        template,
        "-f",
        "best[ext=mp4][height<=1080]/best[height<=1080]",
        video_link,
    ]
)
