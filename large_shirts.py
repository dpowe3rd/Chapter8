# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 8-4


def make_shirt(color, size='large', text='I love Python'):
    """Take the parameters 'size', 'color', 'text', and uses them in as dimensions of a shirt
        which then prints a sentence about the shirt."""

    print('The shirt you want is a ' + size + ' sized, ' + color + " shirt that says '" + text + ", is this correct?")


make_shirt('green')
make_shirt('black', 'medium')
make_shirt('purple', text='Python is great!')
