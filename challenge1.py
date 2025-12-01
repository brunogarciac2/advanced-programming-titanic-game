import random
import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_boxplot(df, challenge_name='challenge_1'):
    """Generate and save boxplot for fare distribution by class"""
    # Create hint directory if it doesn't exist
    hint_dir = 'hint'
    if not os.path.exists(hint_dir):
        os.makedirs(hint_dir)

    # File path for the chart
    chart_path = os.path.join(hint_dir, f'{challenge_name}_boxplot.png')

    # Check if chart already exists
    if os.path.exists(chart_path):
        print(f"[SKIP] Chart already exists: {chart_path}")
        return chart_path

    print(f"[GENERATING] Creating boxplot: {chart_path}")

    # Filter out zero fares for realistic boxplot
    df_valid = df[df['Fare'] > 0].copy()

    # Create the boxplot
    plt.figure(figsize=(12, 7))
    sns.set_style("whitegrid")
    ax = sns.boxplot(data=df_valid, x='Pclass', y='Fare', palette='muted', hue='Pclass', legend=False)

    # Get statistics for each class and add min/max labels
    for i, pclass in enumerate([1, 2, 3]):
        class_data = df_valid[df_valid['Pclass'] == pclass]['Fare']

        if len(class_data) > 0:
            min_val = class_data.min()
            max_val = class_data.max()
            median_val = class_data.median()

            # Add text annotations for min, max, and median
            ax.text(i - 0.15, min_val, f'Min: £{min_val:.2f}',
                    ha='left', va='bottom', fontsize=9, color='darkblue', fontweight='bold')
            ax.text(i + 0.15, max_val, f'Max: £{max_val:.2f}',
                    ha='left', va='bottom', fontsize=9, color='darkred', fontweight='bold')
            ax.text(i, median_val, f'Median: £{median_val:.2f}',
                    ha='center', va='top', fontsize=9, color='darkgreen', fontweight='bold')

    plt.title('Average Fare Distribution by Class (Box Plot)', fontsize=16, fontweight='bold')
    plt.xlabel('Passenger Class', fontsize=12)
    plt.ylabel('Fare (Pounds)', fontsize=12)
    # Map Pclass values (1, 2, 3) to labels
    plt.xticks([0, 1, 2], ['1st Class\n(Pclass=1)', '2nd Class\n(Pclass=2)', '3rd Class\n(Pclass=3)'])

    # Save the plot
    plt.tight_layout()
    plt.savefig(chart_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"[OK] Chart saved to {chart_path}")
    return chart_path


def get_fare_statistics_by_class(df):
    """Get fare statistics for each class to generate realistic fake data"""
    stats = {}
    for pclass in [1, 2, 3]:
        # Filter out zero fares (missing data) to get realistic statistics
        class_data = df[(df['Pclass'] == pclass) & (df['Fare'] > 0)]['Fare']

        # If no valid data for this class, use a fallback range
        if len(class_data) == 0:
            stats[pclass] = {
                'min': 0,
                'max': 100,
                'median': 50,
                'mean': 50
            }
        else:
            stats[pclass] = {
                'min': class_data.min(),
                'max': class_data.max(),
                'median': class_data.median(),
                'mean': class_data.mean()
            }
    return stats


def format_passenger(passenger_data) -> dict[str, object]:
    """Format passenger data for game cards (accepts Series or dict)"""
    # Handle both pandas Series and dictionaries
    if isinstance(passenger_data, dict):
        get_val = lambda key, default: passenger_data.get(key, default)
    else:
        get_val = lambda key, default: passenger_data.get(key, default)

    return {
        "name": get_val('Name', "N/A"),
        "Pclass": get_val('Pclass', "N/A"),
        "Age": get_val('Age', 0),
        "Sex": get_val("Sex", "N/A"),
        "Fare": round(get_val('Fare', 0), 2),
        "Embarked": get_val('Embarked', "N/A")
    }




