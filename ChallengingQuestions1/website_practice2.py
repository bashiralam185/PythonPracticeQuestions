# input=["1, 2, 3, 4", "2, 3, 4, 5, 6"]      output=[2, 3, 4]. find intersection of string type list containg numbers
# #############################   CODER BYTE #########################################3
# def main():
#     a=["1, 2, 3,4","5, 3, 7, 8"]
#     elements=[]
#     common=[]
#     for i in range(len(a)):
#         for j in a[i]:
#             if j==" " or j==",":
#                 pass
#             else:
#                 if j in elements:
#                     common.append(j)
#                 elements.append(j)
#     print(common)
# main()




# take the str string as parameter which will containes single digits letters and questions marks. check if there are excatly equal number of 
# of q marks as the sum of all the  digits. if yes return true else false
######################### CODE BYTE ###########################################3


# def main():
#     string=input("enter a string")
#     count=0
#     sum=0
#     for i in string:
#         if i=="?":
#             count+=1
#         try:
#             if int(i)/1!=0:
#                 sum+=int(i)
#         except:
#             pass
#     if count==sum:
#         print("True")
#     else:
#         print("Fasle")
# main()








# print reverse of input string
# ################ CODE BYTE ############################################33
# def main():
#     x=""
#     string=input("enter sentence")
#     for i in string:
#         x=i+x
#     print(x)
# main()
    









# empty box is a game played with two D-sided dice, one box and collection of T panaalty tokens. the value of the panalty tokens are 1....take
# at the begning of the game all panelty tokens are in the box.
# the game consist of one or more turns, in each turn you roll the dice and get number which is your power.
# now you have to get panalty tokens from the box. if you got the same number you won . you can use your tokens uless they finishesd
# if you exceed the number you lost 
########################################## TOP CODER #####################################################
# from random import randint
# import time

# def main():
#     box=[1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     your_sore=randint(20, 40)
#     your_choice=0
#     while True:
#         your_sore+=randint(1, 6)+randint(1, 6)
#         time.sleep(2)
#         print(f"***********************\n\n\n{your_sore}\n\n************************")
#         print(box)
#         you=int(input("enter your numbr from box"))
#         if you in box:
#             box.remove(you)
#             pass
#         else:
#             print("Invalid input")
#             break
#         your_choice+=you
#         print(f"your score is {your_choice}\n\n")
#         if your_sore>your_choice:
#             print(" you are close! go ahead")
#             time.sleep(2)
#         elif your_choice==your_sore:
#             print("congrates you won the game")
#             break
#         else:
#             print("Sorry you lost!")
#             break
# main()
        














# it is a game of War between you and opponent,
# create a list of guns each gun can detroy differnt number of arramy. let you arrmy be [1, 1, ,1,1, 1, 2, 2, 2, 3, 3 ,3 10] where 10 is the king.
# if you kill all of the opponent army you will win.
# ######################################## MY OWN ############################################################
# import random
# from random import randint
# import time
 
# guns=["pistol", "TDM", "karansharkove", "mezail", "air_jet" ]
# your_army=[1, 1, 1 ,1, 1, 1, 1,1, 1, 1, 1, 2, 2, 2, 2, 2 ,2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 10]
# enemy_army=[1, 1, 1 ,1, 1, 1, 1,1, 1, 1, 1, 2, 2, 2, 2, 2 ,2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 10]
# def main():
#     while True:
#         print("**********************************************************************************\n\n\n\n")
#         print(your_army)
#         print("\n\n\n")
#         print(enemy_army)
#         print("************************************************************************************")

