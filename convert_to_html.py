import json
import re
from generate_challenge import generate_game_data, save_game_data
import tabulate


def markdown_to_html(md_text):
    """Convert basic markdown to HTML (supports multiple reveal blocks)"""
    html = md_text

    import uuid
    # correction for multiple reveal blocks
    def replace_reveal(m):
        reveal_id = str(uuid.uuid4())[:8]
        return (
            f'<div class="answer-reveal">'
            f'<button class="reveal-btn" onclick="toggleAnswer(\'{reveal_id}\')">Click to Reveal Answer</button>'
            f'<div class="answer-content" id="answer-{reveal_id}" style="display:none;">'
            f'{m.group(1).strip()}</div></div>'
        )

    html = re.sub(
        r'\[\[REVEAL_ANSWER\]\](.*?)\[\[END_REVEAL\]\]',
        replace_reveal,
        html,
        flags=re.DOTALL
    )

    def replace_sound(m):
        id = str(uuid.uuid4())[:8]
        sound_src = m.group(1).strip() 
        return (
            ## Note can change the css to something else
            f'<audio id="audio-{id}">'
            f'<source src="{sound_src}" type="audio/wav">'
            f'</audio>'
            f'<button class="reveal-btn" onclick="playSound(\'{id}\')">Click to Play Message</button>'
        )

    html = re.sub(
        r'\[\[PLAY_SOUND\]\](.*?)\[\[END_SOUND\]\]',
        replace_sound,
        html,
        flags=re.DOTALL
    )

    def replace_reveal_hint(m):
        reveal_id = str(uuid.uuid4())[:8]
        return (
            f'<div class="answer-reveal">'
            f'<button class="reveal-btn" onclick="toggleHint(\'{reveal_id}\')">Click to Reveal Hint</button>'
            f'<div class="answer-content" id="answer-{reveal_id}" style="display:none;">'
            f'{m.group(1).strip()}</div></div>'
        )

    html = re.sub(
        r'\[\[REVEAL_HINT\]\](.*?)\[\[END_HINT\]\]',
        replace_reveal_hint,
        html,
        flags=re.DOTALL
    )

    # Markdown → HTML replacements
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)

    # regardless of quotes or spaces
    html = re.sub(
        r'!\[(.+?)\]\((.+?)\)',
        r'<div class="chart-container"><img src="\2" alt="\1" style="max-width:100%;height:auto;border-radius:8px;box-shadow:0 4px 8px rgba(0,0,0,0.1);"></div>',
        html
    )

    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    html = re.sub(r'```([\s\S]+?)```', r'<pre><code>\1</code></pre>', html)
    html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)
    html = re.sub(r'^---', r'<hr>', html, flags=re.MULTILINE)
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)

    # Lists
    lines = html.split('\n')
    html_lines, in_list = [], False
    for line in lines:
        if line.strip().startswith('-'):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(f'<li>{line.strip()[1:].strip()}</li>')
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(line)
    if in_list:
        html_lines.append('</ul>')
    html = '\n'.join(html_lines)

    # Paragraphs
    paragraphs = html.split('\n\n')
    html_paragraphs = []
    for para in paragraphs:
        para = para.strip()
        if para and not para.startswith('<') and '</' not in para:
            html_paragraphs.append(f'<p>{para}</p>')
        else:
            html_paragraphs.append(para)
    html = '\n\n'.join(html_paragraphs)
    return html



def format_challenge_1(data):
    """Format Challenge 1 to Markdown"""
    md = f"## {data['title']}\n\n"
    md += f"**Story:** {data['story']}\n\n"
    md += f"**Task:** {data['task']}\n\n"
    
    # Add hint chart if it exists
    if 'hint_chart' in data and data['hint_chart']:
        md += f"![Box Plot]({data['hint_chart']})\n\n"
    
    md += "### Passenger Cards (Show to Players)\n\n"

    fake_card_index = -1
    for i, card in enumerate(data['passenger_cards']):
        md += f"**Card {i + 1}**\n"
        md += "```\n"
        for key, value in card.items():
            if key != "_is_fake":  # Don't show GM marker
                md += f"{key}: {value}\n"
        md += "```\n"

        if card.get("_is_fake"):
            fake_card_index = i + 1

    md += "\n---\n"
    md += "### GM Guide\n\n"
    md += f"> **Hint:** {data['hint']}\n"
    md += f"> **Answer:** [[REVEAL_ANSWER]]{data['answer']} **(In this game, this card is Card {fake_card_index})**[[END_REVEAL]]\n"
    md += "> **Obtain:** **Temporal Coordinate Fragment 1** hidden under the forged card.\n\n"
    return md


