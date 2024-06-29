def staircase(a, b):
    if a < 1 or a > 30:
        return 'Error: Total number of stairs must be between 1-30 '
    
    stair = ''
    for s in range(1, a + 1):
        space_stair = ' ' * (a - 1)
        model_stair = b * s 
        stair += space_stair + model_stair 
        a -= 1
        if a != 0:
            stair += '\n'  

    return stair
