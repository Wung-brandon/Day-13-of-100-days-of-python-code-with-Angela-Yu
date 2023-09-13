########DEBUGGING#########

#Describe the problem                      
""" def my_function():            
    for i in range(1,21):            
    if i == 20:                         
            print("you got it")             
my_function()                      
 """
 
"""Reproduce the bug
from random import randint
dice = ['1','2','3','4','5','6','7','8','9']
dice_num = randint(0,8)
print(dice[dice_num])"""

#play computer
""" year = int(input("What's your of birth?:"))
if year > 1980 and year <= 1994:
    print("You are a millenial")
elif year > 1994:
    print("You are a Gen Z") """

#print is your friend
""" pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f'pages = {pages}')
print(f'word_per_page = {word_per_page}')
print(f"The number of total words is {total_words}") """

#Use a debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        #print(new_item)
        b_list.append(new_item)
    print(b_list)
    
mutate([1,2,3,5,13])