from hogwarts import Hogwarts
from hogwarts.model import Wizard

castle = Hogwarts.makeHogwarts()
wizards = castle.wizards()

print "Wizards:    ", wizards
#print "Names:      "
#print "Photos:     "
#print "Friendly:   "
#print "Hufflepuffs:"
#print "Lex last:   "

########

#def name(wizard):
#    return wizard.getName()
#
#def inHouse(house):
#    return lambda wizard: wizard.house == house
#
#def greaterBy(fn):
#    return lambda a, b: a if fn(a) > fn(b) else b
#
#print "Wizards:    ", wizards
#print "Names:      ", map(name, wizards)
#print "Photos:     ", map(Wizard.getPhoto, wizards)
#print "Friendly:   ", filter(lambda w: w.getFriends().size() > 2, wizards)
#print "Hufflepuffs:", len(filter(inHouse(House.Hufflepuff), wizards))
#print "Lex last:   ", reduce(greaterBy(name), wizards)
