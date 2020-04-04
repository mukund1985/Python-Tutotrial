# List Challange

# So, in the previous two videos we've talked about lists and
#
# figured out how they work in Python.
#
# So, what I'm gonna do now is just run you through another example
#
# of a more complicated version and then move onto a challenge.
#
# Now, what we're gonna do is we're gonna use a concept we've used earlier,
#
# which is a meal in a cafe.
#
# So, what I'm going to do is type in some code.
#
# I'm going to actually delete what
#
# we've got on the screen here because we don't need it anymore.
#
# And I'm going to start typing menu equals two empty square brackets,
#
# which is an empty list.
#
# Then we do menu.append.
#
# Notice the square brackets.
#
# Egg, spam, bacon.
#
# Bacon like so.
#
# So that's our first entry and I'm just gonna copy the first part of this so
#
# I can copy it and paste it rather than type it each time.
#
# The next menu option is going to be egg, sausage, bacon.
#
# Next one is going to be egg, and spam.
#
# Next one, egg, bacon, spam.
#
# Next one, egg, bacon,
#
# sausage, spam.
#
# Next one is going to be spam, bacon, sausage, and more spam.
#
# Oops.
#
# Then we're going to have two more here.
#
# Spam, egg, spam.
#
# Spam, bacon, spam.
#
# And the last one we're gonna have is spam,
#
# egg, sausage, spam.
#
# So first things first, you might be wondering why is there so
#
# much spam in these meals?
#
# Well, the menu's actually taken from a Monty Python sketch.
#
# And if you want to search the Internet for Monty Python spam sketch,
#
# then you can find out more about that.
#
# You actually watch it on YouTube as well when you feel you need to take a break.
#
# So incidentally that sketch is the reason we now refer to junk email as a spam.
#
# But anyway so what we've done here is we've actually created the empty list
#
# as you saw on line one.
#
# And we then went through and appended each of the meals to it.
#
# And of course each of the meals as you'll now see in square brackets is actually
#
# listed its own right containing the details of that meal.
#
# So we can actually print something out.
#
# We can type print Menu.
#
# Actually run that.
#
# We can actually see the entries.
#
# So it's a little bit hard to see because it's actually menus within menus,
#
# but you can sort of see that there's the first on there on the screen,
#
# separated by a comma, and they've each got their own square brackets to
#
# indicate they're actually each a list in their own right.
#
# Now that we've actually got a list and we've got a lot of entries.
#
# We can actually start writing a for loop and
#
# actually testing to see how the in operator works.
#
# So we could do something like for meal in menu.
#
# Then we could put if not spam
#
# in meal, print meal.
#
# So if we actually run this and
#
# I'll just comment out this first line here, just to remove the confusion.
#
# And what that should do, and what that actually does is only shows the entry
#
# which is on line three that doesn't contain spam.
#
# And again each of the items on the menu are themselves lists.
#
# So the for loop here initially, for meal in menu, is going through and
#
# grabbing a list with each iteration.
#
# So the first time it goes through the for
#
# loop, the meal variable is set to the list, which is the first list in the list.
#
# So to speak.
#
# And from there we can put if not spam in meal, and
#
# that's actually searching through that individual list, the list that of
#
# course is sort of a sub-list of a major list, if that makes sense.
#
# Then we're actually determining that that wasn't in there, and we're only printing
#
# out the contents if the word spam wasn't found as one of the list entries.
#
# So again, you can see that Python is extremely powerful,
#
# the way it's been designed and how it actually handles this, is like this.
#
# Okay, so it's time for a challenge.
#
# What I am going to do is go to the first line and paste in the challenge.
#
# And that should be without spam.
#
# So let's actually talk now about what the challenge is actually about.
#
# So what you need to do is add to the program below.
#
# So that if it finds a meal without spam in it,
#
# that it then prints out each of the ingredients of the meal.
#
# At this stage you can see that we printed out everything, but you need to actually
#
# go through each individual item, rather than just printing the entire list.
#
# So you'll need to set up the menu as we did in lines five to 13 there.
#
# So type that in to start with, and then you'll need to modify the for
#
# loop in some way.
#
# This code down here.
#
# So then, basically prints out each ingredient separately,
#
# rather than just printing out just the list as it's currently doing.
#
# Okay? So, pause the video.
#
# Go away and actually see if you can come up with a solution to that.
#
# When you're finished, come back and check my solution.
#
# Okay so how did you get under?
#
# Did you figure it out?
#
# So we're actually on the right track here.
#
# We've actually got a lot of the code in build already.
#
# So we've got the first loop the outside loop with is going through each meal
#
# that's in the menu list then grabbing that meal.
#
# So that needs to stay there.
#
# We also need to put the if not in there, so
#
# that we only get the meals that haven't got spam in them.
#
# And we can print out this initial list.
#
# We can leave that in there like we're seeing on the screen.
#
# But what we then need to do is iterate through the list of
#
# entries in this particular meal and print those out.
#
# So to do that, we stay at this indentation level cuz we're only processing a meal
#
# if it doesn't contain spam.
#
# And we type in for ingredient in meal,
#
# colon print ingredient, so that is literally it.
#
# So we are taking it to the next level we're actually now going through the list
#
# from the meal.
#
# So first, the outer entry, the initial for loop, that was the master list,
#
# the list of all the menus, whereas the inner list for ingredient in meals is just
#
# as you can see it's actually the ingredients within a specific list.
#
# So, if we actually run that now.
#
# We finally get the output egg, sausage, bacon, and
#
# we're getting that because there's only one entry in here that hasn't got spam..
#
# And then also, we're then cycling through that list that we retrieved, and
#
# actually printing out the individual items.
#
# So, that's it.
#
# That's the challenge, I hope you did well with that.
#
# And, I hope you've got a lot out of this section.

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

for meal in menu:
    if not "spam" in meal:
        print(meal)

# challange -

# if it find  a meal without spam it prints out each of the ingredients of the meal.


for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingredients in meal:
            print(ingredients)












