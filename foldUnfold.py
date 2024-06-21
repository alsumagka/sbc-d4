from random import randint #nag import og randint from random library kay randint raman ang gamiton

user = input("FOLD OR UNFOLD? ").upper() #nangayo og user input nga ang data type kay string then gi convert into upper case ang user input
print(f"USER: {user}") #gi print ang user input gamit f-string

C2 = "FOLD" if randint(1, 2) == 1 else "UNFOLD" #random ang pag generate og result sa c2, e print ang fold if 1 then unfold if 2
print(f"C2: {C2}") #gi print ang result sa c2

C3 = "FOLD" if randint(1, 2) == 1 else "UNFOLD" #random ang pag generate og result sa c3, e print ang fold if 1 then unfold if 2
print(f"C3: {C3}") #gi print ang result sa c3

if user == C2 == C3: # nag condition ta nga kung same ang result sa user, c2, ug c3
    print("DRAW") # e print ang output kung na meet ang condition
elif user == C2 and user != C3: #nag elif condition kung same ang result sa user og c2 pero dili same sa c3
    print("C3 wins") #e print ang output kung na meet ang condition
elif user != C2 and user == C3: # nag elif condition kung dili same og result si user og c2 pero same si user og c3
    print("C2 wins") #e print ang output kung na meet ang condition
else: #else condition kay ang tig salo sa mga condition nga wala na meet
    print("User wins") #e print ang output sa mga wala na meet nga condition
