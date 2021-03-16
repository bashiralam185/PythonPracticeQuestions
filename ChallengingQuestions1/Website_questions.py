
# Game wich generates auto numbers ,. each numbers has its own points and the player having more points will be winner
# ############################33THis KATA is intended as a small challenge for my students   (CODE WAR) #################################
# from random import randint
# import time
# def main():
#     Score_set=[]
#     for i in range(3):
#         Player_data={'name':'', 'N_kills':0, 'Assist':0, 'Demage':0, 'Healing':0, 'Streak':0, 'EN_kills':0}
#         Player_name=input("enter name of player")
#         print("\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\n\nPLEASE enter data of player")
#         normal_kill=randint(1, 9)
#         assist=randint(1, 20)
#         demage=randint(100, 500)
#         healing=randint(1, 40)
#         streak=randint(2, 10)
#         En_kill=randint(1, 5)
#         Player_data['name']=Player_name
#         Player_data['N_kills']=normal_kill
#         Player_data['Assist']=assist
#         Player_data['Demage']=demage
#         Player_data['Healing']=healing
#         Player_data['Streak']=streak
#         Player_data['EN_kills']=En_kill
#         print(f"PLAYER{i}  SCORE \n\n{Player_data}")
#         score_Board=(normal_kill*100)+(assist*50)+(demage*0.5)+(healing*0.5)+(2**streak)+(En_kill*500)
#         Score_set.append(score_Board)
#         time.sleep(1)
#         print("\nWAIT NEXT PLAYER IS PLAYING")
#         time.sleep(1)
#         print("\n\n\DONE\n\n")
#     if Score_set[0]> Score_set[1] and Score_set[0]>Score_set[2]:
#         print(f"\n\n\n%%%%%%%%%%%%%%%%%%%\n\n\n\nHERE is your winner \nPLAYER ONE with {Score_set[0]} Scores\n\n")
#         print(f"player two has {Score_set[1]} and player 3 has {Score_set[2]}")
#     elif Score_set[1]>Score_set[0] and Score_set[1]>Score_set[2]:
#         print(f"\n\n\n%%%%%%%%%%%%%%%%%%%\n\n\n\nHERE is your winner \nPLAYER TWO with {Score_set[1]} Scores\n\n")
#         print(f"player one has {Score_set[0]} and player 3 has {Score_set[2]}")
#     else:
#         print(f"\n\n\n%%%%%%%%%%%%%%%%%%%\n\n\n\nHERE is your winner \nPLAYER THREE with {Score_set[2]} Scores\n\n")
#         print(f"player one has {Score_set[0]} and player 2 has {Score_set[1]}")
# main()






# Your tast is to write a function which returns the sum of the following series upto nth term
# series=1+1/4+1/7+1/10.............. (################## CODE WAR ##########################)
# def main(terms):
#     denominator=1
#     sum=0.00
#     for i in range(1,terms+1):
#         series=i/denominator
#         sum+=series
#         denominator=denominator+3

#     print(f" the sum of the series is {sum}")
# main(int(input("enter number")))






# Two Tortoise named A and B start race. A has speed of 720 and B has 800. When A covers distance of 70 B just starts. Find the time B takes to Pass by A
# ################################## CODE WAR ############################################3

# def main(speed1, speed2):
#     distance=int(input("enter the distance traveled by B"))
#     Time=(distance/(speed1-speed2))*60
#     print(f"\n\n\n\nIt will take {Time} minutes to pass A")

# speed1=int(input("enter speed in meter/hour"))
# speed2=int(input("entetr speed of slower one in meter/hour"))
# main(speed1, speed2)
    







# abba=abab  TRUE      aabb=aaab  False
# ############################### CODE WAR####################################
# def main():
#     one=input("enter first word")
#     two=input("enter second word")
#     One=[]
#     Two=[]
#     for i in one:
#         One.append(i)
#     for i in two:
#         Two.append(i)
#     for i in One:
#         if i in Two:
#             Two.remove(i)
#     if len(Two)==0:
#         print("True")
#     else:
#         print(Two)
# main()





# trun a given rectangle to many squares
# ####################### CODE WAR ############################

# def main( lenght, width):
#     for i in range ( 1, lenght+1):
#         for j in range ( 1, width+1):
#             if (lenght/i==width/j):
#                 print(f"\n\n\n\n\n\ square of lenght {lenght/i} can be formed")
#                 print(f"total squares formed by this lenght are {i*j}\n\n\n\n\n")
# length=int(input("enter lenght"))
# width=int(input("enter width"))
# main(length, width)





