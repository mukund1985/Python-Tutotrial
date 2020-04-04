# List part 2 -

# So, in the previous video we started with an introduction to lists, and
#
# we went through various scenarios to sort of see how we could manipulate some
#
# basic lists and indeed actually talked about what lists were.
#
# So, as it turned out we went through three ways to create a list,
#
# the first was enclosing the item in square brackets by concatenating existing lists,
#
# adding two together, and also by using a function that returns a list,
#
# which I used in this example, sorted.
#
# We can also use the list type constructor, which is like a list in brackets,
#
# with brackets.
#
# And constructors will make more sense when I've introduced classes,
#
# which will be in a later section of this course.
#
# But for now, just think of the list constructor as just another function that
#
# you can actually call.
#
# So, if you use list with no parameters it just creates an empty list.
#
# So, I'm going to delete this code and
#
# we're going to start with a clear slate here.
#
# Like so.
#
# So, using a list as I said with no parameters, it just creates an empty list.
#
# So we can type, and that ends up being exactly the same as the first option here.
#
# So, I've got list_1 = [], which is an empty list,
#
# but I can also do this, list_2 = list[].
#
# And in both cases, what they do is they create an empty list.
#
# So basically, they're both identical as you can see.
#
# And just to confirm that, we can actually print this out.
#
# I can type print, list1.format.
#
# This data's called 1, and
#
# print list 2.format, this data's got 2.
#
# And I can put if list_1 =, this data's called 2.
#
# Print the list are equal, we can actually run this.
#
# We can see that both are empty lists, list 1 and list 2 are both empty.
#
# So, you can see there and we get confirmation by doing the comparison
#
# the double equals sign to compare them, and
#
# they are both considered equal by Python.
#
# Now ,I don't think we've actually mentioned this before, but
#
# actual, when you call a function such as print or sorted.
#
# So, function in this example being print.
#
# You can see this stuff in the middle here.
#
# They're actually called parameters or arguments.
#
# So, the parameter in our last print function code was the string
#
# the lists are equal.
#
# So, this is actually a parameter.
#
# That's a parameter that we're passing to the function called print.
#
# But later in the course, we'll start actually creating our own functions, and
#
# we'll actually cover parameters and arguments then in more detail.
#
# But strictly speaking, the lists are not equal is an argument.
#
# But the two terms, argument and parameters are often used interchangeably.
#
# So, the list constructor, and again the constructor is using the list
#
# with the brackets, can be called with no parameters as we've done.
#
# We can also call it with a single iterable parameter.
#
# So, in Python an iterable is just an object that is capable of
#
# returning its members one at a time.
#
# So, all the sequence types built into Python are actually iterable, and
#
# we can actually pass a string to the list, so we could do something like this.
#
# print(list("The lists are equal.")) like so, we can run that.
#
# And you can see what's happened there is automatically,
#
# Python has actually created a list from what we sent to one character at a time.
#
# So each item, each letter, of this string,
#
# has been added individually, as a separate option in that actual list.
#
# And that's what the constructor's actually doing.
#
# It's actually doing that for us, and I'm recalling that list function.
#
# So, creating a list whose members are each of the characters in the string
#
# that we passed to the list.
#
# And this was the lists are equal, is what we actually passed to it.
#
# So it can actually be very useful to do that, if you wanna assign a list to
#
# another variable, and have them then reference different lists.
#
# So, a normal assortment works as in other languages, and it can actually confuse
#
# newcomers to programmers, as I'm gonna show in the following example, so,
#
# I'm gonna type in some code here, comment this out.
#
# We can put even = [2, 4, 6, 8].
#
# Then, we type another, even = even.
#
# Then we can type another, even.sort(reverse=True),
#
# note the capital T for True.
#
# We can do print(even), so if we actually run this,
#
# you can see what's actually happened there.
#
# We've actually got it printing out even, even though,
#
# we're actually updating another variable.
#
# So, we've created another_even variable and assigned it to even.
#
# Then, we actually updated the values of even using sort.
#
# And we actually used the reverse equal true parameter to actually
#
# return the results sort of last to first, instead of first to last.
#
# But the important thing here was that, even though we haven't actually updated
#
# even directly we've used another variable called even.
#
# Because we've updated that variable it actually updated the variable
#
# even as well.
#
# So, in other words both variables even and another even
#
# refer actually to the exact same list so that and that's why when we used the sort,
#
# both [INAUDIBLE] were actually sorted as you can see, because we're actually
#
# printing out the first list, which we didn't actually directly use the .sort on.
#
# And just to confirm that what we can actually do, after the assignment we can
#
# confirm that they're the same by typing print, another_even is even.
#
# And that should actually return true.
#
# So if we actually run that, it actually returns true,
#
# which actually says from Python's perspective these two are the same thing.
#
# They're actually pointing to the same list.
#
# But if we actually create a new list for another even variable,
#
# and pass in the parameter of even, we can get that not to be the case.
#
# So we can actually type list here, the function list,
#
# well the constructor list, we're passing even, that current list to that, and
#
# list is going to return, in fact, a new list.
#
# So, when we do this print down here, we should find that that comes up and
#
# says false.
#
# But we still will end up getting the same results,
#
# because we're still ultimately sending the same information.
#
# So, if we actually run this, you can see that's now false.
#
# And that's because they're no longer the same list.
#
# We had a list that was created for even.
#
# And then we used the list constructor, passing the even list.
#
# And the list constructor actually returns us a new list.
#
# So, consequently, there's two separate lists now.
#
# The even variable has got its own list.
#
# And the other _even variable has also got its own list, as well.
#
# Just to confirm, we can actually do another test there and print another.
#
# Instead of putting is we can put equals equals then actually run that.
#
# That's gonna tell us to say at this point now it's true,
#
# because that's saying whether the contents are equal, not whether they're
#
# actually pointing to different variables in memory if that makes sense,
#
# in different lists essentially.
#
# So, it's important to know, The difference there between the double equal.
#
# So, we're actually comparing it to see whether what's in the lists are the same
#
# as supposed is.
#
# We're saying is this the same list that's actually in memory somewhere.
#
# So, that's gonna return false, cause it's separate now.
#
# And again, equals is the contents of the lists the same.
#
# That's gonna return true.
#
# Now, if you really wanted a new version of even, the first variable,
#
# we could have actually done something like this, where instead of putting list,
#
# we could have actually done something like sorted, even,
#
# reverse equals true, true, we could run that.
#
# And that's now false, because we sorted it into a different order.
#
# So, sorter does return a new list, but now it's sorting it in a different order.
#
# And just to confirm, I set that to be is and run it.
#
# It's still set to false,
#
# because they're actually pointing to different lists still.
#
# And setting that to equals we correctly get false as well,
#
# and that's because the sorted function returns a separate list.
#
# So moving on.
#
# So earlier, we concatenated or appended our even and odd list.
#
# That's actually in a previous video.
#
# And we actually produced a new list called numbers,
#
# that included all the items from both lists.
#
# I'm gonna put some more code on the screen.
#
# And see, if you can actually guess what this will do.
#
# So, I'm gonna comment that out and put the even in there.
#
# And we're gonna put an odd equals 1, 3, 5, 7, 9 and
#
# this is from the previous video when we're dealing with adding these things together.
#
# What do you think is gonna happen if I put numbers equals even, odd and print it out?
#
# So, can you guess what's that gonna actually produce?
#
# Let's run that and see.
#
# Now, it actually returns a list containing two lists.
#
# So, you can see, sort of lists within a list.
#
# That's the list number one, which is based on the contents of even, and
#
# the second one is based on the contents of odd, and now are both appended into in
#
# one master list, and just to confirm that, instead of actually printing that out,
#
# let's actually change that and actually add some code here and put a for loop.
#
# So, for numbers_set in numbers.
#
# Print.
#
# Number set.
#
# And it actually should have been number set just to be technically correct.
#
# Like so. And then, we'll put for,
#
# noting the indent level for value in number_set.print(value).
#
# So, in the outer loop number_set iterates through the members of numbers,
#
# so it's assigned each of the two lists in turn.
#
# And within the inner loop itself the value iterates through the members of those
#
# sets, so it's assigned each of the even numbers first time around
#
# then each of the odd ones in the second time around.
#
# So if we actually run that,
#
# we can actually see we can go right through the list.
#
# We can go through and print out the number set first.
#
# This is the initial print.
#
# And then, the second follow-up is going through each of those numbers
#
# within that list and printing them out.
#
# It does that for both lists because we've got an initial for
#
# loop, the outside one, which actually goes through all the contents.
#
# So, we're actually gonna end this video here.
#
# In the next video I'm gonna go through and
#
# just show you a few more examples of using lists the way we've been using them.
#
# And we'll actually then introduce you to a mini challenge to finish that off.

list_1 = []
list_2 = list ()

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

if list_1 == list_2:
    print("Both the lists are equal")

print(list("Both the lists are equal"))


even = [2,4,6,8]
another_even = even
another_even.sort(reverse=True)
print(even)

even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = [even,odd]

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)













