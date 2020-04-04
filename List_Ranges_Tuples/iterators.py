# Iterators in Python

# So now's actually a good time in the course to actually discuss a very
#
# important feature of Python.
#
# And that's actually iterators and iterable objects.
#
# Now an iterator is an object that represents a stream of a data.
#
# So it actually returns the stream,
#
# or the actual data in the stream, one element at a time.
#
# Now, any object that supports iteration is called iterable, and we've actually seen
#
# two iterable objects already so far in the course, and that's strings and lists.
#
# So, as we've seen I'm gonna type in some code.
#
# We can actually use a for loop to iterate over each of the characters in a string.
#
# So let's actually type that out.
#
# We're gonna use string 1234567890, and
#
# you see this a few times now in the course, something similar.
#
# For char in the string.
#
# Print char.
#
# And if we actually run that, we actually get the results we can see on the screen.
#
# But what's actually happening behind the scenes is that there's an iterator that's
#
# created from the string.
#
# And the for loop actually uses that iterator to return each item
#
# of the string, or each element in this case.
#
# 1,2, 3, 4, 5, 6, 7, 8, 9, and 0.
#
# And when there are no more items the iterator returns an error and the for
#
# loop actually terminates.
#
# So, note in this case that the for loop handles the error, and that's why you
#
# haven't actually seen an error when you're actually running the code.
#
# What we'll do is we'll actually create an iterator from the string
#
# rather than letting the for loop create one implicitly,
#
# and that's gonna be easier to see what's going on when we do that.
#
# So use the iter function to do that, so
#
# what I'm gonna do is just comment out the for loop.
#
# And what we're going to do is put my and
#
# the school interrator, equals hitter, and that's the function.
#
# And then we pass the name, in this case, the string variable that we want, and
#
# if we can actually do a print, my interrator, so if we actually do that and
#
# we actually run that.
#
# We actually get a string iterator object showing on the screen.
#
# Now this is actually just showing the object representation,
#
# supposedly a memory allocation of where that is,
#
# but to actually see it in use, we can do something like this.
#
# Print next my iterator and then print next
#
# my iterator the rest you do that and run it.
#
# We get the values one and two as you can see on the screen there so
#
# it's actually going through one element at a time and that's what the next did,
#
# it actually returned the first element.
#
# Next again and then return the second element, and so on and so forth.
#
# So basically each time that we use next, in my iterator,
#
# we're passing the iterator that we created in line 5.
#
# That's what it's doing, it's actually going through the list.
#
# And obviously again getting back to the for loop, that was doing that for
#
# us essentially behind the scenes.
#
# So what we're doing its actually created the code that more less is happening
#
# behind the scenes.
#
# So if we wanted to go right through to the end we could actually create some more.
#
# So we've got ten entries, so if we have another 8, 1, 2, 3, 4, 5, 6,
#
# 7, 8, so that should actually be ten now, if we actually run that we actually get
#
# all the elements, 1 through to 0 essentially, so you can see there.
#
# So that's the exact number of elements that are in the string.
#
# But if we actually now, add actually one more.
#
# So in other words, we know now that we're already at the end of the string,
#
# let's actually see what happens when we try to go beyond that.
#
# So we actually run that.
#
# And you can see, we actually get an error.
#
# And if we just expand it out so we can see it.
#
# You can it manage to go through and count through to zero successfully and than it
#
# comes off and basically say, a trace back call last and stop it's duration.
#
# And that's basically line 18.
#
# Which has, as expected, crashed because there weren't any more elements.
#
# So, once we've covered error handling in the future,
#
# if you have nothing better to do, then you could actually write all your four loops
#
# by explicitly requesting an iterator using the enter function.
#
# And calling next until you get an error, and this is,
#
# again, exactly what the four loop does for us, it actually does it automatically.
#
# It keeps using next until it sees the stop iteration i error
#
# which is this area here on the screen.
#
# When it sees that it actually terminates for us automatically.
#
# So before it implicitly creates an iterator from the iterable object
#
# that we want to iterate over.
#
# Now of course we don't have to do all that.
#
# But it's useful to actually understand how iterators work, and it'll also become even
#
# more useful when we come to creating our own iterable classes later in the course.
#
# Just to help consort like that, let's just close down the run we're doing.
#
# And comment out this code.
#
# Now paste that code in again.
#
# I just want you to consider these two loops here.
#
# Now let me just get the right indent levels going.
#
# Again, very important to get your indent levels correct.
#
# So consider these two.
#
# So the first one's just a standard for loop.
#
# The second one, for_char in iter String.
#
# So I consider both of these scenarios,
#
# they actually both do exactly the same thing.
#
# But this second example here, is what's actually happening in the first case.
#
# The for up here,
#
# it's implicitly creating an iterator from the iteratable string object.
#
# So basically if you're just putting for char in string, then essentially what's
#
# happening behind the scenes is Python is actually adding this iter to that string.
#
# So it was actually creating that iterator for us.
#
# So, it can be very useful again to know that and
#
# you'll be finding out more about iterators as we move through the course.
#
# So, let's just come up now with a mini challenge
#
# to help you understand iterators a bit more.
#
# I'm gonna top that out now.
#
# So here is the mini challenge we've got for the writers.
#
# So create a list of items and you can use either strings or
#
# numbers in the list, it doesn't really matter, and then from that
#
# create an iterater using the iter function that we actually went through.
#
# Now, next use a for loop to loop n times.
#
# Now, n is the number of items in your list and
#
# each time around the loop is next on your list to print the next item.
#
# And just as a hint there, use the len function,
#
# we've talked about previously, rather than counting the number of items in the list.
#
# So, go away and see if you can figure that out, and type up some code and
#
# get that working, and when you're ready to come back and
#
# compare your code to mine, I'll be here waiting.
#
# So pause the video now, and I'll see you when you get back.
#
# So how did you get on?
#
# Did you come up with a good solution for that?
#
# So let's go through with my implementation, and
#
# bearing in mind this is just a implementation.
#
# There's lot's of different ways to do these things.
#
# Let's come up and start by typing the lists or creating the lists.
#
# Which will be my_list =, and I'm gonna use just the days of the week.
#
# So Monday, Tuesday,
#
# Wednesday Thursday,
#
# Friday, Saturday,
#
# Sunday, like so.
#
# Next I'm gonna create the iterator.
#
# That's my iterator equals iter my_list
#
# the iter function creates that iterator, as we talked about.
#
# And then we're gonna go through using the four loop.
#
# So I'm gonna do four i in range zero,
#
# I'm using lan to get the number of elements from the list.
#
# Mine is called list.
#
# Remembering that the lead in this case on a list actually returns the number of
#
# elements that are actually existing in the list itself.
#
# So, that's the for loop.
#
# And then we're gonna use next underscore item equals equals next my iterator so
#
# we're iterating through one element at a time, so that's giving us the next
#
# element, or the next item, in this case a string from the list.
#
# And we're going to print that out print next item.
#
# So that's the solution, so
#
# if we actually run that to make sure that it's working we can see we get Monday,
#
# Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.
#
# And we can see that it's actually working fine.
#
# So the idea of this challenge was to help you understand iteratives.
#
# Now of course you wouldn't want to access the items in the list
#
# in that way normally.
#
# You'd probably want to do something a lot simpler like you've learned earlier
#
# that in the course, like four i in minor's called a list Print(i), and
#
# obviously that would return the same results.
#
# Oops, I forgot a call in there.
#
# And then again, that obviously returns the same result.
#
# But the point again here was to teach you what iterators are and how to use them.
#
# And as mentioned, later in the course we'll actually be creating our own classes
#
# that use iterable objects.
#
# And you'll be understanding a little bit more about iterators then.
#
# So I hope you enjoyed that.
#
# And then, next video, we're gonna actually start looking in more detail at ranges,
#
# which I've used a few times already in the course.

# String and loops are iterator in python

# string = "1234567890"

# for char in string:
    #    print(char)
    # pass
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# Create a list of item (you may use either strings or numbers in the list), then create an iterator using the iter()
# function.
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.

# hint: use the len() function rather than counting the number of items in the list

string = "1234567890"

my_iterator = iter(string)

for n in range(0, len(string)):
    next_item = next(my_iterator)
    print(next_item)

print("above is same of what we do generally ")


for n in string:
    print(n)


















