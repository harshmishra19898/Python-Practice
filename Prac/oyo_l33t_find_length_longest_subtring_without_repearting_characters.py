'''
Find Length of longest substrings without repeating characters
ex- input:aabzbcca
    output:3   
'''

''' Plan 
Step 1- take input s , take 2 pointers l and r and initiaize them to 0, declare an empty set, declare , maxlength to 0 
Step 2- go through letter of s by making a for loop where r is varies from 0 to length of input -1 
Step 3 - make a while loop which checks if letter by r pointer is  if it is character set then remove letters pointed by l pointer from  character set 
         and increment the left pointer

         after that come out of the loop once letter pointed by r pointer is no longer in  character set and 
           add the letter by the r pointer to the character set 
         and calculate maxlength by taking max ( maxlength, r-l+1)
'''

def calculate_length_of_longest_substring_without_repeating_characters(input):
    s=input
    char_set = set()
    l = 0 
    r = 0 
    max_length=0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l +=1
        char_set.add(s[r]) 
        max_length= max(max_length, r-l+1)
    return max_length
    

inp= "aabzbcca"
max_len = calculate_length_of_longest_substring_without_repeating_characters(inp)
print(max_len)