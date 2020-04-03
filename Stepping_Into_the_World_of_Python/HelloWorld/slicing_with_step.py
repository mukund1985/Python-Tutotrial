####### Slicing with Step ################

# So far we've only been providing two values to our slices, the start and stop
#
# values. But slices can also take a step value, which defaults to one. So let's see
#
# some examples before we discuss the syntax more formally. So what I'm going
#
# to do is delete the code, other than the definition of parrot on line 3,
#
# and I'm going to type on line 5, print parenthesis parrot square bracket
#
# 0:6:2, and close off the square bracket and parentheses, and we'll put a
#
# comment to the effect of the output being capital N r e. And on line 6 I'm
#
# going to type print parenthesis parrot left square bracket 0:6:3 this
#
# time, and right square bracket and parenthesis, and comment, the output
#
# should be Nw. So the slice on line 5 is starting from index 0, which is the
#
# capital N, extracting all the characters up to, but not including index 6, which is
#
# the i, in steps of 2.
#
# So let's confirm that that works by running it, and you
#
# can see we get the output that we thought we should get, and you can see
#
# that we've got that output. Alright so another example of a slice where the
#
# step is as follows; so I'm going to start type some code on line 8. I'm going to start by
#
# typing number equals, and double quotes 9 comma 2 2 3 comma 3 7 2 comma 0 3 6
#
# comma 8 5 4 comma 7 7 5 comma and 8 0 7, and we've got a closing double quote there.
#
# Now on line 9 if I type print parentheses number then square
#
# brackets again 1 colon colon 4, and closing off the
#
# right bracket and right parenthesis. Now if we run that, it doesn't appear to be very
#
# useful but it does illustrate using a step in slices. So it starts at position 1,
#
# which is the first comma, and it's slicing every fourth character. The list
#
# extends all the way to the end of the string and that's because we've omitted
#
# the stop value, and that gives us all the commas. So I said it didn't appear to be
#
# useful, however, it can be. In order to show you how it's useful, we're gonna have
#
# to use some things that we'll be looking at later. I don't like doing this
#
# generally, and I won't be doing it often, but I think something like that slice
#
# will make more sense if you can see a practical application of it. So what I'm
#
# going to do is start by changing some of the separators. At the moment they're all
#
# commas, but it's possible we may have to process a stream that contains a mix of
#
# separators. So what I'm going to do is use a mix of commas, semicolons, colons
#
# and spaces. These are all the things you might find used as separators when
#
# processing data. So we've got 9 comma 2 2 3. Let's change the comma
#
# after the 2 2 3 to a semicolon, and then moving on we've got, after
#
# 3 7 2, we'll replace that comma with a colon. The next one after the O 3 6,
#
# we'll put a space there instead, and we'll leave the next one,
#
# 8 5 4, leave that as a comma, and the one down the end here
#
# before the 8 0 7, we'll add a semicolon there as well. So if we run this program
#
# again now, we've changed those separators. You can see with the output there, we've
#
# actually got comma, semi colon, colon space, comma, semicolon. So why is that
#
# useful? Well if that number string represents seven values that appear in a
#
# data file, we can use the separator string to split out the seven values. Now
#
# this is the bit that I don't want you to worry about. Think of it as a
#
# demonstration. It's all stuff that you'll be learning about in later videos.
#
# So what I'm going to do is start by binding a variable to the slice instead of
#
# printing it out. So I'm going to change line 9 there. Instead of print, we're going
#
# to type separators is equal to, and I'll just remove the parenthesis on the end
#
# there, and then we're going to print separators.
#
# So we've now going a string containing all the separators that we used in
#
# numbers. Now it's not necessary to print it, but on line 10 I'm doing that anyway,
#
# just to confirm that we've got the separators, and obviously that should
#
# work because we've just only made a small change there, by binding it to the
#
# separators variable. Now we can use the separators to split out the individual
#
# values. This is the interesting part. So what I'm going to do is add that. I'm
#
# going to close down the run window, and on line 12 I'm going to type values is
#
# values = "".join(char if char not in separators else " " for char in number).split()
#
# Then on the next line
#
# print([int(val) for val in values])
#
# Now I don't expect that code on lines 12 and 13 to make sense. Again, I'm using it to
#
# demonstrate why extracting every third character from a string might be useful.
#
# As you work through the course, you'll learn what this code's doing and you'll
#
# be able to write code like that for yourself. Now if you're typing the code in
#
# as you watch, you may want to copy and paste those two lines from the
#
# transcript for this video. The source code is also available in the resources
#
# for this video if you want to do that. It's very important that you use the
#
# correct type of brackets. The second one you see me use was a square bracket, and
#
# obviously, I'm using parentheses there, which some people also call brackets,
#
# as well. So basically, make sure you've typed it in exactly as you can see it
#
# here in order for it to work. Now if we run this program, and you can see the output
#
# is now showing us the seven values that we've extracted from the string, that
#
# we bound to the number variable on line 8. I think that's pretty impressive when
#
# you consider it's only a few lines of code there, and I'll just bring that back on
#
# the screen so you can see it. It's very hard to come up with real-world examples,
#
# when all we've covered so far in the course are variables, ints and strings, but
#
# hopefully, that demonstration has put the slice into a useful context. So make sure
#
# though, you understand how that slice on line 9 is working, and then I'll see
#
# you in the next video. And in that video we're going to look at slicing backwards.


#         432109876543210
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

# print(parrot[start:stop:slice])
# slice is nothing but jump and print the position of that given number
# For example below 2::4 - so it will start at 2 and since we have not given any stop it will go untill last
# and it will maintain to print 4th positioner  so it will print 230878

#         0123456789012345678901234
number = '9,223,372,036,854,775,807'
print(number[1::4])
print(number[1::3])
print(number[2::4])

number = '9,223;372:036 854,775:807'
seperators = number[1::4]
print(seperators)

values = ''.join(char if char not in seperators else ' ' for char in number).split()
print([int(val) for val in values])