def format_challenge_2(data):
    """Format Challenge 2 (Echoes of Deck C) to Markdown."""
    md = f"## {data['title']}\n\n"
    md += f"**Story:** {data.get('story_intro', '')}\n\n"

    echoes = sorted(data.get('echoes', []), key=lambda e: e.get('label', ''))

    # Stage descriptions
    stages = data.get('stages', {})
    md += "### Puzzle Stages (GM Overview)\n\n"
    for stage_key in ["stage1", "stage2", "stage3"]:
        stage = stages.get(stage_key)
        if not stage:
            continue
        md += f"- **{stage.get('name', stage_key.title())}:** {stage.get('task', '')}\n"
    md += "\n"

    # Echoes shown to players
    md += "### Echoes (Show to Players)\n\n"
    for echo in echoes:
        lab = echo.get('label', '?')
        text = echo.get('text', '')
        md += f"- Echo {lab}: {text}\n"
    md += "\n"

    # Temporal Signal graph (shown to players)
    graph = data.get('graph')
    if graph:
        md += "### Temporal Signal Graph (Show to Players)\n\n"
        md += f"**{graph.get('title', 'Graph')}**\n\n"
        if graph.get('description'):
            md += graph['description'] + "\n\n"

        image_path = str(graph.get('image', '') or '').strip().replace("\\", "/").replace("'", "")
        if image_path:
            md += f"![Temporal Signal Graph]({image_path})\n\n"

    # Optional hints section (for GM; reveal selectively to players)
    hints = data.get('hints', [])
    if hints:
        md += "### Hints (GM Reference)\n\n"
        for hint in hints:
            lvl = hint.get('level', '?')
            stage = hint.get('stage', '?')
            unlock = hint.get('unlock_condition', 'manual')
            htype = hint.get('type', 'text')

            prefix = f"- **Level {lvl}**"

            if htype == 'text':
                content = hint.get('content', '')
                md += f"{prefix}: [[REVEAL_HINT]]{content}[[END_HINT]]\n"
            elif htype == 'image':
                desc = hint.get('description', 'Visual hint')
                path = str(hint.get('path', '')).strip().replace("\\", "/").replace("'", "")
                if path:
                    img_md = f"![{desc}]({path})"
                    md += f"{prefix}: [[REVEAL_HINT]]{img_md}[[END_HINT]]\n"
                else:
                    md += f"{prefix}: [[REVEAL_HINT]]{desc}[[END_HINT]]\n"
        md += "\n"

    md += "---\n"
    md += "### GM Guide\n\n"

    md += (
        "The final answer for this challenge is a 4-letter code derived from the birth-year band chart; "
        "solve the stages in order to reveal it.\n\n"
    )

    sol = data.get('solution', {})
    real_labels = sol.get('real_labels', [])
    fake_labels = sol.get('fake_labels', [])
    fake_reasons = sol.get('fake_reasons', {})
    timeline_order = sol.get('timeline_order', [])
    scrambled_all = sol.get('scrambled_all', '')
    scrambled_real = sol.get('scrambled_real', '')
    real_timeline_order = sol.get('real_timeline_order', [])
    final_code = sol.get('final_code', '')

    # Build explanation text
    explanation_lines = []
    if real_labels:
        explanation_lines.append(f"Real echoes: {', '.join(real_labels)}.")
    if fake_labels:
        reasons = [f"{lab} ({fake_reasons.get(lab, 'inconsistent data')})" for lab in fake_labels]
        explanation_lines.append("Fake echoes: " + ", ".join(reasons) + ".")
    if scrambled_all:
        pass  # GM already has full data; no need to surface scrambled letters including fakes
    if scrambled_real:
        explanation_lines.append(
            "After removing fake echoes, initials from real echoes in timeline order: "
            + " ".join(scrambled_real)
            + "."
        )
    if real_timeline_order:
        explanation_lines.append(
            "Real echoes in timeline order (earliest → latest): "
            + " → ".join(real_timeline_order)
            + "."
        )

    explanation_text = " ".join(explanation_lines)

    answer_text_lines = []
    if final_code:
        answer_text_lines.append(f"Final code: {final_code}.")

    # Fake vs real summary
    if fake_labels:
        reasons = [f"{lab} ({fake_reasons.get(lab, 'inconsistent data')})" for lab in fake_labels]
        answer_text_lines.append("Fake echoes: " + ", ".join(sorted(reasons)) + ".")
    if real_labels:
        answer_text_lines.append("Real echoes: " + ", ".join(sorted(real_labels)) + ".")

    # Timeline reasoning
    if real_timeline_order:
        answer_text_lines.append(
            "Real echoes in timeline order (earliest → latest): " + " → ".join(real_timeline_order) + "."
        )

    # Letter extraction detail
    letter_details = sol.get('letter_details') or sol.get('letter_choices', [])
    if letter_details:
        answer_text_lines.append(
            "Letters pulled from displayed names by birth-year band positions (timeline order): "
            + " ".join(letter_details)
            + "."
        )

    answer_text = " ".join(answer_text_lines)

    md += f"> **Answer:** [[REVEAL_ANSWER]]{answer_text}[[END_REVEAL]]\n"

    md += "> **Obtain:** **Temporal Coordinate Fragment 2** revealed when all three stages are solved.\n\n"

    return md


