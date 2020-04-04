# So in this video we're gonna continue on talking about ranges.
#
# And just at the end of the previous video we started talking about
#
# equality with ranges.
#
# And just to run this example again.
#
# So you can see that, I'll just make it more space here.
#
# That my range which was set here, you can see under decimals which is the range
#
# 3:40:3 and using a range actually topping it out actually returned the same result.
#
# So we actually returned true, in other words,
#
# saying both ranges were the same effectively, or equal in other words.
#
# What would actually happen, do you think, if we actually typed this?
#
# Print range 052 equal to range 062.
#
# So, what do you think that's going to print?
#
# True or false?
#
# Let's just run that.
#
# If there the numbers are different, we're actually gonna get true.
#
# So why you might be asking, is that equal when clearly they numbers are different?
#
# Well it's all got to do with the same sequence of values.
#
# So it's regardless of how the values were specified, it's what the end result is.
#
# So in other words,
#
# it's what the range actually returns that is important here to test equality.
#
# Obviously, it was quite easy on line three, testing equality,
#
# because they're identical.
#
# But on line four, of course, we've got one which has got 052 as the range,
#
# and the second one is 062.
#
# Can easily see what's going on here by actually printing out a list.
#
# So if we do a print, list, range, 052, and
#
# then we do the same thing for 062.
#
# It'll actually become clear why that is actually equal when you think maybe at
#
# first glance it shouldn't be.
#
# And you can see that because we're stepping by two,
#
# the actual sequence that ended up being generated was 024 in both cases.
#
# And, that's actually what the test for equality is.
#
# So, it was actually testing what the result of the range is,
#
# not the actual numbers that were typed in to come up with the range.
#
# So, it's very important distinction there.
#
# And just in relation to slicing again, we did start doing that.
#
# So a slice connects to the step value of a slice could also be negative.
#
# So it can go r equals range, 0 comma 100,
#
# print r, and we're gonna do for i in r,
#
# colon, colon, minus 2, print i.
#
# And if you run that, you can say basically we're stepping back,
#
# going backwards to start two at a time.
#
# Starting from the hundred and basically going down to one.
#
# Which of course is identical to typing for i in range.
#
# 99, 0, -2,
#
# print i, and fix the typo.
#
# So you can see those two commands were basically identical.
#
# Okay we see that they're both the same, and
#
# we can actually confirm that by just doing a print.
#
# Separate them and you can see we got one counting down to one and standing for
#
# 99 and the second one is 99 counting down to one so that's actually working.
#
# And do another space there, and take careful note of this line.
#
# To print(range(0,
#
# 100)[::-2] ==
#
# is equal to range 99, 0, -2.
#
# And if you run that, we should get true.
#
# And you can see we actually get true there.
#
# So that's correct.
#
# But if we actually do this for i in range, 0, 100,
#
# -2, print i.
#
# We gonna run that.
#
# We actually get nothing.
#
# We only get the true which is from this line here.
#
# We don't actually get any output from that.
#
# The reason is because in the negative slice example,
#
# a negative step causes a slice to be reversed.
#
# Now, the same effect is obtained by specifying a negative step in the range,
#
# and you can see whether we've done that.
#
# But the start and end values must also be reversed,
#
# otherwise the reading, the way it's coming across,
#
# is that it starts at 0 and moves in steps of minus 2, until you hit 100.
#
# So you can see what the problem is there and that's never gonna obviously work if
#
# it's moving back from zero, which is why we didn't get any output.
#
# But the slice, in contrast to that, is returning items from a sequence and
#
# that as we saw if a negative index is specified then you start counting
#
# from the end of the sequence.
#
# So it's -1 being the last item, -2 second to last, etc.
#
# So, a range with a negative step can be very useful for counting a for
#
# loop backwards, but a negative slice is also extremely useful, and
#
# I'm gonna show you why.
#
# So, we're gonna first comment out this code.
#
# And let's try an example.
#
# So, I would type backstring.
#
# So, what I will do, for reasons that will come up is I am going to paste this in.
#
# I will paste that in, backstring.
#
# Then I will actually type, print backstring colon, colon, negative one.
#
# We'll actually run that, Python is a very powerful language.
#
# So you can see what it's actually done there.
#
# It's basically a simple way to process the range in reverse order,
#
# as you can see in that example where the words were deliberately typed in reverse.
#
# It was that one line,
#
# we managed to get it to actually appear as Python is a very powerful language.
#
# So applying this last finagly step to an existing range is also,
#
# is a very simple way to process that range in reverse order.
#
# And as another example, r = range(0,
#
# 10), for i in r[::-1],
#
# print(i), and we can do that.
#
# And we get a similar result.
#
# We get it reverse, so we get the results of the range respectively reversed
#
# from 9 to 0, in the same way that when we actually printed the string,
#
# we actually got the results backward as well.
#
# So that's actually it, so it's now time for a challenge.
#
# So, the challenge is gonna be a little bit different this time.
#
# It's gonna get you to, well I'm gonna type in what to do, but
#
# it's more a bit of experimentation required on your behalf.
#
# So basically I want you to experiment.
#
# With different ranges,
#
# in slices to get a feel for how they work.
#
# So basically the challenge is not so much a challenge, it's more a way,
#
# it's more of a request to actually get you to experiment with different ranges and
#
# slices.
#
# The idea is to get a feel for how they're gonna work.
#
# So remember that you can actually print the range as well as iterating through it
#
# to print the values.
#
# And also you can actually check that also checks that you,
#
# the range is actually what you expected.
#
# Because as you can see in some circumstances, as I've shown in this
#
# video, ranges don't always come back as you would think they would.
#
# And you might also want to include things like I've shown there,
#
# o = range(0, 100, 4), printing out for contents of o, and
#
# actually using the slice with the colon colon 5 I have there on line 8,
#
# printing out the values of p, and using a for i in p and printing out i.
#
# And basically see if you can work out what this code is going to do and
#
# what's gonna be printed before you actually run the program.
#
# Now if you're unsure what's gonna happen, you can actually use for
#
# loop to print out the values of o to see why p actually returns what it does.
#
# We're gonna actually run this, and
#
# then I'll leave this with you to actually experiment with.
#
# This is one of those things, range is where it becomes a lot more familiar and
#
# makes more sense once you've actually spent some time testing it and
#
# going through it.
#
# So, let's just run this result or run this little program.
#
# And there's the results that it printed out, which may or
#
# may not be what you thought it would be.
#
# All right, so I'm going to actually leave this video here now,
#
# leave it to do some experimentation.
#
# In the next video, we're gonna talk about tuples or tuples, depending on how you
#
# pronounce it, which is something that is a very, very useful concept in Python.



decimals = range(0,100)
my_range = decimals[3:40:3]
print(my_range == range(3,40,3))
print(range(0,5,2) == range(0,6,2))
print(list(range(0,5,2)))
print(list(range(0,6,2)))

r = range(0,100)
print(r)

for i in r[::-2]:
    print(i)

print("*" * 50)
for i in range(99, 0, -2):
    print(i)

print("*" * 50)

print(range(0,100)[::-2] == range(99, 0, -2))

for i in range(0,100, -2):
    print(i)   # it will not print anything because if you are choosing -2 then order should be reverse like 100,0

print("*" * 50)

for i in range(100,0, -2):
    print(i)   # so this is what this working - so the start value will always be higher. in case of negative slice

print("*" * 50)

backString = "egaugnal lufrewop yrev a si nohtyP"
print(backString[::-1])


print("*" * 50)

r = range(0,10)
for i in r[::-1]:
    print(i)









