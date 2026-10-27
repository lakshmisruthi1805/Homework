question1 = "What is my name ?"
question2 = "What is my age ?"
question3 = "What is my school name ?"
question4 = "Where do i live ?"
question5 = "What are my favourite hobbies ?"
question6 = "What is my favourite sport ?"
question7 = "How many firends do i have ?"
question8 = "What do i want to become when i grow up ?"
question9 = "What is my favourite festival ?"
question10 = "What is my favourite colour ?"
question11 = "What foods do i love the most ?"
question12 = "What is my favourite season among the four ?"
question13 = "What is my favourite web series ?"
question14 = "Do i like to go to school ?"
question15 = "What matters to me the most ?"
answer1 = "My name is Lakshmi Sruthi."
answer2 = "My age is 14."
answer3 = "My school name is Jane Austen College."
answer4 = "I live in UK."
answer5 = "My hobbies are to dance and read books."
answer6 = "My favourite sport is badminton."
answer7 = "I have 20 friends."
answer8 = "I want to become a doctor when i grow up."
answer9 = "My favourite festival is Diwali."
answer10 = "My favourite colour is purple."
answer11 = "I love to eat chicken biryani,panipuri,pizza and dal and rice with mango pickle."
answer12 = "My favourite season is summer."
answer13 = "My favourite web series is The Family Man."
answer14 = "I love to go to school because i can meet my best friends and learn new things."
answer15 = "My family and my friends matter to me the most."
while True:
    prompt = input("Prompt: ")
    if prompt.lower().replace(" ","") in  question1.lower().replace(" ",""):
        print(f"Response: {answer1}")
    elif prompt.lower().replace(" ","") in  question2.lower().replace(" ",""): 
        print(f"Response: {answer2}")
    elif prompt.lower().replace(" ","") in  question3.lower().replace(" ",""): 
        print(f"Response: {answer3}")
    elif prompt.lower().replace(" ","") in  question4.lower().replace(" ",""):
        print(f"Response: {answer4}")
    elif prompt.lower().replace(" ","") in  question5.lower().replace(" ",""):
        print(f"Response: {answer5}")
    elif prompt.lower().replace(" ","") in  question6.lower().replace(" ",""):
        print(f"Response: {answer6}")
    elif prompt.lower().replace(" ","") in  question7.lower().replace(" ",""):
        print(f"Response: {answer7}")
    elif prompt.lower().replace(" ","") in  question8.lower().replace(" ",""):
        print(f"Response: {answer8}")
    elif prompt.lower().replace(" ","") in  question9.lower().replace(" ",""):
        print(f"Response: {answer9}")
    elif prompt.lower().replace(" ","") in  question1.lower().replace(" ",""):
        print(f"Response: {answer10}")
    elif prompt.lower().replace(" ","") in  question1.lower().replace(" ",""):
        print(f"Response: {answer11}")
    elif prompt.lower().replace(" ","") in  question1.lower().replace(" ",""):
        print(f"Response: {answer12}")
    elif prompt.lower().replace(" ","") in  question1.lower().replace(" ",""):
        print(f"Response: {answer13}")
    elif prompt.lower().replace(" ","") in  question1.lower().replace(" ",""):
        print(f"Response: {answer14}")
    elif prompt.lower().replace(" ","") in  question1.lower().replace(" ",""):
        print(f"Response: {answer15}")
    else: 
        print("Sorry I cannot answer this question. My knowledge is limited.")