def format_challenge_3(data):
    """Format Challenge 3 (Lifeboat Code) to Markdown"""
    md = f"## {data['title']}\n\n"
    md += f"**Story:** {data.get('story', '')}\n\n"
    md += f"**Task:** {data.get('instructions', data.get('task', ''))}\n\n"
    
    # render hint charts
    if 'hint_chart' in data and data['hint_chart']:
        if isinstance(data['hint_chart'], list):
            for idx, chart_path in enumerate(data['hint_chart']):
                clean_path = str(chart_path).strip().replace("\\", "/").replace("'", "")
                md += f"![Hint Chart {idx + 1}]({clean_path})\n\n"
        else:
            clean_path = str(data['hint_chart']).strip().replace("\\", "/").replace("'", "")
            md += f"![Hint Chart]({clean_path})\n\n"
    elif 'static_clues' in data:
        md += "### Survival Clues\n\n"
        for clue in data['static_clues']:
            md += f"**{clue['heading']}**\n\n{clue['content']}\n\n"
    
    md += "### Passenger Cards (Show to Players)\n\n"
    for i, card in enumerate(data['passengers']):
        md += f"**Card {i + 1}**\n"
        md += "```\n"
        for key, value in card.items():
            if key != 'Survived':
                md += f"{key}: {value}\n"
        md += "```\n"

    md += "\n---\n"
    md += "### GM Guide\n\n"
    md += f"> **Hint:** Use the survival charts above to infer the 4-digit lifeboat code.\n"
    md += f"> **Answer:** [[REVEAL_ANSWER]]{data['correct_code']}[[END_REVEAL]]\n"
    md += "> **Obtain:** **Temporal Coordinate Fragment 3** hidden within the lifeboat control panel.\n\n"

    return md

