
def main():
    video_downloader.main(is_example=True)
    video_to_pdf.get_screenshots(is_example=True)
    video_to_pdf.create_pdf(is_example=True)


if __name__ == "__main__":
    import sys
    from os import path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    import video_downloader
    import video_to_pdf
    main()
