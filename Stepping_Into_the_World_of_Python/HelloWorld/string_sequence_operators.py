########### String Operators ##############

# In this video, we'll look at three operators that apply to strings. In fact,
#
# they apply to any sequence type.
#
# Alright, so back to the code. I'm going to create a new Python
#
# file called sequence operators.
#
# So we've already seen the plus operator used for
#
# strings to concatenate them. So let's just type in a few strings, so I'm gonna start
#
# with typing string1 equals "he's ", with a single quote there, but the
#
# string in double quotes, string2 equals "probably ", in double quotes, with a space
#
# after the y, string3 equals "pining ", with a space at the end of the letter g,
#
# string4 is equal to "for the " space, and double quote there, and then string5 equals double
#
# quotes "fjords", and then I'm going to print on line 7, string1 + string 2 + string3,
#
# whoops I put a space there, string3 + string4 + string5.
#
# But the plus isn't necessary when concatenating string literals, though, in Python,
#
# so we could also do print, so on line 9, double quotes he's space, then another space outside the
#
# double quotes, probably, space there, another closing off double quote,
#
# another set of double quotes but after a space there to separate it, pining space,
#
# whoops, space outside of the double quote
#
# for the and space space and Fjord's, not sure if I pronounced that correctly.
#
# Alright,
#
# so that'll print the same thing and if we run this, we should see both
#
# outputting the identical output, and obviously I made a typo.
#
# Run it again
#
# and we've got the identical output in both cases. So I mentioned this second way,
#
# because it's how Python works, not because we think you'd ever want to do
#
# something like that. I'm sure you'd agree that the first
#
# example on line 7 is a bit easier to read. Now with that said, strings can also
#
# be multiplied, which is a bit weird if you're coming from another programming language.
#
# I can come down on line 11, I can type print parentheses Hello in double
#
# quotes with a space before the closing double quote.Then I'm going to put * 5.
#
# Now you can't actually perform arithmetic multiplication on strings, of course.
#
# Instead what happens is, the star or multiplication operator repeats the
#
# sequence a certain number of times; 5 in this case.
#
# So if we run the code
#
# you can see we've got the word Hello printed, or outputted, five times.
#
# Now lists and tuples can also be multiplied, as we'll see when we look
#
# at those sequence types later in the course.
#
# You can't concatenate or multiply a range though, and that's not a problem
#
# because you probably wouldn't want to do that anyway. Now once again, operator
#
# precedence applies, so if I type some other code here,
#
# if I type print parentheses double quotes Hello, space before the closing double quote,
#
# multiplied by 5 plus 4. So this example wouldn't print Hello nine times, and again, we're
#
# talking about operator precedence there. So if we run this program, we'll see that
#
# we'll get an error, and the reason we're getting an error is because Hello, in
#
# double quotes, x 5 evaluates to a string, and then there's an attempt to then add
#
# the numeric number 4 to it and it fails for that reason. So what we can do is, I'm
#
# going to show you two things here, and they actually do different things.
#
# So firstly, I'm going to change line 13 to put five + four in
#
# parentheses, but then also I can type on line 14, print parentheses double quotes
#
# Hello space again and multiplied by 5, plus and 4 in double quotes.
#
# Now because of the parentheses, line 13 evaluates 5 + 4 to get 9, so it should
#
# then repeat the string 9 times. Line 14 should repeat the string 5 times
#
# and then append the string 4 to it, so let's just run that and confirm that's how it
#
# works, and can see that works, as I mentioned. Alright, so there's also an
#
# operator to check if one string is a sub-string of another. To do that,
#
# we actually check if one thing is in another. So let's start by typing some code.
#
# On line 16 I'm going to type, today equals Friday, and that's in double quotes
#
# because it's a string.
#
# Okay, next I'm going to type print parentheses double quotes,
#
# day in today, and put a comment here for each, which
#
# should be True, print fri in today, and obviously the first part's in double
#
# quotes, as you can see there. That should also be True; third example, print
#
# parentheses and we'll put t h u r in today, which should obviously be False,
#
# and lastly we do a print parentheses parrot in double quotes in double quotes fjord.
#
# That should also be False,
#
# and I'll just clean up these a little bit.
#
# So here, the in operator evaluates to True if the first thing exists in the second,
#
# and false otherwise. We'll be using that a lot when we look at conditions and for loops,
#
# and you'll get plenty of practice using it and see loads of real examples.
#
# So I'm not going to discuss it any further now, but we'll just run that to confirm we're
#
# getting the results that we think we should. You can see we get True, True,
#
# False, False, which goes in line with the code from 17 to 20, and getting the expected values.
#
# Alright so let's end the video here
#
# and in the next one, we're going to look at the various ways we can format
#
# strings, and some of the string methods that allow us to manipulate them.


# Python 3 has 5 sequence types built in:

### The string type

##### The string type
##### list
##### tuple
##### range
##### byte and bytearray

string1 = "he's "
string2 = "probably"
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)

print("he's " "probably " "pining " "for the " "fjords")

print("Hello " * 5)

print("Hello " * (5 + 4))

print("Hello " * 5 + "4")

today = "friday"

print("day" in today)       # True
print("fri" in today)       # True
print("thur" in today)      # True
print("parrot" in "fjord")  # False

