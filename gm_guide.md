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
name: Wick, Miss. Mary Natalie
Pclass: 1
Age: 31.0
Sex: female
Fare: 164.87
Embarked: S
```
**Card 2**
```
name: Ford, Miss. Robina Maggie "Ruby"
Pclass: 3
Age: 9.0
Sex: female
Fare: 34.38
Embarked: S
```
**Card 3**
```
name: Petroff, Mr. Pastcho ("Pentcho")
Pclass: 3
Age: nan
Sex: male
Fare: 7.9
Embarked: S
```
**Card 4**
```
name: Holverson, Mrs. Alexander Oskar (Mary Aline Towner)
Pclass: 1
Age: 35.0
Sex: female
Fare: 52.0
Embarked: S
```
**Card 5**
```
name: Asim, Mr. Adola
Pclass: 3
Age: 35.0
Sex: male
Fare: 7.05
Embarked: S
```
**Card 6**
```
name: Parrish, Mrs. (Lutie Davis)
Pclass: 3
Age: 50.0
Sex: female
Fare: 76.61
Embarked: S
```

---
### GM Guide

> **Hint:** GM Hint: Refer to the box plot above. The forged card has a fare that doesn't match its class - either much higher or much lower than typical for that class. Players should compare each card's fare with the distribution shown in the chart for that card's class.
> **Answer:** [[REVEAL_ANSWER]]The forged card: 3rd class (Pclass=3) but paying £76.61, which is much higher than typical 3rd class fares (£4.01-69.55). **(In this game, this card is Card 6)**[[END_REVEAL]]
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

- Echo A: Yasbeck boards at Cherbourg (C); a third-class ticket rustles in hand.
- Echo B: O'Driscoll boards at Queenstown (Q); a third-class ticket rustles in hand.
- Echo C: Lanterns sway as the deck tilts; Moran steadies a stranger amid rising alarm.
- Echo D: In the final chaos, Ali finds space in a lifeboat and slips into the night.
- Echo E: Asplund boards at Southampton (S); a third-class ticket rustles in hand.

**Task:** Arrange the echoes (A–E) in correct chronological order.

---
### GM Guide

> **Answer:** [[REVEAL_ANSWER]]Correct order: E, A, B, C, D. Boarding echoes come first and follow port order S → C → Q; post-impact echoes (tilted/helping/chaos) follow; the lifeboat escape is last.[[END_REVEAL]]
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
Name: Madigan, Miss. Margaret "Maggie"
Pclass: 3
Age: 28
Sex: female
Fare: 7.75
Embarked: Q
```
**Card 2**
```
Name: Moussa, Mrs. (Mantoura Boulos)
Pclass: 3
Age: 43
Sex: female
Fare: 7.23
Embarked: C
```
**Card 3**
```
Name: van Billiard, Mr. Austin Blyler
Pclass: 3
Age: 40
Sex: male
Fare: 14.5
Embarked: S
```
**Card 4**
```
Name: Cunningham, Mr. Alfred Fleming
Pclass: 2
Age: 29
Sex: male
Fare: 0.0
Embarked: S
```

---
### GM Guide

> **Hint:** Use the survival charts above to infer the 4-digit lifeboat code.
> **Answer:** [[REVEAL_ANSWER]]1100[[END_REVEAL]]
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

My secret alias is Lobb, Mr. William Arthur. It's a bit cramped here in third class!

A Guest of the Deep
```
### A Mysterious Code 

![Alphabet Grid](./challenge_4_puzzle_images\alpha_cipher_img.png)

![Puzzle Cipher](./challenge_4_puzzle_images\bill_cipher_img.png)

### A Strange Sound 
![Morse Alphabet](./challenge_4_puzzle_images\morse_code_alphabet.jpg)

[[PLAY_SOUND]]sound.wav[[END_SOUND]]
---
## Game End

Congratulations! You've collected all 5 coordinate fragments, restarted the time machine, and successfully escaped from 1912 at the moment the Titanic sank.
