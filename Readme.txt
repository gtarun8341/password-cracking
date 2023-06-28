# Password Cracker

This is a password cracking script that allows you to crack hashed passwords using a password dictionary. It supports two modes: using a predefined password file or generating a password dictionary using the `crunch` tool.

## Installation

1. Clone the repository:

git clone https://github.com/gtarun8341/password-cracking.git

2. Navigate to the project directory:

3. Install the required dependencies using `pip`:

pip install -r requirements.txt

## Usage

1. Prepare the password dictionary file:

- If you have a predefined password file, place it in the project directory and name it `passwords.txt`.

- If you want to generate a password dictionary using `crunch`, follow these steps:

  - Open the `password_cracker.py` script in a text editor.

  - Uncomment the line that starts with `# generate_password_dictionary(...)`.

  - Customize the `min_length`, `max_length`, and `charset` variables according to your requirements.

  - Save the changes.

2. Run the script:

python password_cracker.py

3. Follow the on-screen prompts:

- Enter the hashed password you want to crack.

- If you have a predefined password file, press Enter without specifying the file path.

- If you want to generate a password dictionary using `crunch`, provide the required parameters when prompted.

- Optionally, specify the hashing algorithm (default: sha256).

4. Wait for the script to finish running. If a matching password is found in the dictionary, it will be displayed. Otherwise, a message will indicate that the password was not found.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


