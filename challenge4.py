import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import json, os, re, random
from pydub import AudioSegment

# Encryption algorithm for caeser cipher
# Key is number between 1 and 25 (inc.)
def encrypt(plain_text, key):
    encrypted_text = ""
    plain_text = plain_text.lower()
    for char in plain_text:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            encrypted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

# Decryption algorithm for monoalphabetic substitution cipher
def decrypt(cipher_text, key):
    # Have to invert key to decrypt
    pass


# Function to create alphabet sheet, true is encrypted, false is plaintext
def generate_alphabet_sheet(encrypted=True):
    if encrypted:
        letters_dir = "./challenge_4_cipher_components"
    else:
        letters_dir = "./challenge_4_alphabet_components"

    # If directory doesn't exist then display while compiling
    if not os.path.isdir(letters_dir):
        print(f"[ERROR] '{letters_dir}' not found.")

    # Creates alphabet sheet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    fig, axes = plt.subplots(4, 7, figsize=(12, 6))

    letters_dir_list = []
    for letter in alphabet:
        letters_dir_list.append(letters_dir + f"/Letter_{letter}.png")

    # Flatten axes for easy iteration
    axes = axes.ravel()

    num_letters = len(alphabet)

    # Loop only through the alphabet
    for i, ax in enumerate(axes[:num_letters]):
        letter_img = mpimg.imread(letters_dir_list[i])
        ax.imshow(letter_img)
        ax.axis("off")

    # Once images run out hide empty subplots
    for ax in axes[num_letters:]:
        ax.set_visible(False)

    plt.tight_layout()
    plt.close()

    return fig

def generate_cipher_puzzle_fig(input_string):
    ### Turns "survived" or "deceased" into an image of the puzzle
    cipher_letters_dir = "./challenge_4_cipher_components"

    cipher_letters_dir_list = []
    for letter in input_string:
        cipher_letters_dir_list.append(cipher_letters_dir + f"/Letter_{letter}.png")

    fig, axes = plt.subplots(1, len(input_string), figsize=(12, 6))

    for i, ax in enumerate(axes):
        coded_letter_img = mpimg.imread(cipher_letters_dir_list[i])
        ax.imshow(coded_letter_img)
        ax.axis("off")

    plt.tight_layout()
    plt.close()

    return fig


# For challenge-4 (A Strange Sound) turn plaintext into morse audio segment
def generate_morse_audio_segment(morse_component_dir, input_string):
    # If directory doesn't exist then display while compiling
    if not os.path.isdir(morse_component_dir):
        print("[ERROR] 'challenge_4_morse_components' not found.")

    output_message = AudioSegment.silent(duration=0)

    for char in input_string:
        char_path = morse_component_dir + f"/{char.upper()}_morse_code.wav"
        output_message += AudioSegment.from_wav(char_path)
        output_message += AudioSegment.silent(duration=2000)

    return output_message

# For challenge-4 (A Strange Sound) hint turn plaintext into morse text
def generate_morse_text(input_string):
    morse_dict = {
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",
        "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
        "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "O": "---",
        "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",  "Y": "-.--",
        "Z": "--.."
    }
    output_morse = ""

    for char in input_string:
        output_morse += morse_dict[char.upper()]
        output_morse += (' ' * 3)

    print(output_morse)
    return output_morse


def generate_key():
    return random.randint(1,25)

def convert_dataframe_to_table(df):
    font_size = 20

    num_rows = df.shape[0]
    num_columns = df.shape[1]

    fig, ax = plt.subplots(figsize=(num_rows, num_columns))
    ax.axis("off")

    # Add custom labels for the player
    custom_labels = ["Name", "Class", "Sex", "Survival"]

    # Create table
    table = ax.table(
        cellText=df.values,
        colLabels=custom_labels,
        loc="center"
    )

    # Bold header row
    for col in range(len(df.columns)):
        table[(0, col)].get_text().set_weight("bold")

    table.auto_set_column_width(col=list(range(len(df.columns))))

    table.scale(xscale=1, yscale=2)

    table.auto_set_font_size(True)
    table.set_fontsize(font_size)

    return fig



