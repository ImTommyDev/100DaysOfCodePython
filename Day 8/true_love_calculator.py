def calculate_love_score(name1, name2):
    # Combine the names and convert to lowercase
    combined_names = (name1 + name2).lower()
    
    # Define the words to search for
    palabra_true = "true"
    palabra_love = "love"
    
    # Count the letters from "true"
    cont_true = 0
    for letter in palabra_true:
        cont_true += combined_names.count(letter)
    
    # Count the letters from "love"
    cont_love = 0
    for letter in palabra_love:
        cont_love += combined_names.count(letter)
    
    # Combine the counts to create the score
    love_score = int(str(cont_true) + str(cont_love))
    
    # Output the score
    print(f"Your love score is {love_score}")

calculate_love_score("Kanye West", "Kim Kardashian")