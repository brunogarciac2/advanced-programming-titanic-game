import json
import pandas as pd

def load_data(filepath='./dataset/Titanic-Dataset.csv'):
    """Load Titanic dataset"""
    try:
        df = pd.read_csv(filepath)
        df['Age'] = df['Age'].dropna()
        df['Fare'] = df['Fare'].dropna()
        df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
        return df
    except FileNotFoundError:
        print(f"{filepath} not found")
        exit()

def generate_game_data():
    from challenge1 import generate_challenge_1
    from challenge2 import generate_challenge_2
    from challenge3 import generate_challenge_3
    from challenge4 import generate_challenge_4
    """Generate fresh game data from dataset"""
    print("Loading Titanic dataset...")
    df = load_data()
    
    print("Generating challenge 1...")
    # Pass the full DataFrame so it can generate the boxplot
    challenge_1 = generate_challenge_1(df)
    
    print("Generating challenge 2...")
    challenge_2 = generate_challenge_2(df)

    print("Generating challenge 3...")
    challenge_3 = generate_challenge_3(df)

    print("Generating challenge 4...")
    challenge_4 = generate_challenge_4(df)

    game_data = {
        "story_background": {
            "theme": "The Temporal Rift on the Titanic",
            "role": "You are a team of time travelers.",
            "goal": "Before the ship sinks, find 5 missing 'temporal coordinate fragments'."
        },
        "challenges": [
            challenge_1,
            challenge_2,
            challenge_3,
            challenge_4
        ]
    }
    
    return game_data


def save_game_data(game_data, filename='game_challenge.json'):
    """Save game data to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(game_data, f, ensure_ascii=False, indent=4)
    print(f"Game data saved to {filename}")


if __name__ == '__main__':
    # If run as standalone, generate and save game data
    game_data = generate_game_data()
    save_game_data(game_data)
    print("\n[SUCCESS] Game data generated successfully!")