# each of them has 100, 50, 25 ruppes. saller dont have money at first to give change back.
# can saller sell all tickets to all the people who are waiting with these money
# ############################# CODE WAR #################################

# def main(number):
#     Money_with_me=[]
#     money=[]
#     m=0
#     for i in range (number):
#         x=int (input("enter the amount!"))
#         money.append(x)

#     money.sort()
#     for i in range (0, len(money)):
#         if money[0]==25:
#             Money_with_me.append(25)
#             money.remove(25)
#             m+=1
#         elif money[0]==50:
#             if 25 in Money_with_me:
#                 Money_with_me.append(50)
#                 Money_with_me.remove(25)
#                 money.remove(50)
#                 m+=1
#             else:
#                 print("No")
#                 break
#         elif money[0]==100:
#             if 25 in Money_with_me:
#                 if 50 in Money_with_me:
#                     Money_with_me.append(100)
#                     Money_with_me.remove(25)
#                     Money_with_me.remove(50)
#                     money.remove(100)
#                     m+=1
#                 else:
#                     tf=[]
#                     for i in Money_with_me:
#                         if i==25:
#                             tf.append(i)
#                     if len(tf)>=3:
#                         m+=1
#                         money.remove(100)
#                         for i in range(3):
#                             Money_with_me.remove(25)
#                     else:
#                         print("No")

#             else:
#                 print("No")
#         else:
#             print("No")
#     if m==number:
#         print("Yes you can!")
    
# number=int(input("enter a number"))
# main(number)






# Given nXn array, return the array elemnts aaranged from outermost elements to the middle element traveling lokwise
# ####################################### CODE WAR ####################################################3


# def main(number):
#     array=[]
#     array_after=[]
#     i=0
#     while i<number:
#         array1=[]
#         j=0
#         while j<number:
#             x=int(input("enter element"))
#             array1.append(x)
#             j+=1
#         array.append(array1)
#         i+=1
#     k=0
#     x=0
#     while k<1:
#         if number==3:
#             while x<number+1:
#                 if x==0:
#                     for y in range(number):
#                         array_after.append(array[x][y])
#                 elif x==1:
#                     array_after.append(array[1 ][-1])
            
                    
#                 elif x==2:
#                     array_after.append(array[2][2])
#                     array_after.append(array[2][1])
#                     array_after.append(array[2][0])
#                 else:
#                     array_after.append(array[1][0])
#                     array_after.append(array[1][1])
#                     break
#                 # array_after.append(array[1][x])
        

                
#                 x+=1
#         if number==4:
#             while x<7:
#                 if x==0:
#                     for y in range(number):
#                         array_after.append(array[x][y])
#                 elif x==1:
#                     array_after.append(array[1][-1])
#                 elif x==2:
#                     array_after.append(array[2][-1])
#                 elif x==3:
#                     y=3
#                     while y>=0:
#                         array_after.append(array[x][y])
#                         y-=1
#                 elif x==4:
#                     array_after.append(array[2][0])
#                 elif x==5:
#                     y=0
#                     while y<3:
#                         array_after.append(array[1][y])
#                         y+=1
#                 else:
#                     array_after.append(array[2][2])
#                     array_after.append(array[2][1])
#                 x+=1
#         k+=1

#     print(array_after)
# number=int(input("enter number size of array"))
# main(number)










# Given the string representation of two integers and return the sum of those two integers
# ############################# CODE WAR #####################################

# def main( one, two):
#     sum=int(one)+int(two)
#     print(sum)
# one=input("ente number ")
# two=input("enter number")
# main(one, two)









# find a series A, B, C with A subseries. print which of the series has the greatest sum
###################################### CODE CHEF ####################################### 
# def main(number):
#     x=0
#     sequence=[]
#     while x<number:
#         num=int(input("enter number of elements\n\n\n"))
#         A=0
#         y=0
#         while y<num:
#             term=int(input("enter the number"))
#             terms=2**term
#             A+=terms
#             y+=1
#         sequence.append(A)
#         x+=1
#     Max=0
#     for i in sequence:
#         for j in sequence:
#             if sequence.index(i)==sequence.index(j):
#                 pass
#             elif i>j:
#                 Max=i
#     S=sequence.index(Max)+1
#     print(f"the term {S} has maximaum sum with {Max} ")
# number=int(input("enter number"))
# main(number)
    










