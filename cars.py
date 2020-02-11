# Darrell Powe III
# # This is a practice exercise from the book "Python Crash Course"
# # Exercise 8-14


def make_cars(make, model, **features):
    car = {}
    car['Make'] = make
    car['Model'] = model
    for k, v in features.items():
        car[k] = v

    print(car)


make_cars("Honda", "Accord Coupe", sunroof='True', luxurypackage='True')
