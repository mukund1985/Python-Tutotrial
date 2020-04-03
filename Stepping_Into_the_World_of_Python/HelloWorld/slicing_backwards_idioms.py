########## Slicing Backwards ############

# We've seen that you can use negative start and stop values in a slice. You can
#
# also use a negative step. There's only one thing to watch out for, and it's
#
# one of those things that's obvious, once it's been pointed out. If I asked you to
#
# count backwards from 99, and stop when you reach 100, how would you get on?
#
# You'd tell me it's impossible, of course, and you can't possibly get to 100 by
#
# counting backwards from 99. Well, neither can Python. Now that you know that, you
#
# won't make the most common error that people make when using negative steps in
#
# a slice. Alright, so let's see some examples. We want to create a new Python
#
# file called sliceback.
#
# So I'm going to start by typing letters equals and the alphabet abcdefg etc.
#
# Then on line 3 I'm going to type backwards equals letters square brackets
#
# 25:0:-1 then the closing right square bracket, and we're
#
# going to print backwards. Alright so I've created a slice that
#
# starts at index 25, which is the z, and I set the stop value to 0 and use the
#
# step of -1. So what do you expect the output to be here? So pause the video
#
# and have a careful think, and come back when you think you've got the answer.
#
# Alright, so let's run the program now to see if you were right.
#
# So we get the letters of the alphabet in reverse order from z down to b. Notice that the letter
#
# a isn't included. We used a stop value of zero, and slices extend up to, but not
#
# including, the stop value. Before I ask you another question, let's review what
#
# we've got here, on line 3. Because we're using a negative step, the start
#
# value must be greater than the stop value. Our slice starts at index position
#
# 25, and it extends down to index position 0, but doesn't include the character
#
# at that position. We're stepping by -1, which produces all the letters from
#
# z down to b. So my second question is, what stop value will let the slice
#
# include the letter a? There's two obvious answers to that but only one of them
#
# works. So have a think and run your code, to try your answer before starting the
#
# video again. So pause the video now.
#
# Alright so how did you get on? So one obvious answer; if a slice doesn't
#
# include the position at the stop value, is to use a stop value of -1.
#
# But unfortunately that's the one that doesn't work, so if we try that, and use a
#
# stop value of -1,
#
# when we run it, we don't get any output. So you may have
#
# worked out why. Remember that negative stop values count backwards from the
#
# end of the sequence. Minus 1 means the last character in the string, which means
#
# we've requested a slice that extends from the z up to, but not including, the z,
#
# and therefore we get nothing. The other obvious answer is to omit the
#
# stop value. Python will default to the start or end of the sequence, if we don't
#
# specify start or stop values. So it's clever enough to work out that it should
#
# reverse the defaults when we're using a negative step. So if I change that now,
#
# get rid of the -1 for our stop. Run this, and you can see that the code works.
#
# With a negative step, the start value will default to the end of the string,
#
# and the stop value defaults to the start of the string. That means we can ommit
#
# our start value as well. So we can go back and do that, and if we run it now,
#
# once again we get the string reversed. A slice of ::-1 is a Python idiom.
#
# When you see that, you'll recognize it as reversing the sequence. I'll cover a few
#
# more slicing idioms in the next video. There's not much else that
#
# I can say about slicing backwards. Just use a negative step and make sure the
#
# start value is greater than the stop value. Experiment with different values
#
# and make sure you're comfortable with what a negative step produces. I'll
#
# finish this video with a challenge, and go over the solution to that challenge
#
# in the next video.
#
# That's your challenge. Have a go at that, and as mentioned








#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]

print(backwards)

backwards = letters[25::-1]   # To get all letter including a

print(backwards)

backwards = letters[::-1]   # there is no need to give the starting value and this is called as Python slicing idiom

# Just start value should be greater than stop value

print(backwards)

#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

# start:stop:slice

# Just use a negative step and make sure the
#
# start value is greater than the stop value

