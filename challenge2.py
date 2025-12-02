import os
import random

import seaborn as sns
import matplotlib.pyplot as plt


def _pclass_to_text(pclass_value) -> str:
    """Convert numeric passenger class to descriptive text.

    Important: we must NOT silently map unknown classes (like 4) to a valid one,
    otherwise fake data in Challenge 2 becomes invisible to players.
    """
    mapping = {
        1: "first-class",
        2: "second-class",
        3: "third-class",
        4: "fourth-class"
    }
    try:
        pclass_int = int(pclass_value)
    except (ValueError, TypeError):
        return "an unknown class"

    if pclass_int in mapping:
        return mapping[pclass_int]

    # Fallback: explicitly show the numeric class
    return f"class {pclass_int}"


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


def generate_ch2_survival_chart(df, challenge_name='challenge_2'):
    """Generate and save survival rate chart by sex and class for Challenge 2."""
    hint_dir = 'hint'
    if not os.path.exists(hint_dir):
        os.makedirs(hint_dir)

    chart_path = os.path.join(hint_dir, f'{challenge_name}_survival_by_sex_class.png')

    # If chart already exists, reuse it
    if os.path.exists(chart_path):
        return chart_path

    # Prepare data: survival rate by (Sex, Pclass)
    if 'Survived' not in df.columns:
        return None

    df_clean = df.dropna(subset=['Sex', 'Pclass', 'Survived']).copy()
    df_clean['Sex'] = df_clean['Sex'].str.lower()
    df_clean = df_clean[df_clean['Sex'].isin(['male', 'female'])]

    grouped = (
        df_clean.groupby(['Sex', 'Pclass'])['Survived']
        .mean()
        .reset_index()
    )

    plt.figure(figsize=(8, 6))
    sns.lineplot(data=grouped, x='Pclass', y='Survived', hue='Sex', marker='o')
    plt.title('Survival Rate by Sex and Passenger Class')
    plt.xlabel('Passenger Class (1 = highest)')
    plt.ylabel('Survival Rate')
    plt.ylim(0, 1)
    plt.xticks([1, 2, 3], ['1st', '2nd', '3rd'])
    plt.tight_layout()
    plt.savefig(chart_path, dpi=300, bbox_inches='tight')
    plt.close()

    return chart_path



def generate_temporal_signal_graph(graph_info, challenge_name='challenge_2'):
    """Render the Survival-by-Birth-Year bar chart with letter positions."""
    hint_dir = 'hint'
    os.makedirs(hint_dir, exist_ok=True)
    chart_path = os.path.join(hint_dir, f"{challenge_name}_temporal_signal.png")

    x_labels = graph_info.get("x_labels", [])
    y_values = graph_info.get("y_values", [])
    positions = graph_info.get("positions", [])
    x_label = graph_info.get("x_axis_label", "Birth year band")
    y_label = graph_info.get("y_axis_label", "Value")
    title = graph_info.get("title", "Temporal Signal")

    if not x_labels or not y_values or len(x_labels) != len(y_values):
        return chart_path

    plt.figure(figsize=(9, 6))
    bars = plt.bar(range(len(x_labels)), y_values)

    plt.xticks(range(len(x_labels)), x_labels, rotation=15, ha="right")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Annotate bars with both value and letter position (if provided)
    for idx, bar in enumerate(bars):
        height = bar.get_height()
        label = f"{height:.2f}"
        if idx < len(positions) and positions[idx] is not None:
            label += f" → letter {positions[idx]}"
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            label,
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold"
        )

    plt.tight_layout()
    plt.savefig(chart_path, dpi=300, bbox_inches="tight")
    plt.close()

    return chart_path



def _last_name(full_name: str) -> str:
    """Extract the passenger's last name (dataset uses 'Last, Title. First')."""
    if not isinstance(full_name, str):
        return "Passenger"
    cleaned = full_name.strip()
    if not cleaned:
        return "Passenger"
    if ',' in cleaned:
        cleaned = cleaned.split(',', 1)[0]
    parts = cleaned.split()
    return parts[-1] if parts else "Passenger"


