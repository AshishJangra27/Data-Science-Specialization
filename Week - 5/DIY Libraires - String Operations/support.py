def title_(txt):
    t = ''
    for word in txt.split(' '):
        if (len(word) == 1):
            t += upper_(word) + ' '
        else:
            temp = upper_(word[0]) + word[1:] + ' '
            t += temp
    return t[:-1]

def isalnum_(ch):
    if (ord(ch) >= 48 and ord(ch) <= 57) or (ord(ch) >= 97 and ord(ch) <= 122) or (ord(ch) >= 65 and ord(ch) <= 90):
        return True
    else:
        return False
    
def isdigit_(ch):
    if (ord(ch) >= 48  and  ord(ch) <= 57):
        return True
    else:
        return False
    
def upper_(txt):    
    t = ''
    for i in txt:
        if (ord(i) >= 97 and ord(i) <= 122):
            t += chr(ord(i) - 32)
        else:
            t += i
    return t

def lower_(txt):    
    t = ''
    for i in txt:
        if (ord(i) >= 65 and ord(i) <= 90):
            t += chr(ord(i) + 32)
        else:
            t += i
    return t

def capitalize_(txt):    
    t = ''   
    if (ord(txt[0]) >= 97 and ord(txt[0]) <= 122):
        t = chr(ord(txt[0]) - 32)            
    else:
        t = txt[0]                           
      
    for i in txt[1:]:                        
        if (ord(i) >= 65 and ord(i) <= 90):  
            t += chr(ord(i) + 32)            
        else: 
            t += i                           
    return t                                 