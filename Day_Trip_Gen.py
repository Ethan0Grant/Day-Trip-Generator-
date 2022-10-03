import random as r

greeting_message = "Welcome! Thank you for using the day trip generator!"
print(greeting_message)


#LIST OF FEATURES 
locations = ["Killington, Vermont", "Orlando, Florida", "Los Angeles, California", "Gatlinburg, Tennessee", "New York, New York"]
restaurants = ["Waffle House", "The BBQ Shack", "Antonino Bertolo's Pizza", "Japan House", "Mcdonalds"] 
transportation = [ "Walking", "Bicycle", "Car", "Airplane", "Bus"]
entertainment =  ["Amusement Park", "The Beach", "Movie Theater", "The Zoo", "Hiking"]


options = {"location": locations, "restaurant": restaurants, "transportation": transportation, "entertainment": entertainment}
selections = {"location":None, "restaurant":None, "transportation":None, "entertainment":None}




def generate_trip():
    for key in selections.keys():
        selections[key] = r.choice(options[key])


def regenerate_item(category):
    if category not in options.keys():
        return "Invalid category. Please review trip."

    else:
        rerolled = False
        while not rerolled:
            pick = r.choice(options[category])
            if pick  != selections[category]:
                rerolled = True
            selections[category] = pick
        return "Sucessfully regenerated {}.".format(category)


def print_trip():
    print("Location: {}\nRestaurant: {}\nTransportation: {}\nEntertainment: {}".format(selections["location"], selections["restaurant"], selections["transportation"], selections["entertainment"]))

generate_trip()


satisfied = False

while not satisfied:
    print_trip()
    user_response = input("Are you satisfied wuth your trip? (Y/N): ")
    if user_response.lower() == "y":
        satisfied = True
        print("Enjoy your trip!")
    elif user_response.lower() == "n":
        category = input("Which category are you not satisfied with? ")
        print(regenerate_item(category.lower()))
    else:
        print("Invalid response. Please review trip")