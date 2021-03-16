# challenge 1
# print a joke to the user 
# def main():
#     print("once upon a time there was a man! his name was ....")
#     enter=input("Do you want to read more? Y/N")
#     if enter=='Y' or enter=='y' or enter=="":
#         print("he was with his family")

#     else:
#         print("thank you!")
# main()




# challenge 2Write a program that will ask you your name
# It will then display ‘Hello Name’ where ‘Name’ is the
# name you have entered

# def main(name):
#     print(f"hello! {name}")
# name=input("enter your name")
# main(name)




# challenge 3
# Write a program to work out the areas of a rectangle.
# Collect the width and height of the rectangle from the keyboard Calculate the area display the result.

# def main(length, width):
#     area=length*width
#     print(area)
# length=int(input("enter lenght"))
# width=int(input("enter width"))
# main(length, width)





# challenge 4
# Write a program that will work out the
# distance travelled if the user enters in the speed and the time. 

# def main(time, velocity):
#     distance=velocity*time
#     print(f"the distance is {distance}m")
# time=int(input("enter time in seconds"))
# velocity=int(input("enter velcity in m/s"))
# main(time, velocity)





# challenge 5:
# Write a program to work out how many days you have lived for.
# Work out how many seconds you’ve lived for. 

# def date_of_birth():
#     date=int(input("enter date of your birthday"))
#     monnth=int(input("enter month of your birthday"))
#     year=int(input("enter year of your birthday"))
#     days=30-date
#     months=12-monnth
#     years=2020-year
#     numbers_of_days=days+(months*30)+(years*365)+(3*30)+(29)
#     return numbers_of_days
# date_of_birth()
 
# def in_seconds():
#     number=date_of_birth()
#     print(number*24*3600)
# in_seconds()





#challenge 6
# Make a game for seeing how good people are at
# guessing when 10 seconds have elapsed. 

# import time

# def calculating(total):
#     if total<10:
#         x=(total-10)*(-1)
#         print(f"you were {x} seconds close to 10")
#     elif total>10:
#         x=total-10
#         print(f"you were {x} seconds ahead of 10")
#     else:
#         print("Amezing! you stop at exactly 10 seconds")
# def main():
#     print("once you click enter your time will be started. To stop the time click again enter")
#     start=input("please enter to start time:")
#     starting=time.strftime("%S")
#     Starting=time.strftime("%M")
#     ending=input("Enter when you think it has been 10  seconds")
#     if ending=='':
#         end_time=time.strftime("%S")
#         end=time.strftime("%M")
#     Total_time=(int(end)*60+int(end_time))-(int(Starting)*60+int(starting))
#     calculating(Total_time)
    
# main()


# challenge 7




# challenge 8
# Write a program that will accept someone’s date of birth and work out whether they can vote (i.e. Are they 18?)

# import time
# date=int(input("enter date of your birthday"))
# month=int(input("enter month of your birthday"))
# year=int(input("enter year of your birthday"))
# today_date=int(time.strftime("%d"))
# today_month=int(time.strftime("%m"))
# today_year=int(time.strftime("%Y"))
# number_of_days=((31-date)+(12-month)*30)+((today_year-year)*365)+(12-today_month*30)+(31-today_date)
# vote=18*365
# if number_of_days>vote:
#     print("you can vote")
# else:
#     print("you cant vote")
#     print(vote-number_of_days)





# challenge 11

# Write a program that will give the students the answer to logic gate questions

# def main(gate):
#     if gate=='OR':
#         Input=int(input("enter first input"))
#         input2=int(input("Enter second input"))
#         if (Input==1) or( input2==1):
#             print("out put is 1")
#         else:
#             print("out put is 0")
#     if gate=='AND':
#         input1=int(input("enter first input"))
#         input2=int(input("enter second input"))
#         if input1==1 and input2==1:
#             print("output is 1")
#         else:
#             print("output is 0")
#     if gate=='NOT':
#         input1=int(input("enter input"))
#         if input1==1:
#             print("output is 0")
#         else:
#             print("output is 1")
# gate=input("enter the gate")
# main(gate)


# challenge 12
# Write a program that will display all the factors of a number, entered by the user, that are bigger than 1. 
# Tell the user if the number they entered is a prime number
# list=[]
# def main(num):
#     for i in range(1, num):
#         if num%i==0:
#             list.append(i)
#     print("the factors are")
#     print(list)
#     if len(list)==1:
#         print("the number was prime number")
# num=int(input("enter number"))
# main(num)





# challenge 13
# Write a program for a game where the computer generates a random starting number between 20 and 30. 
# The player and the computer can remove 1,2 or 3 from the number in turns. Something like this...

