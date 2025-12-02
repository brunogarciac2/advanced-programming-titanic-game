# The Temporal Rift on the Titanic: GM Guide

**Player Role:** You are a team of time travelers.
**Final Goal:** Before the ship sinks, find 5 missing 'temporal coordinate fragments'.

--- 
## Challenge 1: Purser's Office (Find the Anomaly)

**Story:** You've just boarded and been caught as stowaways. On the desk is a stack of passenger registration cards. You must identify the 'forged' card among them.

**Task:** Out of the following 6 passenger cards, which one is statistically impossible?

![Box Plot](hint\challenge_1_boxplot.png)

### Passenger Cards (Show to Players)

**Card 1**
```
name: Warren, Mrs. Frank Manley (Anna Sophia Atkinson)
Pclass: 2
Age: 60.0
Sex: female
Fare: 107.8
Embarked: C
```
**Card 2**
```
name: Carrau, Mr. Francisco M
Pclass: 1
Age: 28.0
Sex: male
Fare: 47.1
Embarked: S
```
**Card 3**
```
name: Hoyt, Mrs. Frederick Maxfield (Jane Anne Forby)
Pclass: 1
Age: 35.0
Sex: female
Fare: 90.0
Embarked: S
```
**Card 4**
```
name: Hocking, Mrs. Elizabeth (Eliza Needs)
Pclass: 2
Age: 54.0
Sex: female
Fare: 23.0
Embarked: S
```
**Card 5**
```
name: Novel, Mr. Mansouer
Pclass: 3
Age: 28.5
Sex: male
Fare: 7.23
Embarked: C
```
**Card 6**
```
name: Yasbeck, Mrs. Antoni (Selini Alexander)
Pclass: 3
Age: 15.0
Sex: female
Fare: 14.45
Embarked: C
```

---
### GM Guide

> **Hint:** GM Hint: Refer to the box plot above. The forged card has a fare that doesn't match its class - either much higher or much lower than typical for that class. Players should compare each card's fare with the distribution shown in the chart for that card's class.
> **Answer:** [[REVEAL_ANSWER]]The forged card: 2nd class (Pclass=2) but paying £107.80, which is much higher than typical 2nd class fares (£10.50-73.50). **(In this game, this card is Card 1)**[[END_REVEAL]]
> **Obtain:** **Temporal Coordinate Fragment 1** hidden under the forged card.

---
## Challenge 2: Echoes of the Passengers (Timeline Synchronization)

**Story:** Time ripples carry brief echoes of five travelers aboard the Titanic. Align their moments to restore the timeline.

**Known Facts**
- Boarding order by port: Southampton (S) → Cherbourg (C) → Queenstown (Q).
- Phrases like 'boarded at' are before the iceberg impact.
- Words like 'tilted', 'helping', or 'chaos' are after impact but still onboard.
- Mentions of 'escaped' or 'lifeboat' happen last.

### Echoes (Show to Players)

- Echo A: Lurette boards at Cherbourg (C); a first-class ticket rustles in hand.
- Echo B: In the final chaos, Fortune finds space in a lifeboat and slips into the night.
- Echo C: Hoyt boards at Southampton (S); a first-class ticket rustles in hand.
- Echo D: Kilgannon boards at Queenstown (Q); a third-class ticket rustles in hand.
- Echo E: Lanterns sway as the deck tilts; Lang steadies a stranger amid rising alarm.

**Task:** Arrange the echoes (A–E) in correct chronological order.

---
### GM Guide

> **Answer:** [[REVEAL_ANSWER]]Correct order: C, A, D, E, B. Boarding echoes come first and follow port order S → C → Q; post-impact echoes (tilted/helping/chaos) follow; the lifeboat escape is last.[[END_REVEAL]]
> **Obtain:** **Temporal Coordinate Fragment 2** revealed when the order is correct.

---
## Decipher the Lifeboat Code

**Story:** The lifeboat lock requires a 4-digit code based on passengers' survival predictions.

**Task:** Predict which of the 4 passengers survived (1) or perished (0). Use the survival clues provided.

![Hint Chart 1](hint/challenge_3_sex_pclass.png)

![Hint Chart 2](hint/challenge_3_age_group.png)

### Passenger Cards (Show to Players)

**Card 1**
```
Name: Kallio, Mr. Nikolai Erland
Pclass: 3
Age: 17
Sex: male
Fare: 7.12
Embarked: S
```
**Card 2**
```
Name: Haas, Miss. Aloisia
Pclass: 3
Age: 24
Sex: female
Fare: 8.85
Embarked: S
```
**Card 3**
```
Name: Chambers, Mrs. Norman Campbell (Bertha Griggs)
Pclass: 1
Age: 33
Sex: female
Fare: 53.1
Embarked: S
```
**Card 4**
```
Name: West, Miss. Constance Mirium
Pclass: 2
Age: 5
Sex: female
Fare: 27.75
Embarked: S
```

---
### GM Guide

> **Hint:** Use the survival charts above to infer the 4-digit lifeboat code.
> **Answer:** [[REVEAL_ANSWER]]0011[[END_REVEAL]]
> **Obtain:** **Temporal Coordinate Fragment 3** hidden within the lifeboat control panel.

---
## Guest from the Deep

