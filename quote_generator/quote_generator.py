import random

random_quotes = (
    "The only way to do great work is to love what you do.",
    "Stay hungry, stay foolish.",
    "Simplicity is the ultimate sophistication.",
    "Well done is better than well said.",
    "Fortune favors the bold.",
    "Knowledge is power.",
    "The unexamined life is not worth living.",
    "I think, therefore I am.",
    "Actions speak louder than words.",
    "Less is more.",
    "Know thyself.",
    "Everything flows.",
    "Do or do not. There is no try.",
    "The journey of a thousand miles begins with a single step.",
    "What we think, we become.",
    "Turn your wounds into wisdom.",
    "Energy and persistence conquer all things.",
    "The best way out is always through.",
    "Whatever you are, be a good one.",
    "A person who never made a mistake never tried anything new.",
    "Imagination is more important than knowledge.",
    "Life is what happens when you're busy making other plans.",
    "It always seems impossible until it's done.",
    "Be the change you wish to see in the world.",
    "The mind is everything. What you think, you become.",
)

def generate_random_quote():
    return random.choice(random_quotes)

print(generate_random_quote())