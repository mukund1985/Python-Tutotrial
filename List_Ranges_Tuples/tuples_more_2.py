# So continuing on with our discussion about tuples in Python, so we just talked about
#
# this line here in line 15 and how that concept is called unpacking the tuple.
#
# It actually mentioned I'm gonna leave the list item here on line 12,
#
# just to show you how a tuple can be much better than listing situation.
#
# So again if we run the program, making sure we've selected tuples or
#
# whatever name you've called your path and fall.
#
# Click on run. You can actually see how it's unpacked
#
# the top, so in other words with that one line of code on line 15 you've
#
# extracted the contents out of the tuple into three individual variables, title,
#
# artist and year.
#
# So you can see that that makes it very convenient when dealing with
#
# the individual items of tuple by signing them to meaningful named variables.
#
# I'm just cleaning up this a little bit so I'm going to delete that.
#
# So we can actually do something similar or actually the same with the list.
#
# So you can change this.
#
# So we could come along here and we could change this code on line ten and
#
# we could do something like teleca two dot pinned rock.
#
# Like so. I'm going to give it title, artist,
#
# year, equals Metallica 2.
#
# And if we actually run that, we actually get an error.
#
# And this is an example of why you wouldn't want to use a list in this situation where
#
# the code you're working on, or the data you're working on, isn't to be changed.
#
# So it's not immutable.
#
# So a list, you can see, isn't immutable.
#
# We're able to actually append an item to that.
#
# And, of course, when we went to run the code on line 12, we actually failed
#
# because it was too many values to unpack, because we didn't assign enough variables.
#
# To unpack the data out of the list.
#
# So remember that you might be creating code modules.
#
# That will be used in different parts of a program.
#
# And possibly and even probably if you start working professionally.
#
# As a path-end developer by other programmers.
#
# And if you allow such things to be done then frankly.
#
# It's only a matter of time before they will be done.
#
# That's just the nature of programming.
#
# Now because a tuple is immutable in other words it can't be changed
#
# In this case line ten couldn't be executed cuz a tuple doesn't have an append method.
#
# So, this makes your code much more robust to make it a tuple in this scenario and
#
# prevents errors that would actually not appear until someone else was
#
# using the program.
#
# So for example if we try and do something like imelda.append
#
# note that there's no intelligent, IntelliSense, nothing happened.
#
# Try and do that and run it.
#
# I think if I just comment out that line for now.
#
# The point is if we actually run this now, we actually get an error, tuple object has
#
# no attribute append, because of course we can only use the .append with a list item.
#
# Now the other thing to note is that tuple can contain elements that
#
# are themselves tuples.
#
# So let's actually go ahead and
#
# add a track list to the tuple representing the Albert Moore Mayhem.
#
# We're just gonna use the first four songs to save some typing.
#
# So we're gonna clear out the Metallica code because we don't need that anymore.
#
# I'm just going to get rid of all that right now.
#
# And let's actually change this mail order, and
#
# I'm just going to close the running data.
#
# And after date, the year that the album was released,
#
# then I'm going to put a comma, then put a bracket, and
#
# I'm going to type in another bracket, because I'm creating a tuple.
#
# And we're going to create the individual items.
#
# So it's one, in the tracks,
#
# "Pulling the rug" 2, "Psycho".
#
# 3, "Mayhem".
#
# And 4, "Kentish Town Waltz.
#
# I can just do that and get rid of that last bracket there.
#
# So it's another line here, print(imelda).
#
# We're gonna do in this case, we're gonna do title, artist, year, but
#
# also tracks now, the fourth variable, equals imelda.
#
# So we're unpacking the top lagoon.
#
# And of course we're gonna print title, print artist,
#
# print year, print tracks.
#
# So if you run that.
#
# You can see we've correctly now got the information out.
#
# We've got the three fields as before, title, artist and year.
#
# But notice how the fourth entry, tracks,
#
# has been returned as a tuple in its own right.
#
# Now the important thing to note here in this situation,
#
# when adding these extra tuples,
#
# was that it was important to actually enclose the four individual songs.
#
# The track number and the actual song in parentheses.
#
# Otherwise what would happen would be the Python interpreter
#
# would actually evaluate that as a single tuple with eight elements.
#
# In other words, track 1, song 1, track 2, song 2.
#
# So by putting an extra set of parentheses around each,
#
# we're actually making it clear that these are individual tuples in their own right.
#
# So just to show you what I actually mean there I can actually change that.
#
# So I could get rid of these extra brackets, and close this down.
#
# So I get rid of all these brackets.
#
# Just leaving the last bracket in there.
#
# If I actually run that.
#
# You can see, now, we've got single tuple with eight entries.
#
# The four individual track numbers, and the four songs.
#
# And obviously, in that case, we've actually lost a lot of the structure.
#
# Because instead of the tracks obviously having a track number.
#
# With title we've just got eight values, and there's no obvious relationship.
#
# At least not obvious to the computer, anyway.
#
# So we just undo that, and do that again, put the brackets back again.
#
# So we've got individual tuples again.
#
# And it's also possible to extract the individual tracks as well.
#
# So at the moment we got title, artist, year, we've got tracks.
#
# But let's change tracks to track1, track2, track3, and track4.
#
# And now we have to print those out individually, so track1, 2, 3, 4.
#
# So, we can actually run that.
#
# And what I was going to do then, I'll just close that down.
#
# What I was gonna go is get rid of this initial bracket, so
#
# I'm actually just creating four separate tuples effectively here.
#
# If I actually run that, that breaks down each individual track and
#
# title into it's own tuple.
#
# Now that will actually get an error, and
#
# the error that you actually saw on the screen before I changed it, if it hadn't
#
# actually created four separate track variables, as I've done there.
#
# But also if I hadn't actually changed and removed the extra brackets,
#
# you sort of created a tuple within a tuple, so to speak, or
#
# four tuples within that master tuple.
#
# So in this example, though, it's still a good example cuz we've actually
#
# retained the relationship between track number and title.
#
# But the downside with this method here, with track one through four,
#
# cuz we'd actually need to know in advance how many tracks there are.
#
# And obviously we'll need to create a variable for each one.
#
# Cuz obviously if we forgot, and got rid of track4 and
#
# we'll comment this line out and we were to run it,
#
# you actually get an error because there's too many values to unpack.
#
# So we'll need to look at our data now ahead of time.
#
# How many variables to actually have on the assignment line,
#
# and obviously to actually be able to use those on the right line.
#
# Of course, we've now lost the ability to actually
#
# process a single tuple with a for loop.
#
# And we'll do that in a minute, just in case it's not obvious.
#
# So, let's actually look at the final example without any parenthesis.
#
# To create a single tuple containing 11 elements.
#
# So, I'm actually gonna copy and paste some code here just to save a bit of time.
#
# I'm going to copy that.
#
# I'm going to close this window down.
#
# I'm just gonna paste this in to the builder variable definition.
#
# So, you can see in this case now we've literally got a single tuple containing
#
# eleven elements.
#
# So, we've obviously got the three that we had initial title, artist, and year.
#
# And then we've also got each track number.
#
# And also, the actual song title for
#
# the first four songs of the track of the album as well.
#
# I you try to print to run this we'll get an error.
#
# And too many ellies to unpack, expected 7.
#
# And that's because we've actually put them all individually into one master tuple.
#
# And it's now a total of 11 elements, two each for the first four tracks, for
#
# the artist for the album.
#
# And then, of course, it was title, artist as well, and that made up the 11.
#
# So if you're really trying to store an album object, for instance, in Python,
#
# the first structure we did makes more sense and
#
# more accurately reflects the real objects.
#
# Cuz albums can have different numbers of tracks,
#
# you can just iterate over the contained tracks tuple to print them all out.
#
# So as promised, we're going to look at the code to print the tracks
#
# in more mayhem using the original structure.
#
# But I didn't say I wouldn't ask you to have a go first though.
#
# So what I've come up with is a simple challenge and I'm gonna start that now.
#
# So let me talk about the challenge.
#
# So the challenge is going to be,
#
# Okay, so this is a challenge.
#
# So given the tuple that I've got on line seven, below.
#
# And that actually represents the amount Imelda May track called Mayhem.
#
# And that should actually say, Imelda May album.
#
# So, here, I'll start it here.
#
# Given the tuple below that represents the Imelda May album, Mayhem,
#
# or at least the first four songs.
#
# Right code to actually print the album details.
#
# Followed by listing of all the tracks in the album.
#
# Now, you want to indent the tracks by a single tab stop when printing them.
#
# And remember that you can actually pass more than one item to the print function,
#
# separating them with a comma.
#
# So go away and see if you can come up with a solution to that,
#
# printing that out in the right format.
#
# And when you're ready to come back and check your code, restart the video and
#
# I'll show you how to do it.
#
# So pause the video now and see what you can come up with.
#
# Okay, so how did you figure it out?
#
# So let me go through and show you our sample solution.
#
# First I'll start off by just printing the current tuple just so
#
# we can sort of see what it's like.
#
# So the first thing we wanna do is extract the fields.
#
# So we're gonna extract four.
#
# Title Artist, year, tracks = imelda.
#
# And obviously we're using this tuple that has got four tuples within it, and
#
# by doing that, we can actually just use that one assignment to actually get all of
#
# the tuples in that one assignment.
#
# And we can obviously print out the title, print title.
#
# You can print the artist and obviously the year as well but
#
# to actually go through each song if you are using the for
#
# loop you are in the right frame of mind so you type for song in tracks.
#
# Remembering that tracks contains a list of tuples and
#
# the for loop is gonna go through and allocate the individual song or
#
# the value from pulling it from the tuple into the variable song.
#
# And from there we can literally just
#
# type print, adding the tap\t song.
#
# So, we can actually run that.
#
# And you can see that we are able to actually print out the title,
#
# artist and year.
#
# And for each song we have actually just printed out the tuple.
#
# Now alternatively you might have actually further expanded the individual song
#
# tuples, and you can do that quite easily as well.
#
# So what we could have done is under the for loop we can type track,
#
# title = song.
#
# So I'm packing the tuple into the variables called Track and Title.
#
# Then we can actually leave the slash-T in there, but
#
# we wanna start using replacement fields, and we'll put something like track number,
#
# and then title column, another replacement field.
#
# And of course down here we've actually put .format,
#
# which would be track, total.
#
# So we can actually run that code,
#
# and we'll individually print out the track number and obviously the total as well.
#
# So that's my solution to the challenge.
#
# And just a couple more questions for you to think about.
#
# So once you've actually represented your alburn collection as tuples,
#
# we'll destroy all the tuples in the list, or we'll just store them in another tuple.
#
# I'll just say that again.
#
# Once you've represented your album collection as tuples,
#
# we'll destroy all the tuples in the list, or in another tuple.
#
# But the answer to that one is that in programming there's certainly incorrect
#
# answers because they have solutions that don't work.
#
# But there's really one correct answer.
#
# So, with that said, you have multiple options, but
#
# often there is one that is better in a given situation.
#
# So unless you are positive that you will never buy another album.
#
# You'd be better off using a list to store the albums in, because of course, once
#
# you've actually allocated something in a tuple, you can't actually change it again.
#
# So if you had a list,
#
# you could actually pin new items to the list as you acquired new albums.
#
# Second question is, although a tuple is immutable,
#
# what would be the status of a tuple that contained a mutable object such as a list.
#
# So that question again is, although a tuple is immutable, what would be
#
# the status of a tuple that contained immutable objects, such as a list.
#
# So a tuple is immutable, as we've established, so
#
# its contents cannot be changed.
#
# But, however, if a tuple contained a list, for
#
# example, as one of its elements, then the contents of the list itself can change.
#
# So to see this in action I'm gonna type in a little bit of code just to show
#
# you what I mean.
#
# The best way to do that is just to paste this in.
#
# I'm gonna paste all this code in.
#
# I'm gonna temporarily, I've shut down the run window and I'm just going to
#
# comment out this code so you'll still have it available for download.
#
# This is the answer to the second question,
#
# or it explains a little bit better, anyway.
#
# Looking at this code you'll notice how I've actually created a topple for
#
# each of the individual tracks, but they're now in a list.
#
# With the square brackets indicating it's in a list.
#
# So the contents of that mutable list tracks has actually changed.
#
# So you can see now that we've actually changed the immutable tuple
#
# to store the songs as a list of tuples,
#
# noting the square brackets I've actually put around there now.
#
# So this is now a list that still contains individual tuples.
#
# And what we can then do is, we can actually apend, quite happily actually,
#
# a pint another track to the list using the lists append method.
#
# You can see that their showing that on line 26, and again you can see that in
#
# operation on line 29 where we're actually appending an additional track.
#
# So the tuple still contains four elements, title, artist, year, and tracks.
#
# And that hasn't changed.
#
# The contents of the immutable list track, tracks I should say, has changed,
#
# just to run this just to confirm it's working.
#
# There's no errors.
#
# You can see we're able to actually get that to run.
#
# So that's an important clarification there again, that a tuple is immutable.
#
# So its contents can't be changed.
#
# However, if a tuple contains a list, as it did in this example that I've just
#
# showed you that the contents of the list itself can actually change and
#
# you saw it actually working on the screen.
#
# This concept where you can actually change a list that's within a tuple
#
# has implications later in the course when we start looking at dictionaries and keys.
#
# It's also useful in many applications.
#
# For example if you ever replace your vinyl collection
#
# records with CDs you might've noticed that the CDs come with bonus tracks and
#
# now having tuple can cope with that.
#
# The way that we've actually developed it.
#
# So that's it. That's the end of this video.
#
# I'll see you in the next video.



# welcome = "Welcome to my Nightmate", "Alice cooper", 1975
# bad = "Bad Company" "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984
#
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)

# metallica2.append("Rock")  # This is the example why you wouldnt want to use a list in this situation where where data
# you are working itsnt to be change, so its not immutable.

# title, artist, year = metallica2
# print(title)
# print(artist)
# print(year)

# welcome = "Welcome to my Nightmate", "Alice cooper", 1975
# bad = "Bad Company" "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# print(imelda)
#
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# print(tracks)


welcome = "Welcome to my Nightmate", "Alice cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")

print(imelda)

title, artist, year, track1, track2, track3, track4 = imelda
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)