**Story:** 
    
    The Captain has contact you and your group with an urgent mission. He claims there 
    is a stowaway on board and he is calling himself the 'Guest of the Deep'! 
    Leading you into a strange room, he tells you this is the stowaway's base of operations.
    The Captain has created a list of suspects, however, unfortunately the captain isn't sure
    which one of the suspects is the darstadly stowaway. Can you use your deductive powers
    to decipher the puzzles and obtain the identity of this 'Guest of the Deep' 
    before they get away?!
    
    



**Task:** Solve the puzzles and find the identity of the stowaway.

### Possible suspects 

![Suspect Table](./assets/images\suspect_table.png)

### Letters from the Stowaway 

The captain hands you two letters. You have no problem reading the first but the second appears to be written in some sort of code. Maybe the encoded letter contains some sort of clue as to the identity of this mysterious Guest of the Deep?

**Plaintext Letter**```
R.M.S. TITANIC
MARCONI WIRELESS SERVICE
APRIL 12, 1912
Dear Reader,
Life aboard The Titanic unfolds with luxury befitting its grandeur as passengers enjoy sumptuous meals in elegantly appointed dining rooms while engaging in social activities ranging from glamorous balls to quiet evenings by the piano. Leisure seekers partake in excursions exploring exotic locations along our scenic routes, indulging in first-class comforts that promise an unparalleled voyage.
Warm regards,
Aboard The Titanic
Yours, sincerely

    The Guest of the Deep.
```
**Encrypted Letter**```
R.M.S. TITANIC
MARCONI WIRELESS SERVICE
APRIL 12, 1912
It's a bit cramped here in third class! Dear Reader,
Life aboard the RMS Titanic offers an unparalleled sense of luxury as we sail through serene waters across uncharted seas.
Passengers enjoy gourmet meals served at our elegant dining rooms with breathtaking views from grand balconies stretching along both sides of the vessel's imposing decks, while first-class guests lounge in plush armchairs adorned by exquisite artwork and hand-knitted carpets. Second- and third-class passengers are catered to as well through meticulously maintained dining areas that boast an array of delightful dishes crafted for every palate.
Entertainment is abundant with opulent theaters hosting lavish shows such as enchanting operas performed nightly, complemented by lively jazz bands filling the airwaves during our leisurely cruises at sea or casual gatherings on deck. Guests can indulge in swimming pools located strategically around both public and private sections; these are ideal spots to unwind while basking under golden sun rays.
Staying active aboard this magnificent vessel is effortless with a plethora of activities available for guests aged eighteen years plus, including an Olympic-standard gymnasium featuring the latest equipment as well as numerous other indoor spaces perfect suited for engaging games or even hosting intimate social events. 
The ship's staff remains committed to delivering exceptional service at every turn during our voyage; we strive tirelessly through endless hours spent ensuring that all aspects of passenger comfort are met and exceeded.
As Titanic glides gracefully across the open ocean, life onboard presents guests with an unforgettable experience unparalleled by any other mode of travel ever conceived. The promise it holds for countless memorable adventures is truly extraordinaryâ€”one simply cannot match!
Best regards,
Aboard RMS Titanic
Yours, sincerely

    The Guest of the Deep.
```
### A Mysterious Code 

As you work to decipher the letters, you look across the stowaway's desk and find a notebook containing the following patterns. Can you make any sense of it?![Encoded Alphabet Grid](./assets/images\encoded_alphabet_img.png)

![Puzzle Cipher](./assets/images\bill_cipher_img.png)

### A Strange Sound 
As you try to decipher the mysterious code. The ship's Marconni Machine begins to whir. Rushing to the Radio Room, you hear a strange message.![Morse Alphabet](./assets/images\morse_code_alphabet.jpg)

[[PLAY_SOUND]]./assets/audio\morse.wav[[END_SOUND]]
### Hints
> **Letters from a Stowaway Hint:** [[REVEAL_HINT]]Compare the headers of each letter. Maybe you'll be able to decipher a pattern.[[END_HINT]] **Letters from a Stowaway Further Hint:** [[REVEAL_HINT]]Moving each letter around the alphabet by 11, gives it an encrypted letter. Move each letter back by 11 and you will have the decrypted letter. If you go past the letter 'a' loop back around to 'z'[[END_HINT]] **A Mysterious Code Hint:** [[REVEAL_HINT]]![Plaintext Alphabet Grid](./assets/images\plaintext_alphabet_img.png)[[END_HINT]] **A Mysterious Code Further Hint:** [[REVEAL_HINT]]Align the alphabet with the encoded alphabet. Each symbol refers to a unique letter.[[END_HINT]] **A Strange Sound Hint:** [[REVEAL_HINT]]--   .-   .-..   .   [[END_HINT]] **A Strange Sound Further Hint:** [[REVEAL_HINT]]Each of the morse symbols refers to a letter of the alphabet, with a space to differentiate letters.[[END_HINT]]
### Final Answer
> **Final Answer:** [[REVEAL_ANSWER]]The alias of the Guest from the Deep is: **Rice, Master. Eugene**[[END_REVEAL]]---
## Game End

Congratulations! You've collected all 5 coordinate fragments, restarted the time machine, and successfully escaped from 1912 at the moment the Titanic sank.
