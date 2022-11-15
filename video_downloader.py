#!/usr/bin/env python3
from __future__ import unicode_literals
import pathlib
import youtube_dl
import os


def main(is_example=False, example_video_url=None) -> None:
    # *default video
    link = None
    currentdir_path = pathlib.Path(__file__).parent.resolve()
    if not is_example:
        link = input("Enter the link of video: ")
    else:
        link = example_video_url
        currentdir_path = os.path.join(currentdir_path, "example")
    if not os.path.exists("videos"):
        os.makedirs(os.path.join(currentdir_path, "videos"))
    ydl_opts = {
        'outtmpl': os.path.join(currentdir_path, "videos", '%(title)s.%(ext)s'),
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    except:
        print("Something wents wrong, try again or try another link")


if __name__ == "__main__":
    main()
