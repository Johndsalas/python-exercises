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



def anagrams(word, words):
   
    print(check_list)
    count = 0
  
    anagram_list = []
  
    for string in words:

         word = word
  
    for letter in string:
      
        if letter in word:
           
               word = word.remove(letter)
               print(check_list)
          
        else:

            count += 1
      
    if count == 0:
      
          anagram_list.append(string)
          print(anagram_list)
    
return anagram_list


anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])