### Challange -

# 1. Create a slice that produces the character qpo using the letters variable

backwards = letters[16:13:-1]
print(backwards)

# 2. Slice the string to produce edcba

backwards = letters[4::-1]
print(backwards)

# 3. Slice the string to produce the last 8 character

backwards = letters[25:17:-1]
print(backwards)

# or

print(letters[:-9:-1])


# Next Video


# Alright so how did you get on with the challenge from the last video.
#
# The first part of the challenge was to slice the string to produce the letters q, p and o.
#
# So let's have a go at doing that. So I'm going to type, on line 7, print
#
# parentheses letters square brackets 16:13:-1
#
# So we're standing at position 16.
#
# We're extending backwards, up to, but not including the character at position 13.
#
# So let's run that, and there's the letters q, p and o. So next we want a
#
# slice to produce the letters edbca. The easiest way to include the beginning
#
# is to type print parentheses letters[4::-1]. So if we
#
# run that,
#
# and there's the letters edcba.
#
# Finally, we wanted the last eight
#
# characters in reverse order. So we'll be using a negative step value, which means
#
# the start will default to the end of the string and can therefore be omitted.
#
# So to type that, I'm going to do a print parentheses letters square brackets
#
# :-9:-1
#
# Alright so running that, and there's the last 8 letters, zyxwvuts. Now there are other solutions you could have
#
# used, especially when returning items from the beginning and end of the
#
# sequence. Using default values for the start and stop is recommended, when
#
# trying to return a certain number of characters from the beginning or end of
#
# a sequence. If you managed to produce the correct strings with your slices, well done.
#
# Alright, so I'll finish talking about slices for now, by looking at some
#
# common idioms that Python programmers use and recognize.
#
# In the last video, I mentioned that a slice of ::-1 is a Python idiom. When you see
#
# that, you'll recognize it as reversing the sequence.
#
# Let's see some more idioms. The first is to return the last n items in a
#
# sequence. So let's say we wanted the last four characters from letters. So I'm
#
# going to come down, and on line 15 I'm going to type print parentheses letters
#
# [-4:] If I run that you should get the last
#
# four letters, wxyz. Whenever you see a slice with a negative start value and
#
# defaults for the stop and step, that just returns the end of the sequence.
#
# Our common use of that is to get the last item by specifying -1 for the start
#
# value. So let's have a go doing that. So I'm going to type print parentheses then
#
# letters[-1:] Run that, we get the last item, in this case, the z.
#
# Now you can also use a slice to get the first character, very similar. We just
#
# type print(letters[1:]
#
# Run that, and I actually did that the wrong way, because that obviously gave us
#
# everything but the first, starting at sequence position 1. It should have been [:1],
#
# which is what I meant to type. Running that, we now get the letter a, which is
#
# the first item in the sequence, the first character. Now that last one is useful
#
# because it doesn't give an error if the sequence is empty. It may though, be more
#
# natural to get the item at index position 0, and that works with a string.
#
# So we could also do it as print(letters[0]),
#
# and that's the same, gives us the same result. That works, but what would happen
#
# if our string was empty? So I'm going to go up and delete the letters, or the
#
# characters rather, on line 1. So I'll make that an empty string.
#
# Run the program, and we now get an error, and the error is: string index out of range.
#
# You can't access the first item of a sequence that doesn't
#
# any items. So looking at the code, the slice on line 17 produces an empty
#
# string, instead of crashing with an index error, and just to confirm, if I run it again,
#
# the error's actually talking, or is showing on line 18, as you can see there.
#
# So I had no problems with executing line 17. So the idiom on line 17 is
#
# useful for getting the first item in a sequence, without your code crashing.
#
# If the sequence is empty, you'll get an empty sequence back, and that's often
#
# what you'd want to happen. Alright so that's the end of slices, for now.

# Some idioms see -

# Last four character

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])



letters = ""
print(letters[:1])
print(letters[0])