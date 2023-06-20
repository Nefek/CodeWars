def disemvowel(string_):

    for i in string_:
        if i in "euioaEUIOA":
            string_ = string_.replace(i, "",1) 
        
    return string_
