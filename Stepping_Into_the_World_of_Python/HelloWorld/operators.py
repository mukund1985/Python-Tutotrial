##### NUMBERIC OPERATORS ####

# To look at some of the Python operators that we can use with numbers,
#
# We're going to continue with our Hello World project.
#
# So we want to create a new file here. We'll call this one operators.
#
# So what I'll do, is start by binding a couple of labels to two int values.
#
# Remember that you'll also hear that described as assigning the values to the variables,
#
# but that's not the best way of thinking about it in Python.
#
# So I'm going to type a = 12, and on the next line, b = 3.
#
# Whenever we use the name a, Python knows that it refers to the value 12.
#
# Similarly, b will refer to the value 3.
#
# So let's create some expressions to see the basic Python arithmetic operators.
#
# So I'll start on line 4, print parentheses, and then within the parentheses, a + b.
#
# Next line, print parentheses again, this time a - b,
#
# and what I'll do is, actually, go back up to the previous line.
#
# I'll do a tab and I'll just put the expected results there. So 15 would be the value of the first one,
#
# the next one, 9. Alright line 6, parentheses after the keyword print, a * b, and the value for that should be 36.
#
# Next line, print parentheses and then a / b,
#
# and that should give us the value 4.0.
#
# Next line, print, then in parentheses a integer division, which is two forward slashes with b,
#
# and that should give us the value of 4, and again it's integer division,
#
# and it's rounded down towards minus infinity.
#
# And the last line we'll do a, be consistent here with the formatting, a percent b, which is the remainder operator.
#
# and that's going to 0 modulo and it's the remainder
#
# after integer division.
#
# Alright, I'll just fix this line up as well, just so it's consistently spaced.
#
# Alright and there we have it.
#
# So probably, there shouldn't be any real surprises here,
#
# except possibly the use of an asterisk for multiplication, if you're new to programming languages.
#
# x is a valid name for a variable, which means we have to use the asterisk for multiplication.
#
# So just run the program first, to make sure we get the expected results,
#
# and you saw me add those as comments, in the, or for, each line. So we'll run it,
#
# and there's our results, as you can see, exactly as we've got written in the comments.
#
# Note though that although we're using int values,
#
# division produces a float result, 4.0, which you can see in the source code on line 7.
#
# Now if we use two forward slashes to perform integer division, then the result is an integer.
#
# You saw that on line 8 and we got the expected result 4, in this case.
#
# So that can be important if we intend to use that value in a place where an int must be used.
#
# So to give the example, I'm going to add some code to print a blank line, then the numbers 1 to 3.
#
# Now don't worry too much about understanding this next bit of code.
#
# I'll use one here to illustrate the point, but we're going to be discussing for loops in detail,
#
# in the next section in this course. For now, just make sure that you put 4 spaces before the word print,
#
# and a colon at the end of the for line, and you'll see what that means when I start typing now.
#
# Alright, so here I am now on line 11. I'm going to add print, and an empty parenthesis to print an empty line,
#
# or blank line, and then next I'm going to type for on line 13, for i in range, and parenthesis, 1, 4
#
# in the parenthesis, and then colon immediately after that.
#
# Now if I just press Enter, you can see that IntelliJ has tabbed that for us, but if that's not happened
#
# for you automatically,
#
# you'll need to put those four spaces in, as I mentioned.
#
# So print and parentheses, the letter i, and if I run this, you can see we get the results 1 to 3.
#
# Now the values we used in range, and I'll just close down the run window now,
#
# there on line 13, must be integers.
#
# So if I change this to use a / b, come down here, so instead of 4, changing that to a / b,
#
# we get an error there, or we will get an error when we run it.
#
# As you can see, we've got a type error there: float object cannot be interpreted as an int
#
# So performing integer division, using two forward slashes instead of one, would actually prevent this problem,
#
# and you can see we get the numbers 1 2 3 and the warning has now disappeared.
#
# So essentially, we change the code to perform integer division and the result of a // b, two foreward slash b,
#
# is now an int.
#
# We'll see another way to cope with situations like this, but for now it's something you need to be aware of.
#
# Python is strongly typed, and you can't use a float in places where an int must be used.
#
# Alright, so code like a + b, as I've done up here on line 4, is called an expression.

a = 12
b = 3

print(a+b)  # 15
print(a-b)  # 9
print(a*b)  # 36
print(a/b)  # 4.0
print(a//b)  # 4 integer division, rounded down towards minus infinity
print(a%b)  # 0 module: the remainder after integer deivison

print()

for i in range(1, 4):
    print(i)

for i in range(1, a / b):
    print(i)


for i in range(1, a // b):
    print(i)