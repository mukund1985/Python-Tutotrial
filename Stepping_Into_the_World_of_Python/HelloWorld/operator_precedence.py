# It's something you'll have learnt about in basic maths class, and we're going to see how it applies
#
# to expressions in Python. Before I start that though, I'm going to delete lines 16 through 21 in our program.
#
# I added those just to show you what the for loop was doing,
#
# but I don't want to leave it as an example of how you should code,
#
# and in fact I'll take this opportunity to delete the for loop as well.
#
# Alright, so our examples so far have been very simple expressions,
#
# but they can be much more complicated.
#
# So consider the following line as I type it, and see if you can work out what will be printed,
#
# before you run the program. So I'm going to type, on line 13, print and in parentheses I'm going to type a + b
#
# divided by 3 minus 4 multiplied by 12. Then we've got our closing parenthesis.
#
# So if you can figure out what the answer will be, let's actually run the program and see what happens.
#
# You can see we've got the answer: -35.0.
#
# Now if you're surprised that the answer is -35.0 rather than 12,
#
# then maybe you weren't paying attention in school.
#
# Don't worry, your computer isn't broken
#
# and you can reliably perform arithmetic in Python, but like with all programming languages,
#
# you have to understand some basic rules of the arithmetic operators.
#
# Operator precedence is a fancy term for the relative importance given to each of the operators.
#
# If they were all equally important we could just read the expression on line 13 from left to right,
#
# and we would get the result 12: a is 12 + b which is 3, is 15, divided by 3 gives 5,
#
# minus 4 leaves 1 times 12 equals 12.
#
# However multiplication and division have higher precedence than addition and subtraction,
#
# so those operations will be performed first.
#
# Now many programming languages work in the same way.
#
# This isn't just a peculiarity of Python.
#
# So b divided by 3 is 1.0, and 4 times 12 is 48
#
# So the expression, therefore, is evaluated as 12 plus 1.0 take 48, which is -35.0.
#
# Now if you want to make your expressions clear and unambiguous, you can use parenthesis freely,
#
# even when Python doesn't specifically require them.
#
# So, along those lines, we could revise our example from line 13, and instead type
#
# print parentheses a + and another set of parentheses and b divided by 3 in those parentheses,
#
# then a minus, then parentheses 4 times 12. Then we've got our two closing right parentheses.
#
# I'll just space that out a little bit so it's a little bit easier to read.
#
# So if you run this code again, we get the identical answer -35.0 printed twice.
#
# So in other words, both these expressions evaluate to the same value.
#
# Now, if we had intended the earlier expression to reduce the result 12,
#
# we'd write it a different way.
#
# We could do print parentheses,
#
# and we're going to add another three parentheses here, so we've got four in total to the left hand side.
#
# Then a + b, closing parenthesis, divided by 3, closing parenthesis,
#
# - 4 closing parenthesis, multiplied by 12, and there we've got our last closing parenthesis at the end of the line.
#
# And now if we run that, we correctly get the result of 12.0,
#
# or, we could revise that because dividing by 3 is higher precedence than subtracting 4.
#
# We can actually remove one set of parentheses.
#
# So what I could do is change that to print, and we want three left parenthesis this time,
#
# and it's going to be a + b, closing parenthesis, divided by 3 - 4,
#
# closing right parentheses, multiplied by 12, and the final closing parenthesis.
#
# If you run the program again now, we get the same answer, 12.0.
#
# Now we could also use variables to hold the intermediate values if we wanted to.
#
# So if I come down here to line 18, I could type c = a + b. On the next line,
#
# d = c / 3, and e = d - 4,
#
# and we can do a print, in parentheses, e multiplied by 12.
#
# Now if we run that we,
#
# we also get the value 12 outputted.
#
# So there will be times when it makes sense to break up an expression into smaller parts, as we've done here.
#
# I think in this example, though, the code's harder to read, and difficult to work out what's going on.
#
# Compare the two previous examples and see which one you think's easier to read.
#
# Okay, so I mentioned learning about operator precedence at school.
#
# Unfortunately, many schools use acronyms to help you remember the order of evaluation,
#
# but the acronyms are ambiguous.
#
# So common acronyms are;
#
# So multiplication and division have equal precedence, which is higher than addition and subtraction,
#
# and addition and subtraction have equal precedence.
#
# Because multiplication and division are equal, expressions using those operations are evaluated from left to right.
#
# So let's go ahead and on line 23, I'll do a print, left and right parentheses to give us a bit of space.
#
# Then on line 25 I'm going to type print parentheses
#
# and within the parentheses I'm going to top a divided by, then another set of parentheses, b multiplied by a,
#
# closing parenthesis and divided by b, closing parentheses.
#
# and if I run this program,
#
# we get the result 0.1111111111
#
# and that's 12 times 3 is 36, and 12 divided by 36 is 1/3 divided by 3 is 1/9.
#
# If you were taught using those acronyms, make sure you're interpreting them correctly.
#



a = 12
b = 3

print(a+b)  # 15
print(a-b)  # 9
print(a*b)  # 36
print(a/b)  # 4.0
print(a//b)  # 4 integer division, rounded down towards minus infinity
print(a%b)  # 0 module: the remainder after integer deivison

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

# Operator Precedence Acronyms

# PEMDAS: - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction