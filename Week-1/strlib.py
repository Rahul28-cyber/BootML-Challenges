def countword(string):
    lst = string.split(" ")
    words = 0
    for item in lst:
        if(len(item)>0):
            words = words + 1
    return words

def numofchars(string):
    modified = string.replace(" ","")
    return len(modified)
