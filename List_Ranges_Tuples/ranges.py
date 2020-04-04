# Ranges -

# So it's now time to talk about ranges.
#
# Now we've actually used ranges a few times in for loops, and
#
# we use that to loop a specified number of times.
#
# So it's time we take a more detailed look at what they actually are.
#
# So in Python 3 range is actually a built in type.
#
# But in Python 2, it was implemented as a function.
#
# So in a simplest form, we can create a range just by specifying an n value.
#
# So we could do something like print(range(100)).
#
# And if we actually run that, And
#
# return a range, which is a range from 0, 130.
#
# It's not really terribly exciting, but what it does do is show you to get
#
# back a range object with a start of 0 and a stop of 100.
#
# Printing a range object like that isn't useful.
#
# And when they come into their own,
#
# you get the most ever, you start iterating over, for example, to cause the for
#
# loop to repeat a block of code many times as we've actually seen.
#
# We can also use them to use them to create another object such as the list.
#
# So, as an example we can come back here and actually type my under score list,
#
# = listrange(10),
#
# and now if we actually print my list.
#
# Actually run that.
#
# You notice how we've automatically got these 10 elements through from
#
# zero to nine just by actually using the range and passing
#
# the end range of 10 and automatically created those elements for us.
#
# So again, if you're passing a single value to range the value's taken to be the end
#
# value and the start value defaults to zero in that scenario,
#
# as you can see that with the first element being zero right here at the top.
#
# But you can also specify start range,
#
# there's nothing stopping you from doing that.
#
# So you could do something like,
#
# even = list(range (0, 10, 2).
#
# Or we can try odd = list(range (1, 10, 2).
#
# Print (even), print (odd).
#
# That's just another more extended use of the range.
#
# And for some reason we've some extra brackets here,
#
# we'll get rid of those brackets to make it valid.
#
# We'll try running that.
#
# And we can see now we've got 0, 2, 4, 6, 8, and 1, 3, 5, 7, 9.
#
# So we're creating the list called even, the first one from a range.
#
# And we put the range of 0 as the start ten as the end, but
#
# you also use the steps, that third number there to skip by two.
#
# So we've actually got only even numbers.
#
# By starting on zero and skipping two with two, four, six, eight.
#
# And likewise with the odd.
#
# We did the opposite there.
#
# We started on one.
#
# Still went to the end rows of ten, but skip by two, and
#
# then went to skip only the odd numbers.
#
# So one, three, five, seven, nine in this example.
#
# Now Python 3 ranges are very efficient in terms of memory.
#
# In other words, if you did something like this,
#
# range[0,10] or range[0, say.
#
# They're actually both gonna use the same amount of memory, believe it or not.
#
# So that's fine. But
#
# if we actually change the code up here, and actually start using large numbers,
#
# like instead of 10, putting 1,000, and
#
# 1,000 for both of those, that will still actually work, as you can see.
#
# Notice there was a slight pause there, and
#
# now we've actually got a huge set of numbers.
#
# And It's literally going to be 1,000 elements, as you can see,
#
# right through to 1,000 there.
#
# 998, 999 were the last elements,
#
# bearing in the mind the last one's always not used.
#
# So you do need to go steady with the zeroes though, because if you made
#
# the value say 10,000, it can actually take quite a while for the lists to be created.
#
# And each list will occupy a fair amount of memory.
#
# So the range itself is always gonna return the same amount.
#
# I will use the same amount of space, but when you're creating a list of that range
#
# then of course the list has to actually expand out to use all the elements within
#
# that range and it can actually start taking up a lot of memory.
#
# Kind of interesting in part two ranges didn't behave like that at all.
#
# Old bellies were calculated and returned as a sequence,
#
# remember we talked about sequences to a degree in this course,
#
# Python 2 also had an x range that behaved much like the Python 3 range object does.
#
# And Python 3 diversion 2x range has become range and there's no longer an x range.
#
# So if you're converting path from two code and you actually see the x
#
# range being used, you can just change x range to range for pathway three and
#
# it's going to work just fine.
#
# Now ranges don't support all the operations
#
# that you can perform on sequences.
#
# The reason for that is largely because they represent sequences
#
# that follow a defined pattern.
#
# And so for example the multiplication operator to repeat a range is not allowed,
#
# nor is concatenation, pending in other words.
#
# Other than that you can perform all the usual sequence operations or ranges.
#
# Now we didn't actually cover the index method when dealing with two sequences,
#
# when we actually discussed strings and lists.
#
# But I'm gonna show you how to do that now and
#
# how you can access individual element index over sequence using it.
#
# So it's gonna come in handy for our code.
#
# So I'm just gonna select that and comment that code out.
#
# And let's just top something like my underscore string equals,
#
# and we'll do all the letters of the alphabet.
#
# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P,
#
# Q, R, S, T, U, V, W, X, Y, Z, or Zed.
#
# As we say in Australia.
#
# If I do a print(my_string.Index e).
#
# And if I do a print my underscore string for,
#
# eventually run that So
#
# the index of the character e is actually the character position four in the string.
#
# Remember, we count from zero.
#
# So zero was A, one is B, two is C, three is D, four is E.
#
# So the index, dot index is actually returning the number.
#
# Pointing to the character position
#
# of whatever you've actually pass here as the parameter.
#
# So we can also apply indexes.
#
# Though the index function to ranges as well.
#
# So we can so
#
# something like small underscore decimals equals range zero, ten.
#
# Then we're gonna do print small decimals.
#
# We can also do print small decimals.index3.
#
# If we actually run that, we actually get the value three there,
#
# being the third, being effectively the fourth position.
#
# Cuz, of course, the counting again started from ten, so zero, one, two, three.
#
# And you can interestingly enough also index into the range.
#
# So for example, if you created a large range,
#
# like if we did something like odd = range(1,
#
# 10000, 2) Print odd.
#
# Bearing in mind this is just a range,
#
# not a list of ranges as we did earlier in the video.
#
# We can actually do print, Odd, 985.
#
# Run it five.
#
# And you can see that actually gives us the value from the 985th odd number,
#
# which is pretty handy and also pretty fast to process as well.
#
# And it's also possible to check if a value that you pass is actually in a range and
#
# you can use that using the in operator.
#
# So we can do something like sevens equals range.
#
# We'll start from seven.
#
# Seven.
#
# We can put x equal int, input.
#
# Please enter a positive number less than one million.
#
# And we can put if x in sevens,
#
# print is divisible using the replacement
#
# field, divisible by seven.
#
# Format x.
#
# So we can actually run that.
#
# Please enter a positive number less than 1 million.
#
# So you could do something like say, 987.
#
# 987 is divisible by seven.
#
# And let's do a number that we know isn't divisible by seven.
#
# 50.
#
# We don't get any error, don't get any messages,
#
# I should say, because the number 50 isn't divisible by seven.
#
# Because, again, just to confirm, we started a range starting at number seven,
#
# and went through to a million,
#
# and only actually showing numbers that were incremented by seven each time.
#
# You can see that ranges can actually be very powerful.
#
# In addition to that you can also apply slice ranges as well.
#
# So we can print our small decimals that we defined above again so
#
# small decimals just to confirm we're on that same page.
#
# Then we can also do my_range = small decimals 2, ::2.
#
# Print my range just to see what it does.
#
# Print my range.
#
# And print(my_range.index(4), and
#
# then actually run that after you just actually answered a question.
#
# So it was 50 there.
#
# There's the two other ranges.
#
# So you can see that my_range has become the range from zero to ten in steps of
#
# two, by just actually entering ::2 there.
#
# And the index of the value 4 in the range is 2.
#
# And of course the range is 0, 2, 4, 6, and 8.
#
# Things to remember, is that by not specifying the start and or
#
# stop, it'll actually default to the start and it'll end on the sequence.
#
# So in other words specifying colon, colon two as we did here.
#
# What that means is to slice all of the small decimal elements but
#
# stepping every other value.
#
# So ::2 was skipping one each time.
#
# So just to clarify that with another example.
#
# Now we'll just comment some of this code out now.
#
# So if we do something like decimals equals range, 0, 100 print decimals.
#
# My_range = decimals.
#
# It would be something like three 43 print my range.
#
# For I in my underscore range.
#
# print(i) and we can do just to separate it a little bit
#
# put = times 40 so put a bit of a separator there.
#
# And just add a bit of space here.
#
# And then we'll finish off with a for
#
# i in range(3, 40, 3):, print(i).
#
# Let's get rid of some of those lines now.
#
# Okay, so if we actually run that.
#
# You can actually see what's happened here.
#
# So, the my_range has been created by taking a slice from decimals
#
# to return a new range.
#
# So as a result of that it shouldn't come as any surprise that the last two ranges
#
# can actually be tested for equality and return true.
#
# So in other words we can actually come back here and
#
# actually do something like this.
#
# print(my_range) Is equal to range (3, 40, 3).
#
# Actually run that.
#
# We actually get the answer true, because they're actually considered,
#
# well they actually are, technically equal.
#
# So I'm actually gonna finish the video here.
#
# In the next video we're going to continue on and go through a few more examples of
#
# range, and then I'm gonna come up with a challenge for
#
# you to help your understanding of range.


print(range(100))

my_list = list(range(10))
print(my_list)

even = list(range(0,10,2))
odd = list(range(1,10,2))

print(even)
print(odd)


my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0,10)
print(small_decimals)

print(small_decimals.index(3))

odd = range(1,10000,2)
print(odd)

print(odd[985])

sevens = range(7, 1000000, 7)
x = int(input("Please enter a positive number less than one million: "))
if x in sevens:
    print("{} is divisible by seven".format(x))
else:
    print("No it is not")


print(small_decimals)

my_range = small_decimals[::2]
print(my_range)
print(my_range.index(4))


print("=" * 40)

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)


print("=" * 40)

for i in range(3,40,3):
    print(i)

print(my_range == range(3,40,3))