# In group stage matches of the compitition , countirs are divieded into 8 groups . there will four teams in each group. these teams 
# in each group are ranked based on mathces they play against each other. each team plays two matches and top teams from each group
# will qualifiy to the final. Show who won the final

# import time
# from random import randint
# def Group1(team1, team2, team3, team4):
#     team1_score=0
#     team2_score=0
#     team3_score=0
#     team4_score=0
#     start=input("enter to start match")
#     if start=="":
#         print(f"\n\n\n%%%%%%%%%% MATCH between {team1} and {team2} has started%%%%%%%%%%%%%%%%%\n\n\n")
#         time.sleep(2)
#         score1=randint(1, 5)
#         team1_score=team1_score+(score1*3)
#         score2=randint(1, 5)
#         team2_score+=score2*3
#         if team1_score>team2_score:
#             team1_score=team1_score+3
#             print(f"congrates to {team1}")
#         else:
#             team2_score+=3
#             print(f"congrates to {team2}")


#         print("\n\n\n\n\n Match finished\n\n\n")
#         print(f"SCORE \n\n{team1}====>{team1_score}\n\n{team2} ====>{team2_score}")
#     start=input("enter to start match")
#     if start=="":
#         print(f"\n\n\n%%%%%%%%%% MATCH between {team3} and {team4} has started%%%%%%%%%%%%%%%%%\n\n\n")
#         time.sleep(2)
#         score3=randint(1, 5)
#         team3_score+=score3*3
#         score4=randint(1, 5)
#         team4_score+=score4*3
#         if team3_score>team4_score:
#             team3_score+=3
#             print(f"congrates to {team3}")
#         else:
#             team4_score+=3
#             print(f"congrates to {team4}")


#         print("\n\n\n\n\n Match finished\n\n\n")
#         print(f"SCORE \n\n{team3}====>{team3_score}\n\n{team4} ====>{team4_score}")
#     start=input("enter to start match")
#     if start=="":
#         print(f"\n\n\n%%%%%%%%%% MATCH between {team1} and {team4} has started%%%%%%%%%%%%%%%%%\n\n\n")
#         time.sleep(2)
#         score1=randint(1, 5)
#         print(team1_score)
#         team1_score=team1_score+(score1*3)
#         print(team1_score)
#         score4=randint(1, 5)
#         team4_score+=score2*3
#         if team1_score>team4_score:
#             team1_score=team1_score+3
#             print(f"congrates to {team1}")
#         else:
#             team4_score+=3
#             print(f"congrates to {team4}")


#         print("\n\n Match finished\n\n\n")
#         print(f"SCORE \n\n{team1}====>{team1_score}\n\n{team4} ====>{team4_score}")
#     start=input("enter to start match")
#     if start=="":
#         print(f"\n\n\n%%%%%%%%%% MATCH between {team3} and {team2} has started%%%%%%%%%%%%%%%%%\n\n\n")
#         time.sleep(2)
#         score3=randint(1, 5)
#         team3_score+=score1*3
#         score2=randint(1, 5)
#         team2_score+=score2*3
#         if team3_score>team2_score:
#             team3_score+=3
#             print(f"congrates to {team3}")
#         else:
#             team2_score+=3
#             print(f"congrates to {team2}")


#         print("\n\n Match finished\n\n\n")
#         print(f"SCORE \n\n{team3}====>{team3_score}\n\n{team2} ====>{team2_score}")

#     print("\n\n\n%%%%%%%%%%%%%%%%%%%%%%%% SO here we go to points Table %%%%%%%%%%%%%%%%%%%%%%%%")
#     print(f' {team1} ===========>{team1_score}')
#     print(f' {team2} ===========>{team2_score}')
#     print(f' {team3} ===========>{team3_score}')
#     print(f' {team4} ===========>{team4_score}')
#     time.sleep(3)            
#     qualifing_team=[]
#     if team1_score> team2_score and team1_score>team3_score and team1_score>team4_score:
#         qualifing_team.append(team1)
#         print(f"{team1} qualifies to finals")
#     elif team2_score> team1_score and team2_score>team3_score and team2_score>team4_score:
#         qualifing_team.append(team2)
#         print(f"{team2} qualifies to finals")
#     elif team3_score> team2_score and team3_score>team1_score and team3_score>team4_score:
#         qualifing_team.append(team3)
#         print(f"{team3} qualifies to finals")
#     elif team4_score> team2_score and team4_score>team3_score and team4_score>team1_score:
#         qualifing_team.append(team4)
#         print(f"{team4} qualifies to finals")
#     x=qualifing_team[0]
#     return x
# def main():

