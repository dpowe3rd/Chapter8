# Darrell Powe III
# # This is a practice exercise from the book "Python Crash Course"
# # Exercise 8-11


def show_magicians(names):
    """
    This function loops through a list of names and returns the names of the people in the list.

    :param names: Gets passed a modified list on names of magicians
    :return: Individual names
    """

    while names:
        name = names.pop()
        print(name)


def make_great(new):
    """
    This function loops through a list and modifies it, by adding 'The Great ' before their name, popping the item and
    adds it to another list.
    :param new: Gets passed a list on names of magicians
    :return:
    """
    while new:
        magician = 'The Great ' + new.pop() + '!'
        list_of_new_magicians.append(magician)


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
list_of_new_magicians = []

make_great(list_of_magicians[:])

print("-- List of Unchanged Magicians --\n")
show_magicians(list_of_magicians)

print("\n-- List of Changed Magicians --\n")
show_magicians(list_of_new_magicians)