def format_challenge_4(data):
    """Format Challenge 4 (Letters from a Stowaway) to markdown"""
    md = f"## {data['title']}\n\n"
    md += f"**Story:** {data.get('story', '')}\n\n"
    md += f"\n\n**Task:** {data.get('instructions', data.get('task', ''))}\n\n"

    md += '### Possible suspects \n\n'

    if "suspect_table_img_path" in data and data["suspect_table_img_path"]:
        md += f"![Suspect Table]({data['suspect_table_img_path']})\n\n"

    md += "### Letters from the Stowaway \n\n"

    md += f"The captain hands you two letters. You have no problem reading the first but the second appears to be written in some sort of code. Maybe the encoded letter contains some sort of clue as to the identity of this mysterious Guest of the Deep?\n"

    md += "\n**Plaintext Letter**"
    md += "```"
    md += f"{data['plaintext_letter']}"
    md += "```\n"

    md += "**Encrypted Letter**"
    md += "```"
    md += f"{data['encrypted_letter']}"
    md += "```\n"

    md += '### A Mysterious Code \n\n'

    md += f"As you work to decipher the letters, you look across the stowaway's desk and find a notebook containing the following patterns. Can you make any sense of it?"

    if "encoded_alphabet_img_path" in data and data["encoded_alphabet_img_path"]:
        md += f"![Encoded Alphabet Grid]({data['encoded_alphabet_img_path']})\n\n"

    if "encoded_key_img_path" in data and data["encoded_key_img_path"]:
        md += f"![Puzzle Cipher]({data['encoded_key_img_path']})\n\n"

    md += "### A Strange Sound \n"

    md += "As you try to decipher the mysterious code. The ship's Marconni Machine begins to whir. Rushing to the Radio Room, you hear a strange message."

    if "alpha_morse_img_path" in data and data["alpha_morse_img_path"]:
        md += f"![Morse Alphabet]({data['alpha_morse_img_path']})\n\n"

    md += f"[[PLAY_SOUND]]{data['morse_wav_path']}[[END_SOUND]]\n"

    md += "### Hints\n"

    md += f"> **Letters from a Stowaway Hint:** [[REVEAL_HINT]]Compare the headers of each letter. Maybe you'll be able to decipher a pattern.[[END_HINT]]"
    md += f" **Letters from a Stowaway Further Hint:** [[REVEAL_HINT]]Moving each letter around the alphabet by {data['caeser_key']}, gives it an encrypted letter. Move each letter back by {data['caeser_key']} and you will have the decrypted letter. If you go past the letter 'a' loop back around to 'z'[[END_HINT]]"
    md += f" **A Mysterious Code Hint:** [[REVEAL_HINT]]![Plaintext Alphabet Grid]({data['plaintext_alphabet_img_path']})[[END_HINT]]"
    md += f" **A Mysterious Code Further Hint:** [[REVEAL_HINT]]Align the alphabet with the encoded alphabet. Each symbol refers to a unique letter.[[END_HINT]]"
    md += f" **A Strange Sound Hint:** [[REVEAL_HINT]]{data['morse_text_hint']}[[END_HINT]]"
    md += f" **A Strange Sound Further Hint:** [[REVEAL_HINT]]Each of the morse symbols refers to a letter of the alphabet, with a space to differentiate letters.[[END_HINT]]\n"

    md += "### Final Answer\n"

    md += f"> **Final Answer:** [[REVEAL_ANSWER]]The alias of the Guest from the Deep is: **{data['stowaway_name']}**[[END_REVEAL]]"

    return md

def get_html_template():
    """Return HTML template with embedded CSS"""
    # Use raw strings to avoid double escaping
    css = """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .content {
            padding: 40px;
        }
        
        h1 {
            font-size: 2.2em;
            color: #667eea;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }
        
        h2 {
            font-size: 1.8em;
            color: #764ba2;
            margin: 30px 0 15px;
            padding-bottom: 8px;
            border-bottom: 2px solid #764ba2;
        }
        
        h3 {
            font-size: 1.4em;
            color: #555;
            margin: 20px 0 10px;
        }
        
        h4 {
            font-size: 1.2em;
            color: #666;
            margin: 15px 0 8px;
        }
        
        p {
            margin-bottom: 15px;
            text-align: justify;
        }
        
        strong {
            color: #667eea;
            font-weight: 600;
        }
        
        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', monospace;
            color: #d63384;
        }
        
        pre {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 15px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        pre code {
            background: transparent;
            color: inherit;
            padding: 0;
            border-radius: 0;
        }
        
        blockquote {
            border-left: 4px solid #667eea;
            padding-left: 20px;
            margin: 20px 0;
            background: #f8f9fa;
            padding: 15px 20px;
            border-radius: 5px;
            font-style: italic;
            color: #555;
        }
        
        hr {
            border: none;
            height: 3px;
            background: linear-gradient(to right, #667eea, #764ba2);
            margin: 30px 0;
            border-radius: 2px;
        }
        
        ul {
            margin: 15px 0 15px 30px;
        }
        
        li {
            margin-bottom: 8px;
        }
        
        .card {
            background: #fff;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            padding: 20px;
            margin: 15px 0;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
            border-color: #667eea;
        }
        
        .gm-hint {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            margin: 15px 0;
            border-radius: 5px;
        }
        
        .answer-box {
            background: #d1ecf1;
            border-left: 4px solid #0dcaf0;
            padding: 15px;
            margin: 15px 0;
            border-radius: 5px;
        }
        
        .chart-container {
            text-align: center;
            margin: 30px 0;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
        }
        
        .chart-container img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
        }
        
        .answer-reveal {
            margin: 20px 0;
        }
        
        .reveal-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 14px;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 4px 8px rgba(102, 126, 234, 0.3);
        }
        
        .reveal-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4);
        }
        
        .reveal-btn:active {
            transform: translateY(0);
        }
        
        .answer-content {
            background: #fff9e6 !important;
            color: #000000 !important;
            border-left: 4px solid #ffc107;
            padding: 15px;
            margin: 15px 0;
            border-radius: 5px;
            animation: fadeIn 0.5s ease-in;
            font-weight: 500;
        }
        
        .answer-content strong {
            color: #d63384 !important;
            font-weight: bold;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .print-btn {
            background: white;
            color: #667eea;
            border: 2px solid white;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        .print-btn:hover {
            background: #f8f9fa;
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        }
        
        .print-btn:active {
            transform: translateY(0);
        }
        
        @media print {
            body {
                background: white;
                padding: 0;
            }
            
            .print-btn {
                display: none !important;
            }
            
            .container {
                box-shadow: none;
                max-width: 100%;
            }
            
            .header {
                page-break-after: avoid;
            }
            
            h1, h2, h3 {
                page-break-after: avoid;
            }
            
            pre {
                page-break-inside: avoid;
            }
            
            blockquote {
                page-break-inside: avoid;
            }
            
            /* Reveal all answers in print */
            .answer-content {
                display: block !important;
            }
            
            .reveal-btn {
                display: none !important;
            }
        }
        
        @media (max-width: 768px) {
            .container {
                margin: 10px;
            }
            
            .header h1 {
                font-size: 1.8em;
            }
            
            h2 {
                font-size: 1.5em;
            }
            
            .content {
                padding: 20px;
            }
        }
    """
    
    template_str = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GM Guide - The Temporal Rift on the Titanic</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>CssStringPlaceholder</style>
