# YouTube Video Scraper

YouTube Video Scraper using YouTube API & youtube-dl


### `search.py` Search for a certain amount of videos from given keywords


#### Require:

- Python 3.5 and above
- `pip3 install --upgrade google-api-python-client`
- `pip3 install --upgrade youtube_dl`

### `batch_download.py` downloads all videos from a video list like `video_lst_test.json`

#### Require:

- Python 3.5 and above
- [youtube_dl](https://github.com/ytdl-org/youtube-dl) or `pip3 install --upgrade youtube_dl`
- [aria2c](https://aria2.github.io/) (optional: for faster download)
- [FFmpeg](https://ffmpeg.org/) (optional: for format conversion)


### `url_download.py` downloads a video from given url

- Usage:
`python3 url_download.py https://www.youtube.com/watch?v=gHtrPzhKEhk`


### `merge.py` merges all video lists into one list to eliminate duplication.

- It merges all `video_lst_xxxxx.json` in the current directory into one `merged_video_lst.json`.
