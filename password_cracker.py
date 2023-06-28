import hashlib
import subprocess

def hash_password(password, algorithm='sha256'):
    hash_object = hashlib.new(algorithm)
    hash_object.update(password.encode('utf-8'))
    return hash_object.hexdigest()

def generate_password_dictionary(min_length, max_length, charset):
    command = ['crunch', str(min_length), str(max_length), charset]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
    return process.stdout

def crack_password(hashed_password, password_dictionary, algorithm='sha256'):
    for line in password_dictionary:
        password = line.strip()
        hashed = hash_password(password, algorithm)
        if hashed == hashed_password:
            return password
    return None

def main():
    hashed_password = input("Enter the hashed password: ")

    password_dictionary_file = input("Enter the path to the password dictionary file (leave empty to generate): ")

    if password_dictionary_file:
        with open(password_dictionary_file, 'r') as file:
            password_dictionary = file.readlines()
    else:
        min_length = int(input("Enter the minimum password length: "))
        max_length = int(input("Enter the maximum password length: "))
        charset = input("Enter the character set for passwords (e.g., abcdef123): ")
        password_dictionary = generate_password_dictionary(min_length, max_length, charset)
    algorithm = input("Enter the hashing algorithm (default: sha256): ") or 'sha256'
    cracked_password = crack_password(hashed_password, password_dictionary, algorithm)
    if cracked_password:
        print("Password cracked:", cracked_password)
    else:
        print("Password not found in the dictionary.")

if __name__ == "__main__":
    main()
