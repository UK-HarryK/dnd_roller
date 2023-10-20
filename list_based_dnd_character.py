import random # it is best practice to import any required modules at the top of your file. They will be loaded first

# Okay, let's define some requirements. First off, we want this app to have as few lines of code as possible (comments notwithstanding)
# Secondly, we need to use lists. Python has a few different types of arrays, lists, tuples and sets. I will try to use all three
# Thirdly, we want to repeat ourselves as little as possible. This will require functions.
# And finally, we need our app to role DnD characters! I'm only going to refactor the behaviour of your original code, I won't be adding anything

# So the first thing we need to do is define our traits. These will not change, we simply want to refer to them.
# For this reason, a tuple makes the most sense. These are arrays that are ordered and unchangeable.

sex = ("Male", "Female")

races = ("Elf", "Human", "Tiefling", "Dwarf")

personalities = ("Abrasive", "Absent Minded", "Agressive")

bard_subs = ("Bard", "College of Creation", "College of Eloquence", "College of Lore")

paladin_subs = ("Paladin", "Eldritch Knight", "Holy Knight", "Blood Knight")

warlock_subs = ("Warlock", "Fiend", "Celestial", "Fathomless")

rogue_subs = ("Rogue", "Cutthroat", "Assassin", "Thief")

classes = (rogue_subs, warlock_subs, paladin_subs, bard_subs) # It should be noted that class is a reserved keyword, hences classes

variables = {sex, races, personalities, classes}

# Here we can see that instead of defining the classes individually, we can define the class and subclasses in the same tuple. As tuples cannot be changed
# and are ordered, we can reliably access the class, and avoid it when rolling subclass
# Indexed means we can access the values can be accessed by their position in the list, starting at 0. So, sex[0] is equal to "Male". Lists and tuples are indexed, sets are not

# Now we can define a couple of functions that will allow us to repeatably roll characters

def class_roller(arr):
    d = len(arr) # As mentioned previously, arrays are indexed from 0. len(arr) counts the length of the array from 1, and the random.randrange() defaults to start at 0, but WILL NOT INCLUDE the given number in the number generation
    r = random.randrange(1, d) # As shown earlier, we wouldnt want to roll for the first entry in each subclass tuple, as this is reserved to tell us which class has been rolled
    sub = arr[r]
    return [sub, arr[0]] # We return a list, with the class and subclass



def die_roller(arr): # In the spirit of DRY, we are defining a function that will allow us to roll the die based on the array
    d = len(arr)
    r = random.randrange(d)
    if type(arr[0]) is tuple: # This if statement checks to see if the tuple we are rolling contains tuples, and therefore is rolling class and subclass
        return class_roller(arr[r])
    return arr[r]

character = []

for x in variables:
    character.append(die_roller(x))

print(character)