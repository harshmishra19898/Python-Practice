'''
Q2)find length of  largest substring in string  without repeating characters  ex [aabbcca]
Substring - a contigious part of a string
'''

'''
a - a
a - a, ab, abz
b-  b, bz 
z - z, zb, zbc
b - b, bc 
c-  c
c - c, ca
a-  a
'''

input = "aabzbcca"
#print("input is "+input)

# find all non repeating sub strings for all indexes 
# how to check if given substring contains all unqiue alphabets?-> cont occurences of each element
subtr_list=[]
n=len(input)
for i in range(0,n):
    substr=""
    for j in range(i,n):
        substr=input[i:j+1]
        #ca
        #print(substr,j,"j")
        p=""
        count_char_dic={}
        for k in range(0,len(substr)):
           
            if substr[k] in p:
                
                count_char_dic[substr[k]]+=1
            else:
                p+=substr[k]
                count_char_dic[substr[k]]=1
        #print(substr,"substr")
        #print(count_char_dic,i,"i")
        #print(count_char_dic)
        value_list=[]
        for key, value  in count_char_dic.items():
            value_list.append(value)
        greatest_val = 0
        for val in value_list:
            if val > greatest_val:
                greatest_val = val 
        if greatest_val != 1:
            pass
        else:
            subtr_list.append(substr)

            
#print(subtr_list)
subs_len_list=[]
for subs in subtr_list:
    subs_len_list.append(len(subs))

greatest_no=0
for no in subs_len_list:
    if no > greatest_no:
        greatest_no = no
print("The Length of the longest substring from the given input string "+"\""+input+"\"" +" is",greatest_no)
print("Substring list with non repeating characters:"+ "\n",set(subtr_list))

          







