# Given the tuple below that represents the Imelda May album "More Mayhem"
# Write code to print the album details, followed by a listing of all the tracks
# in the album.
# Indent the track by a single tab stop when printing them ( remember that you
# can pass more than one item to the print function, separting them with a comma.

# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# print(imelda)
#
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# # for song in tracks:
# #     print("\t", song)
#
# for song in tracks:
#     track, title = song
#     print("\tTrack Number {}, Title: {}".format(track, title))

imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

print(imelda)

imelda[3].append((5, "All For You"))  # this is list append method

title, artist, year, tracks = imelda
tracks.append((6, "Etermity"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title =song
    print("\tTrack Number {}, Title: {}".format(track, title))