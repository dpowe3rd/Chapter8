# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 8-7


def make_album(artist_name, album_title, tracks=int(12)):
    """Creates a dictionary based on information given."""

    album = {'name': artist_name.title(), 'album': album_title.title(), 'length': tracks}
    return album


aboogie = make_album('a-Boogie', 'Artist', 16)
micheal = make_album('micheal jackson', 'bad')
ski = make_album('ski mask the slump god', 'stokley', 20)

print(aboogie)
print(micheal)
print(ski)