# set
This project lets you write bots that play everyone's favorite game, Set.

# What to do
Write a subclass of `BasePlayer` (from `basic_players.py`) that implements the `find_set` function. Then set up a test in `set.py` and run `python3 set.py`.

# N dimensions
Unlike the actual Set game, which only supports four dimensions (color, number, shape, shading), your bots can play Set with an arbitrary number of dimensions. Note the difference between number of dimensions and number of values. There will always be three possible values for each dimension, which means a set will always consist of three cards.

# Gameplay
Some aspects of Set gameplay don't work too well with computer time trials and n != 4 dimensions, so your bots will play a slightly different version of the game. Gameplay goes as follows:
  1) The dealer selects cards from the deck until there are at least 12 cards and at least one set.
  2) The player runs `find_set` on the visible cards and returns a set.
  3) The three cards are removed from the set.
  4) Repeat 1-3 until there are no cards in the deck and condition 1 is not met.
Only the time the player spends in `find_set` is counted.
