# List in Python

# In this video we're going to go through an introduction to lists.
#
# You've already looked at one sequence type, which is the tech sequence type,
#
# STR or string, and
#
# we also looked at some of the operations that can be performed on the string.
#
# Now Python actually provides six additional built in sequence types.
#
# And they are the List, the Range, the Tuple and
#
# these three types we'll be discussing in this section.
#
# And there's also three binary sequence types that will be the subject of future
#
# sections, but we'll talk about those.
#
# So there's actually useful summary of the operations that can be performed on
#
# sequences.
#
# What I'm going to do is just open up some documentation and show you that.
#
# Gonna paste the link there and you can see the link now just by making it a little
#
# bit larger so you can read it on the screen.
#
# If you go to that page and have a look, you can see that there's a good summary as
#
# I mentioned of the various operations that can be performed.
#
# And the table itself is actually quite useful, but
#
# unfortunately the actual text itself is written as a formal definition.
#
# And it's really not that easy to understand.
#
# Good news is that we'll be explaining it all in this course here anyway.
#
# You're looking at these operations on the screen.
#
# Even though they're a little bit hard, bit cryptic to read what they actually mean,
#
# we've actually used the first eight already in the course.
#
# And if you look at the next two, min and max,
#
# they're probably fairly obvious as to what they do.
#
# Give you the smallest item and the largest item.
#
# And even if the results are reduced, they are not always what you might expect.
#
# Which you'll actually find we're not actually using them.
#
# But count could've been useful in our previous change as well.
#
# This is the s.count, total number of occurrences, and we could've actually used
#
# that to check that the input string contained exactly three full stops.
#
# So let's actually go back and check that out and see how to do that in some code.
#
# So, what we could've done is started off and put ipAddress = input.
#
# Please enter an IP address, like so.
#
# In terms of validating it,
#
# we could've done print ipaddress.count and put dot in there.
#
# So we're counting how many dots, full stops are actually in there.
#
# So if we actually run that.
#
# Please enter an IP address 192.168.0.1.
#
# You can see we got the number three there.
#
# And again we can just try another one.
#
# We could just try a bogus one 10.5.4.3.2.1.
#
# And that's returning five even, that's an invalid IP address.
#
# You can see that it's actually correctly returning the right number
#
# from stops it's found.
#
# So that would have been very useful.
#
# There's also another I want that we're gonna look at in this section.
#
# If we go back to the form again, we're gonna be using index.
#
# Index or the first occurrence of x in s.
#
# So all these operations that I'm showing you can be performed on any sequence type,
#
# but we're actually gonna be using them with lists here.
#
# Let's go back to the code again.
#
# It probably helps though if we start off by talking about what is a list.
#
# So what actually is a list in Python?
#
# Think of a list as a sequence of things.
#
# Now those things could be strings, numbers, classes, or
#
# pretty much anything else.
#
# So if a list can be a sequence of strings, and
#
# a string is itself a sequence type which we talked about earlier,
#
# then it makes sense that a list can also be a sequence of lists, which it can.
#
# So this makes an incredibly useful,
#
# if a little bit confusing initially, as we're about to see.
#
# So we're gonna actually start by looking at the dead parrot list we used when
#
# discussing four loops in a previous section.
#
# We're gonna make a slight change and assign the list to a variable So
#
# I'm just going to comment this code out.
#
# So let's type parent_list =
#
# ["non pinin'", "no more",
#
# "a stiff", bereft of love".
#
# Again, Monty Python references there.
#
# And this time I've assigned it, as you can see, to a variable.
#
# And we can use our for loop, for state in parrot list: and print.
#
# This parrot is + state.
#
# So again, the list on line three it's
#
# created when closing the individual items in square brackets as you can see there.
#
# It's separating each item in the list with a comma.
#
# And we can actually run this to confirm that it works.
#
# As parrot is, you can see non-pointing is the first entry,
#
# no more was the second one, stiff and bereft of love.
#
# So it actually went through the flow each entry is a separate entry in the list and
#
# we're able to print a message out.
#
# It's also quite easy to append to a list after you've created it.
#
# So if you wanted to do that elsewhere in the code, you could actually come down in
#
# here and type parrot_list.append and type in something like Norwegian Blue.
#
# And then if we run that, we can
#
# see that we successfully added an entry to the end of the list by using the .append.
#
# Now the other thing we can do is have a list of numbers.
#
# So, obviously we've used strings there.
#
# But there's nothing stopping us from actually having numbers so
#
# we can do something like, even equals 2, 4, 6, 8.
#
# And we can say odd equals 1, 3, 5, 7, 9, like so.
#
# And we could put numbers = even + odd, print numbers.
#
# So here we are actually concatenating the even and odd lists and
#
# we're assigning the result to a third list, a new list, called numbers.
#
# So let's actually try running that first.
#
# And you notice we've actually got 246813579 so it successfully appended it
#
# to numbers that were in the odd list at the end of the even list and
#
# actually created a third list when we actually added to the numbers.
#
# So the actual numbers list contains the sum of both of them.
#
# And we've got a couple of errors so
#
# I should actually make an attempt to actually fix those.
#
# So we need to be adding that as white space we have to get in to do this for
#
# all our code, to make sure the code's actually valid each time.
#
# And this is actually telling us that the list creation could be rewritten as
#
# a list literal.
#
# So I think and that's some more advice from IntelliJ, but
#
# we'll actually leave that for the time being anyway.
#
# We'll come back to that.
#
# But looking at the list that's been combined there,
#
# as you can see, they're not actually in order.
#
# So obviously it'd be nice if we could automatically get those in order so
#
# they actually started from lowest number to highest number.
#
# And that's actually quite easy to do.
#
# So we can actually, very simply use the sort method which is part of a list and
#
# type numbers.sort, like so.
#
# And once we do that and
#
# run it again you can see we've now got the numbers correctly in order.
#
# Now the sort method itself doesn't return the sorted list, and
#
# if you've actually used other languages this may be what you expect.
#
# You may expect the sort method to actually return the sorted list, so
#
# in other words this is not going to work.
#
# So, if I give you an example, if we actually remove that,
#
# and actually comment that line out.
#
# And if you did something like this, print numbers.sort, you might assume that that
#
# would actually print out the contents of what was a sort of numbers.
#
# And certainly that would be the case in other programming language.
#
# But if you run that we actually get None, we get something completely different.
#
# And the reason for that is that Guido Van Rossum,
#
# the guy who invented Python, he chose this behavior deliberately, and
#
# the idea was to provide a hint that the sort method works on the object that it
#
# was called upon, rather than creating a new object.
#
# And that's very important here that It's not actually creating anything.
#
# So the sort method or
#
# function, the idea of it is that it actually works on the existing variable,
#
# the object in other words, it doesn't actually create a new object.
#
# And that's why in this case .sort returns nothing.
#
# So, we would then delete that code out again and come back here.
#
# And so, we've got at this point, our list.
#
# Numbers.sort works on that list, and resorts out, and then printing it out
#
# obviously prints out the same variable, which has now been sorted.
#
# And I've got the numbers in the right order like so.
#
# So if you are new to programming, some of this discussion may not make much sense.
#
# You might be wondering what I'm talking about when I'm talking about the .sort
#
# returning an object.
#
# And you are probably quite happy with the way it works.
#
# And I think indeed it actually does make sense and it's quite intuitive.
#
# But the reason I'm bringing it up is because it's particularly important if you
#
# have a seen this in other languages you have to get used to this type of
#
# behavior [INAUDIBLE].
#
# Generally speaking if a method acts on an object and changes it,
#
# mutates it in other words.
#
# Then the method is going to return none but
#
# the actual variable object has been updated.
#
# Now there is a way around this if you want to create a new object rather than
#
# sorting the one you have,
#
# there's actually a built in function sorter that's going to do that.
#
# So we could actually change this code out.
#
# So we'll get rid of .sort and what we'll do is actually come up here and
#
# delete that code and put numbers but use a method called sorted.
#
# Like so and sorted is a function that's built in to Python.
#
# If we run that, you can see we've got the same result,
#
# we've actually got it sorted, and that does actually return and the number,
#
# cuz obviously we're printing this out.
#
# So it's returned a new list containing the sorted numbers.
#
# So that's different than the .sort function you saw before.
#
# This sorted function actually returns the actual new object.
#
# And of course, with that said, we're printing it there, but
#
# there's nothing stopping us actually just putting
#
# numbers_in_order = sorted(numbers), like so.
#
# And then just printing.
#
# Print numbers in order, which essentially is the same thing, so
#
# that's going to work as well.
#
# If we run that, we get the numbers at sorted in the right order.
#
# So, at that point, obviously, we've got two lists.
#
# We've got numbers, and numbers in order, and they've got the same items, but,
#
# obviously, different orders.
#
# The first one, numbers has got the numbers unsorted, and
#
# numbers in order has obviously has got the sorted numbers.
#
# The other thing to keep in mind is at this point,
#
# even though they can both contain the same items, Python will
#
# not treat them as equal as we can see with this code we're about to write.
#
# And this important distinction is,
#
# over top, if numbers equals numbers
#
# in order Print the lists are equal.
#
# And again they've got the same numbers in them so you'd think maybe that would work,
#
# but we'll try putting an else in there.
#
# The lists are not equal.
#
# So, I've actually run that.
#
# We actually get the message back, the lists are not equal.
#
# And that's because even though we've got the same numbers,
#
# they're actually in a different order.
#
# So obviously the first set of numbers was unordered, and
#
# the second set of numbers was ordered.
#
# And as far as Python is concerned, they aren't equal.
#
# But we could do something like this.
#
# We could actually do a test for if numbers_in_order
#
# is equal to sorted numbers.
#
# Print, and we'll actually copy the rest of the code there, so
#
# we'll just do exactly the same.
#
# Copy that, paste that.
#
# So now we're actually testing numbers in an order which has already been sorted,
#
# and we're comparing that to the return from this sorted function,
#
# which will actually be numbers, sorting the unsorted list or sorted lists,
#
# that should now come back and say they're equal.
#
# And the lists are equal at this point,
#
# because obviously we've got same numbers and also they're both sorted as well.
#
# So again, if you're used to other programming languages,
#
# this may well be very confusing to you.
#
# The two objects are not the same and they would not test equal in Java for example.
#
# But Python works as you would intuitively would expect if you're new to programming.
#
# And it's obviously a bonus for you, if you actually are new to programming.
#
# So, I'm gonna end this video here.
#
# In the next video we're going to continue our work on lists.
#
# And we're going to look at some different formats and
#
# ways to actually use replacement fields, lists, and so on and so forth.


# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]

parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print("This parrot is " + state)

even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = odd + even
# numbers.sort()

numbers_in_order = (sorted(numbers))

print(numbers_in_order)

if numbers == numbers_in_order:
    print("The list is equal")
else:
    print("The lists are not equal")

if numbers_in_order == sorted(numbers):
    print("The list is equal")
else:
    print("The lists are not equal")












