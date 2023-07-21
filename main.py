def running_main_code(link):
    if link == "1":
        print()
        print("you have to selected Youtube option")

        import yt_project
    elif (link == "2"):
        print()
        print("you have selected Instagram option")
        print()

        import instagram
    else:
        print("select only 1 for youtube and 2 for instagram")
        link = input("-> ")
        running_main_code(link)

print("what do you want to select instagram or youtube")
print()
print("select 1 for Youtube")
print("select 2 for instagram")

selection_button = input("->")
print()
running_main_code(selection_button)