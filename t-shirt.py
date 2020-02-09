# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 8-3


def make_shirt(size, color, text, font):
    """Take the parameters 'size', 'color', 'text', and 'font' and uses them in as dimensions of a shirt
    which then prints a sentence about the shirt."""

    print('The shirt you want is a ' + size + ' sized, ' + color + " shirt that says '" + text + "' in '" + font +
          "' font, is this correct?")


make_shirt('medium', 'black', 'Python is great!', 'Old Fashioned')

make_shirt(font='Times New Roman', size='large', text='Python is great!', color='green')
