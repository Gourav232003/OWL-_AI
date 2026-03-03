from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'owl-ai-secret-key'

# Store messages in memory (for demo purposes)
messages = []

@app.route('/')
def home():
    """Home page with welcome message and navigation."""
    return render_template('home.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """Chat interface for interacting with Owl AI."""
    if request.method == 'POST':
        user_message = request.form.get('message', '').strip()
        if user_message:
            # Add user message
            messages.append({'role': 'user', 'content': user_message})
            # Generate AI response (placeholder)
            ai_response = generate_response(user_message)
            messages.append({'role': 'assistant', 'content': ai_response})
        else:
            flash('Please enter a message.', 'warning')
    return render_template('chat.html', messages=messages)

@app.route('/about')
def about():
    """About page with information about Owl AI."""
    return render_template('about.html')

@app.route('/clear')
def clear():
    """Clear chat history."""
    messages.clear()
    flash('Chat history cleared!', 'success')
    return redirect(url_for('chat'))

def generate_response(user_message):
    """Generate a simple AI response (placeholder for actual AI integration)."""
    import random
    from datetime import datetime

    user_message_lower = user_message.lower()

    # ──────────────────────────────────────────────
    # 1️⃣  Greeting Intent
    # ──────────────────────────────────────────────
    if any(w in user_message_lower for w in ('hello', 'hi', 'hey', 'howdy', 'greetings',
                                              'good morning', 'good afternoon', 'good evening')):
        return random.choice([
            "Hello! 🦉 I'm Owl AI. How can I help you today?",
            "Hi there! Ask me anything.",
            "Hey! 🦉 Welcome to Owl AI. What can I do for you?",
        ])

    # ──────────────────────────────────────────────
    # 7️⃣  Goodbye Intent  (checked early so "exit" / "bye" aren't caught elsewhere)
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('bye', 'goodbye', 'see you', 'take care', 'later', 'exit')):
        return random.choice([
            "Goodbye! 🦉 Have a great day!",
            "See you soon!",
            "Take care! Come back anytime. 👋",
        ])

    # ──────────────────────────────────────────────
    # 2️⃣  About Owl AI Intent
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('who are you', 'what is owl', 'tell me about yourself',
                                                'about owl', 'what are you', 'your name',
                                                'who made you', 'who created you', 'who built you', 'creator')):
        return random.choice([
            "I am Owl AI, your intelligent assistant designed to answer questions and help with tasks. 🦉",
            "I'm here to provide quick answers and useful information.",
            "I'm Owl AI — a demo assistant built with Flask and Python to showcase an interactive AI chat interface. 🛠️",
        ])

    # ──────────────────────────────────────────────
    # 3️⃣  Help Intent
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('help', 'what can you do', 'show commands',
                                                'capabilities', 'features', 'abilities')):
        return random.choice([
            ("You can ask me about Python, web development, AI, or general knowledge.\n"
             "Try asking: 'Explain Flask', 'What is Machine Learning?', or 'Tell me a fun fact!'"),
            ("Here are some things you can try:\n"
             "• Ask about programming — Python, Flask, loops, lists\n"
             "• Request a joke or fun fact\n"
             "• Ask for the current time or date\n"
             "• Say 'motivate me' for an inspirational quote\n"
             "• Ask me to do math — e.g. 'calculate 25 + 17'"),
        ])

    # ──────────────────────────────────────────────
    # 4️⃣  Programming Help Intent
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('python', 'flask', 'loop', 'variable',
                                                'function', 'list and tuple', 'tuple',
                                                'machine learning', 'web development',
                                                'code', 'programming', 'coding', 'developer',
                                                'explain', 'difference between')):
        # --- Specific sub-topics ---
        if 'loop' in user_message_lower:
            return ("A loop in Python is used to repeat a block of code. There are two types:\n"
                    "• for loop — iterates over a sequence (list, string, range, etc.)\n"
                    "• while loop — repeats as long as a condition is True.\n"
                    "Example:\n"
                    "  for i in range(5):\n"
                    "      print(i)")
        elif 'flask' in user_message_lower:
            return ("Flask is a lightweight Python web framework used to build web applications. "
                    "It provides tools for routing, templating (Jinja2), and request handling. "
                    "This very app is built with Flask! 🐍")
        elif 'list and tuple' in user_message_lower or ('list' in user_message_lower and 'tuple' in user_message_lower):
            return ("Lists and tuples both store ordered collections, but:\n"
                    "• Lists are mutable — you can change their items:  my_list = [1, 2, 3]\n"
                    "• Tuples are immutable — once created, they can't be changed:  my_tuple = (1, 2, 3)\n"
                    "Use tuples when data shouldn't change; lists when it should.")
        elif 'machine learning' in user_message_lower or 'ml' in user_message_lower:
            return ("Machine Learning is a branch of AI that lets computers learn from data "
                    "without being explicitly programmed. Common types:\n"
                    "• Supervised Learning (classification, regression)\n"
                    "• Unsupervised Learning (clustering, dimensionality reduction)\n"
                    "• Reinforcement Learning (reward-based learning)")
        elif 'variable' in user_message_lower:
            return ("A variable in Python stores data. You don't need to declare its type:\n"
                    "  name = 'Owl AI'\n"
                    "  age = 1\n"
                    "  is_smart = True\n"
                    "Python figures out the type automatically (dynamic typing).")
        elif 'function' in user_message_lower:
            return ("A function is a reusable block of code defined with the 'def' keyword:\n"
                    "  def greet(name):\n"
                    "      return f'Hello, {name}!'\n"
                    "Functions help keep your code organised and DRY (Don't Repeat Yourself).")
        else:
            return random.choice([
                ("I love talking about code! 🐍\n"
                 "Python tip: Use list comprehensions for concise loops —\n"
                 "  squares = [x**2 for x in range(10)]\n"
                 "Feel free to ask me more about programming!"),
                ("Web development with Python is awesome! Two popular frameworks:\n"
                 "• Flask — lightweight & flexible\n"
                 "• Django — batteries-included & scalable\n"
                 "Ask me about either one!"),
            ])

    # ──────────────────────────────────────────────
    # 5️⃣  Motivation Intent
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('motivat', 'inspir', 'quote', 'encourage',
                                                'tired', 'i feel', 'give me a quote')):
        return random.choice([
            "Keep going! Every expert was once a beginner. 💪",
            "Small progress is still progress. Don't stop now! 🚀",
            "\"The only way to do great work is to love what you do.\" — Steve Jobs 💡",
            "\"Believe you can and you're halfway there.\" — Theodore Roosevelt 🌟",
            "\"In the middle of every difficulty lies opportunity.\" — Albert Einstein 🔬",
            "\"A wise owl sat on an oak; the more he saw, the less he spoke.\" — Edward H. Richards 🦉",
            "\"It does not matter how slowly you go as long as you do not stop.\" — Confucius 🏃",
        ])

    # ──────────────────────────────────────────────
    # 6️⃣  Time / Date Intent
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('time', 'date', 'today', 'day')):
        now = datetime.now()
        if 'time' in user_message_lower:
            return f"The current time is: {now.strftime('%I:%M %p')} ⏰"
        else:
            return f"Today's date is: {now.strftime('%A, %B %d, %Y')} 📅"

    # ──────────────────────────────────────────────
    #  Gratitude
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('thank', 'thanks', 'appreciate')):
        return "You're welcome! I'm always happy to help. Is there anything else you'd like to know? 😊"

    # ──────────────────────────────────────────────
    #  Jokes
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('joke', 'funny', 'laugh', 'humor')):
        return random.choice([
            "Why do owls never go courting in the rain? Because it's too wet to woo! 🦉😄",
            "What do you call an owl that does magic tricks? Hoo-dini! 🎩",
            "Why don't owls study for tests? They prefer to wing it! 📚",
            "What's an owl's favourite subject? Owl-gebra! 🧮",
            "Knock knock! Who's there? Owl. Owl who? Owl be seeing you later! 👋",
        ])

    # ──────────────────────────────────────────────
    #  Fun Facts
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('fun fact', 'interesting fact', 'did you know', 'tell me something')):
        return random.choice([
            "🦉 Owls can rotate their heads up to 270 degrees!",
            "🌍 Honey never spoils — archaeologists have found 3,000-year-old honey that's still edible!",
            "🐙 An octopus has three hearts and blue blood.",
            "🚀 A day on Venus is longer than a year on Venus.",
            "💡 The first computer bug was an actual moth found in a Harvard relay computer in 1947.",
            "🎵 The shortest song ever recorded is 1.316 seconds long.",
            "🧬 Humans share about 60% of their DNA with bananas!",
        ])

    # ──────────────────────────────────────────────
    #  Weather
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('weather', 'temperature', 'forecast')):
        return "I can't check live weather yet, but I recommend checking a service like OpenWeatherMap or your phone's weather app! ☀️🌧️"

    # ──────────────────────────────────────────────
    #  Basic Math
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('calculate', 'math', 'add', 'subtract', 'multiply', 'divide', 'sum')):
        import re
        match = re.search(r'(\d+(?:\.\d+)?)\s*([+\-*/x×÷])\s*(\d+(?:\.\d+)?)', user_message)
        if match:
            a, op, b = float(match.group(1)), match.group(2), float(match.group(3))
            ops = {'+': a + b, '-': a - b, '*': a * b, 'x': a * b, '×': a * b,
                   '/': a / b if b else 'undefined (division by zero)',
                   '÷': a / b if b else 'undefined'}
            result = ops.get(op, 'unsupported operator')
            return f"🧮 {match.group(1)} {op} {match.group(3)} = {result}"
        return "I can do basic math! Try something like: 'calculate 25 + 17' or 'multiply 6 * 7'."

    # ──────────────────────────────────────────────
    #  Mood / How Are You
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('how are you', "how's it going", 'how do you feel')):
        return "I'm running smoothly, thank you for asking! 😊 How are you doing?"

    # ──────────────────────────────────────────────
    #  Music
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('music', 'song', 'playlist', 'listen')):
        return "I can't play music, but I hear owls are great at hooting in tune! 🎵🦉 Try Spotify or YouTube for your favourite tunes."

    # ──────────────────────────────────────────────
    #  Food
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('food', 'recipe', 'cook', 'eat', 'hungry')):
        return "Feeling hungry? I can't cook, but here's a quick idea: a classic grilled cheese sandwich never disappoints! 🧀🍞 What cuisine do you enjoy?"

    # ──────────────────────────────────────────────
    #  Games
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('game', 'play', 'bored', 'entertain')):
        return ("Let's play a quick game! Think of a number between 1 and 10… 🎲\n"
                "Got it? I'll guess… 7! Was I right? 😄\n"
                "(I'm not actually psychic — yet!)")

    # ──────────────────────────────────────────────
    #  Compliments
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('you are great', 'awesome', 'smart', 'amazing', 'love you', 'cool')):
        return "Aww, you're making me blush (if owls could blush)! Thank you — you're pretty amazing yourself! 🦉❤️"

    # ──────────────────────────────────────────────
    #  Apology
    # ──────────────────────────────────────────────
    elif any(w in user_message_lower for w in ('sorry', 'apolog')):
        return "No need to apologise! Everything's fine. How can I help you? 🙂"

    # ──────────────────────────────────────────────
    #  Catch-all Question
    # ──────────────────────────────────────────────
    elif '?' in user_message:
        return ("That's a great question! While I'm a demo version, I'm designed to help answer "
                "questions and assist with various tasks. Try asking: 'Explain Flask', "
                "'What is Machine Learning?', or 'Tell me a fun fact!'")

    # ──────────────────────────────────────────────
    #  Fallback
    # ──────────────────────────────────────────────
    else:
        return (f"I received your message: \"{user_message}\". I'm still learning! "
                "Try asking for a joke, a fun fact, the time, or type 'help' to see what I can do. 🦉")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