def generate_challenge_2(df):
    """Challenge 2: Echoes of Deck C – unified multi-step puzzle."""

    cols_needed = ['Name', 'Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'Survived']
    missing = [c for c in cols_needed if c not in df.columns]
    if missing:
        raise ValueError(f"Titanic dataset missing columns for Challenge 2: {missing}")

    clean_df = df.dropna(subset=cols_needed).copy()
    clean_df = clean_df[(clean_df['Age'] > 0) & (clean_df['Fare'] > 0)]

    TITANIC_YEAR = 1912
    fare_stats = get_fare_statistics_by_class(clean_df)

    # Build birth-year bands and survival rates (data-driven mapping)
    age_df = clean_df.dropna(subset=['Age', 'Survived']).copy()
    age_df['BirthYear'] = TITANIC_YEAR - age_df['Age']

    def birth_year_band(y):
        if y < 1875:
            return "before 1875"
        if y <= 1885:
            return "between 1875 and 1885"
        if y <= 1895:
            return "between 1886 and 1895"
        return "from 1896 onwards"

    age_df['Band'] = age_df['BirthYear'].apply(birth_year_band)

    surv_by_band = (
        age_df.groupby('Band')['Survived']
        .mean()
        .reset_index()
        .sort_values('Survived')  # lowest survival first
    )

    band_to_position = {
        row['Band']: idx + 1
        for idx, (_, row) in enumerate(surv_by_band.iterrows())
    }

    graph_info = {
        "id": "survival_by_birth_year",
        "title": "Survival Rate by Birth-Year Band",
        "description": (
            "The chart is already sorted from the lowest survival rate to the highest. "
            "Use it as a key: the leftmost band (lowest survival) maps to the 1st letter of each surname, "
            "the next band maps to the 2nd letter, then the 3rd, and the rightmost band (highest survival) "
            "maps to the 4th letter. Apply those positions to the real echoes to decode the final word."
        ),
        "x_labels": surv_by_band['Band'].tolist(),
        "y_values": surv_by_band['Survived'].round(3).tolist(),
        "x_axis_label": "Birth-year band",
        "y_axis_label": "Survival rate",
        "positions": [band_to_position.get(band, 4) for band in surv_by_band['Band'].tolist()],
    }

    birth_year_key = [
        {
            "range": row['Band'],
            "position": band_to_position.get(row['Band'], 4),
            "survival_rate": round(float(row['Survived']), 3),
        }
        for _, row in surv_by_band.iterrows()
    ]

    graph_image = generate_temporal_signal_graph(graph_info)
    graph_info["image"] = graph_image

    labels = list("ABCDEFG")  # 7 echoes
    fake_labels = random.sample(labels, 3)
    real_labels = [lab for lab in labels if lab not in fake_labels]

    # Ensure real echoes cover multiple ports and give two distinct pre-board ports for ordering
    real_map = {}
    embark_priority = ['S', 'C', 'Q']
    port_groups = {p: clean_df[clean_df['Embarked'] == p] for p in embark_priority}

    # Choose up to two ports for the pre-board real echoes (prefer distinct)
    available_ports = [p for p in embark_priority if not port_groups[p].empty]
    pre_ports = available_ports[:]
    random.shuffle(pre_ports)
    pre_ports = pre_ports[:2]

    remaining_labels = real_labels.copy()
    random.shuffle(remaining_labels)

    # Assign pre-board labels to distinct ports when possible
    pre_labels: list[str] = []
    for port in pre_ports:
        if not remaining_labels:
            break
        lab = remaining_labels.pop()
        pre_labels.append(lab)
        real_map[lab] = port_groups[port].sample(1).iloc[0]

    # Assign any remaining real labels from the route pool; fallback to any passenger
    route_pool = clean_df[clean_df['Embarked'].isin(embark_priority)]
    if route_pool.empty:
        route_pool = clean_df
    for lab in remaining_labels:
        real_map[lab] = route_pool.sample(1).iloc[0]

                # if lab not in real_map.values():
                  #  real_map[lab] = row
                 #   break
        #if lab not in real_map:
          #  real_map[lab] = clean_df.sample(1).iloc[0]

    def embarked_name(code: str) -> str:
        mapping = {
            'S': 'Southampton',
            'C': 'Cherbourg',
            'Q': 'Queenstown',
            'B': 'Belfast',   # plausible but invalid in manifest
            'N': 'New York',  # additional plausible but invalid port
        }
        return mapping.get(str(code).upper(), f"Unknown port '{code}'")

    def class_fare_word(pclass, override_word: str | None = None) -> str:
        """Return a fare descriptor keyed by class unless overridden. Terms are unique per class."""
        if override_word:
            return override_word
        bucket = {
            1: ["a lavishly priced ticket", "an opulently priced ticket"],
            2: ["a moderately priced ticket", "a middle-class fare ticket"],
            3: ["a shoestring-priced ticket", "a barebones fare ticket"],
        }.get(int(pclass), ["a ticket"])
        return random.choice(bucket)

    def sex_word(sex: str) -> str:
        return "man" if str(sex).lower().startswith('m') else "woman"

    event_phrases = [
        "early in the voyage, just after we boarded at Southampton, when everything still felt calm.",
        "later that afternoon as we walked the boat deck, wandering the corridors to find our cabins.",
        "in the evening after we had left Cherbourg, with the sea calm and the ship steady.",
        "around the time we reached Queenstown, before anything had tilted or gone wrong.",
        "just after a sudden jolt in the night when the ship struck something and the deck began to tilt.",
        "a little later, as we were helping others amid growing chaos near the lifeboats.",
        "near the very end, after we escaped into a lifeboat and watched the ship in the distance."
    ]

    event_stage_map = [
        "pre_board",      # early calm at Southampton
        "pre_board",      # afternoon boat deck
        "pre_board",      # evening after Cherbourg, calm
        "pre_board",      # around Queenstown, calm
        "impact",         # jolt/tilt
        "post_impact",    # helping amid chaos
        "lifeboat",       # escaped in lifeboat
    ]
    event_route_port = [
        "S",  # early at Southampton
        "S",  # afternoon boat deck (still early)
        "C",  # after leaving Cherbourg
        "Q",  # around reaching Queenstown
        None, # impact at sea
        None, # post-impact chaos
        None, # lifeboat/escape
    ]

    available_indices = list(range(len(event_phrases)))
    pre_indices = [i for i, stage in enumerate(event_stage_map) if stage == "pre_board"]
    impact_indices = [i for i, stage in enumerate(event_stage_map) if stage == "impact"]
    post_indices = [i for i, stage in enumerate(event_stage_map) if stage == "post_impact"]
    lifeboat_indices = [i for i, stage in enumerate(event_stage_map) if stage == "lifeboat"]

    event_order_by_label: dict[str, int] = {}

    # Build a deterministic structure for real echoes: two pre-board (distinct ports), one impact, one post-impact
    real_pool = real_labels.copy()
    random.shuffle(real_pool)

    # Assign two pre-board events with distinct route ports when possible
    random.shuffle(pre_indices)
    selected_pre = []
    used_ports: set[str] = set()
    for idx in pre_indices:
        if not real_pool:
            break
        port_hint = event_route_port[idx]
        if len(selected_pre) >= 2:
            break
        if port_hint is None or port_hint not in used_ports:
            lab = real_pool.pop()
            selected_pre.append(idx)
            if port_hint:
                used_ports.add(port_hint)
            available_indices.remove(idx)
            event_order_by_label[lab] = idx
    # If we still need a second pre-board and only same-port options remain
    if len(selected_pre) < 2 and real_pool and pre_indices:
        remaining_pre = [i for i in pre_indices if i not in selected_pre]
        if remaining_pre:
            idx = remaining_pre[0]
            lab = real_pool.pop()
            available_indices.remove(idx)
            event_order_by_label[lab] = idx

    # Assign impact
    if real_pool and impact_indices:
        idx = impact_indices[0]
        if idx in available_indices:
            lab = real_pool.pop()
            available_indices.remove(idx)
            event_order_by_label[lab] = idx

    # Assign post-impact (prefer post_impact, fallback to lifeboat)
    if real_pool:
        post_list = post_indices or lifeboat_indices
        if post_list:
            idx = post_list[0]
            if idx in available_indices:
                lab = real_pool.pop()
                available_indices.remove(idx)
                event_order_by_label[lab] = idx

    # Assign remaining labels (fake or leftover real) randomly
    for lab in labels:
        if lab in event_order_by_label:
            continue
        idx = available_indices.pop(random.randrange(len(available_indices)))
        event_order_by_label[lab] = idx

    def build_echo_text(row_dict: dict, event_phrase: str) -> str:
        age = int(round(row_dict['Age']))
        sex = sex_word(row_dict['Sex'])
        pclass_txt = _pclass_to_text(row_dict['Pclass'])
        embarked_txt = embarked_name(row_dict['Embarked'])
        fare_txt = class_fare_word(row_dict['Pclass'], row_dict.get('_fare_word'))
        last = _last_name(row_dict.get('Name', 'A passenger'))
        return (
            f"I am {last}, a {age}-year-old {sex} travelling in {pclass_txt}. "
            f"I boarded at {embarked_txt}, and my ticket was {fare_txt}. "
            f"This echo comes from {event_phrase}"
        )

    echoes = []
    initial_by_label: dict[str, str] = {}
    birth_year_by_label: dict[str, int] = {}
    letter_pos_by_label: dict[str, int] = {}
    band_by_label: dict[str, str] = {}

    # Real echoes (A–D)
    for lab in real_labels:
        row = real_map[lab]
        row_dict = row.to_dict()
        event_phrase = event_phrases[event_order_by_label[lab]]
        text = build_echo_text(row_dict, event_phrase)

        last = _last_name(row_dict.get('Name', 'Passenger'))
        initial_by_label[lab] = last[0].upper() if last else "?"
        birth_year_by_label[lab] = int(TITANIC_YEAR - row_dict['Age'])

        band = birth_year_band(birth_year_by_label[lab])
        letter_pos_by_label[lab] = band_to_position.get(band, 4)
        band_by_label[lab] = band

        echoes.append({
            "label": lab,
            "text": text,
            "embarked": row_dict['Embarked'],
            "pclass": int(row_dict['Pclass']),
            "is_fake": False,
        })

    # Fake echoes: either impossible ports or wildly wrong fares
    fake_rows: dict[str, dict] = {}
    fake_types = []
    for i in range(len(fake_labels)):
        fake_types.append('port' if i % 2 == 0 else 'fare')

    port_fakes = [('B', 'Belfast'), ('N', 'New York')]

    def generate_mispriced_fare(base_row) -> tuple[float, str, str]:
        """Return a mispriced fare, reason string, and a 'wrong' fare descriptor word."""
        pclass = int(base_row.get('Pclass', 3))
        stats = fare_stats.get(pclass, {'min': 0, 'max': 100, 'median': 50})

        # Force a wording mismatch for the class: first-class should not sound cheap; third-class should not sound lavish.
        mismatch = (
            "too_cheap" if pclass == 1
            else "too_lavish" if pclass == 3
            else random.choice(["too_cheap", "too_lavish"])
        )

        if mismatch == "too_cheap":
            new_fare = max(0.1, stats['min'] - random.uniform(5, 20))
            bad_word = class_fare_word(3)
            reason = f"Pclass {pclass} fare description sounds too cheap for this class (using third-class wording)."
        else:
            new_fare = round(stats['max'] + random.uniform(10, 40), 2)
            bad_word = class_fare_word(1)
            reason = f"Pclass {pclass} fare description sounds too lavish for this class (using first-class wording)."
        return new_fare, reason, bad_word

    for lab, fake_type in zip(fake_labels, fake_types):
        base = clean_df.sample(1).iloc[0].to_dict()

        if fake_type == 'port':
            code, pname = random.choice(port_fakes)
            base['Embarked'] = code
            reason = f"Embarkation port '{code}' ({pname}) does not appear in the passenger manifest."
        else:
            base['Embarked'] = base.get('Embarked', 'S') or 'S'
            new_fare, reason, bad_word = generate_mispriced_fare(base)
            base['Fare'] = new_fare
            base['_fare_word'] = bad_word

        base['_fake_reason'] = reason
        fake_rows[lab] = base

        event_phrase = event_phrases[event_order_by_label[lab]]
        text = build_echo_text(base, event_phrase)

        last = _last_name(base.get('Name', 'Passenger'))
        initial_by_label[lab] = last[0].upper() if last else "?"
        birth_year_by_label[lab] = int(TITANIC_YEAR - base['Age']) if base.get('Age') else None

        band = birth_year_band(birth_year_by_label[lab]) if birth_year_by_label.get(lab) is not None else None
        letter_pos_by_label[lab] = band_to_position.get(band, 4) if band else 4
        if band:
            band_by_label[lab] = band

        echoes.append({
            "label": lab,
            "text": text,
            "embarked": base['Embarked'],
            "pclass": int(base.get('Pclass', 3)),
            "is_fake": True,
        })

    echoes.sort(key=lambda e: e['label'])

    # Build full timeline ordering for GM reference
    def voyage_stage_rank(echo):
        label = echo['label']
        event_idx = event_order_by_label[label]
        stage = event_stage_map[event_idx]
        # Use event port hint when available (e.g., "after Cherbourg" -> C)
        event_port = event_route_port[event_idx]
        port = event_port or echo['embarked']

        # Stage priority: pre-board (1) < impact (2) < post-impact (3) < lifeboat (4)
        stage_rank_map = {
            "pre_board": 1,
            "impact": 2,
            "post_impact": 3,
            "lifeboat": 4,
        }
        stage_base = stage_rank_map.get(stage, 5)

        # Within pre-board, respect S→C→Q route order
        route_order = {'S': 1, 'C': 2, 'Q': 3}
        route_rank = route_order.get(port, 4) if stage == "pre_board" else 4

        return stage_base * 100 + route_rank * 10 + event_idx

    real_timeline_order = [
        e['label']
        for e in sorted(echoes, key=voyage_stage_rank)
        if not e['is_fake']
    ]

    timeline_clues = []
    for lab in real_timeline_order:
        row = real_map[lab]
        embark_code = row.get('Embarked')
        event_idx = event_order_by_label[lab]
        stage = event_stage_map[event_idx]
        route_port = event_route_port[event_idx] or embark_code
        route_name = embarked_name(route_port)
        event_phrase = event_phrases[event_order_by_label[lab]]
        route_reason = "route order S→C→Q" if stage == "pre_board" and route_port in ['S', 'C', 'Q'] else ""
        event_reason = {
            "pre_board": "pre-impact voyage timing",
            "impact": "impact/tilt",
            "post_impact": "post-impact chaos",
            "lifeboat": "lifeboat/escape timing",
        }.get(stage, "timing clue")
        timeline_clues.append(
            f"{lab}: {route_name} ({route_port}) sets base by {route_reason}; event clue: {event_phrase} ({event_reason})"
        )

    timeline_order = [e['label'] for e in echoes]

    scrambled_all = [f"{e['label']}:{initial_by_label.get(e['label'], '?')}" for e in echoes]
    scrambled_real = [f"{lab}:{initial_by_label.get(lab, '?')}" for lab in real_timeline_order]

    letter_pick_by_label: dict[str, str] = {}
    letter_detail_list: list[str] = []
    final_letters = []
    for lab in real_timeline_order:
        row = real_map[lab]
        surname = _last_name(row.get('Name', 'Passenger'))
        pos = letter_pos_by_label[lab]
        band = band_by_label.get(lab, "?")
        birth_year = birth_year_by_label.get(lab, "?")
        if not surname:
            letter_pick_by_label[lab] = "?"
            final_letters.append("?")
            letter_detail_list.append(f"{lab}:? (index {pos}, band {band}, birth year {birth_year})")
            continue
        idx = min(pos - 1, len(surname) - 1)
        picked = surname[idx].upper()
        letter_pick_by_label[lab] = picked
        final_letters.append(picked)
        letter_detail_list.append(f"{lab}:{picked} (index {pos}, band {band}, birth year {birth_year})")

    final_code = ''.join(final_letters)

    challenge = {
        "id": 2,
        "title": "Challenge 2: Echoes of Deck C",
        "story_intro": (
            "You intercept seven 'echoes' from passengers on Deck C. Some are consistent with "
            "the Titanic passenger manifest, others are corrupted fabrications. You know that "
            "Titanic's route took her first from Southampton (S) to Cherbourg (C), then to Queenstown (Q) "
            "before turning west into the Atlantic, and that later that night she struck an iceberg and "
            "chaos unfolded as lifeboats were loaded. Somewhere within these seven fragments lies a small "
            "group of passengers whose story, told in the right order, hides a coded word that can stabilise "
            "the temporal rift on Deck C."
        ),
        "echoes": echoes,
        "birth_year_key": birth_year_key,
        "graph": graph_info,
        "stages": {
            "stage1": {
                "name": "Separate Truth from Fiction",
                "task": (
                    "Start by finding the fabrications. Some echoes use impossible embarkation data or other "
                    "inconsistencies, including ticket wording that doesn't match the passenger's class "
                    "(first-class should sound expensive, second-class should sound moderate, third-class should sound cheap). "
                    "Identify which echoes could come from the real manifest and which are fake."
                ),
                "input_type": "set_of_labels",
                "expected_answer_key": "real_labels",
                "on_correct": "unlock_stage2",
                "on_wrong": {
                    "unlock_hint_levels": [1],
                    "allow_retry": True,
                },
            },
            "stage2": {
                "name": "Reconstruct the Night",
                "task": (
                    "With only the real echoes kept, order those real echoes chronologically across the voyage/night. "
                    "Use the voyage details and the language in the echoes to piece the sequence together."
                ),
                "input_type": "ordered_labels",
                "expected_answer_key": "real_timeline_order",
                "on_correct": "unlock_stage3",
                "on_wrong": {
                    "unlock_hint_levels": [2],
                    "allow_retry": True,
                },
            },
            "stage3": {
                "name": "Decode the Echo Word",
                "task": (
                    "With only the real echoes in their timeline order, estimate each passenger's birth year "
                    "(Titanic sailed in 1912). Use the **Survival Rate by Birth-Year Band** chart to find each "
                    "passenger's band. The chart is already sorted from lowest survival (left) to highest (right): "
                    "the leftmost band uses the 1st letter of the surname, the next uses the 2nd, then the 3rd, "
                    "and the rightmost uses the 4th. Pull that letter from each surname and read them in your "
                    "real-echo timeline order to reveal the final 4-letter answer."
                ),
                "input_type": "text",
                "expected_answer_key": "final_code",
                "is_final_stage": True,
                "on_correct": "reveal_temporal_fragment",
                "on_wrong": {
                    "unlock_hint_levels": [3],
                    "allow_retry": True,
                },
            },
        },
        "hints": [
            {
                "level": 1,
                "stage": "stage1",
                "type": "text",
                "unlock_condition": "first_wrong_attempt",
                "content": (
                    "Check embarkation ports against the dataset: passengers only embark from S, C, or Q "
                    "(Southampton, Cherbourg, Queenstown). Any echo whose port does not match one of these "
                    "is almost certainly fabricated. Ticket wording key: first-class uses 'lavishly priced' or "
                    "'opulently priced'; second-class uses 'moderately priced' or 'middle-class fare'; third-class "
                    "uses 'shoestring-priced' or 'barebones fare'. If the wording of the ticket doesn't fit the "
                    "class, treat it as a supporting clue for fakery."
                ),
            },
            {
                "level": 2,
                "stage": "stage2",
                "type": "text",
                "unlock_condition": "first_wrong_attempt",
                "content": (
                    "Use both the route and the language of the echoes. References to 'boarded at' and calm, steady "
                    "descriptions belong to the early voyage. Mentions of places like Southampton, Cherbourg, and "
                    "Queenstown also give you a sequence: S → C → Q. After impact, look for the order of signals: "
                    "tilted first, then helping, then chaos. Talk of 'escaped' or 'lifeboats' belongs near the very end."
                ),
            },
            {
                "level": 3,
                "stage": "stage3",
                "type": "text",
                "unlock_condition": "first_wrong_attempt",
                "content": (
                    "Remember Titanic sailed in 1912. Cheat sheet so you don't have to subtract: "
                    "ages 38+ → birth year before 1875 (index 2); ages 27–37 → birth years 1875–1885 (index 2); "
                    "ages 17–26 → birth years 1886–1895 (index 1); ages 0–16 → birth years 1896 or later (index 4). "
                    "Use those birth-year bands on the **Survival Rate by Birth-Year Band** chart. Order the bands "
                    "from lowest to highest survival rate: lowest uses the 1st letter of the name, next uses the "
                    "2nd, then the 3rd, and the highest uses the 4th. Only use passengers from echoes you marked as "
                    "real, and keep them in your real-echo timeline order."
                ),
            },
        ],
        "solution": {
            "timeline_order": timeline_order,
            "real_labels": sorted(real_labels),
            "fake_labels": sorted(fake_labels),
            "fake_reasons": {lab: fake_rows[lab]['_fake_reason'] for lab in fake_labels},
            "scrambled_all": scrambled_all,
            "scrambled_real": scrambled_real,
            "birth_years": birth_year_by_label,
            "letter_positions": letter_pos_by_label,
            "real_timeline_order": real_timeline_order,
            "letter_choices": [f"{lab}:{letter_pick_by_label.get(lab, '?')}" for lab in real_timeline_order],
            "letter_details": letter_detail_list,
            "bands": band_by_label,
            "timeline_clues": timeline_clues,
            "final_code": final_code,
        },
        "meta": {
            "allow_direct_final_answer": True,
            "final_answer_stage": "stage3",
            "final_answer_description": (
                "Players may always attempt to jump straight to the final 4-letter code, but the intended "
                "experience is to solve in order: Stage 1 (fake vs real) → Stage 2 (timeline of real echoes) → "
                "Stage 3 (decoding using the Survival Rate by Birth-Year Band chart)."
            ),
        },
    }

    return challenge