# from random import randint
# def main():
#     secret=randint(20, 31)
#     print(f"the secret number is {secret} ")
#     while True:
#         y=int(input("enter number to subtract from random "))
#         secret=secret-y
#         print(f"the  number left is {secret}")
#         if secret<=0:
#             print("sorry sir! you lost")
#             break
#         computer=randint(1, 3)
#         secret=secret-computer
#         print(f"cpmputer enters {computer}")
#         print(f"the number left is {secret}")
#         if secret<=0:
#             print("You won! congratulation")
#             break
# main()





# challenge 14
# Write a program for a Higher / Lower guessing game 
# The computer randomly generates a sequence of up to 10 numbers between 1 and 13. 
# The player each after seeing each number in turn has to decide whether the next number is higher or 
# lower. If you can remember Brucie’s ‘Play your cards right’ it’s basically that. If you get 10 guesses right you win the game 

# from random import randint

# def main():
#     set=[]
#     count=0
#     while True:
#         number=randint(1, 13)
#         if number not in set:
#             print(f"the number is {number}")
#             enter=input("Higher(h) or Lower(l)")
#             second_number=randint(1, 13)
#             if enter=="l" and second_number not in set:
#                 print(f"the number is {second_number}")
#                 set.append(second_number)
#                 if second_number<number:
#                     count+=1
#                     pass
#                 else:
#                     print("you lost sir! thank you for playing")
#                     break

#             if enter=="h" and second_number not in set:
#                 print(f"the number is {second_number}")
#                 set.append(second_number)
#                 if second_number>number:
#                     count+=1
#                     pass
#                 else:
#                     print("you lost sir! Thank you for playing")
#                     break
#         if count==10:
#             print("congratulations you won!")
#             break
# main()




# challenge  15
# Write a program to count the number of words in a sentence. 
# The user enters a sentence. 
# The program responds with the number of words in the sentence.

# def main(sentence):
#     count=0
#     for i in sentence:
#         if i==" " or i==".":
#             count+=1
#     print("****************************************************************")
#     print(f" total number of words were {count}")

# sentence=input("enter the paragraph")
# main(sentence)




# challenge 16
# Guess the number game.  
# The computer selects a random number between 1 and 100. 
# The user keeps guessing which number the computer has chosen until they get it right. 
# The computer responds ‘got it’ or ‘too high’ or ‘too low’ after each guess. 
# After the user has guessed the number the computer tells them how many attempts they have made. 

# from random import randint
# def main(num):
#     count=0
#     while True:
#         number=int(input("guess the number"))
#         if number>num:
#             print("the guessing number too large")
#             count+=1
#         if number<num:
#             print("the guessing number was too small")
#             count+=1
#         if number==num:
#             print("congrates you got it!")
#             print(f"you tried {count} times")
#         if count==5:
#             print("Sorry you lost!")
#             print(f"the actual number wa {num}")
#             break
# num=randint(1, 100)
# main(num)




#  challenge 17
# grading system

# def main(subject1, subject2, subject3, subject4):
#     average=(subject1+subject2+subject3+subject4)/4
#     if average>=80:
#         print("your grade is A+")
#     elif average>=70:
#         print("your grade is A")
#     elif average>=60:
#         print("your grade is B")
#     elif average>=50:
#         print("your grade is C")
#     else:
#         print("sorry! you failed")

# main(80, 80, 100, 100)
    




# challenge 18
# Write a procedure(sub)  drawstars that will draw a sequence of spaces followed by a sequence of stars.
#  It should accept two parameters—the number of spaces and the number of stars
# class Draw:
#     def __init__(self, space, star):
#         self.space=space
#         self.star=star
#         Space="\t"*self.space
#         Star="*\t"*self.star 
#         print(Space+Star)
# line1=Draw(2, 3)
# line2=Draw(2, 3)
# line3=Draw(3, 1)
# line4=Draw(2, 3)
# line5=Draw(1, 5)
# line6=Draw(2, 3)






# challenge 19
# 









# challenge 20
# Create a Fibonacci sequence generator. ( The Fibo
# nacci sequence was originally used as a basic model 
# for rabbit population growth ). The Fibonacci sequence goes like this

# def main():
#     x=[0, 1]
#     for i in range(2, 50):
#         y=x[i-2]+x[i-1]
#         x.append(y)
#     count=int(input("enter a number"))
#     print(f"the number at {count} is {x[count]}")
# main()
    





# challenge 21
# Write a program that will store names into an array.  
# As a new name is entered it will be added to the end of the array. The user can keep adding names until they enter the dummy value ‘exit’ 
# Once this has been done the program will display any duplicate names.

