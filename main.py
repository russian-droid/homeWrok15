'''
CodeWars kata from codewars.com

Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
'''

def bool_to_word(boolean):
    if bool(boolean) == True:
        x = "Yes"
    else:
        x = "No"
    return x

#------------someone else's solution
def bool_to_word(bool):
    return "Yes" if bool else "No"

#------------someone else's solution
def bool_to_word(bool):
    if bool:
        return 'Yes'
    else:
        return 'No'
