#  STRINGS IN PYTHON
#
# Now in Python, strings can be enclosed in either double or single quotes, as I've mentioned previously.
#
# Let's just go through and type in a couple of examples, noting that these are all valid
#
# Python strings. So the first one we're going to start with, "Today is a good day to learn Python".
#
# You can see that's valid. Next line, using single quotes, "Python is fun".
#
# Next line, print double quotes Python single quote s strings are easy to use,
#
# and on line 4 I'm going to type print parentheses again,
#
# single quote, We can even include double quotes, quotes, in strings. Alright.
#
# So unlike some other languages like Perl, there's no difference between single or double quotes in Python.
#
# However, if you start a string with one type then you must finish it with the same type, and
#
# we've talked about that previously.
#
# If you need to include a single quote in a string, then use double quotes to enclose the string,
#
# like in the third example above.
#
# And similarly,
#
# if your string will include double quotes, then enclose the string in single quotes, as we've done on line 4.
#
# Now we can also concatenate strings to make longer ones, using plus.
#
# Let's go ahead and type print parentheses double quotes hello +
#
# double quotes again, world with a space at the start there.
#
# So that joins the two words together, to make the single string, hello world.
#
# So that's called string concatenation.
#
# Python isn't going to perform addition on the two strings. It just joins them together or concatenates them.
#
# So I'm gonna run the program to check that it prints what we expect.
#
# But remember to check the drop-down in the top right hand corner,
#
# and right-clicking the editor to run the correct program, otherwise you'll run helloworld.py by mistake.
#
# So if we do that without changing that, and run it,
#
# note that we're getting the Hello World output, and not the program output from this program,
#
# which could be a bit confusing for you. So you want to right-click in here instead,
#
# click on run the first time.
#
# By doing that, we're now running this program, and noting that in the top right hand corner,
#
# the drop down has now, or is now showing strings, being the current program that we're running.
#
# And you can see that in the case of line 5,
#
# we've got hello world showing - the two strings concatenated together to form one string -
#
# and we've got the single quotes and double quotes showing, as per the examples on lines 3 and 4,
#
# and the rest of the text, as per what we've set up.
#
# Alright, so we can also store the strings in variables, and then concatenation makes more sense.
#
# So let's go ahead and do that.
#
# So we can come down here,
#
# and I can type greeting equals Hello in double quotes, name equals, we'll type Bruce in double quotes.
#
# I'm gonna put a comment here, hash, if we want a space, we can add that too.
#
# And we type print left and right parenthesis, and within the parentheses we can type greeting,
#
# noting that I've just typed a g and IntelliJ helpfully gives us a menu that we can select from, and if we've got the
#
# menu options selected that we want, we can use the up and down arrow keys, by the way.
#
# But greeting is what we want. I'm going to press ENTER there. That saves us a bit of typing.
#
# So I can then add + single quote with a space in it , + I can put it in n for name, press ENTER,
#
# and if we run the program now,
#
# we can see the strings have been concatenated to produce the output.
#
# So to make this even more useful, we could use the input function to read in a name from the keyboard.
#
# So let's go ahead and do that.
#
# So where we've got name defined on line 7, let's change that to be name equals,
#
# and we'll delete the text Bruce in double quotes
#
# and instead we'll make an input parenthesis double quotes, Please enter your name, and a space.
#
# Then our closing double quote and right parenthesis.
#
# The input function displays the text provided to it, then waits for text to be entered at the keyboard.
#
# So I'm going to right click and run the program.
#
# Now when you run the program, click into the run window with the mouse,
#
# or you can use alt 4 on a PC before typing your name.
#
# So I'm going to come into here and I'm just going to double click it.
#
# I'm going to type Tim with a capital T.
#
# When you press Enter, the text you typed is stored in the variable name.
#
# This is the code on line 7 and then used by the print function to show the greeting.
#
# So if we press ENTER, we can now see the output, Hello Tim.
#
# So that's pretty cool. Our programs can get input from the user. To do that we call the input function,
#
# and then assign the value it returns to a variable.
#
# I mentioned function return values, in the slide at the end of the last video,
#
# so here the return value of the input function, is whatever text the user enters.
#
# So we assign that to the variable, name on line 7.
#
# Assignment is done using the equals symbol, and anything on the right of the equals symbol is evaluated first,
#
# before the assignment happens.
#
# So looking at line 7, that means the input function is called first.
#
# When it finishes, which happens when the user presses enter,
#
# the value it returns is assigned to our variable name.
#
# So let's actually come in here and type in print below the input line, print greeting,
#
# I probably should have done this before, greeting + name,
#
# because I've added the space down here on line 11, but I didn't do it on line 8 to show you what it's like without
#
# the space. So let's run that again.
#
# Click into the run window, Tim, and you see HelloTim without the space, and also Hello Tim with the space.
#
# So as you can see now, on lines 8 and 11,
#
# the value of name is printed out.
#
# Name isn't enclosed in speech marks, and again that's because it's not a string literal.
#
# It's the name of a variable, and Python uses the value whenever it sees the name, name in our case, in our code.
#
# We'll talk about variables more, in a video after the next one.
#
# First though, I want to finish discussing strings by looking at the escape character,
#
# and we'll be doing that in the next video.


print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
name = "Bruce"

# if we want a space, we can add that too

print(greeting + ' ' + name)

name = input(" Please enter your name ")

print(greeting + ' ' + name)