# def main():
#     array=[]
#     duplicate=[]
#     while True:
#         name=input("enter the name")
#         if name=='exit':
#             break
#         if name in array:
#             duplicate.append(name)
#         array.append(name)

#     for i in array:
#         print(i)
#     if len(duplicate)!=0:
#         print("the duplicate names are")
#         for i in duplicate:
#             count=2
#             for j in range(len(duplicate)):
#                 if duplicate[j]==i and j!=duplicate.index(i):
#                     count+=1
#                     break
#             print(f"the name {i} appears {count} times")
            
# main()






# challenge 22
# Create a two-dimensional array of integers 10 by 10. 
# Fill the array with random numbers in the range 0 to 15 
# Display the array on the screen showing the numbers 
# from random import randint
# def main():
#     two=[]
#     for i in range(10):
#         one=[]
#         for j in range(10):
#             x=randint(1, 15)
#             one.append(x)
#         two.append(one)

#     print(two)
# main()







# challenge 23
# Create a simple treasure hunt game. Create a two-dimensional array of integers 10 by 10. 
# In a random position in the array store the number 1. repeat Get the user to enter coordinates where they think the treasure is. 
# If there is a 1 at this position display ‘success’. Until they find the treasure
# from random import randint

# def main():
#     treasure=[]
#     for i in range(10):
#         one=[]
#         for j in range(10):
#             x=randint(2, 15)
#             one.append(x)
#         treasure.append(one)
#     first=randint(0, 9)
#     second=randint(0, 9)
#     treasure[first][second]=1
#     total_treasure=0
#     for i in range(5):
#         print("please selcet the cordinates where you think the treasure is!")
#         Fc=int(input("enter first cordinate"))
#         Sc=int(input("enter second cordinate"))
#         if Fc>first:
#             print("your first cordinate was to high")
#             print("try again")
#         elif Fc<first:
#             print("your first cordinate was to low")
#             print("try again")
#         elif Fc==first:
#             print("Great! you got the first cordinate!")
#             for i in range(2):
#                 sc=int(input("enter second cordinate"))
#                 if sc==second:
#                     print("finally! you got treasure")
#                     print("%%%%%%%%")
#                     print("%%%%%%%%")
#                     print("%%%%%%%%")
#                     print("%%%%%%%%")
#                     print(f"the cordinates were {first} and {second} ")
#                     print("\n\n\n\n\n")
#                     total_treasure+=1
#                     first=randint(0, 9)
#                     second=randint(0, 9)
#                     treasure[first][second]=1
#                     break
    
                
#         if Sc>second:
#             print("your second cordinate was to high")
#             print("try again")
#         elif Sc<second:
#             print("your second cordinate was to low")
#             print("try again")
#         elif Sc==second:
#             print("Great! you got the second cordinate!")
#             for i in range(2):
#                 sc=int(input("enter first cordinate"))
#                 if sc==first:
#                     print("finally! you got treasure")
#                     print("%%%%%%%%")
#                     print("%%%%%%%%")
#                     print("%%%%%%%%")
#                     print("%%%%%%%%")
#                     print(f"the cordinates were {first} and {second} ")
#                     print("\n\n\n\n\n")
#                     first=randint(0, 9)
#                     second=randint(0, 9)
#                     treasure[first][second]=1
                    
#                     total_treasure+=1
#                     break
#         print("***********************************************")
#         print(f"you collect total of {total_treasure}")
#         print("************************************************")

# main()












# challenge 24
# Create a program with the following record structure 
# from random import randint

# def main():
#     home_team=[]
#     other_team=[]
#     team1=0
#     team2=0
#     while True:
#         get=input("do you want to add data or get record")
#         if get=="add":
#             for i in range(10):
#                 home=randint(1, 10)
#                 home_team.append(home)
#                 other=randint(1, 10)
#                 other_team.append(other)
#         if get=="record":
#             print("*****************************************")
#             print(f"the data for home team is {home_team} ")
#             print("\n\n")
#             print(f"the data for other team is {other_team} ")
#             print("******************************************")
#         if get=="show":
#             for i in home_team:
#                 team1=team1+i
#             for i in other_team:
#                 team2=team2+i
#             if team1>team2:
#                 print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n\n")
#                 print(f"Home team is the winner with {team1} points\n\n\n\n\n\n")
#                 print(f"Other team has {team2} points\n\n\n\n\n")
#             if team2>team1:
#                 print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n\n")
#                 print(f"Other team is the winnwe with {team2} points\n\n\n\n\n\n ")
#                 print(f"Home team has {team1} points\n\n\n\n\n")
#             if team1==team2:
#                 print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n\n")
#                 print("Both teams have same score\n\n\n\n\n\n")
#             break
# main()
    









