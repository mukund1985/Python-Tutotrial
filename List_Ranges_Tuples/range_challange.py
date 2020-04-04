# Experiment with different ranges and slices to get a feel for how they work
# Remember that you can print the range as well as iterating through it to print
# its values, to check that your ranges what you expected.
# You may also want to include things like.

o = range(0,100,4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)

# and see if you can work out what will be printed before running the program
# for loop to print out the values of o to see why p returns what it does.