#     print("################## GROUP 1 MATCHES ##########################")
#     team1=0
#     team2=0
#     Team1=Group1('Pakistan', 'Bangladesh' ,'Aus', "END")
#     print("################## GROUP 2 MATCHES ##########################")
#     Team2=Group1('AFg', 'Ind', 'Nz', 'Ireland')
#     score1=randint(1, 5)
#     team1+=score1*3
#     score2=randint(1, 5)
#     team2+=score2*3
#     print("%%%%%%%%%%%%%%%%%%%%%%%% FINAL MATCH HAS STARTED%%%%%%%%%%%%%%%%%%%%%%%%%%")
#     time.sleep(3)
#     print(f"\n\n {Team1}========>{team1}")
#     print(f"\n\n {Team2}========>{team2}")
#     if team1>team2:
#         print(f"\n\n\n\n Congrates to {Team1} ")
#     else:
#         print(f"\n\n\n\n Congrates to {Team2}")
    

# main()










#there are n dianasore placed in line. the ith has i height.
# the rules for the game are as follows:
# initially the leftmost diansore has the ball. the dinosore tht has ball passes the ball to the nearest dianasore 
# tht is taller than him. the process contiunes untill the ball reaches to the tallest one. count the nummber of passes
# ###################################### CODE CHEF ##########################################
# from random import randint
# def dianasour(number):
    
#     dianasours_height=[]
#     x=0
#     while x<number:
#         height=randint(2, 45)
#         dianasours_height.append(height)
#         x+=1
#     number_of_times=0
#     j=0
#     for i in range(0, number):
#         if dianasours_height[j]<dianasours_height[i]:
#             number_of_times+=1
#             j=i
#     return number_of_times


# def main():
#     print("#################### HERE GOES TEAM ONE #########################")
#     team1=dianasour(50)
#     print(f"\n\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n team one has total of {team1} score")
#     print("\n###################### HERE GOES TEAM TWO #######################")
#     team2=dianasour(50)
#     print(f"\n\n\n %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n team two has total of {team2} score")
#     if team1>team2:
#         print("cogrates to team two")
#     else:
#         print("congrates to team one")
# main()





# putu sell M different friuts. he sell them in n buskets. find the busket having the lowest cost
# from random import randint
# def fruit(cost):
#     number_of_buskets=randint(1, 5)
#     total_cost=number_of_buskets*cost
#     return total_cost

# def main():
#     mango=fruit(50)
#     apple=fruit(38)
#     graps=fruit(55)
#     if mango<apple and mango<graps:
#         print(f"mango has the lowest cost {mango}")
#     elif apple<mango and apple<graps:
#         print(f"apples has the lowest cost {apple}")
#     else:
#         print(f"graps has the lowest cost {graps}")
# main()    











# the atm machine only accecpt transection multiple of 5. for every successfull transection the bank charges 0.5/ calculte total amout after withdrawl

# ####################### CODE CHEF ##################################33

# def main(total, transection):
#     if transection>total:
#         print("insufficient balance")
#     if transection%5!=0:
#         print("incorrect transection")
#     else:
#         remaing= (total-transection)-0.5
#         print("trancsection successfull")
#         print(f"your remaing balance is {remaing}")
# total=int(input("enter the total amout"))
# tra=int(input("enter the amout to transect"))
# main(total, tra)








# a company has communication system to communicate each other within a distacne of 1000 meter. if they are
# away by more than 1000 meter they can use the othe one which hs a range of 2000. find the number of employes who are in range
# from random import randint
# def main(num):
#     distance=[]
#     for i in range(0,num):
#         distance.append(randint(500, 2500))
#     Range=0
#     range_of_two=0
#     out_of_range=0
#     for i in distance:
#         if i<=1000:
#             Range+=1
#         elif i>1000 and i<=2000:
#             range_of_two+=1
#         else: 
#             out_of_range+=1
#     print(f" {Range} employes are in range of first one")
#     print(f"{range_of_two} employes are in range two")
#     print(f"{ out_of_range} emplyes are not in range")
# main(40)
    









