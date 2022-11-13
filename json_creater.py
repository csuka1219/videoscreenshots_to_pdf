#!/usr/bin/env python3
import json
from typing import List


class JsonData:
    def __init__(self) -> None:
        self.fname = None
        self.screenshots = []


def select_option_timestamp() -> str:
    """it will ask the user about his choice until the correct answer, then its returns with it"""
    print("-"*30)
    print("Select an option:")
    print("1. add timestamp          <1>")
    print("2. next                   <2>")
    answer = None
    while True:
        answer = input("input: ")
        if answer == "1" or answer == "2":
            break
    return answer


def select_option_video() -> str:
    """it will ask the user about his choice until the correct answer, then its returns with it"""
    print("-"*30)
    print("Select an option:")
    print("1. add video          <1>")
    print("2. done               <2>")
    answer = None
    while True:
        answer = input("input: ")
        if answer == "1" or answer == "2":
            break
    print("-"*30)
    return answer


def timestamp_checker(stamp: str) -> bool:
    """check if the timestamp has the correct form, and return with a logical type"""
    try:
        h, m, s = stamp.split(":")
        if not str.isdigit(h) or not str.isdigit(m) or not str.isdigit(s):
            return False
        if len(h) != 2 or len(m) != 2 or len(s) != 2:
            return False
        if int(h) > 23 or int(m) > 59 or int(s) > 59:
            return False
        return True
    except:
        return False


def get_timestamp() -> str:
    """it will ask the user about the needed timestamp until the correct answer, then its returns with it"""
    while True:
        new_screenshot_stamp = input(
            "Enter timestamp in hh:mm:ss format: ")
        if timestamp_checker(new_screenshot_stamp):
            break
    return new_screenshot_stamp


def fill_data() -> List[JsonData]:
    """it fills a type of JsonData list, with the name of videos and its timestamps, and returns with it"""
    li = []
    while True:
        curent_data = JsonData()
        curent_data.fname = input("Enter the filename of the video: ")
        new_screenshot_stamp = get_timestamp()
        curent_data.screenshots.append(new_screenshot_stamp)
        while True:
            answer = select_option_timestamp()
            if answer == "1":
                new_screenshot_stamp = get_timestamp()
                curent_data.screenshots.append(new_screenshot_stamp)

            if answer == "2":
                break
        li.append(curent_data)
        answer = select_option_video()
        if answer == "2":
            break
    return li


def write_json(json_li: List[JsonData]) -> None:
    """it creates json file from the type of JsonData list"""
    with open("videodata.json", "w") as outfile:
        json.dump({"data": [ob.__dict__ for ob in json_li]}, outfile)


def start() -> None:
    json_li = fill_data()
    write_json(json_li)


if __name__ == "__main__":
    start()
