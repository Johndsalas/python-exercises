
# Find five letter words, whose first letter number value is equal to its last 4
with open('/usr/share/dict/words') as f:
    words = f.read().split('\n')

    five_letter_words = [word for word in words if len(word) == 5]

    for word in five_letter_words:

        first_letter_value = 0

        four_letter_value = 0

        first = True
        
        for letter in word: 
            
            if letter == word[0] and first == True:
                 
                 first_letter_value = ('abcdefghijklmnopqrstuvwxyz'.index(letter.lower()) + 1)

                 first = False
    
            else:

                 four_letter_value += ('abcdefghijklmnopqrstuvwxyz'.index(letter.lower()) + 1)

        if first_letter_value == four_letter_value:

            print(word)

        