#         print("it is your Turn now\n\n")
#         your_gun=random.choice(guns)
#         print(f"\n\n you have {your_gun}")
#         if your_gun=="pistol":
#             print("you can only kill one person")
#             if enemy_army[0]==1:
#                 x=input("")
#                 if x=="":
#                     enemy_army.remove(enemy_army[0])
#             else:
#                 x=input("")
#                 if x=="":
#                     enemy_army[0]-=1
#         elif your_gun=="TDM":
#             print("you can kill two person")
#             if enemy_army[0]==1 and enemy_army[1]==1:
#                 x=input("")
#                 if x=="":
#                     enemy_army.remove(enemy_army[0])
#                     enemy_army.remove(enemy_army[1])
#             elif enemy_army[0]==1 and enemy_army[1]==2:
#                 x=input("")
#                 if x=="":
#                     enemy_army.remove(enemy_army[0])
#                     enemy_army[1]-=1
#             elif enemy_army[0]==2:
#                 x=input("")
#                 if x=="":
#                     enemy_army.remove(enemy_army[0])
#             else:
#                 x=input("")
#                 if x=="":
#                     enemy_army[0]-=2
#         elif your_gun=="karansharkove":
#             print("you can kill up to three person")
#             if 2 in enemy_army:
#                 x=input("")
#                 if x=="":
#                     enemy_army.remove(2)
#                 if enemy_army[0]==1:
#                     x=input("")
#                     if x=="":
#                         enemy_army.remove(enemy_army[0])
#                 else:
#                     x=input("")
#                     if x=="":
#                         enemy_army[0]-=1
#             else:
#                 if enemy_army[0]==1:
#                     enemy_army.remove(enemy_army[0])
#                 if enemy_army[1]==1:
#                     enemy_army.remove(enemy_army[1])
#                 if enemy_army[2]==1:
#                     enemy_army.remove(enemy_army[2])
#         elif your_gun=="mezail":
#             print("you can kill only three")
#             if 3 in enemy_army:
#                 try:
#                     enemy_army.remove(3)
#                 except:
#                     print("no threes are there")
#         else:
#             if len(enemy_army)<=3:
#                 print("you won!")
#                 break
#             else:
#                 print("choose any three whom you want to kill")
#                 one=int(input("enter"))
#                 two=int(input("enter"))
#                 three=int(input("enter"))
#                 enemy_army.remove(one)
#                 enemy_army.remove(two)
#                 enemy_army.remove(three)
        
#         print("\n\n\n you killed some of them")
#         time.sleep(2)
#         print("\n\n\n")
#         print(enemy_army)
#         if len(enemy_army)<=1:
#             print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\nCongratulatons! you won the war\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#             break


#         time.sleep(2)
#         print("your enemies turn\n\n\n")
#         time.sleep(2)
#         enemy_gun=random.choice(guns)
#         print(f"\n\n you have {enemy_gun}")
#         if enemy_gun=="pistol":
#             print("you can only kill one person")
#             if your_army[0]==1:
#                 your_army.remove(your_army[0])
#             else:
#                 your_army[0]-=1
#         elif enemy_gun=="TDM":
#             print("you can kill two person")
#             if your_army[0]==1 and your_army[1]==1:
#                 your_army.remove(your_army[0])
#                 your_army.remove(your_army[1])
#             elif your_army[0]==1 and your_army[1]==2:
#                 your_army.remove(your_army[0])
#                 your_army[1]-=1
#             elif your_army[0]==2:
#                 your_army.remove(your_army[0])
#             else:
#                 your_army[0]-=2
#         elif enemy_gun=="karansharkove":
#             print("you can kill up to three person")
#             if 2 in your_army:
#                 your_army.remove(2)
#                 if your_army[0]==1:
#                     your_army.remove(your_army[0])
#                 else:
#                     your_army[0]-=1
#             else:
#                 if your_army[0]==1:
#                     your_army.remove(your_army[0])
#                 if your_army[1]==1:
#                     your_army.remove(your_army[1])
#                 if your_army[2]==1:
#                     your_army.remove(your_army[2])
#         elif enemy_gun=="mezail":
#             print("you can kill only threes")
#             if 3 in your_army:
#                 try:
#                     your_army.remove(3)
#                 except:
#                     print("no threes are there")
#         else:
#             if len(your_army)<=3:
#                 print("sorry you lost")
#                 break
#             else:
#                 print("choose any three whom you want to kill")
#                 one=int(input("enter"))
#                 two=int(input("enter"))
#                 three=int(input("enter"))
#                 your_army.remove(one)
#                 your_army.remove(two)
#                 your_army.remove(three)
#         time.sleep(2)
#         print("\n\n\n")
#         print(your_army)
#         if len(your_army)<=1:
#             print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\nSOrry Enemies Won the war\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#             break
#         time.sleep(3)
#         print("\n\nfirst round completed\n\n")
#         time.sleep(2)
# main()



        




# it can be seen that the number 125874 and its doule 251748 contains exactly the same digits but in different order. 
# find the smallest number that have the same digits when multiplied by 2 and three and four
# 3###################   PROJECT EULER ##########################################3
# def main():
#     for j in range(100000, 500000):
#         number=j
#         digits=[]
#         multiply2=[]
#         three3=[]
#         two=number*2
#         three=number*3
#         while True:
#             x=number%10
#             y=two%10
#             z=three%10
#             if number/10==0:
#                 break
#             else:
#                 digits.append(x)
#                 multiply2.append(y)
#                 three3.append(z)
#             number=int((number-x)/10)
#             two=int((two-y)/10)
#             three=int((three-z)/10)
#         count=0
#         for i in digits:
#             if i in multiply2 and i in three3:
#                 multiply2.remove(i)
#                 three3.remove(i)
#                 count+=1
#         if len(multiply2)==0 and len(three3)==0 and count==len(digits):
#             print(j)
# main()










