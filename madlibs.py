print("Mad libs where libs get mad.")
print("Start below:")

time = input("Enter a number from 1 to 12: ")
items = input("Enter a noun(plural): ")
name = input("Enter a name: ")
scream = input("Enter any sentence: ")
action = input("Enter a verb: ")

print("It was %s o'clock when I heard a knock at the door." % time)
print("I opened the door and there was a box full of %s with a note saying \"From Mr. %s.\"" % (items, name.title()))
print("Just as I closed the door I heard a scream \"%s.\"" % scream.upper())
print("I froze in place and all I could do was %s." % action)

# It was 6 o'clock when I heard a knock at the door.
#     I opened the door and there was a box full of dolls with a note saying "From Mr. Stephen Sedoll."
#     Just as I closed the door I heard a scream "THE FUTURE IS MADE OF DOLLS."
#     I froze in place and all I could do was shake my head.