from pytube import YouTube

def display_video_stats(yt):
    length_mins = yt.length / 60
    print("Title: %s" % yt.title)
    print("Description - %s" % yt.description)
    print("Rating: %.1f" % yt.rating)
    print("Approx length of video: %d mins" % length_mins)
    print("Number of views: %s" % yt.views)

def get_high_quality_video(streams):
    return streams.get_highest_resolution()

def download_video(video):
    print("Downloading..")
    video.download()
    print("Download completed")

def main():
    print("Enter link: ")
    link = input()
    yt = YouTube(link)
    display_video_stats(yt)
    video = get_high_quality_video(yt.streams)
    download_video(video)

if __name__ == "__main__":
    main()