</head>
<body>
    <div class="container" id="guide-container">
        <div class="header">
            <h1>🎮 GM Guide</h1>
            <p style="font-size: 1.2em; margin-top: 10px;">The Temporal Rift on the Titanic</p>
            <button onclick="captureScreenshot()" class="print-btn" id="screenshot-btn">📸 Capture Full Page</button>
        </div>
        <div class="content">
            ContentPlaceholder
        </div>
    </div>
    
    <script>
    function toggleAnswer(id) {
        const answerDiv = document.getElementById('answer-' + id);
        const btn = event.target;
        
        if (answerDiv.style.display === 'none' || answerDiv.style.display === '') {
            answerDiv.style.display = 'block';
            btn.textContent = 'Hide Answer';
            btn.style.background = 'linear-gradient(135deg, #dc3545 0%, #c82333 100%)';
        } else {
            answerDiv.style.display = 'none';
            btn.textContent = 'Click to Reveal Answer';
            btn.style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
        }
    }

    function toggleHint(id) {
        const answerDiv = document.getElementById('answer-' + id);
        const btn = event.target;
        
        if (answerDiv.style.display === 'none' || answerDiv.style.display === '') {
            answerDiv.style.display = 'block';
            btn.textContent = 'Hide Hint';
            btn.style.background = 'linear-gradient(135deg, #dc3545 0%, #c82333 100%)';
        } else {
            answerDiv.style.display = 'none';
            btn.textContent = 'Click to Reveal Hint';
            btn.style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
        }
    }

    function playSound(id) {
        const audio = document.getElementById('audio-' + id);
        audio.pause();
        audio.currentTime = 0;
        audio.play();
    }
    
    async function captureScreenshot() {
        const btn = document.getElementById('screenshot-btn');
        const container = document.getElementById('guide-container');
        
        // Get all answer elements and buttons
        const allAnswers = document.querySelectorAll('.answer-content');
        const allButtons = document.querySelectorAll('.reveal-btn');
        
        // Save original states
        const originalAnswerStates = Array.from(allAnswers).map(el => el.style.display);
        const originalButtonStates = Array.from(allButtons).map(el => el.style.display);
        
        // Show all answers temporarily for screenshot with better visibility
        allAnswers.forEach(el => {
            el.style.display = 'block';
            el.style.opacity = '1';
            el.style.visibility = 'visible';
            el.style.setProperty('background', '#fff9e6', 'important');
            el.style.setProperty('color', '#000000', 'important');
            el.style.setProperty('border-left', '4px solid #ffc107', 'important');
            el.style.setProperty('border', '1px solid #ffc107', 'important');
        });
        allButtons.forEach(el => {
            el.style.display = 'none';
            el.style.opacity = '1';
        });
        
        // Change button text
        btn.textContent = '📸 Capturing...';
        btn.disabled = true;
        
        // Force browser to render changes (longer wait for better rendering)
        await new Promise(resolve => setTimeout(resolve, 500));
        
        try {
            // Use html2canvas to capture the entire container with better options
            const canvas = await html2canvas(container, {
                backgroundColor: null,
                scale: 2,  // Higher quality
                useCORS: true,
                logging: false,
                allowTaint: false,
                removeContainer: false,
                onclone: function(clonedDoc) {
                    // Force all answer content to be visible in the clone with VERY visible colors
                    const clonedAnswers = clonedDoc.querySelectorAll('.answer-content');
                    clonedAnswers.forEach(el => {
                        // Use very visible background and text colors
                        el.style.cssText = 'display: block !important; ' +
                                         'opacity: 1 !important; ' +
                                         'visibility: visible !important; ' +
                                         'background-color: #fef3c7 !important; ' +
                                         'color: #000000 !important; ' +
                                         'border: 2px solid #f59e0b !important; ' +
                                         'font-weight: 600 !important; ' +
                                         'padding: 15px !important; ' +
                                         'margin: 15px 0 !important; ' +
                                         'border-left: 4px solid #f59e0b !important;';
                        
                        // Get all text inside and make it black
                        const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
                        let node;
                        while (node = walker.nextNode()) {
                            node.nodeValue = node.nodeValue;
                        }
                    });
                }
            });
            
            // Convert canvas to image and download
            const imgData = canvas.toDataURL('image/png', 1.0);
            const link = document.createElement('a');
            link.download = 'gm_guide_full_page.png';
            link.href = imgData;
            link.click();
            
            btn.textContent = '✅ Saved!';
            
            // Restore original states
            setTimeout(() => {
                allAnswers.forEach((el, idx) => {
                    el.style.display = originalAnswerStates[idx] || 'none';
                    el.style.opacity = '';
                    el.style.visibility = '';
                });
                allButtons.forEach((el, idx) => {
                    el.style.display = originalButtonStates[idx] || 'block';
                    el.style.opacity = '';
                });
                
                btn.textContent = '📸 Capture Full Page';
                btn.disabled = false;
            }, 2000);
            
        } catch (error) {
            console.error('Screenshot failed:', error);
            btn.textContent = '❌ Error - Retry';
            btn.disabled = false;
            
            // Restore original states on error
            allAnswers.forEach((el, idx) => {
                el.style.display = originalAnswerStates[idx] || 'none';
                el.style.opacity = '';
                el.style.visibility = '';
            });
            allButtons.forEach((el, idx) => {
                el.style.display = originalButtonStates[idx] || 'block';
                el.style.opacity = '';
            });
        }
    }
    </script>
