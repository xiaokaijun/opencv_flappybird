from game import wrapped_flappy_bird as game

game_state = game.GameState()

while True:
    do = [1,0]
    image,reward,terminal = game_state.frame_step(do,manual=True)
    print(reward,terminal)
