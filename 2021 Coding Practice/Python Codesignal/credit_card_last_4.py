# https://edabit.com/challenge/iRCwdDBkNcHM5QeAm

def card_hide(card):
    
    
    card_hidden = ""
    # i = 0
    
    # for number in card:
    #     if i < 12:
    #         card_hidden += "*"
    #     else:
    #         card_hidden += card[i]
    #     i += 1
    for digit in card[-len(card):-4]:
        card_hidden += "*"
    for digit in card[-4:]:
        card_hidden += digit
    
    print(card_hidden)
    
    return card_hidden


card_hide("1234123456785678") # ➞ "************5678"
card_hide("8754456321113213") # ➞ "************3213"
card_hide("35123413355523") # ➞ "**********5523"
card_hide("12345") # ➞ "**********5523"

print('#####################')