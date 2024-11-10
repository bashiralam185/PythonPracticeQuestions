#write a program to find all such numbers between 1000 and 3000 such that the digits are
# even. The number should be printed in comma separated sequence


# main_list=[]
# for i in range(1000, 3000):
#     count=0
#     list=[]
#     last_digit=i%10
#     list.append(last_digit)
#     while True:
#         second_last=int((i-last_digit)/10)
#         list.append(second_last%10)
#         third_last=int((second_last-second_last%10)/10)
#         list.append(third_last%10)
#         fourth_digit=int((third_last-third_last%10)/10)
#         list.append(fourth_digit)
#         break
#     for i in list:
#         if i%2==0:
#             count+=1
#     if count==4:
#         main_list.append(list)
# print(main_list)



#write a program to to count the number of letters and digits in the given sentence

# user_input=input("enter the sentence containing digits")
# digits=0
# letters=0

# for i in user_input:
#     digit=['1' ,'2', '3', '4', '5', '6', '7', '8', '9', '0']
#     if i==" ":
#         pass
#     elif i in digit:
#         digits+=1
       
#     else:
#         letters+=1
        

# print(f"number of digits are  {digits}")
# print(f"number of letters are  {letters}")



#write a program and print the number of upper and lower case letters

# sentence=input("enter the sentence")
# upper=0
# lower=0
# for i in sentence:
#     if i.isupper():
#         upper+=1
#     if i.islower():
#         lower+=1

# print(lower)
# print(upper)


#write a promgam that computes the value of a+aa+aaa+aaaa wiht a given digits

# number=input("enter one digit number")
# n1=int("%s" %number)
# n2=int("%s%s" %(number, number))
# n3=int("%s%s%s" %(number, number, number))
# n4=int("%s%s%s%s" %(number, number, number, number))
# print(n1+n2+n3+n4)




#create a strong password
# password=input("Please enter your password")
# char=0
# digits=0
# Up=0
# Lo=0
# total=0
# for i in password:
#     total+=1
#     cha=['!', '@', '#', '$', '%', '&']
#     number=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     if i in cha:
#         char+=1
#     if i in number:
#         digits+=1
#     if i.isupper():
#         Up+=1
#     if i.islower():
#         Lo+=1
# if char<2:
#     print("Atleast two special character")
# elif  digits<2:
#     print("your password must have at least 2 digits")
# elif Up<2:
#     print("your passwords must have at least 2 upper letter")
# elif Lo<2:
#     print("password must have atleast 2 lower letters")
# elif total<8:
#     print("password must have atleast 8 characters")
# else:
#     print("congrates! your password has been created")





#enter the data ( name, age, height) and sort them in accending order in form of tuples in the list

# num_of_data= int(input("enter the number of data"))
# list=[]
# for i in range( 0, num_of_data):
#     tup=()
#     name=input("enter the user name")
#     age=int(input("enter the age"))
#     height=int(input("enter the height"))
#     tup=tup+(name,)+(age,)+(height,)
#     list.append(tup)
# list.sort()
# print(list)



#create a function to find the number divisible by 7 form 1 to n

# def main(num):
#     for i in range(1, num):
#         if i%7==0:
#             print(i)

# main(89)



#write a program to print the maximum lenght of stirng
# def main(first, second):
#     one=[]
#     two=[]
#     for i in first:
#         one.append(i)
#     for i in second:
#         two.append(i)
#     if len(one)>len(two):
#         print(len(one))
#     elif len(one)==len(two):
#         print("both have same length")
#     else:
#         print(len(two))

# first=input("enter sentence")
# second=input("enter sentence")
# main(first, second)


#pythoagorous 
# import math
# def main(lenght, width):
#     hy=((lenght**2)+(width**2))**0.5
#     print(hy)
# l=int(input("enter lenght of triangle"))
# w=int(input("enter width of triangle"))
# main(l, w)


#write a program to generate dist of numbers and their squares

# def main():
#     d=dict()
#     for i in range(1, 21):
#         d[i]=i**2
#     print(d)
# main()






# write a funtion to print the square of odd numbers from the list
# def main(x):
#     for i in x:
#         if i%2!=0:
#             print(i*i)
# list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# main(list)


### This it sample test for checking





        
