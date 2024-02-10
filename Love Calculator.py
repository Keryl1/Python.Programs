print("The love calculator is calculating you score...")
name1 = input("What is your name?\n").lower()
name2 = input("What is your name?\n").lower()

t_count_1 = name1.count("t") + name2.count("t")
t_count_2 = name1.count("r") + name2.count("r")
t_count_3 = name1.count("u") + name2.count("u")
t_count_4 = name1.count("e") + name2.count("e")



true_count = str(t_count_1 + t_count_2 + t_count_3 + t_count_4)


l_count_1 = name1.count("l") + name2.count("l")
l_count_2 = name1.count("o") + name2.count("o")
l_count_3 = name1.count("v") + name2.count("v")
l_count_4 = name1.count("e") + name2.count("e")


love_count = str(l_count_1 + l_count_2 + l_count_3  + l_count_4)
love_count_str = true_count + love_count
love_count_int = int(love_count_str)

if love_count_int < 1 or love_count_int > 90: 
  print(f"Your score is {love_count_int}, you go together like coke and mentos. ")
elif love_count_int >= 40 or love_count_int <= 50:
  print(f"Your score is {love_count_int}, you are alright together. ")
else: 
  print(f"Your score is {love_count_int}. ")





 


