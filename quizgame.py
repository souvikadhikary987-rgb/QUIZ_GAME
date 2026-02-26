questains=[('1.How many colours In indian flag..'),
           ('2.What Is the capital of west bengal..'),
           ('3.Which city Is known AS PINK CITY OF INDIA...')]
guesses=[]
options=[('A.1','B.2','C.3','D.4'),
         ('A.KOLKATA','B.DELHI','C.JAIPUR','D.MUMBAI'),
         ('A.KOLKATA','B.DELHI','C.JAIPUR','D.MUMBAI')]
answer=['C','A','C']
option_no=0
score=0
for q in questains:
    print(q)
    print("......................................")
    for opt in options[option_no]:
        print(opt)
    g=input("Enter your answer(A,B,C,D): ").upper()
    guesses.append(g)
    if g==answer[option_no]:
        print("CORRECT")
        score+=1
    option_no+=1
s=score/len(questains)*100
print(f"Correct answers are :" , answer, end="")
print()
print(f"Your answers are:",guesses ,end="")
print()
print(f"Score={s}%")