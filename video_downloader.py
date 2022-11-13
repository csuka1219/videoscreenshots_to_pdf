#!/usr/bin/env python3
from __future__ import unicode_literals
import youtube_dl
import os


def main() -> None:
    # test 10mp video: https://www.youtube.com/watch?v=BaW_jenozKc
    currentdir_path = os.getcwd()
    if not os.path.exists("videos"):
        os.makedirs("videos")
    ydl_opts = {
        'outtmpl': os.path.join(currentdir_path,"videos", '%(title)s.%(ext)s'),
    }
    print("Enter the link of video: ", end="")
    link = input()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


if __name__ == "__main__":
    main()
