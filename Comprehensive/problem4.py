# Problem Statement
# You are given a list of sentences. Your task is to perform the following operations using list comprehensions:

# Create a list of the number of words in each sentence.
# Create a list of sentences that contain a specific word (e.g., "Python").
# Create a list of the first word in each sentence.
# Create a list of the lengths of each sentence (in terms of the number of characters).

sentences = [
    "Python is a popular programming language.",
    "It is used for web development, data analysis, and more.",
    "Python is known for its readability and simplicity.",
    "Many developers prefer Python for its versatility.",
    "Learning Python can be fun and rewarding."
]

# Task 1
# Example output: [6, 8, 7, 7, 6]
# Create a list of the number of words in each sentence.

word_length = [len(sentence.split()) for sentence in sentences]
print(word_length)

# Task 2
# Example output: ['Python is a popular programming language.', 'Python is known for its readability and simplicity.', 'Many developers prefer Python for its versatility.', 'Learning Python can be fun and rewarding.']
# Create a list of sentences that contain a specific word (e.g., "Python").
key = "Python"
sentences_with_key = [sentence for sentence in sentences if key in sentence]
print(sentences_with_key)

# Task 3
# Example output: ['Python', 'It', 'Python', 'Many', 'Learning']
# Create a list of the first word in each sentence.
first_word = [sentence.split()[0] for sentence in sentences]
print(first_word)

# Task 4
# Example output: [41, 52, 53, 47, 39]
# Create a list of the lengths of each sentence (in terms of the number of characters).

word_len = [len(sentence) for sentence in sentences]
print(word_len)