#unknown game and is incomplete with some errors! 
# import random
# def main():
#     cards=[1, 1, 1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 100, 100 ]
#     player1_list=[]
#     player2_list=[]
#     board=[]
#     total1=0
#     total2=0
#     Player1=[]
#     Player2=[]
#     for i in range(4):
#         x=random.choice(cards)
#         Player1.append(x)
#         cards.remove(x)
#         y=random.choice(cards)
#         Player2.append(y)
#         cards.remove(y)
#     while True:
#         board.append(cards[1])
#         print(board)
#         while True:
#             print("player one")
#             print(Player1)
#             card=int(input("enter the card you want to place"))
#             if card>=board[-1]:
#                 Player1.remove(card)
#                 board.append(card)
#                 if len(cards)!=0:
#                     CARD=random.choice(cards)
#                     Player1.append(CARD)
#                 else:
#                     pass
#             else:
#                 for i in board:
#                     player2_list.append(i)
#                     board.remove(i)
#                 break
#             print("computer")
#             print(Player2)
#             print("\n\n\n\n board")
#             print(board)
#             computer=int(input("enter for computer"))
#             if computer>=board[-1]:
#                 Player2.remove(computer)
#                 board.append(computer)
#                 if len(cards)!=0:
#                     CArd=random.choice(cards)
#                     Player2.append(CArd)
#                 else:
#                     pass
#             else:
#                 for j in board:
#                     player1_list.append(j)
#                     board.remove(j)
#             if len(cards)==0:
#                 break
#             print("Board")
#             print(board)
#         if len(cards)==0:
#             break
#     for one in player1_list:
#         total1+=one
#     for two in player2_list:
#         total2+=two

#     print("HERE IS THE RESULT\n\n")
#     if total2>total1:
#         print("computer won  and has total score of ")
#         print(total2)
#         print(f" you have score of {total1}")
#     else:
#         print("you won the game with")
#         print(total1)
#         print(f" computer has total of {total2}") 
# main()







# maximum sum of number a'b; where a and b are less tha 10;
################ PROJECT EULER #####################

# def main():
#     sum=0
#     a=0
#     b=0
    
#     for i in range(1, 40):
#         for j in range(1, 40):
#             number=i**j
#             Sum=0
#             while number>=1:
#                 last_digit=number%10
#                 Sum+=last_digit
#                 number=int((number-last_digit)/10)
#             if Sum>sum:
#                 sum=Sum
#                 a=i
#                 b=j
#     print(sum)
#     print(a**b)
#     print(a)
#     print(b)
# main()







#enter a password of 5 digits and then ask the user to input any three codes from his pawword.
#aked this three times if he missed to times break the statment else successfull the  entry

# from random import randint
# def main():
#     password=int(input("enter password of 5 numbers"))
#     count=0
#     error=0
#     while True:
#         digit_number=5
#         x=randint(1, 6)
#         number=password
#         while True:
#             digit=number%10
#             if digit_number==x:
#                 break
#             else:
#                 digit_number-=1
#                 number=int((number-digit)/10)
#         print(f"enter digit number {x}")
#         secret_digit=int(input("enter here"))
#         if secret_digit==digit:
#             count+=1
#         else:
#             error+=1
#         if error>1:
#             print("sorry you missed your chance")
#             break
#         if count==3:
#             print("successfully you enter your code")
#             break

# main()








#a number chain is created by continously adding the squares of the digits in an number to form a new numer util it has been seen.

# def main(num):
#     number_set=[]
#     number_set.append(num)
#     while True:
#         if num<10:
#             if num in number_set:
#                 number_set.append(num)
#                 print(number_set)
#                 break
#             else:
#                 number_set.append(num)
#                 num=(num*num)
#         elif num<100:
#             last_digit=num%10
#             num=int((num-last_digit)/10)
#             num=(last_digit*last_digit)+(num*num)
#             if num in number_set:
#                 number_set.append(num)
#                 print(number_set)
#                 break
#             else:
#                 number_set.append(num)
#         if num>=100:
#             last_digit=num%10
#             num=int((num-last_digit)/10)
#             middle_digit=num%10
#             num=int((num-middle_digit)/10)
#             num=(num*num)+(middle_digit*middle_digit)+(last_digit*last_digit)
#             if num in number_set:
#                 number_set.append(num)
#                 print(number_set)
#                 break
#             else:
#                 number_set.append(num)
        
# main(44)






