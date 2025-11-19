from typing import List

def scissor_rock_paper_winner(user_moves,comp_moves):
    m = min(len(user_moves),len(comp_moves))
    user_count = 0
    comp_count = 0
    for i in range(m):
        if user_moves[i] == "scissor" and comp_moves[i] == "paper":
            user_count += 1
        elif user_moves[i] == "paper" and comp_moves[i] == "rock":
            user_count += 1
        elif user_moves[i] == "rock" and comp_moves[i] == "scissor":
            user_count += 1
        elif user_moves[i] == "paper" and comp_moves[i] == "scissor":
            comp_count += 1
        elif user_moves[i] == "rock" and comp_moves[i] == "paper":
            comp_count += 1
        elif user_moves[i] == "scissor" and comp_moves[i] == "rock":
            comp_count += 1
        else:
            return "Error"
    if user_count > comp_count:
        return "user"
    elif comp_count > user_count:
        return "computer"
    else:
        return "tie"

user_moves=['scissor','rock','paper','rock','rock']
comp_moves=['paper','scissor','rock','scissor','scissor']

print(scissor_rock_paper_winner(user_moves,comp_moves))
