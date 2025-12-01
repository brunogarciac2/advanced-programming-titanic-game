import random


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


def _pclass_to_text(pclass_value) -> str:
    """Convert numeric passenger class to descriptive text."""
    mapping = {
        1: "first-class",
        2: "second-class",
        3: "third-class"
    }
    try:
        return mapping[int(pclass_value)]
    except (ValueError, TypeError, KeyError):
        return "third-class"


def generate_challenge_2(df):
    """Challenge 2: Echoes of the Passengers (Timeline Synchronization)"""
    ports = ['S', 'C', 'Q']
    port_groups = {p: df[df['Embarked'] == p] for p in ports}

    def pick_by_port(port_code):
        group = port_groups.get(port_code)
        if group is not None and len(group) > 0:
            return group.sample(1).iloc[0]
        return df.sample(1).iloc[0]

    s_row = pick_by_port('S')
    c_row = pick_by_port('C')
    q_row = pick_by_port('Q')

    def boarding_text(row, port_label):
        name = _last_name(row.get('Name', 'Unknown'))
        pclass_txt = _pclass_to_text(row.get('Pclass', 3))
        return (
            f"{name} boards at {port_label} ({row.get('Embarked', '?')}); "
            f"a {pclass_txt} ticket rustles in hand."
        )

    echo_board_s = {'stage': 'boarding', 'port': 'S', 'text': boarding_text(s_row, 'Southampton')}
    echo_board_c = {'stage': 'boarding', 'port': 'C', 'text': boarding_text(c_row, 'Cherbourg')}
    echo_board_q = {'stage': 'boarding', 'port': 'Q', 'text': boarding_text(q_row, 'Queenstown')}

    post_row = df.sample(1).iloc[0]
    post_text = (
        f"Lanterns sway as the deck tilts; {_last_name(post_row.get('Name', 'A passenger'))} "
        f"steadies a stranger amid rising alarm."
    )
    echo_post = {'stage': 'post_impact', 'port': None, 'text': post_text}

    esc_row = df.sample(1).iloc[0]
    esc_text = (
        f"In the final chaos, {_last_name(esc_row.get('Name', 'A passenger'))} "
        f"finds space in a lifeboat and slips into the night."
    )
    echo_escape = {'stage': 'escape', 'port': None, 'text': esc_text}

    echoes = [echo_board_s, echo_board_c, echo_board_q, echo_post, echo_escape]
    random.shuffle(echoes)
    letters = ['A', 'B', 'C', 'D', 'E']
    for idx, echo in enumerate(echoes):
        echo['id'] = letters[idx]

    stage_rank = {'boarding': 1, 'post_impact': 2, 'escape': 3}
    port_rank = {'S': 1, 'C': 2, 'Q': 3, None: 0}
    sorted_true = sorted(
        echoes,
        key=lambda e: (stage_rank.get(e['stage'], 99), port_rank.get(e.get('port'), 0))
    )
    solution_letters = [echo['id'] for echo in sorted_true]

    known_facts = [
        "Boarding order by port: Southampton (S) → Cherbourg (C) → Queenstown (Q).",
        "Phrases like 'boarded at' are before the iceberg impact.",
        "Words like 'tilted', 'helping', or 'chaos' are after impact but still onboard.",
        "Mentions of 'escaped' or 'lifeboat' happen last."
    ]

    return {
        "id": 2,
        "title": "Challenge 2: Echoes of the Passengers (Timeline Synchronization)",
        "story_intro": "Time ripples carry brief echoes of five travelers aboard the Titanic. Align their moments to restore the timeline.",
        "echoes": [{"letter": echo['id'], "text": echo['text']} for echo in echoes],
        "known_facts": known_facts,
        "task": "Arrange the echoes (A–E) in correct chronological order.",
        "solution": ", ".join(solution_letters),
        "explanation": (
            "Boarding echoes come first and follow port order S → C → Q; "
            "post-impact echoes (tilted/helping/chaos) follow; the lifeboat escape is last."
        )
    }

