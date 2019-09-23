def countBits(n):

    count = 0
    n = bin(n)

    for letter in n:

       if letter == "1":

           count += 1

    return count
       
countBits(0)
countBits(4)
countBits(7)
countBits(9)


def namelist(names):

    lst = []
    
    for dict in names:
    
        lst.append(dict['name'])

    print(lst)