########## Slicing in Python ###############

# Python sequence types let you create a slice.
#
# The only sequence type we've looked at so far is the string type, so let's
#
# continue with our strings2 program. What I'll do is delete all the code
#
# except for the comment and the parrot definition, so let's go ahead and do that.
#
# So we can produce a slice by providing three numbers separated by colons.
#
# Now these numbers are the start, stop and step values. I'll introduce the step value
#
# soon, but first let's look at slicing without a step. So we're going to type print
#
# parentheses parrot left square bracket 0 colon 6 and right square bracket, then
#
# our right parentheses. I'm going to add a comment as well, hash N o w, sorry
#
# N o r w e g. So here we're telling Python to start at position 0 and slice
#
# up to, but not including, position 6, and I've added a comment with a hash
#
# character there to indicate the result that we should get. So if we run the
#
# program now, we get the output in the output pane, Norweg.
#
# So when I said not including,
#
# that's important and something that new Python programmers often forget.
#
# The last character you specify isn't included in the slice. It turns out that
#
# not including that last character makes slices much easier to use, but it'll
#
# probably catch you out at first. In fact, not including that final value is
#
# something that happens in other places in Python, such as ranges.
#
# Now don't do this if you're at work, in an open-plan office, but if you're somewhere safe
#
# where you're not going to get funny looks, say out loud 10 times, "up to but not
#
# including", "up to but not including", "up to but not including". Alright, so getting
#
# back to our code, the slice on line 5 produces the characters from index 0 up
#
# to, but not including, index 6. So let's see some more examples to understand how
#
# slices work. So let's say we wanted the characters w e from the string, then we'd
#
# slice from position 3, the w, up to but not including position 5,
#
# the g. So let's type in the code for that. So on line 6 I'm going to type
#
# print left parenthesis parrot left square bracket, then we're going to type 3
#
# colon 5, as I mentioned, then our right square bracket, right parenthesis,
#
# and we'll run the program. We should see w e outputted, and there's w e in the
#
# output pane. So what else can we do? Well we can get the first word by
#
# getting the slice from position 0, up to but not including position 9. So let's try that.
#
# So print left parenthesis parrot left square bracket 0 colon 9, then our
#
# right square bracket and right parenthesis, and we'll run that,
#
# and there's the entire word, Norwegian. When creating a slice, the first value is the
#
# position to start at, as you've seen. That's separated from the position to
#
# stop at with a colon, which again, you've seen. But if you don't provide a start
#
# value, you still need the colon. So we could write that last slice, that we've
#
# got on line 7, differently, by typing print, on line 8, a left parenthesis
#
# parrot left square bracket, then just colon 9 this time, right square
#
# bracket right parenthesis, and we can run that. And as you see we get exactly the
#
# same result, and that's this time, the difference is, we didn't provide a start
#
# value. Basically, our lines 7 & 8 both do the same thing because the start value
#
# defaults to the start of the sequence, and obviously on line 7 we included the
#
# start value and line 8, we didn't include it.
#
# Alright so let's look at some slides to explain exactly what's going on here.
#
# So at this point you should be able to create a slice
#
# that returns the word blue, so pause the video and come back when you've had a
#
# go at that.
#
# Alright, so welcome back. So to slice the word blue from our string, we need to
#
# start at position 10, and extend up to position 14. So let's do that.
#
# So I'm going to type print left parenthesis parrot left square bracket, 10 colon 14
#
# right square bracket and right parenthesis, and if we run that, we should see the word Blue.
#
# And there's Blue on the screen. And again,
#
# there's no character at position 14, but remember that slices extend up to, but
#
# not including, the stop value. We saw that we can leave out the start value and it
#
# will default to the start of the sequence. If we leave out the stop value
#
# then it defaults to the end of the sequence. So that means that we can
#
# rewrite the last line, line 10, on line 11, as print left parenthesis parrot left
#
# square bracket 10 colon, and this time we're leaving off the other value. So
#
# we've got a right square bracket and right parenthesis and if I run that, we
#
# get the same output, in this case, the word Blue. It's important to include the
#
# colon that separates the start and stop values. We haven't provided a stop value,
#
# but we still need the colon, so that Python knows that we want a slice.
#
# Without the colon, that would be in index, and we'd get a single character at
#
# position 10. I mentioned that there are four different things that square
#
# brackets are used for, and slicing is the second thing. They're used for indexing
#
# and they used for slicing. If you use square brackets for slicing, you must
#
# have at least one colon, otherwise it's in fact, an index and not a slice.
#
# Alright so I've got a question for you. Before I ask it, we'll have a quick recap.
#
# If the first number in a slice is omitted, the slice will start from the
#
# beginning of the string, and if the second number is omitted, it'll run to
#
# the end of the string. So it's a recap,
#
# print parentheses parrot left square bracket colon 6 right square bracket
#
# right parenthesis, and print left parenthesis parrot left square bracket
#
# 6 colon, then a right square bracket and right parenthesis. So again, the first number in
#
# a slice is omitted, the slice starts at the beginning of the string, and if
#
# the second number is omitted, it'll run to the end of the string.
#
# The slice indices are defined such as string square bracket colon n + string square
#
# bracket n colon, is the same as the original string. So to show you what I
#
# mean I'm going to type some code on line 16 this time, print left parenthesis
#
# parrot left square bracket colon 6. We've got a right square bracket,
#
# + this time, I'm going to add a space there, and a plus, another space then parrot
#
# left square bracket 6 colon, then we've got our right square bracket and our
#
# right parenthesis again.
#
# So if we run this,
#
# you can see, in fact, we've got the
#
# entire Norwegian Blue outputted to the screen. So at this point, my question to
#
# you is, what happens if we only have a colon in the slice? In other words, what
#
# will this produce?
#
# print left parenthesis parrot left square bracket colon and right
#
# square bracket parentheses. So have a think about that and see if you can
#
# figure it out before running the program. Pause the video now and come back when
#
# you've got an answer.
#
# Alright so welcome back. Did you work it out?
#
# Well if you don't provide a start value,
#
# the slice starts at the beginning of the sequence. So there's no start
#
# value on line 18, so we start at the beginning. Now if you don't provide a stop
#
# value, the slice extends up to the end of the sequence, and we haven't got a stop
#
# value on line 18 either. So that means the slice will start at the beginning
#
# and extend right up to the end. So if we run the program now,
#
# we get the complete string printed out.
#
# So you might be wondering at this point, why we'd don't want to do that.
#
# When dealing with strings you probably wouldn't, and I'll
#
# come back to it when we look at another sequence type, a list.
#
# When dealing with lists, a slice like this one, that produces a copy of the entire original,
#
# can be very useful. I've covered it now because we're looking at start and stop
#
# values in a slice, and we'll see some practical applications of it, later in
#
# the course. Alright I'm going to stop the video here.
#
# Before watching the next video,
#
# experiment with slices with different strings. So a good one that you
#
# might want to experiment with, would be this one which I'll add to the source code.
#
# So letters equals, and we're going to add the letters of the alphabet,
#
# like so.
#
# So that can be a good string to actually experiment with, but you can use any
#
# strings you want. Create some slices and make sure you get the results you wanted.

#         432109876543210
#         012345678901234
parrot = "Norwegian Blue"
print(parrot)

# Slice = Start, Stop and Step Values

print(parrot[0:6])  # Output - starting from 0 but not included 6th so Norweg - upto but not including
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

letter = 'abcdefghijklmnopqrstuvwxyz'
print(letter[:])
print(letter[3:8])