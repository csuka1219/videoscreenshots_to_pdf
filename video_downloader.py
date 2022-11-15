#!/usr/bin/env python3
from __future__ import unicode_literals
import pathlib
import youtube_dl
import os


def main(is_example=False) -> None:
    # test 10mp video: https://www.youtube.com/watch?v=BaW_jenozKc
    link = "https://www.youtube.com/watch?v=h9a-jL_uY38"
    currentdir_path = pathlib.Path(__file__).parent.resolve()
    if not is_example:
        link = input("Enter the link of video: ")
    else:
        currentdir_path = os.path.join(currentdir_path, "example")
    if not os.path.exists("videos"):
        os.makedirs(os.path.join(currentdir_path, "videos"))
    ydl_opts = {
        'outtmpl': os.path.join(currentdir_path, "videos", '%(title)s.%(ext)s'),
    }
    # *default video

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    except:
        print("Something wents wrong, try again or try another link")


if __name__ == "__main__":
    main()