# cheif belong to a very rich family ehich owns gold mines. Today he brought N golds coins and decieded to
# form triangle ucinf thesecoins. 
# he put one in 1st row, 2 in second row and so on. tell him what will be the height of triangle
# ############################  CODE CHEF ###################################################
# def main(number):
#     points=0
#     height=0
#     while True:
#         if number<=0:
#             break
#         else:
#             points+=1
#             if number>=points:
#                 height+=1
#                 number-=points

#             else:
#                 break
#     print(height)
# main(10)
        






# chef two and chef ten are playing a gaem with a number x . on one turn they can multilpy x by 2. the goal of the game is to make x divisible
# by 10. help the chefs find the smallest number of turns necessary to win fame  or determine it is impossible
# def main(number):
    
#     for i in range(number):
#         times=0
#         Not=0
#         number=int(input("enter a number"))
#         while True:
#             if number%10==0:
#                 break
#             else:
#                 number=number*2
#                 times+=1
#                 Not+=1
#             if Not>20:
#                 print("not possible")
#                 break
#         print(times)
# main(int(input("enter number")))





# scackdown wa hosted in the following years. for each test cases print a single line conataing the string was 
# hosted if snackdown was hosted in that year, else print not hosted
# ###################### PROJECT EULER ###########################333
# def main(year):
#     years=[2010, 2012, 2015, 2017, 2019]
#     one=0
#     for i in years:
#         if year==i:
#             print("HOSTED")
#             break
#         else:
#             one+=1
#     if len(years)==one:
#         print("NOT HOSTED")
# main(int(input("enter year")))









# the prime factoees of 13195 are 5, 7, 13 and 29.
#   what is the largest prime factor of any other number
# ################################# PROJECT EULER ########################################

# def main(number):
#     prime_factor=[]
#     for i in range(1, number):
#         if number%i==0:
#             prime=2
#             for j in range(2, i):
#                 if i%j==0:
#                     break
#                 else:
#                     prime+=1
#             if prime==i or prime==i-1:
#                 prime_factor.append(i)
#     if len(prime_factor)!=0:
#         print(prime_factor)
#         print(prime_factor[-1])
#     else:
#         print("no prime factors")
# main(int(input("enter a number")))
            






# a pralindromic number reads the same both ways. the largest palindrome made from product of two digits number is 9009 =91x99
# frind the largest palindrome made from the product of  3 digits numbers
# ###################################### PROJECT EULER #####################################################
# def main():
#     palindrome=[]
#     numbers=[]
#     for i in range(100, 1000):
#         for j in range(100, 1000):
#             y=i*j
#             if int(y/100000)==0:
#                 if int(y/10000)==y%10:
#                     s=int(y/1000)
#                     l=y%100
#                     if s%10==int(l/10):
#                         palindrome.append(y)
#             if int(y/1000000)==0:
#                 if int(y/100000)==y%10:
#                     s=int(y/10000)
#                     l=y%100
#                     if s%10==int(l/10):
#                         t=int(y/1000)
#                         x=y%1000
#                         if t%10==int(x/100):
#                             palindrome.append(y)
#                             # print(i)
#                             # print(j)
#     # print(palindrome)
#     # print("\n\n\n\n\n")
#     # print(numbers)

#     print(f"the largest pralindrome number is {palindrome[-1]}")
# main()







# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without out any reminder
# what is the smallest positive number that is evenly divided by all of the numbers from 1 to 20.
# ###############################  PROJECT EULER ################################################
# def main():
#     x=2501
#     while x>2501:
#         number=0
#         for i in range(1, 21):
#             if x%i==0:
#                 number+=1
#             else:
#                 break
#         if number==20:
#             print(x)
#             break
#         x+=1
# main()








# there is exactly one theroem that say a+b+c==1000. find the product of a*b*c
# ############################# PROJECT EULER ###############################

# def main():
#     numbers=[]
#     for i in range(1, 1000):
#         for j in range(1, 1000):
#             for k in range(1, 1000):
#                 if i+j+k==1000:
#                     numbers.append(i)
#                     numbers.append(k)
#                     numbers.append(j)
#                     break
#             if len(numbers)!=0:
#                 break
#         if len(numbers)!=0:
#             break
#     print(numbers[0]*numbers[1]*numbers[2])
# main()










# the sum of prime numbers below 10 is 2+3+5+7 is 17. find the sum of all the prime numbers below one million
# ################################## PROJECT EULER #############################################

