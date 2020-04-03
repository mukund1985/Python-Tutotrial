#### String Replacement


# When printing strings and numbers, it would often be convenient to display
#
# So let's swing over to the code and create a new file.
#
# I'm going to call this one repfields.
#
# Alright, so I'm going to start by typing age equals 24, then on line 2 we're going to do print parentheses
#
# double quotes, my age is, space double quote + str age in parentheses +
#
# double quotes space years, closing double quote and right parenthesis.
#
# So if we run the program, we confirm we get the output, my age is 24 years, and no longer
#
# getting an error now, when we're using the plus operator to concatenate numbers
#
# and strings. So using the string function helps us to, basically, coerce an integer
#
# into a string, but this can rapidly become tedious; having to coerce every
#
# variable using the string function. Python 3 provides a much better
#
# mechanism, and that has improved further in Python 3.6. So python 3 allows strings
#
# to be formatted using replacement fields and the dot format method. And these are
#
# probably best explained with a few examples. So let's change line 2,
#
# instead of using the string function, I'm going to put my age is, and I'm going
#
# to put left and right curly braces before the closing double quote,
#
# with a zero in between them.
#
# So my age is, space left and right curly braces,
#
# zero between that and a space years. I'm going to delete all the code up until the right
#
# parenthesis, and replace outside the double quote with dot format age in parentheses.
#
# So this will produce the same output as the previous example,
#
# but without having to coerce the number into a string. So let's just run this
#
# to confirm that it works. We get the same output; my age is 24 years.
#
# So the replacement field is represented by the left curly brace the 0 and the right
#
# curly brace, which is then replaced by the first value in the format list,
#
# age in this case. And at the moment we've only got the one value in there and
#
# that's the variable age. So that doesn't look like much of an improvement over
#
# the previous code, but consider this one instead; so I'm going to type it out.
#
# Line 4, I'm going to type print parentheses and double quotes, there are, and we'll add
#
# some replacement fields. So first one I'm going to do is a zero and get all of
#
# these in curly braces, There are zero days in, then a curly brace again, 1
#
# with curly braces comma, and we'll do the same for 2, 3, 4, 5, 6 and 7.
#
# 2, 3. 4, 5, and you can see I'm putting commas and putting curly
#
# braces around these numbers again, 6 and we'll finish off the last one.
#
# We'll put and, replacement field 7.
#
# So I'm going to do that, then press enter there.
#
# On the next line, type dot format, then another set of parentheses,
#
# and I'm going to type 31 comma in the left parenthesis, well after the left parenthesis
#
# Jan, March, or M a r, the abbreviations I'm going to use here,
#
# May, oops, I missed a double quote there.
#
# July, August, October, and the last one, December.
#
# Then a closing parentheses. So I've split that code over two lines, which is something
#
# you'll see done a lot in Python. Long lines are actually frowned upon in the
#
# Python style guide, which we'll talk more about later. For now, just know that
#
# Python allows you to split your lines of code like I've just done.
#
# Alright, so the replacement fields are replaced by the values that appear in the dot format
#
# method call, with the first value replacing 0, the second replacing 1 and
#
# so on. So you can see there, we've actually got a total of 7 replacement fields
#
# defined on line 4, and each of those values are going to go into the
#
# respective number, 0 through 7. So we've got a total of 8 items in the list after
#
# the dot format, and each of those will go into the replacement fields numbered 0
#
# through 7 in our string. So if we run the program now,
#
# and comparing the output at
#
# the bottom of the screen with the values that appear inside the parentheses
#
# after the dot format method call.
#
# Of course, you probably wouldn't use string literals
#
# inside format, because of course they can just be included in the string.
#
# So we could have, in this case, replaced what we did there, with something that's probably a
#
# lot more readable; print There are, replacement field 0 days in, in Jan,
#
# March, May, July, August, October and December and dot format.
#
# So that does exactly the same thing, but I just wanted to demonstrate that you can have multiple replacement fields
#
# inside a string, and we'll just run that to confirm, and I probably should have
#
# written it like that, and to be consistent, run it again and we've got the identical output.
#
# The other thing to keep in mind is that fields can be used more than once,
#
# and they don't have to appear in the order that the values are provided to the dot
#
# format method call. It's the field index, the number inside
#
# the curly braces, that determines which value to be used.
#
# So here's an example to demonstrate that.
#
# So I'm gonna come down here on line 8, print parentheses,
#
# I'm gonna start with a double quote Jan:
#
# I'm gonna start with replacement field 2, then Feb: 0 replacement field, Mar:
#
# I'm gonna use 2 again, Apr: with replacement field 1, May: 2, Jun: 1,
#
# replacement field 1, Jul: replacement field 2, Sep: 1 and Oct: 2,
#
# replacement field 2, two more, Nov: replacement field 1 comma Dec: replacement field 2.
#
# and obviously, I've got a large font here so we're not gonna be able to
#
# see the entire contents on that line, on this one line. So what I'm going to do is
#
# actually go to the end there, press enter there, dot format, and I'm going to put
#
# three values; 28, 30 and 31.
#
# So if we run the program, and you can see now that
#
# wherever there's a replacement field 0, it's replaced with the first value in
#
# the list, 28. We've only got replacement field 0 once for February,
#
# and all the replacement field 1 fields are replaced with the second value, which is 30,
#
# and the third value, 31, is used to replace all the replacement field 2 replacement fields.
#
# Now you can also use triple quotes. What I'll do is I'll print
#
# a blank line first, and close this run window down. We'll just print an empty line,
#
# and we can also do something similar using triple quotes. So I could do print
#
# parentheses three quotes, triple quotes in other words,
#
# press ENTER there. Then what I'm going to do is take a copy of this entire line,
#
# just save me typing it again. Okay, take a copy of that. I'm going to go back and
#
# paste it after the triple quotes. Then what I'm going to do is just press ENTER
#
# after each one to make it a bit more readable, and because I'm pressing enter
#
# on a separate line now, I'm also going to remove the double quotes,
#
# remove the comma rather. So we've got February, March.
#
# That's the end of the line now, so I'm going to add the three closing double quotes there,
#
# and I'm just going to put our format statement after that, dot format
#
# parenthesis 28, 30, 31, like so. So now if we run that,
#
# I'm looking at the output for this program. Each month is appearing on a new line and the
#
# number of days is also showing on there as well. So that, I'm sure we agree, would be very
#
# difficult, or would be very messy, to reproduce with string concatenation.
#
# So the actual replacement is pretty easy to work out.
#
# So replacement field zero is replaced with 28, and you can see the example there,
#
# showing us on line 14. So it's automatically coerced to be a string for us.
#
# Replacement field 1 is replaced by 30. We've defined that as the second entry
#
# in our format list there, and replacement field 2 is replaced by 31.
#
# You can see, obviously, the same use of the replacement fields in the code
#
# and we can see the output showing down the bottom of the screen. Now if we'd used
#
# replacement field 3 in the string, then we'd have to produce, or provide rather,
#
# another value in the dot format method call. Alright so make sure you understand

age = 24
print("My age is " + str(age) + " Years ")

print("My age is {0} years".format(age))


print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))

print()

print("Jan: {2}, Feb: {0}, March: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1}, "
      "Dec: {2}" .format(28,30,31))

print()

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}
""".format(28,30,31))

