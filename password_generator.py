import random        #to generate random character
import string        #for character set

## Define Character Set

def generate_password(length,use_uppercase,use_lowercase,use_digit,use_symbol):
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase    ##contains all uppercase letters
    if use_lowercase:
        characters += string.ascii_lowercase    ##contains all lowercase letters
    if use_digit:
        characters += string.digits    ### contains all the digits (from 0 to 9)
    if use_symbol:
        characters += string.punctuation   ### contains all symbols

    if not characters:
        return "Please select at least one character set"
    
    ### Generate Password using random.choice()
    
    password = "".join(random.choice(characters) for i in range(length))

    return password

### Getting User Input 

def main():
    try:
        length = int(input("Enter password Length :"))
        if length<=0:
            print("Password must be positive integer.")
            return
    except ValueError:
        print("Invalid input. please enter a number.")
        return
    
    use_uppercase = input("Include Uppercase letters?(yes/no) :").lower()=="yes"
    use_lowercase = input("Include Lowercase letters?(yes/no) :").lower()=="yes"
    use_digit = input("Include Digits?(yes/no) :").lower()=="yes"
    use_symbol = input("Include Symbol?(yes/no) :").lower()=="yes"


    ### Generate and Display password

    password = generate_password(length,use_uppercase,use_lowercase,use_digit,use_symbol)

    print("Generated Password is :", password)

if __name__=="__main__":
    main()