# THE ESCAPE CHARACTER -
#
# The backslash character has got a special meaning in strings.
#
# It's used to escape the character that follows it, to give that character special meaning.
#
# Now some examples are backslash n, to start a new line, and backslash t to insert a tab.
#
# So let's go ahead and create a new Python file.
#
# I'm going to call this one escapechar.py
#
# Alright, so start by typing splitString is equal to,
#
# and in double quotes, This string has been, and we'll put a backslash n there, and type split over.
#
# Then backslash n several backslash n lines,
#
# and to confirm what this looks like, we're going to type print, and in parenthesis, splitString, like so.
#
# Now before I run this, remember to check what your IDE thinks you want to run.
#
# Now we haven't executed this code before, so we have to right click in the editor to run it from there,
#
# and you can see in the top right hand corner,
#
# it's going to run strings if we just click on this button here,
#
# which is not what we think should happen.
#
# So I'm just going to close that off. I'll just type in the answer there, close that off.
#
# So again, what we need to is right-click and select run.
#
# Alright, and now we can see those backslash characters and what they're doing.
#
# You can see how the string has been indeed spit over several lines in the output.
#
# So whenever the print function sees backslash n in a string,
#
# it causes it to start a new line.
#
# Many IDEs will color escape characters differently in the code,
#
# as IntelliJ IDEA is doing on my screen. You can see that on line 1, the various backslash ns there.
#
# Alright, so that was backslash n. We can also tab the output.
#
# So using backslash t causes Python to tab to the next stop before printing. So let's go ahead and try that.
#
# So I'm going to type tabbedString is equal to, and in double quotes I'm going to type 1\t2\t3\t4, you guessed it, \t5.
#
# Alright and then print that out to print and in parentheses, tabbedString this time, and we'll run this.
#
# We can see the numbers 1 to 5 are printed out, tabbed across the screen.
#
# Now different consoles have different tab stops. In IDEA, the tab stops are every four characters.
#
# But if you run this program from, say, a terminal or a command prompt,
#
# the tab stops will probably be set to eight characters, so keep that in mind.
#
# So the backslash can also be used to escape special characters, such as quotes and double quotes,
#
# and that can be useful if they you've got a string containing both of those characters.
#
# So to see what I mean, let's type some more code.
#
# So I'm going to type print parenthesis and single quote,
#
# and I'm going to type The pet shop owner said, and then double quote, No, no, and a space, we're gonna put a
#
# backslash single quote, bear with me here, e backslash single quote again, s then r.
#
# Hopefully you're recognizing the reference here, and three periods, he backslash single quote s resting,
#
# and closing double quote, a period and a single quote which is already there, and the right parenthesis.
#
# So that's one option, or what we can do,
#
# is we can come back and also try another version of that,
#
# and we can put, and I'll put a comment there, hash or. We can do it another way print, and put a double quote this time,
#
# The pet shop owner said, space backslash double quote
#
# No, no, space single quotes e, and we're putting the e in single quotes there,
#
# s for e's uh comma three periods, he's resting.
#
# Then we want to put a backslash double quote a period,
#
# then we've got the closing double quote from the start of the line, and the right parentheses.
#
# Let's just run this first.
#
# So you can see now that what the pet shop owner said is in double quotes, but his statement includes apostrophies,
#
# and that means that we have to escape one or the other.
#
# So on line 7, the string is delimited with single quotes, as you saw,
#
# and we have to escape any single quotes that appear in the string.
#
# However, on line 9 what we've done, is we've delimited using double quotes,
#
# and that means the double quotes inside the string must be escaped.
#
# Now another alternative is when you use triple quotes, which we'll do now,
#
# there's no need to escape any quotes inside the string. So I'm going to type print
#
# left parenthesis and three double quotes, and noting that IntelliJ added the last three for us automatically,
#
# and I can type The pet shop owner said,
#
# then a double quote. Notice we're not using the backslash now for escape characters, no, no, single quote,
#
# e single quote, s for e's uh semicolon three periods, he single quote he's resting.
#
# Then we've got our double quote to close off the quote, from the start of No, no, he's uh, ... he's resting
#
# and we want to put a period there, and we'll just put a space and the three double quotes on the right-hand side.
#
# Close off the print line with the right parenthesis.
#
# So basically, when we're using triple quotes there, there's no need to escape any quotes inside the string.
#
# Python knows that the string doesn't end, until it finds those matching triple quotes at the end.
#
# And just to confirm this we'll run it,
#
# and as you can see, we've got exactly the same output.
#
# So another reason we might want three consecutive quotes
#
# is because of a feature Python provides, to make strings spanning lines more readable.
#
# So the string that we split over several lines earlier, is not easy to read because of the embedded backslash ns.
#
# but Python allows the string to be split over several lines without doing that, by using triple quotes
#
# So to see what I mean, let's type some code in.
#
# We'll do this on line 13. So I'm going to type anotherSplitString is equal to, three double quotes,
#
# This string has been, I'm pressing enter there, split over, enter, several, enter, lines.
#
# Then on the next line, which is the line after, just to make it clear, and I'm gonna print another string, anotherSpitString.
#
# If we run that,
#
# and you can see This string has been split over several lines.
#
# So we're basically getting line breaks in the output.
#
# Now if you want to lay out a string with breaks, but don't want every one to start with a new line when printed,
#
# then what you can do is escape the end of a line with a backslash.
#
# So to see what I mean there,
#
# we can come to the end of the line. We'll come up here to line 13, has been been space, we'll put a backslash there.
#
# On the next line, do the same, space backslash several backslash after the space,
#
# and now if we run this, you'll see the difference in the output.
#
# The string has been split over several lines, is actually no longer true.
#
# It's now all on the same line because we've used the backslash to escape the end of the line.

splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')

# or

print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

# So you can see now that what the pet shop owner said is in double quotes, but his statement includes apostrophies,
#
# and that means that we have to escape one or the other.
#
# So on line 179, the string is delimited with single quotes, as you saw,
#
# and we have to escape any single quotes that appear in the string.
#
# However, on line 183 what we've done, is we've delimited using double quotes,
#
# and that means the double quotes inside the string must be escaped.

# Now another alternative is when you use triple quotes, which we'll do now,
#
# there's no need to escape any quotes inside the string like below -

print("""The pet shop owner said "No, no, 'e's uh,...he's resting".  """)

print("""The pet shop owner said "No, no, \
'e's uh,...he's resting".  """)

anotherSplitString = """This string has been
split over
several
lines"""

print(anotherSplitString)

anotherSplitString = """This string has been \
split over \
several \
lines"""

print(anotherSplitString)

# Excercise

print("""Number1\tThe Larch
Number2\tThe Hosrse Chestnut""")


# Alright so we finished the last video by getting the text to output all on one line,
#
# even though we've split up our code, and that's the code on lines 13 through 15.
#
# And I'll be talking about code style a bit later,
#
# and we'll see why you might want to split the lines of code up like that.
#
# The good news is that it doesn't just work with triple quotes either.
#
# I can actually split, coming back up here to line 11,
#
# I can split that up as well.
#
# So I'm coming down here to the end of line 11.
#
# So let's do it after the no no, so no no comma.
#
# I'm going to put a space and a backslash there, and press Enter,
#
# and I'll just remove that initial space there at the start so it's directly under, because we've already got a space
#
# after the no-no. So when I run the program,
#
# we still get the whole message on the single line, which is pretty neat.
#
# Alright, so in total that's three ways to delimit strings in your code.
#
# We've also looked at using the escape character, the backslash, to add special characters like a line feed or tab.
#
# But what if you wanted to include the backslash character in your string.
#
# Well, there are a few ways of doing that.
#
# Let's see some examples of that.
#
# So I'm going to come down, firstly, on line 21. Let's make a start, and we're going to type
#
# print parentheses double quotes, and we'll type in our path so
#
# C:\Users\timbuchalka\notes.txt,
#
# then close off the string and the right parenthesis
#
# Now obviously, as I was typing that and looking at it now, clearly there's something funny going on there,
#
# because the IDE, in this case, has highlighted slash users,
#
# and if you look carefully it's also underlining imbuchalka, and it's saying there's a spelling mistake.
#
# typo in word, as you can see there.
#
# Now what's important about that warning isn't that it's a spelling mistake.
#
# I wouldn't expect any dictionary to contain the word timbuchalka.
#
# Now what's interesting is that it mentions imbuchalka, without the t.
#
# Because of the backslash character it's interpreting the t of tim as a tab character,
#
# and it's also interpreted the n of notes as a line feed character.
#
# The backslash before Users is also causing problems.
#
# Backslash U also has a special meaning, and it's used to include things like accented characters in your strings.
#
# Okay, so we obviously can't include backslash characters just by typing them,
#
# so let's see two ways we can handle this.
#
# What I'm going to do is duplicate this first line to give us two copies to work with.
#
# So in IntelliJ, command D, sorry ctrl D, will do it on a PC,
#
# command D on a Mac.
#
# So the first way is to escape the backslash by putting another backslash before it.
#
# So we'll just literally find all the backslashes in the string and add a second backslash.
#
# So that looks better. By escaping the backslash with another backslash,
#
# we've told Python that we want the backslash character to be output.
#
# The second way is to use a raw string.
#
# Raw strings are intended for use with regular expressions,
#
# and we can create a raw string by prefixing the string with the letter r, r for raw .
#
# So I can come up to line 22 now, and put an r there,
#
# and you can see now that that line also looks better.
#
# Now when I run the program,
#
# both lines now print the same thing, with a single backslash in each place.
#
# In general, I'd recommend using the first method, escaping your backslash characters.
#
# We'll see why that's preferable to using raw strings, a bit later in the course.
#
# Alright, so let's finish this video here, and in the next one, we'll look at variables in Python.
#
# And it turns out we've used a couple of variables already.


# It has issue print("C:\Users\timbuchalka\notes.txt")
# We can change like this -
print("C:\\Users\\timbuchalka\\notes.txt")
print(r"C:\Users\timbuchalka\notes.txt")