</body>
</html>"""
    
    # Insert CSS
    return template_str.replace('CssStringPlaceholder', css)


def main():
    # Generate fresh game data (regenerates every run)
    game_data = generate_game_data()

    # Save the JSON file for reference
    save_game_data(game_data)

    # Start building Markdown
    md_output = f"# {game_data['story_background']['theme']}: GM Guide\n\n"
    md_output += f"**Player Role:** {game_data['story_background']['role']}\n"
    md_output += f"**Final Goal:** {game_data['story_background']['goal']}\n\n"
    md_output += "--- \n"

    # Format function mapping
    format_functions = [
        format_challenge_1,
        format_challenge_2,
        format_challenge_3,
        format_challenge_4
    ]
    print("Converting challenges to Markdown...")
    for i, challenge_data in enumerate(game_data['challenges']):
        md_output += format_functions[i](challenge_data)
        md_output += "---\n"

    md_output += "## Game End\n\n"
    md_output += "Congratulations! You've collected all 5 coordinate fragments, restarted the time machine, and successfully escaped from 1912 at the moment the Titanic sank.\n"
    
    # Save markdown file
    print("Saving Markdown file...")
    with open('gm_guide.md', 'w', encoding='utf-8') as f:
        f.write(md_output)
    print("[OK] gm_guide.md saved")
    
    # Convert markdown to HTML
    print("Converting Markdown to HTML...")
    html_content = markdown_to_html(md_output)
    
    # Wrap in template - replace ContentPlaceholder with actual content
    template = get_html_template()
    html_output = template.replace('ContentPlaceholder', html_content)
    
    # Write to HTML file
    output_filename = 'gm_guide.html'
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_output)

    print(f"[OK] {output_filename} saved")
    print("\n[SUCCESS] All guides generated successfully!")
    print("You can open gm_guide.html in your web browser to view the guide.")


if __name__ == "__main__":
    main()