# challenge 25/26
#  Dealer game
# from random import randint

# def main():
#     Player_one=100
#     dealer=100
#     while True:
#         player_card=0
#         dealer_card=0
#         bat=int(input("enter you bat"))
#         if bat>Player_one:
#             print("you dont have that much mony")
#             continue
#         while True:
#             card=randint(1, 10)
#             player_card+=card
#             print(f" your Card number is(( {card} )) and total number is (( {player_card} ))")
#             if player_card>21:
#                 print("%%%%%%%%%%%%%%%%%%%%%%\n\n\n\n")
#                 print("Soryy! you lost\n\n\n")
#                 Player_one-=bat
#                 dealer+=bat
#                 break


#             Next=input("you want card or not")
#             if Next=="card":
#                 pass
#             else:
#                 break
#         print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n\n ")
#         print(f"So, Player has total number of {player_card}\n\n\n ")
#         while True:
#             card=randint(1, 10)
#             dealer_card+=card
#             print(f"Dealer Card number is {card} and total number is (({dealer_card}))")
#             if dealer_card>player_card and dealer_card<22:
#                 print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\n")
#                 print("Dealer won the game\n\n")
#                 Player_one-=bat
#                 dealer+=bat
#                 break
#             if dealer_card>21:
#                 print("%%%%%%%%%%%%%%%%%%%%\n\n\n")
#                 print("dealer lost the game")
#                 Player_one+=bat
#                 dealer-=bat
#                 break
#             Next=input("next card")
#             if Next=="card":
#                 pass
            
#         print("%%%%%%%%%%%%%%%%\n\n\n\n")
#         print(f" Total Amount of Player is (({Player_one})) and dealer is (( {dealer}))\n\n\n\n\n")

#         want_to_play=input("do you want to play one more time")
#         if want_to_play=="yes":
#              pass
#         else:
#             break

# main()








# challenge 26
# The computer generates a 4 digit code The user types in a 4 digit code. Their guess. The computer tells them how many digits they guessed correctly
# from random import randint
# def main():
#     num_list=[]
#     number=randint(1000, 9999)
#     last_digit=number%10
#     Slast_digit=int((number-last_digit)/10)%10
#     Tlast_digit=int((((number-last_digit)/10)-Slast_digit)/10)%10
#     first_digit=int(number/1000)
#     num_list.append(first_digit)
#     num_list.append(Tlast_digit)
#     num_list.append(Slast_digit)
#     num_list.append(first_digit)
#     count=0
#     for i in range(12):
#         guess_list=[]
#         guess=int(input("enter you guess number"))
#         last_guess=guess%10
#         Slast_guess=int((guess-last_digit)/10)%10
#         Tlast_guess=int((((guess-last_digit)/10)-Slast_digit)/10)%10
#         first_guess=int(guess/1000)
#         guess_list.append(first_guess)
#         guess_list.append(Tlast_guess)
#         guess_list.append(Slast_guess)
#         guess_list.append(last_guess)
#         for i in guess_list:
#             if i in num_list:
#                 if num_list.index(i)==guess_list.index(i):
#                     print(f"{i} is correct \n\n")
#                     count+=1
#                 if num_list.index(i)!=guess_list.index(i):
#                     print(f" {i} is correct but placed incorrectly\n\n")
#             else:
#                 print(f"{i} is not in digit")
#         if guess==number:
#             print("%%%%%%%%%%%%%%%%%%%%%%%%\n\n\n\n")
#             print("Great! you got it")
#             print(number)
#             break
#     if guess!=number:
#         print(number)
#         print("you lost")




# main()







# challenge 27
# from random import randint
# player=input("enter word")
# word=[]
# for i in player:
#     word.append(i)

# def main():
#     count=0
#     a='*'*len(word)
#     Guess=[]
#     for j in a:
#         Guess.append(j)
#     while True:
#         guess_word=input("enter letter")
#         if guess_word in word:
#             x=word.index(guess_word)
#             Guess[x]=guess_word
#         else:
#             print("wrong guess")
#             count+=1
#         if count>5:
#             print("&&&&&&&&&&&&&")
#             print("\n\n\n\n Sorry! you lost\n\n\n\n\n")
#             break
#         if Guess==word:
#             print("%%%%%%%%%%%%%%%%%%%%\n\n\n")
#             print("congrates you won !\n\n\n\n\n\n")
#         print(Guess)
# main()
