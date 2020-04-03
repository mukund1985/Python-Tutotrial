####### Binary search algorithm implementation

# In the last video, we saw how a binary chop can be used, to reduce the number of
#
# guesses needed. In this video, we'll write the code to let the computer guess a number.
#
# The code will implement the algorithm
#
# that we discussed in the slides, in the last video. So an algorithm is a set of
#
# steps that are followed, to perform a task or calculate a result. So I'm going
#
# to start with a couple of variables for our low and high values. We need a new
#
# file for this, and we're going to call this new Python file hilo.
#
# We're gonna take the opportunity to close some of these other tabs. Alright, so the variables I'm
#
# starting with: low equals one and high equals 1000. So next we need some simple
#
# instructions and get the program to wait until we're ready. So on line 3, print
#
# parentheses double quotes Please think of a number between,
#
# and we need our left and right curly braces and another set of left and right curly braces,
#
# because obviously we're going to change that to the actual numbers, dot format outside of
#
# the double quotes, low comma high in parentheses and the closing parenthesis.
#
# Then we need to add a line to get started, so import parentheses double quotes,
#
# press ENTER to start. So on line 5, we're not interested in anything that
#
# the human types. We're just calling the input function so that the computer
#
# waits until the user presses the enter key to start the game.
#
# It will be useful to count the number of guesses. We know that the computer should
#
# be able to get the correct answer with ten guesses at most, and that's because
#
# we're having the range of numbers each time, and two to the power of 10 is 1,024.
#
# So that's slightly more than 1,000. In fact, the computer can guess any number
#
# from 1 to 1,023, within 10 guesses. But 1,023 is a strange number to
#
# show to the user. That's why we're sticking with 1,000. Alright so we need
#
# a variable now to store the number of guesses,
#
# so on line 7, I'll type guesses equals 1. Alright so we'll use a while loop to
#
# let the computer keep guessing until it gets the answer. After each guess the
#
# human will tell the computer whether to guess higher or lower, or if it got the
#
# answer right. We'll keep looping until the answer is correct and break out of
#
# the loop when it is. So I'm going to do a while True colon, then on line 9,
#
# guess equals low plus, and in parentheses, high take low, integer division so two slashes there, 2.
#
# So we're dividing by 2 there and making sure that we're using integer
#
# division. Now I mentioned while True in an earlier video. True is always true,
#
# which means this loop will go round forever.
#
# Sometimes it's easier to do that then break out of the loop at some point,
#
# rather than trying to include a condition in the while loop. So what we
#
# want, is for the loop to stop when the computer gets the right answer, but
#
# because the computer doesn't know the answer, we can't include a test here. So
#
# what I mean is, on line 8 here, we can't do something like wild guess is not
#
# equal to answer, because we don't actually know the value of answer. So I'm going to
#
# do that change and go back to what we had, while True, so that the program will
#
# keep looping. The line 9 is the formula that we saw in the slides in the
#
# previous video. It calculates the midpoint between the low and high values
#
# to produce the next guess. So what we'll do is we'll print the guess, then ask the
#
# user to type H if the computer should guess higher, L if the computer should guess
#
# slower or C if the guess was correct. And we can include the text that we want to
#
# print in the input prompt. So I'm going to come down here, line 10,
#
# high underscore low is equal to input parentheses double quotes My guess
#
# is and left and right curly braces. Full stop. Should I guess
#
# higher or lower? - should I type better as well. Should I guess higher or lower? Enter h
#
# or l, or c if my guess was correct, and then double quotes, and we can't really see
#
# now and I'm going to actually talk about having lines that are too long, in a minute.
#
# We're gonna keep typing for now and put dot format left parenthesis guess
#
# two right parentheses, then outside of that I'm going to do dot casefold. So again, as I
#
# pointed out there, that line is a bit long. So you can easily see here the
#
# problem that long lines can cause, because it's hard for me to show it all
#
# on the video. In fact, I can't show the entire line on the video right now.
#
# I don't want to digress here, but I will be talking about line length and other
#
# things about formatting a code in a later video. Remember this example and
#
# how inconvenient it is for you to type the code from my screen, when we come
#
# back to code style, noting that you can't see it all at once. For now, though, what I'm
#
# going to do is split this line. So I'm going to position the cursor before
#
# the E of enter. I'm going to type a double quote, then I'm going to press Enter.
#
# That gives an error, as you can see, but that's okay, just enter another double
#
# quote here and that then delimits the split-up string correctly. If I go back
#
# now, we can see the whole thing on the screen. The double quote should line up
#
# with the one on the line above but don't worry too much about that just yet. We'll
#
# leave it as it is for now. What we will do is position the cursor again before the
#
# dot of format, up here before the dot, press ENTER again. That's now split the
#
# line into three. Now rather than lining up manually, what you could do is go to
#
# the code menu and choose Reformat code. Most modern IDEs have a similar feature,
#
# and now the code is correctly formatted, as you can see. Alright so I think you'd
#
# agree now, that's easier to read. You can now see all the code on my screen and I
#
# don't have to scroll sideways as much to show it to you.
#
# Alright so moving on with this program, we've got four possibilities to deal
#
# with. The user could enter h for a high guess, so let's start with that.
#
# So I'll start that on line 14. If high underscore low is equal to
#
# h in lowercase : Remember we're using case fold on line 12,
#
# so we're guaranteed it's going to be in lowercase. And the comment here, we want
#
# to Guess higher. The low end of the range becomes 1 greater than the guess.
#
# Now I'm not going to add the code for guessing higher. Let's get all the
#
# conditions in place first. That'll let you see what the conditions are, but it
#
# will cause a problem. Because the error message is very confusing, I want to get
#
# the error and explain it. Right, so moving on now, the next condition to test is if
#
# the user enters l for lower. So we're going to go ahead and do that on line 17:
#
# elif high_low is equal to l : again in lower case, and a comment
#
# for that will be Guess lower. The high end of the range becomes 1 less than the guess.
#
# So we're getting errors here but we'll ignore them for the moment.
#
# Next the input would be c if the guess is correct, so let's move down on to that,
#
# line 20, elif high_low is equal to c in double quotes, lower case c :
#
# So what I'll do here is print out the answer here, no need to add a comment, so print
#
# parentheses double quotes I got it in, left and right curly braces
#
# guesses exclamation mark double quote dot format guesses. Alright we'll scroll up a
#
# little bit so we can see the other code. Alright so that's the three conditions
#
# that we expect, but humans often don't do what we expect, and we should also deal
#
# with anything else that they might type. We're gonna use an else block to do that.
#
# I'm gonna come down here, on line 23, else colon print parentheses Please enter h, l or c.
#
# So if they do anything else, we just remind
#
# them what the three options are. Alright, so I'm going to stop the video here and
#
# in the next one, we'll look at why we've got those errors.

