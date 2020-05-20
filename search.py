# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import json

import googleapiclient.discovery

from developer_key import KEY


def videoListBySearch(search_string):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = KEY

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    request = youtube.search().list(
        part="snippet",
        order="relevance",
        q=search_string,
        safeSearch="none",
        type="video",
        videoDefinition="any",
        maxResults=50,
    )
    response = request.execute()

    items = response["items"]

    video_lst = []

    for i in items:
        id = i["id"]["videoId"]
        video_url = "https://www.youtube.com/watch?v=" + id
        video_title = i["snippet"]["title"]
        video_lst.append((id, video_url, video_title))

    with open("video_lst.json", "w") as output:
        json.dump(video_lst, output, indent=4)

    return video_lst


if __name__ == "__main__":
    search_string = "car crash compilation"
    video_lst = videoListBySearch(search_string)
    for index, video in enumerate(video_lst):
        print(f"{index+1} - {video[2]}")
