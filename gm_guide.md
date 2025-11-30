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
name: Honkanen, Miss. Eliina
Pclass: 3
Age: 27.0
Sex: female
Fare: 7.92
Embarked: S
```
**Card 2**
```
name: Vander Cruyssen, Mr. Victor
Pclass: 1
Age: 47.0
Sex: male
Fare: 3.14
Embarked: S
```
**Card 3**
```
name: Dimic, Mr. Jovan
Pclass: 3
Age: 42.0
Sex: male
Fare: 8.66
Embarked: S
```
**Card 4**
```
name: McGowan, Miss. Anna "Annie"
Pclass: 3
Age: 15.0
Sex: female
Fare: 8.03
Embarked: Q
```
**Card 5**
```
name: Hippach, Miss. Jean Gertrude
Pclass: 1
Age: 16.0
Sex: female
Fare: 57.98
Embarked: C
```
**Card 6**
```
name: Nakid, Mr. Sahid
Pclass: 3
Age: 20.0
Sex: male
Fare: 15.74
Embarked: C
```

---
### GM Guide

> **Hint:** GM Hint: Refer to the box plot above. The forged card has a fare that doesn't match its class - either much higher or much lower than typical for that class. Players should compare each card's fare with the distribution shown in the chart for that card's class.
> **Answer:** [[REVEAL_ANSWER]]The forged card: 1st class (Pclass=1) but paying £3.14, which is much lower than typical 1st class fares (£5.00-512.33). **(In this game, this card is Card 2)**[[END_REVEAL]]
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

- Echo A: Carlo boards at Cherbourg (C); a second-class ticket rustles in hand.
- Echo B: Dennis boards at Southampton (S); a third-class ticket rustles in hand.
- Echo C: Smith boards at Queenstown (Q); a third-class ticket rustles in hand.
- Echo D: In the final chaos, Goldsmith finds space in a lifeboat and slips into the night.
- Echo E: Lanterns sway as the deck tilts; Mockler steadies a stranger amid rising alarm.

**Task:** Arrange the echoes (A–E) in correct chronological order.

---
### GM Guide

> **Answer:** [[REVEAL_ANSWER]]Correct order: B, A, C, E, D. Boarding echoes come first and follow port order S → C → Q; post-impact echoes (tilted/helping/chaos) follow; the lifeboat escape is last.[[END_REVEAL]]
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
Name: Clarke, Mrs. Charles V (Ada Maria Winfield)
Pclass: 2
Age: 28
Sex: female
Fare: 26.0
Embarked: S
```
**Card 2**
```
Name: Harknett, Miss. Alice Phoebe
Pclass: 3
Age: 48
Sex: female
Fare: 7.55
Embarked: S
```
**Card 3**
```
Name: McMahon, Mr. Martin
Pclass: 3
Age: 28
Sex: male
Fare: 7.75
Embarked: Q
```
**Card 4**
```
Name: Todoroff, Mr. Lalio
Pclass: 3
Age: 28
Sex: male
Fare: 7.9
Embarked: S
```

---
### GM Guide

> **Hint:** Use the survival charts above to infer the 4-digit lifeboat code.
> **Answer:** [[REVEAL_ANSWER]]1000[[END_REVEAL]]
> **Obtain:** **Temporal Coordinate Fragment 3** hidden within the lifeboat control panel.

---
## Guest from the Deep

**Story:** 
    
    The Captain has called you and your group to the deck of the ship with an 
    urgent mission. Telegrams have been intercepted from the ship's Marconi machine
    and it appears there is a stowaway on board! Unfortunately, the dastardly 
    stowaway has managed to scramble one of the telegrams using a mysterious code. 
    The Captain has created a list of 10 suspects. Can you decipher the letter and
    obtain the identity of the suspect before they get away?!
    
    

**Task:** Decode the encrypted letter and select the name from the list of suspects.

### Possible suspects 

![Suspect Table](./challenge_4_puzzle_images\suspect_table.png)

### Letters from the Stowaway 

**Plaintext Letter**```
R.M.S. TITANIC
MARCONI WIRELESS SERVICE
APRIL 12, 1912

Good afternoon, I have snuck aboard this mighty vessel.
Now time to implement my darstardly plan!
Yours Sincerely,

A Guest of the Deep
```
**Encrypted Letter**```
R.M.S. TITANIC
MARCONI WIRELESS SERVICE
APRIL 12, 1912

My secret alias is Keane, Miss. Nora A. I like it here in second class!

A Guest of the Deep
```
### A Mysterious Code 

![Encoded Alphabet Grid](./challenge_4_puzzle_images\encoded_alphabet_img.png)

![Puzzle Cipher](./challenge_4_puzzle_images\bill_cipher_img.png)

### A Strange Sound 
![Morse Alphabet](./challenge_4_puzzle_images\morse_code_alphabet.jpg)

[[PLAY_SOUND]]sound.wav[[END_SOUND]]
> **A Mysterious Code Hint:** [[REVEAL_HINT]]![Plaintext Alphabet Grid](./challenge_4_puzzle_images\plaintext_alphabet_img.png)[[END_HINT]]
---
## Game End

Congratulations! You've collected all 5 coordinate fragments, restarted the time machine, and successfully escaped from 1912 at the moment the Titanic sank.
