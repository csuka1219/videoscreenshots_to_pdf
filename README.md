# videoscreenshots_to_pdf
 
Hi! This python3 based application allows you to download videos from the Youtube with a single link and then get screenshots from the video at specific time and finally the application convert the screenshots into a pdf file.
This application can be very useful when you have a long video of a boring lecture but you want to save the ppt-s.

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

