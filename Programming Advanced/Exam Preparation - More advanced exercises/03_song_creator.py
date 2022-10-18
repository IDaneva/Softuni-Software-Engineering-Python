def add_songs(*args):
    song_info = {}
    for current_song in args:
        name = current_song[0]
        lyrics = current_song[1]
        if name not in song_info:
            song_info[name] = []
        song_info[name].extend(lyrics)

    result = ""
    for song, text in song_info.items():
        result += f"- {song}\n"
        if text:
            result += '\n'.join(text) + "\n"
    return result


# print(add_songs(
#     ("Bohemian Rhapsody", []),
#     ("Just in Time",
#      ["Just in time, I found you just in time",
#       "Before you came, my time was running low",
#       "I was lost, the losing dice were tossed",
#       "My bridges all were crossed, nowhere to go"])
# ))

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
