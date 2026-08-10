

def list_all_video(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def exit_app():
    pass

videos = []
while True:
    print("\n Youtube manager | choose an option  ")
    print("1. list of all youtube video ")
    print("2. Add a youtube video")
    print("3 update a youtube video details")
    print("4 delete a youtube video")
    print("5 Exit the app ")
    choice = input("enter you choice")

    match choice:
        case '1':
            list_all_video(videos)

        case '2':
            add_video(videos)

        case '3':
            update_video(videos)

        case '4':
            delete_video(videos)

        case '5':
            break

        case _:
            print("Invalid choice")
        

        