# def main():
#     prime=[2, 3]
#     for i in range(4, 20000):
#         x=2
#         for j in range(2, i):
#             if i%j==0:
#                 break
#             else:
#                 x+=1
#         if x==i:
#             prime.append(i)
#     sum=0
#     for j in prime:
#         sum+=j
#     print(sum)
# main()







# the sequence of triangle numbers is genrated by adding the nutural numbers so the 7th triangle number would be 1+2+3+4+5+6+7=28
# its factores are 28+1, 2, 4, 7, 14, 28
# what is the value of the first triangle number to have over 100 divisors?
# ############################ PROJECT EULER ###################################
# def main(number):
#     j=1
#     while True:
#         sum=0
#         primes=[]
#         for i in range(1, j):
#             sum+=i
#         for i in range(1, sum+1):
#             if sum%i==0:
#                 primes.append(i)
#         if len(primes)>number:
#             print(j)
#             print(primes)
#             break
#         j+=1
# main(int(input("enter number")))










# the following iterative sequances is defined for the set of positive integers. n=n/2(even) and n=3n+1 (odd)
#  using the rule above and starting with 13, we generate 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
# it can be seen that starting at 13 finishes at 1 has 10 terms (collatz problem.)which starting number
# under one thousand has the longest chain
# ####################################### PROJECT EULER ##################################################
# def main():
#     largets=0
#     largest_factors=[]
#     num=0
#     for i in range(1, 1000):
#         numbers=[i]
#         while True:
#             if i==1:
#                 break
#             elif i%2==0:
#                 i=int(i/2)
#                 numbers.append(i)
#             else:
#                 i=(3*i)+1
#                 numbers.append(i)
#         if len(numbers)>largets:
#             largest_factors=numbers
#             largets=len(numbers)
#             num=numbers[0]

#     print(len(largest_factors))
#     print("\n\n\n")
#     print(largest_factors)
#     print(num)
# main()



# xaxis=[]
# x=4
# i=4
# while True:
#     if i==0:
#         break
#     elif x==i:
#         xaxis.append(x)
#         i-=1
#         # for j in range(i):
#         #     xaxis.append(1)
#     elif x%i==0:
#         for j in range(0,int(x/i)):
#             xaxis.append(i)
#         i-=1
#     else:
#         xaxis.append(i)
#         i-=1
# print(xaxis)
        











# starting in the top corner of 2x2 grid and olny being able to move to the right or down, there are exactly 6 routes to the bottom corner.
# how many such routes are there through a 20x20 grid
# ####################################### PROJECT EULER #####################################################33
# from itertools import permutations
# xaxis=[]
# x=10
# i=10      fdkd
# while True:
#     if i==0:
#         break
#     elif x==i:
#         xaxis.append(x)
#         i-=1
#         # for j in range(i):
#         #     xaxis.append(1)
#     elif x%i==0:
#         for j in range(0,int(x/i)):
#             xaxis.append(i)
#         i-=1
#     else:
#         xaxis.append(i)
#         i-=1
# print(xaxis)
# total=0
# for i in range(1, len(xaxis)+1):
#     y=list(permutations(xaxis, i))
#     for j in range(i):
#         sum=0
#         for k in y[j]:
#             sum+=k
#             if sum==10:
#                 total+=1
# print(total)
# print(total*2)





# 2 raise to power 15 is 32768 and the sum of digits is 26. what is the sum of the the digits of 2 rise to power of 1000
# ################################## PROJECT EULER #########################################
# def main(number):
#     power=2**number
#     digits=[]
#     while True:
#         y=power%10
#         power=int((power-y)/10)
#         digits.append(y)
#         if power==0:
#             break
#     sum=0
#     for i in digits:
#         sum+=i
#     print(sum)
    
# main(1000) 





# if the number 1 to 5 are written out in words in , one two three four are 3+3+5+4=15 in total.if all the numbers from 1 to thousands inclusive are
# written out in words, how many letters would be used?
# ####################################### PROJECT EULER ###########################################3
# def main(number):
#     print(number)
#     letter=input("enter number in words")
#     letters=[]
#     for i in letter:
#         if i==" " or i=="-":
#             pass
#         else:
#             letters.append(i)
#     print(len(letters))
# main(342)










# n! means n*n-1....2*1.  for example of 5!=120. sum of digits of 5! is 1+2+0=3, Find the sum of digits of 
# n facatorial number, 
# #################################### PROJECT EULER ###################################################
# def main(number, factorial):
#     while True:
#         if number==1:
#             break
#         else:
#             factorial=factorial*number
#             number-=1
#     Sum=0
#     while True:
#         if factorial==0:
#             break
#         else:
#             digit=factorial%10
#             Sum+=digit
#             factorial=(int(factorial-digit)/10)
#     print(Sum)
# main(50, 1)