# Alright so why are we getting these errors that showed up at the end of the
#
# last video? Well we've got errors because you must have valid code inside each of
#
# the code blocks. A comment doesn't count. Notice that there's a red tick in the
#
# right margin next to lines 15 and 18, and I can select them up here, and also there's this
#
# red squiggle under each comment on line 15 and 18. Now this can be confusing
#
# when you're starting but it's the syntax rules of Python.
#
# You must have code inside a code block. If there's no code, and that includes
#
# just having a comment, then you'll get an error like this. So notice that there
#
# isn't an error on line 21 or line 24. There is code inside those two blocks,
#
# so we don't get that error. If getting an error wasn't confusing enough though, the
#
# error message makes it even worse. And if I hover over one of them again, you can see the
#
# error we're getting there is: indent expected. But of course, looking at that
#
# you can see those comments are already indented - they're obviously indented.
#
# So we can see that on the screen. You may not see an error if you're using a
#
# different IDE, but you will get it when you try to run your code. So things like
#
# this can have you tearing your hair out. Fortunately, there are very few times
#
# when something like this happens, and now that I've pointed it out, you'll remember
#
# it and avoid tearing your hair out. What you'll often find programmers doing,
#
# is adding a dummy bit of code inside the indented block, to clear this error.
#
# So there's a specific keyword in Python for that and that's called pass. So I'm going to
#
# come up here to line 16, tab over and type pass. So come down to line 19,
#
# tab over and type pass again. Now pass doesn't do anything, but it makes the
#
# code syntactically correct. So think of it as a placeholder for the real code
#
# that you'll add later, and you can see that that's fixed the errors and we've
#
# now got the basic structure of our code. Alright so it's time to work out what
#
# we really want to do in place of those pass statements. If the computer had to
#
# guess higher, well then we alter the low value of the range and go around the
#
# loop again. So let's do that. So I'm going to replace that pass on line 16 with low
#
# equals guess plus 1, which is in line with the comment that I've
#
# added on line 15. Now similarly, if we have to guess lower, then the new high value is
#
# one less than the current guess. So come out to line 19, replace the pass,
#
# and it's going to be high equals guess minus 1. Alright so the last step now
#
# in our algorithm, is to break out of the loop when the guess is correct. So we're
#
# going to come down here. Then on line 22, we're going to add the keyword break
#
# so that we do just that. We break out of the while loop if the computer has
#
# successfully guessed it. If you've programmed in other languages, you might
#
# be wondering if we could use a case or switch there. Don't bother searching for
#
# how to do that in Python. Python doesn't have a case or switch statement. If you
#
# haven't programmed before, that won't mean much to you, don't worry about it.
#
# They don't exist in Python. Alright, so that's our algorithm implemented with
#
# Python code. So we're doing a bit more. We're also counting the number of
#
# guesses. So that means therefore we should increase the count before the
#
# loop goes around again. So we need to come down and add that code, and we
#
# both need to add it at the same level as the if, and I'm gonna
#
# put it down here on line 27. Actually, what I'll do is I'll come down here and I'll
#
# just, to be consistent with our code, we're going to take that up one line,
#
# and over here, on line 26 now, I'm going to type guess, or guesses rather, equals
#
# guesses plus 1. So be careful with the indentation there. That line must be
#
# indented one level, as I have it there, so that it's inside the while loop but not
#
# inside the else block. So for now, we're going to ignore this suggestion from IntelliJ.
#
# I'm going to talk about that in the next video, but at this point we've now
#
# finished, our program is finished. Check your code carefully and then in the next

low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1

while True:
    print("Guessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should i guess higher or lower? "
                     "Enter h or l, or c if my guess was correct "
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1

    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess.
        high = guess - 1

    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break

    else:
        print("Please enter h,l or c")

    guesses = guesses + 1

























