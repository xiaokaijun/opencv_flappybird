import numpy as np
from game import wrapped_flappy_bird as game


game_state = game.GameState();

while True:
    do = np.random.choice([True,False],p=[0.2,0.8])
    do = [0,1] if do else [1,0]

    # 随机挑选动作
    image,reward,terminal = game_state.frame_step(do)
    