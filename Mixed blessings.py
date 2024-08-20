# get a list of the primary colours
tubbie_colours = ["red", "green", "blue"]

# get your favourite film
fave_film = "The Book of Fish"

# create a tuple containing all these items
# plus your lucky number
mish_mash = (tubbie_colours,fave_film,5)

# enumerate function
for item_number, item in enumerate(mish_mash):
    print("Item {0} has type {1}: {2}".format(
        item_number, type(item), repr(item)))
