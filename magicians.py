# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 8-9


def show_magicians(names):
    """
    This function loops through a list of names and returns the names of the people in the list.

    :param names: Gets passed a list on names of magicians
    :return: Individual names
    """

    while names:
        name = names.pop()
        print(name)


list_of_magicians = ["Elore",
                     "Andunorim",
                     "Trerius",
                     "Amaex",
                     "Judarin",
                     "Idijamar",
                     "Azahr",
                     "Oveflyn",
                     "Jenior",
                     "Dhubus"]
show_magicians(list_of_magicians)
