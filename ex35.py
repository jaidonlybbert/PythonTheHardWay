# Jaidon Lybbert
# June 28, 2019
# LPTHW ex35

def gold_room():
    print "You enter a room full of gold. How much do you take?"

    input = raw_input("> ")
    try:
        howMuch = int(input)
    except:
        print "That is not a number!"
        exit(0)
    if howMuch < 50:
        print "A humble man, you win!"
        exit(0)
    else:
        print "You lose"

while(True):
    gold_room()
