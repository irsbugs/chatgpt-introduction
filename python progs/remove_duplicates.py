"""
>>     # Remove duplicates in the list
>>     a_list = list(dict.fromkeys(a_list)) <-- Ian version

 a_list = list(map(str.capitalize,a_list)) <-- DL Neil suggestion
 
 
"""

# ChatGPT: remove duplicates from a python list
def remove_duplicates(lst): 
    final_list = [] 
    for num in lst: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
  
# Driver Code 
lst = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40] 
print(remove_duplicates(lst))

# ChatGPT: remove duplicate strings from a python list
def remove_duplicates(listx): 
    new_list = list(dict.fromkeys(listx))  
    return new_list
    
listx = [1,2,3,1,2,3,4,5,6,7,7,8,9,10]
print(remove_duplicates(listx))

"""
# <-- listx was list has error TypeError: 'list' object is not callable

[10, 20, 30, 50, 60, 40, 80]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


invent a name for a flavor of icecream

Cherry Chocolate Ripple Deligh

invent a name for a flavor of green colored icecream

Minty Meadow Breeze

"""
