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
name: Ponesell, Mr. Martin
Pclass: 2
Age: 34.0
Sex: male
Fare: 13.0
Embarked: S
```
**Card 2**
```
name: Stewart, Mr. Albert A
Pclass: 1
Age: nan
Sex: male
Fare: 27.72
Embarked: C
```
**Card 3**
```
name: Bissette, Miss. Amelia
Pclass: 1
Age: 35.0
Sex: female
Fare: 135.63
Embarked: S
```
**Card 4**
```
name: Ward, Miss. Anna
Pclass: 1
Age: 35.0
Sex: female
Fare: 512.33
Embarked: C
```
**Card 5**
```
name: Hewlett, Mrs. (Mary D Kingcome) 
Pclass: 2
Age: 55.0
Sex: female
Fare: 16.0
Embarked: S
```
**Card 6**
```
name: Newell, Miss. Marjorie
Pclass: 1
Age: 23.0
Sex: female
Fare: 3.7
Embarked: C
```

---
### GM Guide

> **Hint:** GM Hint: Refer to the box plot above. The forged card has a fare that doesn't match its class - either much higher or much lower than typical for that class. Players should compare each card's fare with the distribution shown in the chart for that card's class.
> **Answer:** [[REVEAL_ANSWER]]The forged card: 1st class (Pclass=1) but paying £3.70, which is much lower than typical 1st class fares (£5.00-512.33). **(In this game, this card is Card 6)**[[END_REVEAL]]
> **Obtain:** **Temporal Coordinate Fragment 1** hidden under the forged card.

---
## Decipher the Lifeboat Code

**Story:** The lifeboat lock requires a 4-digit code based on passengers' survival predictions.

**Task:** Predict which of the 4 passengers survived (1) or perished (0). Use the survival clues provided.

![Hint Chart 1](hint/challenge_3_sex_pclass.png)

![Hint Chart 2](hint/challenge_3_age_group.png)

### Passenger Cards (Show to Players)

**Card 1**
```
Name: Taussig, Mr. Emil
Pclass: 1
Age: 52
Sex: male
Fare: 79.65
Embarked: S
```
**Card 2**
```
Name: Frolicher-Stehli, Mr. Maxmillian
Pclass: 1
Age: 60
Sex: male
Fare: 79.2
Embarked: C
```
**Card 3**
```
Name: Glynn, Miss. Mary Agatha
Pclass: 3
Age: 30
Sex: female
Fare: 7.75
Embarked: Q
```
**Card 4**
```
Name: Frauenthal, Mrs. Henry William (Clara Heinsheimer)
Pclass: 1
Age: 41
Sex: female
Fare: 133.65
Embarked: S
```

---
### GM Guide

> **Hint:** Use the survival charts above to infer the 4-digit lifeboat code.
> **Answer:** [[REVEAL_ANSWER]]0111[[END_REVEAL]]
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

My secret alias is Mr James Moran. It's a bit cramped here in third class!

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
