import sys
import cv2 as cv
import game.wrapped_flappy_bird as game

game_state = game.GameState()

# 创建实例 若为1,0 ，则什么都不做， 若为0，1则小鸟会向上运动
do = [1,0]
image,reward,terminal = game_state.frame_step(do)

print(image.shape,reward,terminal)

image = cv.cvtColor(image,cv.COLOR_RGB2BGR)
cv.imshow("image",image)
cv.waitKey(0)