from enum import Enum

inp = 'input'

# --- PART 1 --- #

rounds = [line.strip('\n') for line in open(inp).readlines()]

class Shape(Enum):
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'

shapes = {
    'A': Shape.ROCK,
    'B': Shape.PAPER,
    'C': Shape.SCISSORS,
    'X': Shape.ROCK,
    'Y': Shape.PAPER,
    'Z': Shape.SCISSORS
}

scores = {
    Shape.ROCK: 1,
    Shape.PAPER: 2,
    Shape.SCISSORS: 3,
}

# Key is winner, value is loser
stronger = {
    Shape.ROCK: Shape.PAPER,
    Shape.SCISSORS: Shape.ROCK,
    Shape.PAPER: Shape.SCISSORS
}

score = 0
for game_round in rounds:
    (opponent, player) = game_round.split(' ')
    opponent_shape = shapes[opponent]
    player_shape = shapes[player]
    score += scores[player_shape]
    draw = player_shape == opponent_shape
    if draw:
        score += 3
    win = player_shape == stronger[opponent_shape]
    if win:
        score += 6

print(f"Silver: {score}")

# --- PART 2 --- #

class Outcome(Enum):
    WIN = 'WIN'
    LOSE = 'LOSE'
    DRAW = 'DRAW'

outcomes = {
    'X': Outcome.LOSE,
    'Y': Outcome.DRAW,
    'Z': Outcome.WIN
}

score = 0
weaker = {v: k for k, v in stronger.items()} # Key is loser, value is winner
for i, game_round in enumerate(rounds):
    (opponent, outcome) = game_round.split(' ')
    opponent_shape = shapes[opponent]
    needed_outcome = outcomes[outcome]
    if needed_outcome == Outcome.DRAW:
        score += 3
        needed_player_shape = opponent_shape
    elif needed_outcome == Outcome.WIN:
        score += 6
        needed_player_shape = stronger[opponent_shape]
    elif needed_outcome == Outcome.LOSE:
        needed_player_shape = weaker[opponent_shape]
    score += scores[needed_player_shape]

print(f"Gold: {score}")
