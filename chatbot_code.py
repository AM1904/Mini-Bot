import nltk
nltk.download('punkt')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import datetime
import math
import requests
import tkinter as tk
from tkinter import scrolledtext

# Chatbot Functions
def factorial(n):
    """Calculate factorial of a number."""
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)

def fibonacci(n):
    """Generate Fibonacci sequence up to the nth number."""
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def extract_numbers(tokens):
    """Extract numbers from a list of tokens."""
    return [int(token) for token in tokens if token.isdigit()]

def process_input(user_input):
    """Process user input and return chatbot response."""
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)

    # Check for greetings
    if any(word in tokens for word in ["hello", "hi", "hey"]):
        return "MINI BOT: Hello! How can I help you today?"

    # Respond to name-related queries
    elif "your" in tokens and "name" in tokens:
        return "MINI BOT: I am MINI BOT created using Python and NLTK."
    
    elif "great" in tokens or "good" in tokens or "okay" in tokens:
        return "Great, how can i assist you further?"
    
    # Provide today's date
    elif "date" in tokens:
        today = datetime.date.today()
        return f"MINI BOT: Today's date is {today.strftime('%A, %B %d, %Y')}."

    # Mathematical operations
    elif "add" in tokens or "addition" in tokens or "sum" in tokens:
        numbers = extract_numbers(tokens)
        if len(numbers) >= 2:
            return f"MINI BOT: The result is {sum(numbers)}."
        else:
            return "MINI BOT: Please provide at least two numbers for addition."
    elif "subtract" in tokens or "subtraction" in tokens or "difference" in tokens:
        numbers = extract_numbers(tokens)
        if len(numbers) == 2:
            return f"MINI BOT: The result is {numbers[0] - numbers[1]}."
        else:
            return "MINI BOT: Please provide exactly two numbers for subtraction."
    elif "multiply" in tokens or "multiplication" in tokens:
        numbers = extract_numbers(tokens)
        if len(numbers) >= 2:
            result = math.prod(numbers)
            return f"MINI BOT: The result is {result}."
        else:
            return "MINI BOT: Please provide at least two numbers for multiplication."
    elif "divide" in tokens or "division" in tokens:
        numbers = extract_numbers(tokens)
        if len(numbers) == 2:
            if numbers[1] == 0:
                return "MINI BOT: Division by zero is not allowed."
            else:
                return f"MINI BOT: The result is {numbers[0] / numbers[1]}."
        else:
            return "MINI BOT: Please provide exactly two numbers for division."
    elif "factorial" in tokens:
        numbers = extract_numbers(tokens)
        if len(numbers) == 1:
            return f"MINI BOT: The factorial of {numbers[0]} is {factorial(numbers[0])}."
        else:
            return "MINI BOT: Please provide exactly one number for the factorial."
    elif "fibonacci" in tokens:
        numbers = extract_numbers(tokens)
        if len(numbers) == 1:
            return f"MINI BOT: The first {numbers[0]} terms of the Fibonacci sequence are {fibonacci(numbers[0])}."
        else:
            return "MINI BOT: Please provide exactly one number for the Fibonacci sequence."

    # Jokes
    elif "joke" in tokens or "funny" in tokens:
        try:
            response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
            if response.status_code == 200:
                joke = response.json().get("joke")
                return f"MINI BOT: {joke}"
            else:
                return "MINI BOT: Sorry, I couldn't fetch a joke right now. Try again later!"
        except Exception:
            return "MINI BOT: Oops! Something went wrong while fetching a joke."

    elif user_input == "exit":
        return "MINI BOT: Goodbye! Have a great day!"

    else:
        return "MINI BOT: I’m not sure how to respond to that, but I can help you with the date, or math operations."

# GUI Implementation
def send_message():
    """Send user message to chatbot and display response."""
    user_message = user_entry.get()
    if user_message.strip():
        chat_display.insert(tk.END, f"You: {user_message}\n")
        response = process_input(user_message)
        chat_display.insert(tk.END, f"{response}\n\n")
        user_entry.delete(0, tk.END)

# Setting up the tkinter window
root = tk.Tk()
root.title("Chatbot GUI")

# Chat Display
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="normal", width=60, height=20, bg="lightyellow")
chat_display.pack(pady=10)
chat_display.insert(tk.END, "MINI BOT: Hello! I am an NLP-based chatbot. How can I assist you?\n\n you can ask me about date, basic mathematic operations and jokes")

# User Input and Send Button
frame = tk.Frame(root)
frame.pack(pady=10)

user_entry = tk.Entry(frame, width=50, font=("Arial", 12))
user_entry.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(frame, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(side=tk.RIGHT)

scroll = tk.Scrollbar(window)
chat_display.config(yscrollcommand=scroll.set)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Run the application
root.mainloop()

