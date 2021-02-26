word1 = input("Fisrt word: ").lower()
word2 = input("Second word: ").lower()
char = input("Char: ").lower() 
text = " "+open("D:\My_Progs\python\python\individual_tasks\\task3\input.txt", "r").read().lower()
print(f"First word: {text.count(word1)}")
print(f"Second word: {text.count(word2)}")
print(f"Words together : {text.count(f'{word1} {word2}') + text.count(f'{word2} {word1}')}")
print(f"Words starts with char: {text.count(' '+char)}")
    