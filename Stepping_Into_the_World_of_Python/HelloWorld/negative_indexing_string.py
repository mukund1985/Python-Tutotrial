########## Negative Indexing String ####################

# So let's see some more things we can do with indexing,
#
# continuing with the strings2 program from the last video.
#
# Well, we can index backwards in a sequence, by using a negative number,
#
# so parrot square brackets -1 will give the last character e.
#
# So let's try this out.
#
# So I'm gonna come down here, and on line 14 I'm going to type print,
#
# and left and right parentheses just to make a blank line.
#
# Then on line 16 I'm going to type print parentheses parrot,
#
# and as I mentioned, using square brackets and put a -1 inside that square bracket.
#
# Now if we run that.
#
# Alright, so again an e printed after we ran the program, as you can see.
#
# Now note that minus zero doesn't really make sense here,
#
# so when counting from the end of the string, we start counting from -1.
#
# So continuing on, if I type print, on line 17, parentheses parrot and -14 in square brackets,
#
# and run the program,
#
# you can see we get the first N, the capital N, in the string.
#
# So I think a mini-challenge will help solidify negative indexes.
#
# It's really a mini mini challenge so I'm not going to use a slide.
#
# What I will do is take a copy of lines 7 through 12,
#
# and what I'm going to do is copy over lines 16 and 17.
#
# Alright so the mini-challenge is to change the indexes on lines 16 through 21,
#
# to use negative indexing.
#
# So we still want the message, we win, to be printed .
#
# So pause the video and come back, when you want to see my solution.
#
# Alright, welcome back. So to solve the challenge we have to use the index positions from the end of the string,
#
# where the last character is at position -1.
#
# So that means that w is at position -11.
#
# So if I change the 3 there to -11
#
# and run this,
#
# there's the first letter, and what we'll do is we'll go through and finish the rest now.
#
# The next one is -10,
#
# next one, -5,
#
# next one -11,
#
# next one - 8, and the last one, -6.
#
# We can run this and verify we still get the output, we win, one character at a time.
#
# Now you may have noticed that the negative index values can be obtained,
#
# by subtracting the string length 14, from the positive ones.
#
# So you may have actually done something like this, and what I'll do is I take another copy of lines 7 to 12.
#
# I'll come down here,
#
# and I'm gonna paste this down here, on line 23.
#
# So again, what I said was you may notice that the negative index values can be obtained by subtracting
#
# the string length, 14 in this case, from the positive numbers.
#
# So you may have done something like this, just basically, subtracting 14 from each value, so instead of 3,
#
# be 3 minus 14, 4 minus 14, 9 minus 14, 3 minus 14, 6 minus 14 and lastly 8-14
#
# Run the program
#
# and you can see there that we still get the output, we win,
#
# and what we could do to be consistent we could add another print there,
#
# and again, just to make sure we have got a space there and we can see that, we've still got we win.
#
# We've got basically three lots of we win showing on the screen,
#
# which is consistent with the fact that we've done this three times now.
#
# So experiment with negative index values to make sure you're comfortable with how to use them.
#
# You won't use negative index as often as positive ones, but when you do need to use them they're incredibly useful.

#         432109876543210
#         012345678901234
parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

# Negative

print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])
