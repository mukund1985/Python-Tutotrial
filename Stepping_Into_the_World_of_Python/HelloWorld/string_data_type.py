############### The str String Data Type ##############

# We've used strings, in earlier examples, to print messages on the screen.
#
# Now we're going to look at some of the other cool things you can do with them.
#
# So open the Hello World project and create a new Python file.
#
# So I'm gonna do that, and I'm going to call this one strings2.
#
# It's alright to use digits in your file names, by the way, but avoid starting the name with a digit.
#
# We'll be seeing how one program can import code from another program,
#
# but some file names can cause problems with that.
#
# So use the same rules that apply to Python variable names, and you won't get any problems.
#
# Alright, so strings are one of the Python sequence data types,
#
# which makes sense because they are a sequence of characters.
#
# We've seen how to print them out and concatenate strings together,
#
# but we can also pick out individual characters or sub strings.
#
# So let's type some code here.
#
# So I'm gonna start by typing parrot is equal to, and in double quotes, "Norwegian Blue".
#
# Then on line 3 I'm going to print, print parentheses parrot,
#
# then on line 5 I'm going to do print parentheses parrot left square bracket 3 right square bracket,
#
# and that should be parrot.
#
# So run the program to check what it does.
#
# So here we're binding the variable called parrot to the string "Norwegian Blue",
#
# and then printing parrot.
#
# We can also print individual characters from the string,
#
# and the last statement prints the letter w.
#
# Now that might seem odd because w is the fourth letter of Norwegian,
#
# but its usual for programming languages to start counting at zero and not one.
#
# So that's parrot, zero in square brackets is a capital N.
#
# There are 14 characters in Norwegian Blue, numbered from 0 to 13.
#
# So what I'm going to do is add a comment to the code, to show the index positions.
#
# Right so I'm going to come up here to line 1,
#
# and I'm just gonna make a bit of space and paste it in, like so.
#
# So the character N is at position zero, and we've already seen that w is at index position 3.
#
# The last character in the string, the e in Blue, is at position 13,
#
# so that gives 14 characters, numbered from 0 to 13.
#
# If we try to print parrot 14 in square brackets, we'll get an error: index out of range.
#
# So the number inside the square brackets on line 7 is called an index, and it's used to index into the string.
#
# So notice that I've used square brackets on line 7.
#
# There are 4 uses of square brackets in Python,
#
# and they all involve accessing individual items in something.
#
# We'll see them used again when we look at dictionaries and sets.
#
# For now though, it's time for a mini-challenge.
#
# Throughout the course we'll have some challenges.
#
# These give you a chance to practice what we've done so far,
#
# because doing is more effective to learn than just watching.
#
# So don't think of these challenges as tests because they're not that.
#
# You can't fail the challenges as such, because that's not what they're for.
#
# They're there as part of the learning experience to help you understand the Python programming language better.
#
# So if you spend time trying a challenge, but have to look at my solution, that's fine.
#
# If you go straight to my solution,
#
# you won't get as much out of them, as if you will if you spend some time trying to solve the challenge first.
#
# So your challenge is as follows:
#
# So pause the video now and have a go at this, and come back when you're ready to see my solution.
#
# Alrighty so welcome back. How did you go? Did you manage to solve it?
#
# Did you get the correct output?
#
# Well, to get the correct output, we need to use indexing which we've discussed,
#
# and we need to print the correct characters out of the string Norwegian Blue.
#
# The program is already printing the w as we saw, so the next character we want is an e.
#
# Now there are two that we could use, at positions 4 and 13.
#
# I'm going to use the one at index position 4, so I'm going to go ahead and do that.
#
# print parenthesis parrot square bracket 4 and the closing right square bracket,
#
# and we've got our normal right parenthesis.
#
# So next we need a space and that's set at position 9 in our string.
#
# So I'm going to type print parenthesis parrot, left square bracket, and 9,
#
# and we get the word w i n by printing the characters at positions 3, 6 and 8.
#
# So I'm going to quickly do a copy and and paste here to save a bit of time.
#
# So it's positions 3, 6 and 8.
#
# Alright so I'm gonna run the program to check that it works,
#
# and you can see we've got Norwegian Blue output at the top, and then we've got we space win
#
# showing as output, one character at a time, and obviously, that was reading downwards.
#
# Alright, so when I run the program, as you saw, it prints we win reading downwards.
#
# Now if you got the same output and you used indexing to do it, then well done.
#
# Now if you struggled with this concept,
#
# watch the video again and experiment until you're comfortable indexing a sequence,
#
# and try it with different strings as well.

#         012345678901234
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])

# Mini Challange

# Add some code to the program, so that it print out "We win"
# Each character should appear on a separate line
# The program should get the characters from the parrot string, using indexing
# The w is already print out, you just need to print the remaining 5 characters.
# With the text that is already being printed, the final output from the program should be:

print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
