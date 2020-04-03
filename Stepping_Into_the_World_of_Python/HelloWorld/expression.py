############ Expression ##########


# In Python, an expression is anything that can be calculated to return a value.
#
# So on line 4, we've got the expression a + b.
#
# Python evaluates that expression and prints the value 15.
#
# On the next line, we've got a - b, and that evaluates to the value 9.
#
# So working down the code, a multiplied by b is also an expression, evaluating to 36.
#
# Now the next two are similar, a / b and a integer divide by b.
#
# Now they evaluate to 4, but the first one is a floating point value and the second is an int.
#
# And finally on line 9, we've got the expression a and its remainder operator b.
#
# Oh, I said finally there, but it's not actually the last expression in the code.
#
# There are two more expressions on lines 1 and 2,
#
# and it may not be obvious but, strictly speaking, 12 & 3 are also expressions.
#
# They evaluate to the values 12 and 3, respectively, but they're still, technically, expressions.
#
# That means you can use a literal value, anywhere that Python expects an expression.
#
# Now there's also four more expressions at the end of the program,
#
# but I'd only expect you to identify two of them, at the moment.
#
# So can you spot more expressions in the code, after line 9?
#
# Pause the video if you need to, and come back when you've found two more.
#
# Alright so welcome back, did you spot them?
#
# Well firstly, on line 13, we've got the literal value 1 inside the parentheses,
#
# and it evaluates, not surprisingly, to the value 1, but again, it's still an expression.
#
# Now also inside the parentheses, we've got a integer divide by b, and that's the two slashes.
#
# At the moment, that evaluates to 4 because a is currently 12 and b is 3.
#
# So these are the two expressions I expected you to find, but there are more.
#
# So still on line 13, the two expressions we've identified are part of another expression.
#
# So the code range parentheses, and then it's 1, a // by b.
#
# That evaluates to a range of numbers from 1 to 3.
#
# So python has to evaluate that, in order to work out what values to use in the loop.
#
# So it evaluates the expression 1 to get the value 1, and then a // b to get the value 4.
#
# Once it's done that, it has to evaluate range(1, 4).
#
# So that's another expression.
#
# We haven't covered for loops and ranges yet, which is why I wouldn't have expected you to find that expression,
#
# But there's also another one on line 14.
#
# The variable i has to be evaluated so that Python knows what to print.
#
# The first time around the loop, it evaluates to the value 1, next time around it's 2 and
#
# the last time around it evaluates to 3. But hang on a minute, if i on line 14 is an expression,
#
# what about a and b on line 4?
#
# Aren't they also an expression?
#
# Yes they are.
#
# Python evaluates a to get the value 12, and b to get the value 3.
#
# It then adds them, evaluating the expression 12 + 3, and the same thing happens on lines 5 through 9.
#
# So expressions can themselves, be made up of expressions.
#
# In total there were 26 expressions in this code.
#
# Now we'll look at more complex expressions in the next video,
#
# but I'll finish this one by talking about a and b on lines 1 and 2.
#
# They're not expressions.
#
# You can't have an expression on the left of an assignment.
#
# The expression on the right of the equals sign is evaluated,
#
# and the variable on the left is bound to the result.
#
# So a common way of saying that is to say, the value 12 is assigned to the variable a,
#
# but I want to get you used to the idea that we bind, or attach variables to values.
#
# The result is the same. Whenever we refer to a in the code, Python evaluates it as 12.
#
# Okay, so what about i on line 13.
#
# Well that's also not an expression.
#
# i is being bound to each of the values produced by range in turn.
#
# So if I write this code long handed instead of using a for loop,
#
# it should become more obvious. So I'll come down here and I'll start on line 16.
#
# So put i equals 1,
#
# and on line 17 I'm gonna do print parentheses i, then i equals 2,
#
# print i, i equals 3, print i.
#
# Alright, I'll just move that up a bit.
#
# So that does exactly the same thing, where that would take six lines of code instead of two,
#
# which I've got on lines 13 and 14.
#
# But when I run the program,
#
# we get the same three values printed out again.
#
# So if i on lines 16, and i'll just scroll us up so we can see it,
#
# so lines 16, 18 and 20. So if I on those lines isn't an expression,
#
# then it should be clear that it's not an expression on line 13 either.
#
# Alright, so you'll see why we don't have i = 4 later.


a = 12
b = 3

print(a+b)  # 15
print(a-b)  # 9
print(a*b)  # 36
print(a/b)  # 4.0
print(a//b)  # 4 integer division, rounded down towards minus infinity
print(a%b)  # 0 module: the remainder after integer deivison

print()

for i in range(1, a // b):
    print(i)

i = 1
print(i)
i = 2
print(i)
i = 3
print(i)