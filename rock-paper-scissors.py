
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
#     print("try again")



epiloges = ["rock", "paper", "scissors"]
#niki_pc = True
pc_score = 0
pl_score = 0
while pc_score <3 or pl_choice <3:
    rand_ch = epiloges[randint(0,2)]
    pl_choice = input("Choose One: ").lower()
    print(f" PC choice: {rand_ch}, Player choice: {pl_choice}")
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
        print("try again")
