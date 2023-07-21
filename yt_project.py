import pytube
check = "1"
while check =="1":
    print()
    youtube_link = input("Please Enter YouTube videos Link : - ")

    youtube_1 = pytube.YouTube(youtube_link)

    print()
    print("Videos Title : ", youtube_1.title)
    print("Videos_ views : ", youtube_1.views)
    print("channel_link : ", youtube_1.channel_url)
    print("Description of videos :", youtube_1.description)
    print("channel id : ", youtube_1.channel_id)
    print("Videos publish date : ", youtube_1.publish_date)

    print()
    print("If want to doenlaod videos")
    print("Please Enter YES or NO")

    youtube_video = input("->")

    if youtube_video == "YES":
        print("Video downloading in progress....")

        videos = youtube_1.streams.all()
        vid = list(enumerate(videos))
        for i in vid:
            print(i)