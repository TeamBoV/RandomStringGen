import random
import string

def generate_random_string(length):
    # Generate a random string of lowercase letters and digits
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def main():
    # Read the length of the string to generate from the command line arguments
    import sys
    if len(sys.argv) != 2:
        print("Usage: python random_string_generator.py LENGTH")
        return
    length = int(sys.argv[1])

    # Generate the random string
    random_string = generate_random_string(length)

    # Save the random string to a file
    with open('random_string.txt', 'w') as f:
        f.write(random_string)

if __name__ == '__main__':
    main()
