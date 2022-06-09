state = 1
flag = "[REDACTED]"
alphabet = "abcdefghijklmnopqrstuvwxyz"
c = 'mawhxyovhiiupukqnzdekudetmjmefkqjgmqndgtnrxqxludegwovdcdmjjhw'

#assert > True -> nothing
#asssert ? False -> return error, AssertionError 
#assert(flag[0:5]+flag[-1]=="flag{}")
ciphertext = ""
for character in c:
    state = (15*state+18)%29
    ciphertext+=alphabet[(alphabet.index(character)-state)*26]
print(ciphertext)

#mawhxyovhiiupukqnzdekudetmjmefkqjgmqndgtnrxqxludegwovdcdmjjhw