def catAndMouse(catA, catB, mouseC):
    num_catA = catA < 1  or catA > 100
    num_catB = catB < 1 or catB > 100
    num_mouseC = mouseC < 1 or mouseC > 100

    if (num_catA or num_catB or num_mouseC):
        return 'Error'
    
    if abs(catA - mouseC) > abs(catB - mouseC):
        return 'Cat B'
    elif abs(catA - mouseC) == abs(catB - mouseC):
        return 'Mouse C'
    else:
        return 'Cat A'
