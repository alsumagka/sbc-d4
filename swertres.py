from random import randint #nag import og randint from random library kay randint raman ang gamiton


user = input("PLACE YOUR BET (e.g., '1 2 3'): ").split() #nangayo og user input unya gi gamitan og split function
users = [int(x) for x in user] # gi sulod sa list ang user input unya gi gamitan og for loop para e iterate ang user input 1 by 1
result = [randint(0, 9) for _ in range(3)] #nag generate dayun og random integer sulod sa list unya gi gamitan og for loop gihapon

print(f"BET: {' '.join(map(str, users))}") # nag print sa user bet unya nag gamit og join function para ma convert ang list into a single string unya gi gamitan og map para e convert ang integer into string
print(f"RESULT: {' '.join(map(str, result))}") # same og explaination sa taas

if user == result: # if condition kung si user is same og output sa result
    print("You Win!") # nag print kung na meet ang condition
elif sorted(users) == sorted(result): #elif condition kung si user kuno is same og numbers sa result pero dili mao ang plastar, pero nag gamit og sorted nga function para e sort ang plastar in an ascending order. ang 3 2 1 mahimong 1 2 3 
    print("You partially win!") # e print dayun ang output
else: # else condition kay ang tig salo sa mga conditio nga wala na meet
    print("You lose!") # e print dayun ang output sa else
