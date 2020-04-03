# In the previous videos, we stored some strings in variables, without really explaining what was going on.
#
# So let's have another look at strings.py. I'll open that up.
#
# We created that of course, if you recall, in an earlier video.
#
# If you want to download these slides.
#
# In fact the entire slides for the course, go to the very last video this one here in the course.
#
# Right down the bottom there, and watch that video? It's only a short one, and it gives the details of how
#
# to go about downloading, these slides. And it also has got access to, or gives you access to a document with
#
# lots of other information career advice, and so on and so forth. So watch that bonus video to download the slides.
#
# So in this code, strings.py, we've got a string with the value Hello.
#
# That's on line 6 as you can see.
#
# We've attached the name greeting to it.
#
# Whenever we use the name greeting in our code,
#
# Python knows that we're referring to the string, Hello.
#
# On line 7, we use the input function to get some text from the user.
#
# Whatever they type in will be stored in memory, and we attach the name, name, to it.
#
# And you can see there on lines 8 and also on lines 11,
#
# we use those variables to print out the strings.
#
# The Python documentation uses the word bound instead of attached.
#
# It would say that the variable greeting is bound to the string Hello
#
# So what we can do is create another variable called age and bind, or attach it, to the value 24,
#
# and then print it out. So let's have a go at doing that.
#
# I'm gonna come down on line 14 and type age equals 24
#
# And the next line, print parentheses age.
#
# Alright, I don't want to have to keep typing my name in every time we run this program,
#
# so I'm going to go ahead and change line 7 here.
#
# I'm just going to change the input just to a double quote, or set of double quotes and the word Tim.
#
# Alright. So if we run this now, I need to right-click because we're now using strings instead of escapechar,py.
#
# There's no surprises when we run the program. We get the two greetings printed, followed now by the value 24.
#
# In the introduction to Python video, I said that Python is a dynamically typed language,
#
# and also a strongly typed language.
#
# This is a good time to see what that means. So I'll start by explaining what we mean by type.
#
# There are a number of data types built into Python. We've already seen the string and integer types.
#
# Greeting is a string type, and age is an int.
#
# But you don't have to take my word for that. We can ask Python what type it thinks they are.
#
# I'm going to go ahead and type some code for that.
#
# So we'll come down here on line 17, I'm going to type print parentheses type parentheses greeting,
#
# And the two closing parentheses, right parenthesis.
#
# Then line 18, print, same thing there but this time with age, so type parentheses and age,
#
# and the two closing right parenthesis.
#
# So if you run this code now,
#
# and you can see that Python reports that greeting is an object of type string, str, while age is an object of type int.
#
# And it's using the term class there, but we'll talk more about class a little bit later.
#
# But these abbreviations, str and int, are Python abbreviations for string and integer, respectively.
#
# Python's got other types built-in as well.
#
# The float type, for example, that lets you work with numbers that have a decimal part.
#
# We can also create our own types, and we'll be doing that later
#
# So type, which is also called data type, describes the kind of information that we're storing.
#
# It's so usual to talk about a variable being of a certain type,
#
# but it can be more useful to think of values having a type, rather than variables.
#
# When we use the value 24 in our code, Python stores that value somewhere.
#
# The type of the value is int, it's an integer value.
#
# We bound the name age to it, which makes age have the type int.
#
# In Python, you can rebind a name to a different value.
#
# So, for example, we can come down here, and on line 20, I can type age equals, and double quotes, 2 years.
#
# So that stores now, the string value 2 years in memory, and binds the label age to it.
#
# That wouldn't be possible in many other languages.
#
# Once a variable has a type, you can only assign values of that type to it.
#
# Java and C are examples of languages that behave in that fashion.
#
# And that's why I said it can be more useful to think of the value as having the type, than the variable in Python.
#
# Here, age is now bound to a string value. It's no longer an int, it's a string, so let's confirm that.
#
# I'm going to print it out, and then print its type out.
#
# So I'll start on line 21, typing print parentheses age,
#
# on line 22, print parentheses type parentheses age.
#
# And we'll run the code.
#
# Alright, and as you can see, we've now got 2 years and class string showing for our variable age.
#
# So line 20
#
# looks like we're assigning the string value two years to a variable called age,
#
# and that would be true in other languages such as C and Java.
#
# In Python though, it's more helpful to say that we've rebound the label age to the string value 2 years.
#
# So I'll finish by saying that programmers have been talking about assigning values to variables
#
# for, now, over 60 years.
#
# It's become the way we speak and you'll find Python programmers talking in that way.
#
# And you'll probably notice me do it too, in these videos.
#
# It's not wrong, but some things will make more sense if think about a variable as a name or label,
#
# that's bound to a value.

