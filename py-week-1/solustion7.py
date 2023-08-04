my_string = input('ENter your String : ')
my_char = input('ENter your character : ')

vowels = ['a','e','i','o','u','A','E','I','O','U']

new_string = ''
for i in my_string:
    if i in vowels:
        new_string +=my_char
    else:
        new_string += i

print(new_string)
                  
