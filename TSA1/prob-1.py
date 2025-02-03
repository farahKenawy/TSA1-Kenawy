def count_characters(input_string):
    vowels = consonants = spaces = other_chars = 0
    vowel_set = "aeiouAEIOU"

    for char in input_string:
        if char in vowel_set:
            vowels += 1
        elif char.isalpha():
            consonants += 1
        elif char.isspace():
            spaces += 1
        else:
            other_chars += 1

    print("Character Counts:")
    print(f"- Vowels: {vowels}")
    print(f"- Consonants: {consonants}")
    print(f"- Spaces: {spaces}")
    print(f"- Other Characters: {other_chars}")

while True:
    user_input = input("Enter a string (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    count_characters(user_input)
