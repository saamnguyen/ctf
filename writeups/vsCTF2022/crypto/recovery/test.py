from random import randint

password = '123456'
key = ['vs'.join(str(randint(7, 9)) for _ in range(ord(i))) + 'vs' for i in password[::-2]]
print(key)