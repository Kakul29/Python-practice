print("🎮 Welcome to KBC!")
print("You will be asked questions. Each correct answer = ₹10,000\n")

questions = [
    "1. What is India's capital?\nA. Delhi\nB. Chandigarh\nC. Jaipur\nD. Mumbai",
    "2. What is the largest state in India?\nA. Uttar Pradesh\nB. Maharashtra\nC. Kerala\nD. Rajasthan",
    "3. Who is the father of the nation?\nA. Nehru\nB. Modi\nC. Mahatma Gandhi\nD. Jinnah",
    "4. Which prime number comes after 11?\nA. 12\nB. 13\nC. 17\nD. None"
]

answers = ["delhi", "rajasthan", "mahatma gandhi", "13"]

money = 0

for i in range(len(questions)):
    print("\n" + questions[i])
    
    user_ans = input("Enter your answer: ").strip().lower()
    
    if user_ans == answers[i]:
        print("✅ Correct!")
        money += 10000
    else:
        print("❌ Wrong answer. Game over!")
        break

print(f"\n💰 You won ₹{money}")
