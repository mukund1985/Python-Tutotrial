####### Slicing With Negative Numbers #############

# Contining with our strings2 program, I'm going to delete everything except the
#
# definition of parrot on line 3, and also the first slice.
#
# The start, stop and step values in a slice
#
# can also be negative. So let's add some code on line 7,
#
# print then left parentheses parrot left square bracket -4:2
#
# right square bracket then right parenthesis. Now if we run this we'll find
#
# that this actually doesn't print out anything. So it doesn't print the two
#
# characters starting 4 in from the end of the string, and it's printing nothing, as
#
# I mentioned, and that's because you can't go backwards from the starting position.
#
# So instead we'd have to write that as -4, which we've got, but then -2,
#
# and as a comment that should give us Bl.
#
# As another example print
#
# parentheses parrot again, then left square bracket -4:12 right square
#
# bracket right parenthesis, then that will actually give us the same thing. So if we
#
# run this, you can see we've got Bl in both cases there. So the first one, on line 7,
#
# that prints from index -4 and that's B, capital B, up to but not
#
# including the second-to-last character in the string, which is u.
#
# Now the second example, on line 8, prints the same thing but this time it's interpreted as
#
# from index -4, up to but not including index position 12.
#
# So spend some time experimenting with negative indices.
#
# There's nothing tricky about them. they're just counting from the end of
#
# the string, instead of from the beginning. Make sure you can reproduce all the
#
# slices from the last video, using negative indices. I'll do the one on line 5
#
# just to get you started, and we'll do that just immediately under
#
# line 5. So the negative version of that would be print parentheses parrot square
#
# bracket -14:-8. Then we want our right to square bracket right
#
# parenthesis and that should give us the same result.
#
# So let's just run that to make sure that it works, and you can see we've got Norweg
#
# outputted twice. So again, make sure you go through and reproduce all the
#
# slices from the last video, using negative indices, to really make sure
#
# that you understand how they work. But also, with that said, create your own
#
# strings and practice on them as well.


#         432109876543210
#         012345678901234
parrot = "Norwegian Blue"
print(parrot)

# Slice = Start, Stop and Step Values

print(parrot[0:6]) # Norweg

print(parrot[-14:-8]) # Norweg

# print(parrot['0-14':'6-14']) Actually it is doing this 


print(parrot[-4:-2])  # Bl
print(parrot[-4:12])  # Bl


