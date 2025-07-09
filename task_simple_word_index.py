text = """apple and banana one apple one banana
          a red apple and a green apple"""

words_list = text.split()

for word in set(words_list):
    counter = words_list.count(word)
    print(f"{word:<10} - {counter}")