def generate_challenge_1(df):
    """Generate Challenge 1: Find the Anomaly"""
    # Filter out passengers with zero or missing fares for realistic data
    valid_passengers = df[df['Fare'] > 0]

    # Sample 5 real passengers with valid fares
    real_passengers = valid_passengers.sample(5)

    challenge_cards = [format_passenger(row) for _, row in real_passengers.iterrows()]

    # Get fare statistics by class
    fare_stats = get_fare_statistics_by_class(df)

    # Create fake data - randomly select class and generate mismatched fare
    fake_pclass = random.choice([1, 2, 3])

    # Generate a fake name from a random real passenger (also with valid fare)
    fake_template = valid_passengers.sample(1).iloc[0].copy()
    fake_name = fake_template['Name']

    # Generate mismatched fare based on class and direction (high or low)
    is_too_high = random.choice([True, False])  # Randomly choose high or low

    if fake_pclass == 1:
        if is_too_high:
            # 1st class with unusually HIGH fare (above maximum)
            fake_fare = round(random.uniform(
                fare_stats[1]['max'] + 10,  # £512.33 + 10 = £522.33
                fare_stats[1]['max'] * 1.3  # Up to £666
            ), 2)
            direction = "higher"
        else:
            # 1st class with unusually LOW fare (below minimum)
            fake_fare = round(random.uniform(
                0.5,  # Very low
                fare_stats[1]['min'] - 0.5  # £5.00 - 0.5 = £4.50
            ), 2)
            direction = "lower"

        expected_range = f"£{fare_stats[1]['min']:.2f}-{fare_stats[1]['max']:.2f}"
        actual_range = f"£{fake_fare:.2f}"
        anomaly_description = f"1st class (Pclass={fake_pclass}) but paying {actual_range}, which is much {direction} than typical 1st class fares ({expected_range})"

    elif fake_pclass == 2:
        if is_too_high:
            # 2nd class with unusually HIGH fare (above maximum)
            fake_fare = round(random.uniform(
                fare_stats[2]['max'] + 1,  # £73.50 + 1 = £74.50
                fare_stats[2]['max'] * 1.5  # Up to £110
            ), 2)
            direction = "higher"
        else:
            # 2nd class with unusually LOW fare (below minimum)
            fake_fare = round(random.uniform(
                0.5,  # Very low
                fare_stats[2]['min'] - 0.5  # £10.50 - 0.5 = £10.00
            ), 2)
            direction = "lower"

        expected_range = f"£{fare_stats[2]['min']:.2f}-{fare_stats[2]['max']:.2f}"
        actual_range = f"£{fake_fare:.2f}"
        anomaly_description = f"2nd class (Pclass={fake_pclass}) but paying {actual_range}, which is much {direction} than typical 2nd class fares ({expected_range})"

    else:  # fake_pclass == 3
        if is_too_high:
            # 3rd class with unusually HIGH fare (above maximum)
            fake_fare = round(random.uniform(
                fare_stats[3]['max'] + 1,  # £69.55 + 1 = £70.55
                fare_stats[3]['max'] * 1.3  # Up to £90.42
            ), 2)
            direction = "higher"
        else:
            # 3rd class with unusually LOW fare (below minimum)
            fake_fare = round(random.uniform(
                0.5,  # Very low
                fare_stats[3]['min'] - 0.5  # £4.01 - 0.5 = £3.51
            ), 2)
            direction = "lower"

        expected_range = f"£{fare_stats[3]['min']:.2f}-{fare_stats[3]['max']:.2f}"
        actual_range = f"£{fake_fare:.2f}"
        anomaly_description = f"3rd class (Pclass={fake_pclass}) but paying {actual_range}, which is much {direction} than typical 3rd class fares ({expected_range})"

    # Create fake card
    fake_card_data = {
        'Name': fake_name,
        'Pclass': fake_pclass,
        'Age': fake_template['Age'],
        'Sex': fake_template['Sex'],
        'Fare': fake_fare,
        'Embarked': fake_template.get('Embarked', 'S'),
        '_is_fake': True
    }

    fake_card = format_passenger(fake_card_data)
    fake_card["_is_fake"] = True  # Mark as fake in JSON (GM only)
    challenge_cards.append(fake_card)
    random.shuffle(challenge_cards)

    # Generate boxplot for the hint
    chart_path = generate_boxplot(df, 'challenge_1')

    return {
        "id": 1,
        "title": "Challenge 1: Purser's Office (Find the Anomaly)",
        "story": "You've just boarded and been caught as stowaways. On the desk is a stack of passenger registration cards. You must identify the 'forged' card among them.",
        "task": "Out of the following 6 passenger cards, which one is statistically impossible?",
        "passenger_cards": challenge_cards,
        "hint": "GM Hint: Refer to the box plot above. The forged card has a fare that doesn't match its class - either much higher or much lower than typical for that class. Players should compare each card's fare with the distribution shown in the chart for that card's class.",
        "hint_chart": chart_path,  # Add chart path
        "answer": f"The forged card: {anomaly_description}."
    }

