# https://edabit.com/challenge/o3LWAZtjARJHLtyyb
def reverse_case(word):
    
    reversed_word = ""
    
    for letter in word:
        if letter.islower() == True:
            letter = letter.upper()
            reversed_word += letter
        else:
            letter = letter.casefold()
            reversed_word += letter
    
    return reversed_word
    # print()
	# return word - word[]



word1 = "apPle"
word2 = "cheRry"
word3 = "banAna"

print(reverse_case(word1))
reverse_case(word2)
reverse_case(word3)

# .upper()
# .casefold()

# .islower()
# .isupper()