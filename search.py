# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import json
import logging

import googleapiclient.discovery

from developer_key import KEY

# logger = logging.getLogger("ROOT")
# logging.basicConfig(level=logging.DEBUG)


def videoListBySearch(
    search_string: str, NumberOfVideo: int = 50, regionCode: str = "US"
) -> dict:
    # Get logger
    logger = logging.getLogger("videoListBySearch")
    logging.basicConfig(level=logging.INFO)

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = KEY

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    if type(NumberOfVideo) != int:
        raise TypeError("NumberOfVideo must be an integer.")
    elif NumberOfVideo <= 0:
        raise ValueError("NumberOfVideo must be a positive integer.")
    elif 0 < NumberOfVideo <= 50:
        maxResults = NumberOfVideo
        pages = 1
    elif 50 < NumberOfVideo <= 10000:
        maxResults = 50
        if NumberOfVideo % 50 == 0:
            pages = int(NumberOfVideo // 50)
        else:
            pages = int(NumberOfVideo // 50) + 1
    else:
        raise ValueError("NumberOfVideo must less than 10000.")

    video_lst = dict()
    nextPageToken = ""

    while pages > 0:

        logger.info("Calling YouTube Search API")
        request = youtube.search().list(
            part="snippet",
            order="relevance",
            q=search_string,
            safeSearch="none",
            type="video",
            videoDefinition="any",
            maxResults=maxResults,
            pageToken=nextPageToken,
            regionCode=regionCode,
        )
        response = request.execute()

        try:
            nextPageToken = response["nextPageToken"]
            pages -= 1
        except:
            logger.error("No more next page")
            pages = 0

        items = response["items"]

        for i in items:
            id = i["id"]["videoId"]
            url = "https://www.youtube.com/watch?v=" + id
            title = i["snippet"]["title"]
            publishTime = i["snippet"]["publishTime"]
            channelTitle = i["snippet"]["channelTitle"]
            channelId = i["snippet"]["channelId"]

            logger.info(f"Getting Video: {title}")

            video_lst[id] = {
                "title": title,
                "url": url,
                "id": id,
                "publishTime": publishTime,
                "channelTitle": channelTitle,
                "channelId": channelId,
            }

    output_name = ""
    for i in search_string:
        if i == " ":
            output_name += "_"
        else:
            output_name += i

    with open(f"video_lst_{output_name}_{regionCode}.json", "w") as output:
        json.dump(video_lst, output, indent=4)

    logger.info(f"Search result saved in: 'video_lst_{output_name}_{regionCode}.json'")
    return video_lst


if __name__ == "__main__":
    search_string = "road accident video footage"
    video_lst = videoListBySearch(search_string, 300, "SG")
