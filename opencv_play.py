import sys
import cv2 as cv
import numpy as np
from game import wrapped_flappy_bird as game

game_state = game.GameState()
# 什么都不做
init = [1,0]
im,_,_ = game_state.frame_step(init)

bird = cv.imread("assets/sprites/redbird-midflap.png")

pipe = cv.imread("assets/sprites/pipe-green.png")

pipe = pipe[:50,:,:]


def matchTemplate(im,template,mode=cv.TM_CCOEFF):
    """
        模板匹配方法
    """
    res = cv.matchTemplate(im,template,mode)

    min_val,max_val,min_loc,max_loc = cv.minMaxLoc(res)


    if max_val > 1e7:

        left,top = max_loc
        right,bottom = left + template.shape[1],top+template.shape[0]

        return left,top,right,bottom

    return None


im = cv.cvtColor(im,cv.COLOR_RGB2BGR)
bird_left,bird_top,bird_right,bird_bottom = matchTemplate(im,bird)
cv.rectangle(im,(bird_left,bird_top),(bird_right,bird_bottom),255,2)
cv.imshow("image",im)


find_pipe = False
while True:
    action = [0,1]

    im = cv.cvtColor(im,cv.COLOR_RGB2BGR)

    result = matchTemplate(im,bird)
    if result:
        bird_left, bird_top, bird_right, bird_bottom = result
        cv.rectangle(im,(bird_left,bird_top),(bird_right,bird_bottom),255,2)

    if find_pipe:
        # 找到管道了， 缩小图片， 继续寻找下一个管道
        im = im[:,:pipe_right,:]
        result = matchTemplate(im, pipe)
        if result:
            pipe_left, pipe_top, pipe_right, pipe_bottom = result

            action = [0,1] if pipe_top < bird_bottom + 10 else [1,0]

            if bird_left > pipe_right:
                find_pipe = False

    else:
        result = matchTemplate(im,pipe)

        if result:
            pipe_left,pipe_top,pipe_right,pipe_bottom = result

            action = [0, 1] if pipe_top < bird_bottom + 10 else [1, 0]

            find_pipe = True

    if find_pipe:
        cv.rectangle(im,(pipe_left,pipe_top),(pipe_right,pipe_bottom),255,2)

    cv.imshow("im",im)
    cv.waitKey(1)

    im,reward,t = game_state.frame_step(action)

    if t :
        print(t)
        break

cv.waitKey(0)