import random
from datetime import datetime

# NOVA - Your Smart Personal Assistant

name = input("🌸 Hi! I'm NOVA. What should I call you? ").strip()
if not name:
    name = "Friend"

score = 0

# Time-based greeting
hour = datetime.now().hour

if hour < 12:
    greeting = "Good morning"
elif hour < 17:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

print(f"\n✨ {greeting}, {name}!")
print("I'm NOVA, your smart personal assistant! 💜")
print("Type 'menu' to see what I can do.")

# Motivational quotes
quotes = [
    "Believe in yourself. You are capable of amazing things! 🌟",
    "Small steps every day lead to big results! 🚀",
    "Your only limit is your mind. 💜",
    "Dream big and work hard! 🌈"
]

# Jokes
jokes = [
    "Why did the computer go to the doctor? It had a virus! 😂",
    "Why was the math book sad? It had too many problems! 🤣",
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"
]

# Quiz questions
questions = [
    {
        "q": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "q": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Chennai", "C. New Delhi", "D. Hyderabad"],
        "answer": "C"
    },
    {
        "q": "Which language is used in this chatbot?",
        "options": ["A. Java", "B. Python", "C. C", "D. HTML"],
        "answer": "B"
    }
]

def show_menu():
    print("""
╔══════════ 🌟 NOVA MENU 🌟 ══════════╗
║ 1. Chat with me                     ║
║ 2. Check your mood                  ║
║ 3. Study motivation                 ║
║ 4. Play a mini quiz                 ║
║ 5. Tell me a joke                   ║
║ 6. Get a motivational quote         ║
║ 7. Mini calculator                  ║
║ 8. View your progress               ║
║ 9. Exit                             ║
╚═════════════════════════════════════╝
""")

def play_quiz():
    global score
    print("\n🧠 Welcome to NOVA's Quiz Zone!")
    quiz_score = 0

    selected = random.sample(questions, len(questions))

    for item in selected:
        print("\n" + item["q"])
        for option in item["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == item["answer"]:
            print("🎉 Correct! Amazing!")
            quiz_score += 1
        else:
            print("💡 Not quite! The correct answer is",
                  item["answer"])

    score += quiz_score
    print(f"\n🏆 You scored {quiz_score}/{len(selected)}!")
    print(f"Total points earned in this session: {score}")

def calculator():
    print("\n🧮 NOVA Mini Calculator")
    try:
        a = float(input("Enter first number: "))
        op = input("Choose +, -, *, or /: ").strip()
        b = float(input("Enter second number: "))

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                print("⚠️ Cannot divide by zero!")
                return
            result = a / b
        else:
            print("⚠️ Invalid operator!")
            return

        print("✨ Result:", result)

    except ValueError:
        print("⚠️ Please enter valid numbers.")

def mood_response(message):
    if any(word in message for word in
           ["happy", "great", "good", "excited", "awesome"]):
        print("💖 That's wonderful! Keep spreading your happiness!")
    elif any(word in message for word in
             ["sad", "lonely", "upset", "cry", "bad"]):
        print("🌷 I'm here to listen. Take a deep breath.")
        print("Remember, difficult days don't last forever.")
    elif any(word in message for word in
             ["stress", "tired", "anxious", "exam"]):
        print("🫶 Take a little break and focus on one thing at a time.")
    else:
        print("💜 Thank you for sharing your feelings with me!")

# Main chatbot loop
while True:
    user = input(f"\n{name}: ").strip().lower()

    if user in ["bye", "exit", "quit", "9"]:
        print(f"🌸 Goodbye, {name}! Keep shining! ✨")
        print(f"Your quiz points this session: {score}")
        break

    elif user in ["menu", "help"]:
        show_menu()

    elif user in ["hi", "hello", "hey"]:
        print(f"🌷 Hello, {name}! What's on your mind?")

    elif user in ["1", "chat"]:
        print("💬 I'm listening! You can talk to me.")
        print("Try asking how I am or telling me how you feel.")

    elif user in ["2", "mood"]:
        feeling = input("💖 How are you feeling today? ").lower()
        mood_response(feeling)

    elif user in ["3", "study", "motivation"]:
        print("📚 Study tip: Use the 25-minute focus method.")
        print("Study for 25 minutes, then take a 5-minute break.")
        print("You've got this! 🚀")

    elif user in ["4", "quiz"]:
        play_quiz()

    elif user in ["5", "joke"]:
        print("😂", random.choice(jokes))

    elif user in ["6", "quote"]:
        print("🌟", random.choice(quotes))

    elif user in ["7", "calculator", "calc"]:
        calculator()

    elif user in ["8", "progress", "score"]:
        print(f"🏆 {name}, your total quiz points: {score}")

    elif "your name" in user:
        print("I'm NOVA, your friendly personal assistant! 🤖")

    elif "thank" in user:
        print("💜 You're always welcome!")

    elif "secret" in user or "magic" in user:
        print("✨ You discovered NOVA's secret zone!")
        print("You're officially a NOVA explorer! 🚀")

    else:
        print("🤔 I'm still learning my responses!")
        print("Try 'menu' to discover my features.")