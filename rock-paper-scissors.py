#ftiakse ena rock-paper-scissors game
# to programma tha dialegei mia apo tis treis epiloges tuxaia
# sti sunexeia tha zitaei apo ton xristi na dialeksei mia apo tis 3 epiloges
#kai meta apo tis katalliles if statements tha mas deixnei poios kerdise
# kalo tha einai to programma na bgazei mnm ston xristi an exei dwsei alli epilogi aptis 3 vasikes
from random import randint



#YOUR CODE GOES HERE
# epiloges = ["rock", "paper", "scissors"]
# rand_ch = epiloges[randint(0,2)]
# pl_choice = input("Dialekse ena: ").lower()
# print(f" Epilogi upologisti: {rand_ch}, Epilogi paikti: {pl_choice}")
# if pl_choice == rand_ch:
#     print("draw")
# elif pl_choice == "rock":
#     if rand_ch == "paper":
#         print("computer wins")
#     else:
#         print("player wins")
# elif pl_choice == "paper":
#     if rand_ch == "scissors":
#         print("computer wins")
#     else:
#         print("player wins")
# elif pl_choice == "scissors":
#     if rand_ch == "rock":
#         print("computer wins")
#     else:
#         print("player wins")
# else:
#     print("prospathise ksana malaka")



#den tha termatizei mexri opaikths na kerdisei
epiloges = ["rock", "paper", "scissors"]
#niki_pc = True
pc_score = 0
pl_score = 0
while pc_score <3 or pl_choice <3:
    rand_ch = epiloges[randint(0,2)]
    pl_choice = input("Dialekse ena: ").lower()
    print(f" Epilogi upologisti: {rand_ch}, Epilogi paikti: {pl_choice}")
    if pl_choice == rand_ch:
        print("draw")
    elif pl_choice == "rock":
        if rand_ch == "paper":
            pc_score = pc_score+1
            print("computer wins")
        else:
            pl_score = pl_score+1
            print("player wins")
    elif pl_choice == "paper":
        if rand_ch == "scissors":
            pc_score = pc_score+1
            print("computer wins")
        else:
            pl_score = pl_score+1
            print("player wins")
    elif pl_choice == "scissors":
        if rand_ch == "rock":
            pc_score = pc_score+1
            print("computer wins")
        else:
            pl_score = pl_score+1
            print("player wins")
    else:
        print("prospathise ksana malaka")
