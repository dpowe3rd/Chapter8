# Darrell Powe III
# # This is a practice exercise from the book "Python Crash Course"
# # Exercise 8-12


def make_sandwich(*condiments):
    print("You want a sandwich with: ")
    for condiment in condiments:
        print("- " + condiment.title() + "!")


make_sandwich("roast beef", "mayo", "cheese", "avocado", "bacon")
print("\n")
make_sandwich("chicken", "lettuce")
print("\n")
make_sandwich("peanut butter", "jelly", "white bread")
