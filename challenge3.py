
import random
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns


def generate_challenge_3(df):
    """
    Generate Challenge 3 - Titanic Lifeboat Code
    Produces structured data consistent with Challenge 1 format.
    """
    NUM_PASSENGERS = 4
    MIN_SURVIVORS = 1
    MIN_DECEASED = 1

    # randomly select passengers ensuring at least one survivor and one deceased
    survivors = df[df['Survived'] == 1]
    deceased = df[df['Survived'] == 0]

    num_survivors = random.randint(MIN_SURVIVORS, NUM_PASSENGERS - MIN_DECEASED)
    num_deceased = NUM_PASSENGERS - num_survivors

    selected_survivors = survivors.sample(n=num_survivors, replace=False)
    selected_deceased = deceased.sample(n=num_deceased, replace=False)

    challenge_passengers_df = pd.concat([selected_survivors, selected_deceased]).sample(frac=1).reset_index(drop=True)

    passengers_list = []
    correct_code = ""
    for i, row in challenge_passengers_df.iterrows():
        correct_code += str(row['Survived'])

        age_value = row['Age']
        if pd.isna(age_value):
            age_value = random.randint(20, 50)

        fare_value = row['Fare']
        if pd.isna(fare_value):
            fare_value = 30 + (3 - row['Pclass']) * 20

        passengers_list.append({
            "Name": row['Name'] if 'Name' in row and pd.notna(row['Name']) else f"Passenger {i+1}",
            "Pclass": int(row['Pclass']),
            "Age": round(age_value),
            "Sex": row['Sex'],
            "Fare": round(fare_value, 2),
            "Embarked": row['Embarked'] if pd.notna(row['Embarked']) else 'S'
        })


    # generate static clues and charts
    try:
        sex_pclass_survival = (
            df.groupby(['Sex', 'Pclass'])['Survived']
            .mean().unstack().fillna(0)
        )

        age_bins = [0, 10, 20, 40, 60, 100]
        age_labels = ['<10', '10-20', '20-40', '40-60', '60+']
        df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)
        age_survival = df.groupby('AgeGroup')['Survived'].mean()

        sex_pclass_texts = [
            f"{sex.capitalize()} (Class {pclass}): {rate*100:.1f}%"
            for sex in sex_pclass_survival.index
            for pclass, rate in sex_pclass_survival.loc[sex].items()
        ]
        age_texts = [f"{age}: {rate*100:.1f}%" for age, rate in age_survival.items()]

        static_clues = [
            {"heading": "Survival Probability: Sex vs. Pclass", "content": "; ".join(sex_pclass_texts)},
            {"heading": "Survival Probability: Age Groups", "content": "; ".join(age_texts)}
        ]

        # 生成图表generate charts
        hint_dir = "hint"
        os.makedirs(hint_dir, exist_ok=True)

        # 性别+舱位生还率热图sex + pclass survival heatmap
        plt.figure(figsize=(8, 6))
        sns.heatmap(
            sex_pclass_survival,
            annot=True,
            fmt=".2f",
            cmap="YlGnBu",
            cbar_kws={'label': 'Survival Rate'}
        )
        plt.title("Survival Rate by Sex and Pclass")
        plt.tight_layout()
        chart1_path = os.path.join(hint_dir, "challenge_3_sex_pclass.png")
        plt.savefig(chart1_path, dpi=300, bbox_inches="tight")
        plt.close()

        # 年龄段生还率柱状图age group survival bar chart
        plt.figure(figsize=(8, 6))
        sns.barplot(x=age_survival.index, y=age_survival.values, palette="coolwarm")
        plt.title("Survival Rate by Age Group")
        plt.xlabel("Age Group")
        plt.ylabel("Survival Rate")
        plt.tight_layout()
        chart2_path = os.path.join(hint_dir, "challenge_3_age_group.png")
        plt.savefig(chart2_path, dpi=300, bbox_inches="tight")
        plt.close()

        hint_charts = [chart1_path, chart2_path]

    except Exception as e:
        print(f"⚠️ Error generating clues or charts: {e}")
        static_clues = []
        hint_charts = []

    # generate return data
    challenge_data = {
        "id": 3,
        "title": "Decipher the Lifeboat Code",
        "story": "The lifeboat lock requires a 4-digit code based on passengers' survival predictions.",
        "instructions": "Predict which of the 4 passengers survived (1) or perished (0). Use the survival clues provided.",
        "passengers": passengers_list,
        "static_clues": static_clues,
        "hint_chart": hint_charts,   # new: for HTML chart display
        "correct_code": correct_code
    }

    # save JSON file
    try:
        os.makedirs("src", exist_ok=True)
        with open("src/challenge_3_generated.json", "w", encoding="utf-8") as f:
            json.dump(challenge_data, f, ensure_ascii=False, indent=4)
        print("Challenge 3 JSON saved to src/challenge_3_generated.json")
    except Exception as e:
        print(f"Could not save Challenge 3 JSON: {e}")

    return challenge_data