# PRINTING IN PYTHON

print('Hello, World!')

# Although it's very simple, our Hello World program does include a few important basics
#
# Firstly, we've used the Python function print, Python has many functions,
#
# such as mathematical functions like round, to round the number of digits after the decimal point
#
# and char, chr and ord, to convert characters to their numeric representations and vice-versa,
#
# as well as many more.
#
# You can also define your own functions, as we'll see later.
#
# So at the moment we've got a very simple program, that just prints out the text Hello World!
#
# There's a few important things to know about the code, and I've already mentioned that print is a function.
#
# When you call a function in Python, you provide the things you want to print inside parentheses.

# So we've provided a string literal, Hello World!, and that's what got printed.
#
# A string literal is a sequence of characters,
#
# anything you can type on the keyboard, basically, enclosed in quotes.
#
# You can use either a single quote or double quotes to enclose a string.
#
# I used single quotes but you could use double quotes if you wanted to.
#
# It's important, though, to use the same ones, though.
#
# So if you start a string with double quotes, then it has to be terminated with a double quote.
#
# The string literal "Hello World!" is called an argument,
#
# at least in the context of what we're doing here.
#
# We're passing the argument to the print function.
#
# Functions can take more than one argument,
#
# and we'll be looking at how to define those when we write our own functions, later.
#
# So we're passing a string argument to the print function, but we could also print,
#
# for example, the result of calculations.


print(1 + 2)
print(7 * 6)
print()
print("The End")
print("The End", "or is it?", "keep watching to learn more about python", 3)

# When calling a function, you must have parentheses after the function name,
#
# Functions often take a specific number of arguments, but it's also possible to write functions that can take a
#
# variable number of arguments.
#
# The print function that's built into Python has been written that way.
#
# What that means is, we can print several things at once.
#
# So let's change the last line to print several strings and a number.  So a literal,
#
# well that's a value of some type. An example of a numeric literal are the numbers 1, 42 and 98.04,
#
# and an example of a string literal
#
# are "Hello World!", "Giudo van Rossum" and "Python", all in quotes, as you can see there.
#
# Moving on, a function, well that's a named block of code that we can call by using its name.
#
# We can write our own functions, or we can use functions that are built into Python,
#
# such as we've been doing here, with the print function.
#
# In Python, all functions return a value.
#
# Argument: a value passed to a function, in order to give it values to work with.
#
# Now there may be no arguments, or there may be one or more.
#
# Arguments appear in parentheses, after the function name.
#
# If there are no arguments, you still have to type in the left and right parentheses.
#
# Calling a function: using the function name to execute the function's code.
#
# When you call a function, you have to provide the arguments that the function expects.
#
# If it doesn't expect any arguments, don't put anything between the parentheses.
#
# Return value: well that's the value that a function returns.
#
# We haven't talked about that yet, but it belongs in this slide to make the slide complete.
#
# So more on that later, and parameter, also called a formal parameter.
#
# This is something else we haven't discussed yet,
#
# and we'll learn about parameters when we start writing our own functions.
