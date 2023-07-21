import instaloader
def instagram(link):
    loader = instaloader.Instaloader()
    if (link == "1"):
        instagram_Id(loader)
    elif(link == "2"):
        instagram_post(loader)
    else:
        print("Enter 1 for insta ID and 2 for insta post Link")
        print()
        instagram_option = input("-> ")
        instagram(instagram_option)
def instagram_Id(loader):
    # download  all the post and dp....
    # user like = _ajhar_alam
    print()
    user_insta_ID = input("Please Enter your Instagram ID :- ")
    print()

    print("what do you want to download ?")
    print("if you want to download dp only press 1")
    print("if you want to download Post onl press 2 ")
    print("if press another button/value then download only dp")
    print()

    is_only_for_dp = input("->"). strip()
    print()
    print("downloading dp .................")

    if is_only_for_dp == "2":
        is_only_for_dp = False
    else:
        is_only_for_dp = True

    try:
        loader.download_profile(user_insta_ID,profile_pic_only = is_only_for_dp)
        print("Downlod sucessfully...")
        print()
    except:
        print()
        print("Error : faild to download instagram dp")

def instagram_post(loader):
    post_link = input("Enter here instagram Post Link: - ")
    print()
    print("gathering details")

    post = instaloader.Post.from_shortcode(loader.context,post_link.split("/")[-2])

    # post caption of instagram post
    caption = post.caption
    print("caption: ",caption)
    number_of_likes = post.likes
    print("number_of_likes: ", number_of_likes)
    print()

    print("if you want to download post videos")
    print("Please Enter YES or NO")

    instagram_post_download = input("-> ").strip()
    if instagram_post_download == "YES":
        print()
        print("instagram post Downloading.......")

        loader.download_post(post,target='post')
        print()

        print("successfully downloaded")
        print()
    else:
        exit()


instagram_option = input("Enter 1 for insta ID and 2 for insta post Link")
instagram(instagram_option)