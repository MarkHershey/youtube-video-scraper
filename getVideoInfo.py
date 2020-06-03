# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import json
import logging

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from developer_key import KEY

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def get_video_info_by_id(id: str):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    # client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"
    #
    # # Get credentials and create an API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #     client_secrets_file, scopes
    # )
    # credentials = flow.run_console()
    # youtube = googleapiclient.discovery.build(
    #     api_service_name, api_version, credentials=credentials
    # )

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=KEY
    )

    request = youtube.videos().list(part="contentDetails,status", id=id)
    response = request.execute()

    duration = response["items"][0]["contentDetails"]
    license = response["items"][0]["status"]["license"]
    return {"duration": duration, "license": license}


if __name__ == "__main__":
    main()
