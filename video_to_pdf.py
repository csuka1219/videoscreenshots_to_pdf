#!/usr/bin/env python3
import pathlib
import sys
import cv2 as cv
import os
import json
import json_creater
from PIL import Image
import re

currentdata_folders = []


def convert_toms(time: str) -> int:
    """it returns with the length of timestamp in milliseconds"""
    hour, minute, second = time.split(":")
    milliseconds = 0
    milliseconds += int(hour) * 60 * 60 * 1000
    milliseconds += int(minute) * 60 * 1000
    milliseconds += int(second) * 1000
    return milliseconds


def get_screenshots(is_example=False) -> None:
    """It gets screenshots from the videos at the specific time, and saves it into the 'screenshost/{videoname}' folder"""
    currentdir_path = pathlib.Path(__file__).parent.resolve()
    json_fname = "videodata.json"
    if is_example:
        currentdir_path = os.path.join(
            currentdir_path, "example")
        json_fname = os.path.join(
            currentdir_path, "exampledata.json")
    with open(json_fname, "r") as infile:
        # * we load the data in a dictionary
        json_data = json.load(infile)
        for data in json_data['data']:
            # * currentdata_folders contains the name of videos that is in the json file
            foldername = get_cleantext(data['fname'])
            currentdata_folders.append(foldername)
            # * this opencv method will open the video
            video = cv.VideoCapture(
                os.path.join(currentdir_path, "videos", data['fname'])+".mp4")
            # * we iterate through the timestamps and create screenshot at that time
            for time in data["screenshots"]:
                # * we convert the timestamp into milliseconds
                milliseconds = convert_toms(time)
                # * this opencv method goes fast forward to the previously got millisecond in the video
                video.set(cv.CAP_PROP_POS_MSEC, milliseconds)
                # * we get that frame and save it into png
                frame = video.read()[1]
                if not os.path.exists(os.path.join(currentdir_path, "screenshots", foldername)):
                    os.makedirs(os.path.join(currentdir_path,
                                "screenshots", foldername))
                a = cv.imwrite(os.path.join(currentdir_path, "screenshots",
                                            foldername, f"screenshot-{str(time).replace(':','_')}.png"), frame)
                pass


def get_cleantext(s):
    """cleans the string from special characters"""
    return re.sub('[^A-Za-z0-9]+', '', s)


def create_pdf(is_example=False) -> None:
    """It creates a pdf from the png-s of the videos that is in the current json file"""
    list_png = []
    currentdir_path = pathlib.Path(__file__).parent.resolve()
    if is_example:
        currentdir_path = os.path.join(currentdir_path, "example")
    for foldername in currentdata_folders:
        png_path = os.path.join(currentdir_path, "screenshots", foldername)
        list_png.extend([Image.open(os.path.join(png_path, f))
                         for f in os.listdir(png_path) if f.endswith(".png")])
    pdf_name = "out.pdf"
    if is_example:
        pdf_name = os.path.join(currentdir_path, "out.pdf")
    list_png[0].save(pdf_name, "PDF", resolution=100.0,
                     save_all=True, append_images=list_png[1:])


def select_option_json() -> str:
    """it will ask the user about his choice until the correct answer, then its returns with it"""
    print("-"*30)
    print("Select an option:")
    print("1. create new json file          <1>")
    print("2. use the current json file     <2>")
    answer = None
    while True:
        answer = input("input: ")
        if answer == "1" or answer == "2":
            break
    print("-"*30)
    return answer


def main() -> None:
    # * if the json file already exists, the program will ask whether to use this one or create new one
    if os.path.exists("videodata.json"):
        answer = select_option_json()
        if answer == "1":
            json_creater.start()
    else:
        json_creater.start()
    # * it creates 'screenshots' folder if doesn't exist
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    # * it creates 'videos' folder if doesn't exist
    if not os.path.exists("videos"):
        os.makedirs("videos")
    try:
        print("started to export to screenshots")
        # * this method creates the png-s from the videos
        get_screenshots()
        # * this method creates the pdf of the screenshots
        create_pdf()
        print("export finished successfully")
    except:
        # * this exception usually happens, when the timestamp in the json file is bigger than the length of the video, or the json file is corrupted
        print("Error, probably there are some problem with your json file",
              file=sys.stderr)


if __name__ == "__main__":
    main()
