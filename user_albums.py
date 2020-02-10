# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 8-8


def make_album(artist_name, album_title, tracks=int(12)):
    """Creates a dictionary based on information given."""

    album = {'Artist': artist_name.title(), 'Album': album_title.title(), 'Track-Length': tracks}
    return album


while True:
    chk1 = input("Please enter a Artist. You may press 'q' to quit.")
    if chk1 == 'q':
        print('Thank you, have a good day.')
        break
    chk2 = input("Please enter a Album. You may press 'q' to quit.")
    if chk2 == 'q':
        print("Thank you, have a good day.")
        break
    chk3 = input("Optional: Please enter the amount of tracks. You may press 'q' to quit.")
    if chk3 == 'q':
        print('Thank you, have a good day.')
        break

    if chk3 == '':
        album1 = make_album(chk1, chk2)
        print(album1)

        resume = input("Do you want to continue?")
        if resume.lower() == 'yes':
            continue
        else:
            break

    else:
        album2 = make_album(chk1, chk2, int(chk3))
        print(album2)

        resume = input("Do you want to continue? Enter 'yes' or 'no'.")
        if resume.lower() == 'yes':
            continue
        elif resume.lower() == 'no':
            break
