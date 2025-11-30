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
name: Hanna, Mr. Mansour
Pclass: 3
Age: 23.5
Sex: male
Fare: 7.23
Embarked: C
```
**Card 2**
```
name: Navratil, Mr. Michel ("Louis M Hoffman")
Pclass: 1
Age: 36.5
Sex: male
Fare: 643.46
Embarked: S
```
**Card 3**
```
name: Ali, Mr. William
Pclass: 3
Age: 25.0
Sex: male
Fare: 7.05
Embarked: S
```
**Card 4**
```
name: Eustis, Miss. Elizabeth Mussey
Pclass: 1
Age: 54.0
Sex: female
Fare: 78.27
Embarked: C
```
**Card 5**
```
name: Harder, Mr. George Achilles
Pclass: 1
Age: 25.0
Sex: male
Fare: 55.44
Embarked: C
```
**Card 6**
```
name: Adams, Mr. John
Pclass: 3
Age: 26.0
Sex: male
Fare: 8.05
Embarked: S
```

---
### GM Guide

> **Hint:** GM Hint: Refer to the box plot above. The forged card has a fare that doesn't match its class - either much higher or much lower than typical for that class. Players should compare each card's fare with the distribution shown in the chart for that card's class.
> **Answer:** [[REVEAL_ANSWER]]The forged card: 1st class (Pclass=1) but paying £643.46, which is much higher than typical 1st class fares (£5.00-512.33). **(In this game, this card is Card 2)**[[END_REVEAL]]
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

- Echo A: Hassab boards at Cherbourg (C); a first-class ticket rustles in hand.
- Echo B: Lanterns sway as the deck tilts; Turpin steadies a stranger amid rising alarm.
- Echo C: In the final chaos, Moubarek finds space in a lifeboat and slips into the night.
- Echo D: Ryan boards at Queenstown (Q); a third-class ticket rustles in hand.
- Echo E: Goldsmith boards at Southampton (S); a third-class ticket rustles in hand.

**Task:** Arrange the echoes (A–E) in correct chronological order.

---
### GM Guide

> **Answer:** [[REVEAL_ANSWER]]Correct order: E, A, D, B, C. Boarding echoes come first and follow port order S → C → Q; post-impact echoes (tilted/helping/chaos) follow; the lifeboat escape is last.[[END_REVEAL]]
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
Name: Doling, Miss. Elsie
Pclass: 2
Age: 18
Sex: female
Fare: 23.0
Embarked: S
```
**Card 2**
```
Name: Warren, Mrs. Frank Manley (Anna Sophia Atkinson)
Pclass: 1
Age: 60
Sex: female
Fare: 75.25
Embarked: C
```
**Card 3**
```
Name: Fry, Mr. Richard
Pclass: 1
Age: 25
Sex: male
Fare: 0.0
Embarked: S
```
**Card 4**
```
Name: Angle, Mrs. William A (Florence "Mary" Agnes Hughes)
Pclass: 2
Age: 36
Sex: female
Fare: 26.0
Embarked: S
```

---
### GM Guide

> **Hint:** Use the survival charts above to infer the 4-digit lifeboat code.
> **Answer:** [[REVEAL_ANSWER]]1101[[END_REVEAL]]
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

My secret alias is Stephenson, Mrs. Walter Bertram (Martha Eustis). It's quite comfortable here in first class!

A Guest of the Deep
```
### A Mysterious Code 

![Encoded Alphabet Grid](./challenge_4_puzzle_images\encoded_alphabet_img.png)

![Puzzle Cipher](./challenge_4_puzzle_images\bill_cipher_img.png)

### A Strange Sound 
![Morse Alphabet](./challenge_4_puzzle_images\morse_code_alphabet.jpg)

[[PLAY_SOUND]]morse.wav[[END_SOUND]]
> **A Mysterious Code Hint:** [[REVEAL_HINT]]![Plaintext Alphabet Grid](./challenge_4_puzzle_images\plaintext_alphabet_img.png)[[END_HINT]]
> **A Strange Sound Hint:** [[REVEAL_HINT]]....   .   .-..   .-..   ---   [[END_HINT]]
---
## Game End

Congratulations! You've collected all 5 coordinate fragments, restarted the time machine, and successfully escaped from 1912 at the moment the Titanic sank.
