######## String Formatting

# So string replacement fields can also contain formatting, to display values
#
# with a specific number of decimal places, for example.
#
# So let's create a new Python file. I'm going to call it formatting,
#
# and I'm going to use a for loop to generate some output.
#
# We'll be looking at for loops in the next section, so don't worry about what's happening.
#
# Concentrate on the print lines that I'm going to type in this code, to see
#
# the effect of the formatting in the replacement fields. So we're going to
#
# start by printing the values from 1 to 12, with the values of their squares and cubes.
#
# So on line 1 I'm going to type for i in range(1, 13):
#
# and put a colon to the right of the right parenthesis. So on line 2 I'm
#
# going to press ENTER here. You need to make sure there's 4 spaces before print,
#
# which I'm about to type, on line 2. I'm going to type print parentheses,
#
# and in double quotes I'm going to type number, or the abbreviation No, period. Then I'm
#
# going to put replacement field 0, which is our left and right curly braces with a
#
# 0 in the middle, squared is, and replacement field 1, and cubed is, replacement field 2.
#
# Then I'm going to type dot format parentheses i, i. I'm going to use
#
# the exponent operator, which is 2 multiplication signs, 2 then i, exponent
#
# operator again, 3, which is to the power. It's basically raising one number
#
# to the power of another in Python.
#
# Alright so if we run this now,
#
# and you can see we've got the values of the number, the value squared, and the value
#
# cubed, for each of those numbers. And in case it's not obvious now, you can
#
# provide any expressions inside the format parentheses. They don't have to be
#
# variables or literal numbers. On line 2, we've got i exponent operator 2 to get
#
# the number squared, and i exponent operator 3 to get the number cubed.
#
# And the exponent operator, is how you can raise one
#
# number to the power of another in Python. So that's the power to operator as well.
#
# Alright so that works, but as you can see, the numbers aren't - or the
#
# values rather - aren't lined up. So we can fix that in the output, or we'll fix the
#
# output by applying some formatting. So firstly, I'm going to specify a field width
#
# for each of the replacement fields. So all the values for i are a maximum of
#
# two digits, because we're, obviously, only counting from 1 to 12 here. So we can use a
#
# field width of 2 for the first replacement field.
#
# I'm going to use a field width of 4 for the other two fields. So to actually
#
# specify width, we come back up to our line 2, and we add the width by putting a
#
# colon and then the number that we need. So for the first replacement field
#
# zero, I'm going to put :2 there, for a width of 2, and for the other two
#
# replacement fields I'm going to put :4 and :4 again. So if we run the program now,
#
# it's now easier to understand, because the formatting makes it easier to see at a
#
# glance, what the values are. Alright so that looks tidier. The values are now
#
# lining up nicely. So on line 2, we're using 0:2 in
#
# our left and right curly braces for the first replacement field.
#
# 2 is the field width, as I mentioned, and it's separated from the index with a colon.
#
# Now everything in that first column prints in a width of two
#
# characters. So think of it as reserving two spaces on the screen,
#
# so that the one digit values still line up with the two digit ones, and you can see
#
# they're happening there in the output. Now our squares also line up, in a field
#
# width of four characters. Maybe a width of three would look better there; have
#
# a got at changing that yourself, and see what it looks like. Pause the video
#
# and I'll make the change when you come back.
#
# Okay, so if we only want to use three spaces for the square values, the change is
#
# obviously easy enough. We come back up to replacement field 1, change the 4 to
#
# a 3, and if we run it again, well that looks tidier still now, as
#
# you can see. There's now only one space between is and the value on the last
#
# three rows. We can also align the values in their field width. To left align the
#
# values we place a < symbol after the colon. So what I'm going to do is,
#
# just to make this easier to see, I'm going to firstly add a blank line. Then I'm
#
# going to take a copy of the line - of the two lines there. We'll just run it again
#
# so the original code's there as well. So I'm going to paste that in as it was before.
#
# So this time what I'm going to do, again we're trying to left align the values,
#
# so we'll leave replacement field 0 as it is, the first one. For the second one
#
# we're going to put, before the three, I'm going to put the less than sign there,
#
# and for replacement field 2, we're going to put a less than there as well.
#
# So if we run this,
#
# and the values are now left aligned, and if it's not immediately
#
# clear to you what's going on there, scroll up the output to compare the
#
# two blocks. But if we have a look at the formatting here, notice how it's now left
#
# aligned. If we go back up to the top, you can see clearly that was right aligned.
#
# So the alignment symbols are quite visual. The less than, left aligns,
#
# the greater than will right align, and a caret symbol, well that centers within the
#
# field width. So let's center the last column to see what that looks like.
#
# So instead of using the less than there, I'm going to change that by using the caret
#
# symbol instead. And if you run this code again,
#
# you can see the values are now clearly centered, compared to the first output,
#
# which was right justified on the right hand side
#
# and this is obviously for the cubed values.
#
# Now keep in mind that we don't get half spacing in a terminal, so the result
#
# isn't as accurate as centering values in a GUI program, but it's available if you want it.
#
# So for floating-point numbers you can specify a precision - the number
#
# of digits after the decimal point. For our precision, we specify the precision
#
# after a decimal point, following the width.
#
# So let's have a go at doing that, so I'm going to type some more code in.
#
# So I'm going to put an empty line in there,
#
# and the line after, well actually line 11, I'm going to type print
#
# parentheses Pi is approximately,
#
# we're going to put replacement field 0:12,
#
# which is the precision for a floating-point number, then dot format
#
# parentheses 22 divided by 7, and 2 right parentheses to close it off. And let's take a copy of
#
# that line, we're going to make some modifications. So I need another 5 lines.
#
# I'm going to paste that 5 times.
#
# Alright, so on line 12 what we're going to do, is we're going to put an f after the 12.
#
# Next line, we going to put 12.50f, line 14 we're going to put 0:52.50f,
#
# and the next, I'm going to put 62.50f, and the last line, I'm going to put 72.50f.
#
# So the first line of output, well actually, I'll run it first and then we'll talk about it.
#
# So the first line of output, and that's produced from the code on line 12.
#
# I'm going to see if I can get that on the screen at the same time, on line 11 rather,
#
# well that's the general format, and that defaults to printing 15 decimals.
#
# When we specify a floating-point value using the f on line 12,
#
# we get the default of 6 digits after the decimal point.
#
# Now on lines 13 through 16, we're still specifying a floating-point format,
#
# but we also add a precision of 50 and that gives 50 points after the decimal point.
#
# The third line of output corresponds to line 13. If you think it doesn't look
#
# right that's because Python won't truncate a number. We can't put a value
#
# that's got 50 decimals in a field width of 12. Python decides that precision is
#
# more important than field width, and ignores the value 12 that we've
#
# specified for the width, and that's the code on line 13.
#
# Now the next three lines after that, print the same value but in different
#
# field widths. When we specify width greater than 50, you can see that the
#
# effect becomes clear. Now the maximum precision of a Python floating-point
#
# number is between 51 and 53 digits. There's not much point specifying a
#
# precision greater than that. Now this will be easier to see if I left align,
#
# that last line, so I'm going to do that, and then copy it and increase the
#
# precision just to show you what I mean. I'm going do that, copy that last line 16.
#
# I'm going to change the 72.50f to 72.54f, but we're also going to use the
#
# left align, so you can see the value left aligned, and we'll put that
#
# to the left of the 72 after the colon. We run the program now,
#
# and what I should do is,
#
# actually, left align the previous line as well just so you can see the differences.
#
# So we'll do that again as well on line 16, we'll run that again,
#
# and you can see we only get one extra digit in the output. We can see that there's
#
# four digits here but the remaining digits are just padded with zeros,
#
# so there's no actual value there. Alright so I'll finish this video now by
#
# mentioning that the field number in replacement fields is optional.
#
# If they're not specified, then Python takes the value from the format method in order.
#
# So to see what I mean, I'm gonna take a copy of the code again,
#
# this code up here on line six. I'll take a copy of that again.
#
# I'm gonna paste it down here on line 19,
#
# and I'm going to actually remove everything. So we're just going to put
#
# just a left and right curly brace only, for the three replacement fields,
#
# and actually, what I'll do on the third replacement field, I'll just put a
#
# colon 4 there, so we can see that we're still specifying a width.
#
# If we run this,
#
# we can see that the third field shows that you can still use a colon to control the layout,
#
# even if you haven't specified a field number. All the values in the final
#
# column of output are printing in a field with the 4. Now if you don't provide
#
# field numbers, you can't use a value more than once, nor can you change the order
#
# in which values are used. Now our earlier example, with the number of days in the month,
#
# wouldn't have actually worked without field numbers.
#
# Alright, so experiment with different values for the field widths and precision's,
#
# to see how it affects your output,

for i in range(1,13):
    print("No. {0} sqaured is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

print()

print("But the format is not good, so we need to add some field width with replacement field - {1:4} so the 4 is width")

print()

for i in range(1,13):
    print("No. {0:2} sqaured is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1,13):
    print("No. {0:2} sqaured is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))


print()

for i in range(1,13):
    print("No. {0:2} sqaured is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))


print()

print("Pi is approximately {0:12}".format(22 /7 ))
print("Pi is approximately {0:12f}".format(22 /7 ))
print("Pi is approximately {0:12.50f}".format(22 /7 ))
print("Pi is approximately {0:52.50f}".format(22 /7 ))
print("Pi is approximately {0:62.50f}".format(22 /7 ))
print("Pi is approximately {0:<72.50f}".format(22 /7 ))
print("Pi is approximately {0:<72.54f}".format(22 /7 ))

print()

for i in range(1,13):
    print("No. {} sqaured is {} and cubed is {:4}".format(i, i ** 2, i ** 3))