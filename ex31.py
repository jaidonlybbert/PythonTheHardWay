# Jaidon Lybbert
# June 28, 2019
# LPTHW ex31

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a bear eating cheesecake. Wat do?"
    print "1. Take cake"
    print "2. Scream at Bear"

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face."
    elif bear == "2":
        print "The bear eats your legs."
    else:
        print "You survived."

elif door == "2":
    print "etc. etc. stuff happens."
