print("Hello I made it")

# converting to togglecase


def toggle(s):
    l =[]
    for char in s:
        if char.islower():
            l.append(char.upper())
        elif char.isupper():
            l.append(char.lower())
        else:  
            l.append(char)

    return ''.join(l)
w = "Yemma"
result = toggle(w)
print(result)

print(":".join(w))


first = 'Dave'
last = 'Kuhlman'
full = '%s, %s' % (last, first, )
print (full)


strlist = []
strlist.append('Line #1')
strlist.append('Line #2')
strlist.append('Line #3')
str = '\n'.join(strlist)
print (str)



