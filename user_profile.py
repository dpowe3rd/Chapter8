# Darrell Powe III
# # This is a practice exercise from the book "Python Crash Course"
# # Exercise 8-13


def build_profile(first, last, **user_info):
    profile = {'First Name': first.title(), 'Last Name': last.title()}
    for k, v in user_info.items():
        profile[k] = v
    print(profile)


build_profile("darrell", "powe", Location="Bronx", Occupation="Manager", FavoriteFood="Lomo")
