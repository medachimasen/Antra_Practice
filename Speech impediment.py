# Julius Caesar Act 4, Scene 3, 218–224
brutus_speech = "There is a tide in the affairs of men \nWhich, taken at the flood, leads on to fortune; \nOmitted, all the voyage of their life \nIs bound in shallows and in miseries. \nOn such a full sea are we now afloat, \nAnd we must take the current when it serves, \nOr lose our ventures."

# split into the different words
words = brutus_speech.split(" ")

# remove any \n or ,
this_word = 0
for word in words:
    
    this_word += 1

    # get rid of punctuation and new lines
    # (would be better to use translation table)
    word = word.replace(",","")
    word = word.replace(".","")
    word = word.replace("\n","")

    # turn to lower case
    word = word.lower()

    # write changes back to list
    words[this_word-1] = word

# show number of words
print(f"\nNumber of words = {len(words)}\n")

# loop over number of letters from 1 to 10
checksum = 0
for num in range(0,20):

    # show number of words with this many letters
    # (this uses a list comprehension - could do in more
    # long-winded loop instead)
    number_words = len([x for x in words if len(x) == num])
    if number_words > 0:
        checksum += number_words
        print(f"{num}-letter words = {number_words}")

# show the total
print(f"\nCheck total: {checksum}")