greeting = "Hello"
name = "Bruce"

# if we want a space, we can add that too

print(greeting + ' ' + name)

name = "Mukund"

print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age = "2 years"
print(age)
print(type(age))

########### PYTHON IS STRONGLY TYPED LANGUAGE #################


# So the last bit of code that we wrote at the end of the previous video
#
# may well horrify Java and C programmers. So let's just go down look at that code again.
#
# I'll start by reviewing it, so make sure you've opened Hello World project in your IDE if you haven't got it open,
#
# and you've got the strings.py open.
#
# So firstly, on line 14, we've attached the variable age to an int value 24.
#
# Further on, down on line 20, we've reattached that same label to a string value, "2 years".
#
# Age, at that point, is now bound to the string "2 years".
#
# So Java and C programmers might jump to the conclusion that Python is a weakly typed language,
#
# and doesn't care what type things are.
#
# And that's a natural assumption, if you think in terms of assigning a value to a variable.
#
# Looking at it that way, it looks like we've assigned a string value to an int variable.
#
# Age represents an int on line 14, but is given a string on line 20.
#
# If we think in terms of binding a variable to a value, things make more sense
#
# On line 14, age is attached to an int value, 24 is an int and will always be an int.
#
# When we rebind the label age to a string value on line 20, we're saying that we no longer
#
# want that label to refer to an int. We now want to use it to refer to the string value, 2 years.
#
# Now re-using a variable name like that probably isn't a good idea.
#
# You can make your code confusing to read.
#
# What we probably should have done, is bind a more meaningful label to the string.
#
# So something like, we come back to line 20, age underscore in underscore words.
#
# That would now be more obvious as to what we're trying to do here.
#
# But just because Python allows you to re-use a variable name for a different purpose,
#
# that doesn't mean it's not strongly typed.
#
# As an example, let's see what happens if we try to add an int to the string.
#
# So I'm going to modify line 21 here, instead of just printing age, we're going to print,
#
# delete that and we'll put name + double quotes space is space and double quote, closing double quote + age
#
# + and double quotes again, space then years old.
#
# So we saw string concatenation on line 11.
#
# Python knows that greeting and name are bound to strings, and can happily concatenate
#
# the string values, to print out the full greeting.
#
# So I've just modified line 21 and now we're mixing string and int values.
#
# Will it work? Well let's run it to see.
#
# So you can see when we ran - I'll scroll up so we can see the errors -
#
# it prints two greetings and the value of age but then displays an error
#
# So the error you can see there is type error, and that's all happening on our code on line 21.
#
# Python helpfully shows the line number.
#
# You can scroll over and see there, line 21 in module.
#
# It also shows the bit of code that displays the error, as well as a description for what the actual error was.
#
# So a type error means that we've provided a value of one type, int in this case,
#
# when it's expected another type, a string.
#
# So different versions of Python produce slightly different descriptions for that error, by the way.
#
# I got the message: can only concatenate string, not int to string, as you can see on the screen there,
#
# but your version of Python may have said, can't convert int object to string implicitly.
#
# Python knows what to do if you use + with two strings. It concatenates them,
#
# or with two numbers, it calculates their sum.
#
# However, it's got no idea what you intend if you try to add a string and a number.
#
# Some languages, such as Java, will automatically convert the number to a string and concatenate,
#
# but Python doesn't do this, hence the type error.
#
# Automatic type conversion can be useful but it can also be a source of hard to find bugs
#
# and Python tries to prevent you from introducing errors in this way.
#
# Now later in the course, we'll look at handling errors but for now, think of errors as your friend.
#
# When python displays an error like the one above,
#
# it's telling you that your code won't work.
#
# It provides as much information as possible to help you work out why as well.
#
# Errors may be frustrating but you'll learn a lot from getting errors like this,
#
# and more importantly, working at how to fix them.
#
# An advantage of using an IDE like IntelliJ IDEA or PyCharm, rather than the IDLE IDE that ships with Python,
#
# are the hints that IntelliJ provides.
#
# So at the far right to line 21, and I'll just close this run window down,
#
# I hover over that. You see that little yellow dash that I hovered over,
#
# IntelliJ is now showing a tooltip saying, expected type string str but got int instead.
#
# This is a good indication that something is wrong, before you even run your program.
#
# So if your IDE provides warnings and errors like this,
#
# they're extremely useful if you check them out, when you make simple typing errors in long programs.
#
# Alright, so I'll stop the video here and in the next one, we'll look at Python's numeric data types.


age = 24

age_in_words = "2 years"
print(age_in_words)
print(type(age_in_words))


age_in_words = "2 years"
print(name + "is" + age + " years old")
