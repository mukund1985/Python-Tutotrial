####### Formated string f string

# Python 3.6 introduced another way of formatting values in a string.
#
# These are called f-strings or formatted string literals. Now at the moment I won't be
#
# using f-strings in the course. That's because there's no plans to back port
#
# them to earlier versions of Python 3. Python 3.4 is still very common,
#
# and f-strings won't work with that version, or earlier versions. But with that said,
#
# it is worth being familiar with them. So let's have a quick look. I'm going to use the
#
# strings.py file from an earlier video, so I'm going to select that,
#
# and we're going to work with this file. Now at the moment, we've got an error on the last line.
#
# I used that to demonstrate that you can't concatenate a string and an int.
#
# So let's firstly just check this by running it again, confirming we've still got the error.
#
# And you can see we've still got this type error "can only concatenate strings,
#
# not an int to string".
#
# So let's fix that using an f-string. So all we really need to do
#
# to fix that, is to put the letter f before is up here. Put an f before the
#
# double quote and that's literally all we need to do. So an f-string is defined
#
# by putting the letter f before the opening quotes. Now that we've done that,
#
# we can use a variable name, inside curly braces, in a similar way that we've used
#
# replacement fields. So what we can do is delete this extra double quote here,
#
# come up and put age there. We can put age in left and right curly braces, like so.
#
# We can remove the other double quote there, so we've got it all in the one string, now
#
# So as you can see, it looks very similar to a replacement field. It's a lot
#
# cleaner, because we don't have to use .format at the end anymore. So if we run
#
# the program, let's do that just to make sure that it works, and you can see we've no
#
# longer got an error. The output is showing Tim is 24 years old - and Tim
#
# wishes he was 24 years old. Alright, so all the formatting for replacement
#
# fields also works with f-strings. So, for example, I could do some formatting
#
# along these lines. So let's just type some code in. So on line 24 I'm going to type
#
# print parentheses f double quotes Pi is approximately,
#
# and then in left and right curly braces, noting that the right one's added for us
#
# automatically, I can type in an expression 22 / 7:12.50f, and then we've got
#
# our double quote and then our right parenthesis. Now clearly you can see that
#
# I've used an expression rather than a variable name there. So let's just try
#
# running that first, and you can see we've got the value showing.
#
# Now what we can also do is calculate 22 / 7 first, and then use a variable,
#
# so let's do that. So PI on line 25 is equal to 22 divided
#
# by 7. Line 23, we'll do a print parenthesis f double quotes Pi is approximately
#
# and left and right curly braces, and this time we'll use the variable, so pi:12.50f
#
# for formatting,
#
# and, sorry for precision, and then we'll run that again,
#
# and you can see we've got the identical output. So now that you
#
# understand replacement fields, you can change to using f-strings instead, if you
#
# want. But be aware that your code won't run on Python 3 versions, earlier than 3.6,
#
# if you do use them. In the next video, we'll finish this section with a quick
#
# look at yet another way to format strings.
name = "Mukund"
age = 24
age_in_words = "2 years"

# below code is giving error i.e. TypeError: can only concatenate str (not "int") to str

# print(name + " is " + age + " years old")

# Below is example of how to use the above code in f string
print(name + f" is {age} years old")

print(f"pi is approximately {22 / 7:12.50f}")

pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")


data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print( )