# videoscreenshots_to_pdf
 
Hi! This python3 based application allows you to download videos from Youtube with a single link.
You get screenshots from the video at specific times and the application converts the screenshots into a pdf file.
This app can be very useful when you have a long video of a boring lecture but you want to save the showcased notes.

## JSON data example
```JSON
{
  "data": [
    {
      "fname": "video1.mp4",
      "screenshots": [
        "00:00:15",
        "00:02:30",
        "00:05:55"
      ]
    },
    {
      "fname": "video2.mp4",
      "screenshots": [
        "00:10:25",
        "00:12:36",
        "01:05:45"
      ]
    },
    ...
  ]
}
```

## How to use
- For downloading video -> 'video_downloader.py'
- if you want to create only a JSON file -> 'json_creater.py'
- if you want to create pdf use 'video_to_pdf.py', but if you want you can create JSON file also here
- currently works with mp4 video format

## Project idea from [Laszlo Szathmary](https://github.com/jabbalaci)