def generate_challenge_4(df):
    # Generate challenge 4 - Guest of the Deep

    story_text = """

    The Captain has called you and your group to the deck of the ship with an 
    urgent mission. Telegrams have been intercepted from the ship's Marconi machine
    and it appears there is a stowaway on board! Unfortunately, the dastardly 
    stowaway has managed to scramble one of the telegrams using a mysterious code. 
    The Captain has created a list of 20 suspects. Can you decipher the letter and
    obtain the identity of the suspect before they get away?!

    """

    puzzle_img_dir = "./challenge_4_puzzle_images"

    # The columns to check for uniqueness
    columns_to_check = ['Pclass', 'Sex', 'Survived']

    # Randomly choose the stowaway
    stowaway = df.sample(1)

    # Find the indices in the relevant categories that don't match that of the stowaway
    # So that the stowaway is unique from the clues presented
    idx_not_same_as_stowaway = ~(df[columns_to_check].eq(stowaway[columns_to_check]).all(axis=1))

    # Select rows that are not identical to the stowaway in the clue columns
    possible_rows = df[idx_not_same_as_stowaway]

    # Randomly pick 20 rows from these possible rows
    suspects = possible_rows.sample(n=20)

    # Insert the stowaway randomly into the list of suspects
    suspects = pd.concat([suspects, stowaway]).sample(frac=1, ignore_index=True).reset_index(drop=True)

    # Only interested in some of the features
    suspects = suspects[["Name", "Pclass", "Sex", "Survived"]]
    stowaway = stowaway[["Name", "Pclass", "Sex", "Survived"]]

    # Remove anything in brackets from the name column - makes the names easier to display
    suspects["Name"] = suspects["Name"].str.replace(r"\(.*?\)", "", regex=True)
    stowaway["Name"] = stowaway["Name"].str.replace(r"\(.*?\)", "", regex=True)

    # Replace 0 with deceased
    suspects["Survived"] = suspects["Survived"].replace(0, "Deceased")
    stowaway["Survived"] = stowaway["Survived"].replace(0, "Deceased")

    # Replace 1 with survived
    suspects["Survived"] = suspects["Survived"].replace(1, "Survived")
    stowaway["Survived"] = stowaway["Survived"].replace(1, "Survived")

    # Final stowaway name for the user to guess
    stowaway_name = stowaway['Name'].iloc[0]

    # Generate suspect table
    suspect_table = convert_dataframe_to_table(suspects)

    # Save suspect table
    suspect_table_img_path = os.path.join(puzzle_img_dir, "suspect_table.png")
    suspect_table.savefig(suspect_table_img_path, dpi=300, bbox_inches="tight")

    ### Letters from a stowaway puzzle generation
    # Get the stowaway passenger class and convert to int
    stowaway_class = int(stowaway["Pclass"].iloc[0])

    # Generate stowaway line
    if stowaway_class == 1:
        stowaway_class_line = "It's quite comfortable here in first class! "
    elif stowaway_class == 2:
        stowaway_class_line = "I like it here in second class! "
    elif stowaway_class == 3:
        stowaway_class_line = "It's a bit cramped here in third class! "
    else:
        print("Error generating stowaway line")
        stowaway_class_line = "Error generating stowaway line"

    header = """
R.M.S. TITANIC
MARCONI WIRELESS SERVICE
APRIL 12, 1912
"""

    plaintext_letter_llm_response = "plaintext_letter_llm_response.json"
    encrypted_letter_llm_response = "encrypted_letter_llm_response.json"

    try:
        with open(plaintext_letter_llm_response, 'r') as file:
            data = json.load(file)
            plaintext_body = data.get('response')
            # LLMs like to do \n\n replace with \n
            plaintext_body = re.sub(r'\n+', '\n', plaintext_body)
    except:
        print(f"File '{encrypted_letter_llm_response}' not found.")

    try:
        with open(encrypted_letter_llm_response, 'r') as file:
            data = json.load(file)
            encrypted_body = data.get('response')
            # LLMs like to do \n\n replace with \n
            encrypted_body = re.sub(r'\n+', '\n', encrypted_body)
    except:
        print(f"File '{encrypted_letter_llm_response}' not found.")

    plaintext_letter = header + plaintext_body
    encrypted_letter = header + stowaway_class_line + encrypted_body

    # Encrypt the letter
    key = generate_key()
    # Don't encrypt while testing
    # encrypted_letter = encrypt(encrypted_letter, cipher_key)

    caeser_hint = f"Caeser Cipher with key: {key}"

    ### Bill Cipher challenge
    # Generate encoded message
    encoded_key_fig = generate_cipher_puzzle_fig(stowaway["Survived"].iloc[0])
    encoded_key_img_path = os.path.join(puzzle_img_dir, "bill_cipher_img.png")
    encoded_key_fig.savefig(encoded_key_img_path, dpi=300, bbox_inches="tight")

    # Generate encoded alphabet to display to the user as part of puzzle
    encoded_alphabet_fig = generate_alphabet_sheet(True)
    encoded_alphabet_img_path = os.path.join(puzzle_img_dir, "encoded_alphabet_img.png")
    encoded_alphabet_fig.savefig(encoded_alphabet_img_path, dpi=300, bbox_inches="tight")

    # Generate plaintext alphabet to show to user as a hint
    plaintext_alphabet_fig = generate_alphabet_sheet(False)
    plaintext_alphabet_img_path = os.path.join(puzzle_img_dir, "plaintext_alphabet_img.png")
    plaintext_alphabet_fig.savefig(plaintext_alphabet_img_path, dpi=300, bbox_inches="tight")

    ### Morse code challenge
    morse_components_dir = "./challenge_4_morse_components"
    morse_alphabet_path = os.path.join(puzzle_img_dir, "morse_code_alphabet.jpg")

    # Turn the sex of the stowaway into morse
    morse_string = stowaway['Sex'].iloc[0]

    # Turn a string into a morse code wav file
    morse_wav_audio = generate_morse_audio_segment(morse_components_dir, morse_string)
    morse_wav_audio.export("./morse.wav", format="wav")

    # For hint - Turn string into morse code dots and dashes
    morse_text_hint = generate_morse_text(morse_string)

    # Challenge data to be added to the markdown file
    challenge_data = {
        "id": 4,
        "title": "Guest from the Deep",
        "story": story_text,
        "instructions": "Decode the encrypted letter and select the name from the list of suspects.",
        "suspect_table_img_path": suspect_table_img_path,
        "plaintext_letter": plaintext_letter,
        "encrypted_letter": encrypted_letter,
        "caeser_hint": caeser_hint,
        "encoded_key_img_path": encoded_key_img_path,
        "plaintext_alphabet_img_path": plaintext_alphabet_img_path,
        "encoded_alphabet_img_path": encoded_alphabet_img_path,
        "alpha_morse_img_path": morse_alphabet_path,
        "morse_wav_path": "morse.wav",
        "morse_text_hint": morse_text_hint,
        "stowaway_name": stowaway_name
    }

    return challenge_data

