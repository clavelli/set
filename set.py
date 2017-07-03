import basic_players
from game import Game


def run_trial(game, player, times=1):
    times = [game.run(player) for i in range(times)]
    if any(t is None for t in times):
        return None
    return sum(times) / len(times)


if __name__ == "__main__":
    game = Game(4)
    print(run_trial(game, basic_players.StupidPlayer(), times=50))
    print(run_trial(game, basic_players.NaivePlayer(), times=50))
    print(run_trial(game, basic_players.Jason(), times=50))
