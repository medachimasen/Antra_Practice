# take input of house
house_name = input("Which house are you in? ")

# standardize letters
house_name = house_name.lower()

# get house colours
if house_name == "gryffindor":
    house_colours = "scarlet and gold"
elif house_name == "hufflepuff":
    house_colours = "yellow and black"
elif house_name == "ravenclaw":
    house_colours = "blue and bronze"
elif house_name == "slytherin":
    house_colours = "green and silver"
else:
    house_colours = "Not known"

# print color
print("Your house colours are ...\n\n" + house_colours)
    
