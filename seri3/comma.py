def costum(string):
    word=''
    result=[]
    for char in string:
        if char==',':
            result.append(word)
            word=''
        else:
            word+=char
    if word:
        result.append(word)
    
    return result

string="3020,149,NDP;LIBERAL;GREEN;CPC,2;2;2;3,YES;NO;YES;NO"
result=costum(string)
print(result)