# let d(n) be defined as the sum of proper divisors of n . if d(a)==b and d(b)==a where a!=b then a adn b ate 
# called amicable pairs. Evaluate such pairs under 10000
# def main():

#     for i in range(500, 1000):
#         digits=[]
#         for j in range(2,i ):
#             if i%j==0:
#                 digits.append(j)
#         if len(digits)!=0:
#             sum=1
#             Sdigits=[]
#             for k in digits:
#                 sum+=k
#             for l in range(2, sum):
#                 if sum%l==0:
#                     Sdigits.append(l)
#             Sum=1
#             for m in Sdigits:
#                 Sum+=m
#             if Sum==i:
#                 print(i)
#                 print(sum)
# main()











# a perfect numeber for which the sum of its  proper divisors is exacltuy equal to the number. all perfect numbers below 500
# #################################### PROJECT EULER ###############################################

# def main():
#     abdunt=[]
#     insufficient=[]
#     perfect=[]
#     for i in range(1,30):
#         divisors=[]
#         for j in range(2, i):
#             if i%j==0:
#                 divisors.append(j)
#         sum=1
#         for k in divisors:
#             sum+=k
#         if sum>i:
#             abdunt.append(i)
#         if sum<i:
#             insufficient.append(i)
#         if sum==i:
#             perfect.append(i)
#     print(f"abdunt={abdunt}")
#     print(f"insufficient={insufficient}")
#     print(f"perfect={perfect}")
# main()











# the fibnocci sequance is defined by recurrence relation.(0, 1, 1, 2, 3, 5, 8...) the 12th term is the first termto 
# contain three digits. what is the index of the first term in the sequance to contain 1000 digits
# ######################################  PROJECT EULER ######################################################
# def main():
#     sequence=[0, 1]
#     i=0
#     while True:
#         x=sequence[i]+sequence[i+1]
#         sequence.append(x)
#         i+=1
#         if int(x/1000)!=0:
#             print(x)
#             print(sequence.index(x))
#             break
# main()
        






# find all unique combinations of a**b if 2<a<50 and 2<b<50. sort the in accending order'
# ####################### PROJECT EULER ########################################


# def main():
#     items=[]
#     for a in range(2, 30):
#         for b in range(2, 30):
#             x=a**b
#             if x in items:
#                 pass
#             else:
#                 items.append(x)
#     items.sort()
#     print(items)
# main()







# surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits,
#  1634=1+6**4 + 3**4 + 4**4
# fin the sum of all the numbers that can written as the sum of fifth powers of their digits.
# ########################################### PROJECT EULER ################################
# number=[]
# for j in range(100, 10000):
#     list=[]
#     i=j
#     while True:
#         if i/10==0:
#             break
        
#         else:
#             x=i%10
#             list.append(x)
#             i=int((i-x)/10)
            
#     unique=0
#     for num in list:
#         unique+=(num**5)

#     if unique==j:
#         number.append(j)
# print(number)
        








# in the uk the currency is make up of pound(@) and pence(p). there are eight coins in genreal circulation.
# 1p, 2p, 3p, 5p, 10, 20p , 50p and 1@=100p
# it is possible to make @2 in the following way
# 1*@2 + 50p + 20p*2 + 5p + 2p + 3P
# how many different ways can be made using any number of coins??
############################# PROJECT EULER ###################################
# def main():
#     combinatins=[]
#     numbers=[1, 2, 3, 5, 10, 20, 50, 100]
#     for num in numbers:
#         numb=[]
#         for i in range(198):
#             for l in range(70):
#                 for m in range(19):
#                     for n in range(8):
#                         for o in range(1):
#                             euro=(num*i)+(num*l)+(num*m)+(num*n)+(num*o)
#                             if euro==198:
#                                 numb.append(i*num)
#                                 numb.append(l*num)
#                                 numb.append(m*num)
#                                 numb.append(n*num)
#                                 numb.append(o*num)
#                                 break
#         if len(numb)!=0:
#             for i in numb:
#                 combinatins.append(i)
#     print(int(len(combinatins)/5))




# main()







