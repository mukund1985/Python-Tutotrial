# So, now it's time to talk about tuples.
#
# And what tuples are is a term for an ordered set of data.
#
# Now, in Python, tuples are similar to lists which we've already talked about.
#
# But the difference here is that they're immutable.
#
# And what that means is they can't be changed.
#
# So, in other words,
#
# attempting to append an item to a tuple will actually give you an error.
#
# Now, you might have read that definition stated that
#
# lists are enclosed in square brackets, and that's true, and you've seen that.
#
# And that tuples are enclosed in parentheses, but that is not true.
#
# So, a comma is used to separate the elements of a tuple, but
#
# the parentheses are only required when necessary to remove syntactic ambiguity.
#
# So, I'm gonna show you an example of what I mean.
#
# I can put my space here.
#
# So I'm gonna type t = "a", "b", "c",
#
# print(t) print("a", "b",
#
# "c") print A.
#
# B. C.
#
# So, if we actually run that, if you've seen the first example,
#
# the answer is returned in brackets, and that signifies that it is a double, and
#
# also the third example Shows that it's a tuple as well and
#
# you can see why the second example the one on line four.
#
# That's actually just returned the letters a, b, c and that's an example of having to
#
# use parentheses to actually avoid syntactic ambiguity.
#
# So, in other words print will also accept parameters followed by a comma.
#
# So, if you do want to print out a tuple then you'd need to actually put brackets
#
# there as an example.
#
# So, this also applies when you're actually passing a tuple tool function and
#
# as we've seen earlier enclosing an expression in parentheses allows it to be
#
# split over several lines without using line continuation characters.
#
# So, sometimes enclose our tuples in them as well for that reason.
#
# Now, you might prefer to always do so, and that's fine.
#
# Just be aware that if you come across code that does not use parenthesis,
#
# then you'll need to understand what that is.
#
# So, it's up to you.
#
# Probably what I would recommend is to actually
#
# use brackets as much as possible like this when creating a tuple.
#
# Again, we're gonna go through a bit more about what tuples are as we go
#
# through this video but the choice is up to you and you will see examples.
#
# Like the example I started with, like this example here, where they're not enclosed
#
# in parentheses but they're still actually tuples and you need to be aware of that.
#
# Before I continue And this is a digress.
#
# What I want to do, we haven't actually mentioned this before, but
#
# you can also pass a comma separated list of items to the print function, and
#
# it'll print them all on the same line.
#
# And what I mean by that, we're going to actually type some code in to show you.
#
# Let me comment out this code for now.
#
# So, let's start by creating some tuples.
#
# So, first one is welcome = "Welcome to my
#
# Nightmare" Alice Cooper, 1975.
#
# This is a tuple.
#
# Now, notice how it's a different type on the end.
#
# Oops, I've got my equals and so forth done correctly.
#
# And notice how you can have, actually,
#
# different data types on the one line with the tuple.
#
# And we'll do something like this,
#
# bad equals "Bad Company" "Bad Company",
#
# 1974 budgie = Nightflight
#
# 1981 and Imelda
#
# [SOUND] 2011 and
#
# Metallica Ride the Lightning.
#
# 1984.
#
# So, we can actually print Metallica like so.
#
# We can actually run that.
#
# And you can see when we just print it it actually prints out the entire topple.
#
# But, we can also do print Metallica[0] in square brackets.
#
# And we run that.
#
# And surprisingly, we get the first element.
#
# And we can also do the same for the other two.
#
# We can print those separately.
#
# So, we can go like so, 1, and let's put that on a new line, 2.
#
# And we run that.
#
# We get the other elements printing them individually.
#
# But the point I want to make, as I mentioned at the start of the video,
#
# is that tupples are immutable.
#
# So, any attempt to change them,
#
# in this case a Metallica album to say Master of Puppets, would give an error.
#
# So, we can actually do something like that.
#
# We can try typing metallica[0], element 0, = "Master of Puppets".
#
# If we actually run that,
#
# we actually get an error, tuple object does not support item assignment.
#
# So, you can't actually change it in that fashion.
#
# Now, the good thing now is tuples actually support indexing and
#
# slicing, which is sort of a sneaky way of actually correcting any problems or
#
# updating particular entries.
#
# So, for example, I made a typo on line nine.
#
# With the actual name, Imelda Mae.
#
# So, if I've got to change that I can actually type something
#
# like imelda equals imelda.
#
# And we can put 0.
#
# If we actually run that, unless you print that out afterwards, print imelda,
#
# just to make sure it's actually working.
#
# So, if I actually run that,
#
# actually what we want to do is get rid of this error line first now.
#
# So, that that code actually executes.
#
# So, I'll comment that out, run that again.
#
# We actually get more my hand, Emilda May this time,
#
# remembering that initially I actually put it through incorrectly.
#
# It's Emilda, with an E on the start.
#
# So, I've actually got the values correctly added to the, or
#
# updated I should say in the middle of the tuple.
#
# So actually there's two important concepts here.
#
# Firstly, a type being immutable means that you can't change the contents of an object
#
# once you've created it.
#
# But, it doesn't mean that your variable Can't be assigned
#
# a new object of that type, so that's an important clarification here.
#
# So, just to confirm the differences between a immutable object,
#
# an mutable one, an mutable one being changeable,
#
# immutable meaning you can't change consider this current I'm going to add.
#
# So we are going to create a new
#
# one metallic2 equals,
#
# and I'm creating a list this
#
# time instead of a tuple,
#
# lightning [NOISE] Teleca two And
#
# print metallica2.
#
# So, we've created a list there, just to show you the differences.
#
# So, course in the case of the list, that should be metalica2 there, because I'm
#
# updating the list here, in this particular group of code, block of code.
#
# Run that again.
#
# So, in the case of lines 21 to 24, we're working with a list.
#
# And you can see that I was able to directly change the element zero,
#
# the album name, and it worked quite Quite nicely.
#
# But of course in the case above when this error are here when I actually
#
# ran that code Which it got an error and we couldn't actually update it that way.
#
# Because it's an immutable object.
#
# So, again tuple immutable object.
#
# A list is a.
#
# Object, but you can see also that in terms of tuples we were able to get around it
#
# by actually assigning new objects to that variable.
#
# So, in this case Imelda had the initial value set here for the tuple.
#
# They were able to actually recreate it and that works quite nicely.
#
# You'll find that the term immutable works in a lot of languages
#
# you can't change the existing contents, but
#
# you can actually reference it or to a new object of that type.
#
# Now, the second thing that might be obvious, but it is important for
#
# me to actually point out.
#
# Is that expressions on the right hand side of an assignment
#
# are always evaluated before the left hand side.
#
# So, in the imelda example above,
#
# we're taking the first element of the count imelda objects.
#
# I'm talking about this line here, line 18.
#
# So, we're taking the first element of the current IMELDA object
#
# which of course indicts 0 plus the string IMELDA may correctly
#
# typed as I-M-E-L-D-A instead on E-M-I-L-D-A.
#
# Followed by the third element of the current IMELDA to produce a new tuple.
#
# So, you can see that it's actually This would only work if
#
# the computer was actually evaluating this right hand side of the expression first.
#
# If it started evaluating the left hand side first,
#
# then of course this imelda object would already have been updated.
#
# So again, it's looking at these values first and
#
# assigning those before ultimately looking at the left hand side.
#
# To see where these objects are going to actually be saved.
#
# S,o in this case the new tupple was then assigned to the value mild or
#
# after that and it replaces the previous object.
#
# So, it's not the variable that is immutable, but
#
# it's the object that the variable Imelda in this case points to.
#
# So we haven't changed the contents of the tupple object.
#
# What we actually did here on line 18 is we created a new tupple.
#
# And then pointed the variable and the order to reference it.
#
# And again, because the right hand side is evaluated first,
#
# the current contents of an order can be used to create the new topple before
#
# the assignment and that's why line 18 actually worked.
#
# And probably about now you're starting to wonder,
#
# well Why would I actually be using a tuple?
#
# What's the advantages of using tuple over a list?
#
# Because at first glance, you might look at it and think that lists seem more useful.
#
# And while it's actually true that you can generally use a list in place of a tuple,
#
# there's some important reasons why you'd wanna favor tuples over lists.
#
# And then we haven't actually covered hashes or dictionaries yet in the course.
#
# But a dictionary key requires immutable object, and
#
# that removes the choice if you wanna use your object as a dictionary key.
#
# But, you'll be finding out more about that later.
#
# But another key difference, is that a list is intended, although it's not enforced,
#
# to contain items of the same type.
#
# Much like a real world list.
#
# So, you wouldn't add an activity such as sky diving to a shopping list,
#
# for example.
#
# The computing temp of this is homogenous.
#
# So, in other words the list have intended to hold homogenous items.
#
# In other words, meaning items of the same type.
#
# So, tuples are actually intended to hold heterogeneous items.
#
# So, like our albums example where we were storing three different things in
#
# each tuple.
#
# An album title, artist name, and
#
# a year, which you can see that with different types on lines 6 through 10.
#
# Now, the other things to keep in mind is the protection offered by using a tuple.
#
# The things that should not change can actually help prevent
#
# bugs in your programs.
#
# So, in other words, once an album is released, its details do not change.
#
# Prince and the Sensational Alex Harvey Band, notwithstanding.
#
# So, it actually makes sense to store the details in a tuple.
#
# Because of course they're fixed items, which should never change.
#
# So, if your code then attempts to change one of the fields in the tuple,
#
# the attempt is gonna fail and you saw the error earlier in the video.
#
# When I actually tried to do that, on line 17 which is now commented out.
#
# So, that it will file, and
#
# it will actually highlight something that your code probably shouldn't be doing.
#
# So, it's really good from that point of view,
#
# to use a tuple in that way to avoid getting into difficulties later.
#
# So, one example of that might be an adventure game.
#
# So the layout of your game, the various rooms and the links between them will be
#
# fixed throughout the game's, Even if all exits are not immediately available to
#
# the players, so you would actually store that or could store that in tuples.
#
# The players can change though as they gain hit points and
#
# take damage through the game, so a tuple wouldn't be appropriate in this case for
#
# example to storing player details.
#
# So, we're going to digress slightly now and show another way to assign values to
#
# variables that we haven't discussed earlier.
#
# So, what I'm gonna do is create a new pathing file for
#
# this example because we're gonna be coming back to this tuples.py shortly.
#
# So, I'm just gonna come up here, as I've done throughout the course,
#
# and I'm just gonna call this one demo but you can call it whatever you'd like.
#
# And close down the run window for now, and I'll just delete that first line.
#
# So, in Python it's possible to assign values to several variables at
#
# the same time.
#
# And here's an example of setting four variables to the same value.
#
# So, we can put a = b = c = d = 12.
#
# And if we print c, for example, and run that.
#
# And see, we got the answer, 12.
#
# So in that case, all four variables were assigned the value of 12.
#
# But we can also assign different values to multiple variables.
#
# So, another example might be A, B equals 12, 13.
#
# We could print A, B.
#
# You can see, in that case, line three, a's been assigned the value 12,
#
# b's been assigned the value 13.
#
# So, once again, remember that the right hand side is evaluated first.
#
# So, just clarify that, I can do something like this.
#
# I can type So we've got a and b defined as 12, 13, and we've printed the values out.
#
# We can do something like a, b = b, a.
#
# Then we could do print(a is
#
# .Formata.
#
# We're gonna do the same for b.
#
# We can run that, and we can see there we've got the a have been assigned to 13,
#
# and b has been assigned the value of 12.
#
# And again, the value for that, the reason that that's working is the right-hand
#
# assignment is actually calculated, or evaluated I should say first.
#
# Now, looking at line 3, it looks suspiciously like a tupple.
#
# Considering what we've learned in this session.
#
# And that means that we can actually pull out all the elements of a tuple in
#
# a single assignment.
#
# Please go back to the albums Python now.
#
# And we'll just delete a bit of this code.
#
# And we'll fix this tuple up here.
#
# And delete that.
#
# And metallica2 I'm gonna leave as a list there.
#
# We're gonna print out part two if it down here.
#
# This is the example, we can type title.
#
# Artist, year, equals Imelda.
#
# Print title.
#
# Print artist.
#
# Print year.
#
# We actually now run this code.
#
# Run titles.
#
# We get the actual, press the print of the list, which we've left in.
#
# But notice how now that we've extracted the valleys out of the total
#
# into individual variables using the common syntax that I've just shown you.
#
# So, there is actually a term for that.
#
# It's actually called unpacking the tupple.
#
# And just incidentally in this case, where you've got more than one file open, if you
#
# are ever in doubt as to which one is gonna run, come up here to the top right-hand
#
# corner, and you can actually choose which file you actually want to run.
#
# For example, I can choose demo and it will actually run demo.
#
# And run the code for this file.
#
# But, equally I could come back here and select topples and actually run that code.
#
# So, another alternative of course is just to right click the relevant file and
#
# actually run it.
#
# So, we've just touched on unpacking the topple.
#
# Gonna end the video here, and
#
# we'll actually talk more about this in the next video.

# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

welcome = "Welcome to my Nightmate", "Alice cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# metallica[0] = "Master of puppets"  this is why tuples are imutable but like below you can update the tuple, by assigning
# new object.

imelda = imelda[0], "Imelda May", imelda[2] # we didnt change it but we created a new one.
print(imelda)

# below is example of how list is mutable means - it can be changable

metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)

title, artist, year = imelda
print(title)
print(artist)
print(year)


a = b = c = d = 12
print(c)
a, b = 12, 13
print(a,b)

a,b = b,a
print("a is {}".format(a))
print("b is {}".format(b))