# we shall say that an n-digit number is pandigital if it makes use of all the digits from 1 to n exactlty once. eg 5 digit
# numger 15423 is 1 through 5.
# the product 7254 is unsual as the identy 39*186=7254 containg multipicant , multiplier and product is 1 thought
#  9 pandigital. find other pandigital whose multipicant, multiplier and poroduct makes pandigital 
# ############################  PROJECT EULER ####################################3
# def main():

#     for t in range(30, 98):
#         i=t
#         list=[]
#         for u in range(186, 187):
#             j=u
#             x=i*j
#             m=x
#             while m>0:
#                     if i==0:
#                         pass
#                     else:
#                         b=i%10
#                         i=int((i-b)/10)
#                         list.append(b)
#                     if j==0:
#                         pass
#                     else:
#                         c=j%10
#                         j=int((j-c)/10)
#                         list.append(c)
#                     a=m%10
#                     list.append(a)
#                     m=int((m-a)/10)
#             list.sort()
#             k=0
#             for o in range(len(list)-1):
#                 if list[o]==list[o+1]-1:
#                     k+=1
#             if k>=8:
#                 print(f"{t} *{u} =={x}")
# main()

            





# 145 is a curious number as 1!+4!+5!=145.
# find the sum of all numbers which are equal to the sum of the factorial of their digits.
# ############################ PROJECT EULER ##################################

# def main():
#     Sum=0
#     numbers=[]
#     for i in range(1, 1000000):
#         x=i
#         digits=[]
#         while True:
#             if x==0:
#                 break
#             else:
#                 y=x%10
#                 digits.append(y)
#                 x=int((x-y)/10)
#         sum=0
#         for j in digits:
#             fact=1
#             while True:
#                 if j==0:
#                     break
#                 else:
#                     fact=fact*j
#                     j-=1
#             sum+=fact
#         if sum==i:
#             print(i)
#             numbers.append(i)
#     for i in numbers:
#         Sum+=i
#     print(f" the sum is {Sum}")
# main()
        






# the number 73 is uniqe becaue any all its digits are prime. find all the numbers under 1000 which has must be prime and 
# must have prime digits
# ####################### PROJECT EULER ############################

# def main():
#     for i in range(1000):
#         prime_numbers=[]
#         prime=2
#         for j in range(2, int(i/2)+1):
#             if i%j==0:
#                 break
#             else:
#                 prime+=1
#         if prime==int(i/2)+1:
#             prime_numbers.append(i)
#         if len(prime_numbers)!=0:
#             digits=[]
#             for num in prime_numbers:
#                 while True:
#                     if num==0:
#                         break
#                     else:
#                         y=num%10
#                         digits.append(y)
#                         num=int((num-y)/10)
#             Prime=[]
#             for Num in digits:
#                 two=2
#                 for m in range(2, int(Num/2)+1):
#                     if Num%m==0:
#                         break
#                     else:
#                         two+=1
#                 if two==int(Num/2)+1:
#                     Prime.append(Num)
#             if len(Prime)==len(digits):
#                 print(i)
# main()







# take the number 192 and multiply it each of 1, 2, 3 we get 192, 384, 576. By concatanating each product we get the 1 to 9 pandigital.
# what is the largest 1 to 9 panadigital 9-digit numer that can be formed as the number of concatenated prodcuts

# def main():

#     for num in range(1, 500000):
#         digits=[]
#         for i in range(1,10):
#             x=num*i
#             while True:
#                 if x==0:
#                     break
#                 else:
#                     one=x%10
#                     digits.append(one)
#                     x=int((x-one)/10)
#             if len(digits)>=9:
#                 break
#         digits.sort()
#         sum=0
#         for j in range(8):
#             if digits[j]==digits[j+1]-1:
#                 sum+=1
#         if sum ==8:
#             print(num)
#             for s in range(1, i+1):
#                 print(s)
# main()









# if p is the perimeter of a right triangle with the lenght of sides a, b, c there are exaclty three solutios for p=120
# (20, 48, 52)(24, 45, 51)(30, 40, 50). for which value of p<1000 is the number of solutions maximised?

# def main():
    
#     for m in range(120, 121):
#         max=0
#         min=0
#         value=0
#         for a in range(1, 51):
#             for b in range(1, 54):
#                 for c in range(1, 54):
#                     if c**2==(a**2)+(b**2) and a+b+c==120:
#                         min+=1
#         if max<min:
#             max=min
#             value=m
#     print(f"the value is {value} and it has {max/2} number of arrangnet")

# main()

# 