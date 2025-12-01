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
name: Johansson, Mr. Erik
Pclass: 3
Age: 22.0
Sex: male
Fare: 7.8
Embarked: S
```
**Card 2**
```
name: Allen, Mr. William Henry
Pclass: 3
Age: 35.0
Sex: male
Fare: 8.05
Embarked: S
```
**Card 3**
```
name: Allen, Miss. Elisabeth Walton
Pclass: 1
Age: 29.0
Sex: female
Fare: 211.34
Embarked: S
```
**Card 4**
```
name: Navratil, Master. Edmond Roger
Pclass: 2
Age: 2.0
Sex: male
Fare: 26.0
Embarked: S
```
**Card 5**
```
name: Dick, Mrs. Albert Adrian (Vera Gillespie)
Pclass: 1
Age: 17.0
Sex: female
Fare: 57.0
Embarked: S
```
**Card 6**
```
name: Baxter, Mrs. James (Helene DeLaudeniere Chaput)
Pclass: 1
Age: 50.0
Sex: female
Fare: 534.57
Embarked: C
```

---
### GM Guide

> **Hint:** GM Hint: Refer to the box plot above. The forged card has a fare that doesn't match its class - either much higher or much lower than typical for that class. Players should compare each card's fare with the distribution shown in the chart for that card's class.
> **Answer:** [[REVEAL_ANSWER]]The forged card: 1st class (Pclass=1) but paying £534.57, which is much higher than typical 1st class fares (£5.00-512.33). **(In this game, this card is Card 6)**[[END_REVEAL]]
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

- Echo A: Drazenoic boards at Cherbourg (C); a third-class ticket rustles in hand.
- Echo B: Rice boards at Queenstown (Q); a third-class ticket rustles in hand.
- Echo C: Cacic boards at Southampton (S); a third-class ticket rustles in hand.
- Echo D: In the final chaos, Collyer finds space in a lifeboat and slips into the night.
- Echo E: Lanterns sway as the deck tilts; Buss steadies a stranger amid rising alarm.

**Task:** Arrange the echoes (A–E) in correct chronological order.

---
### GM Guide

> **Answer:** [[REVEAL_ANSWER]]Correct order: C, A, B, E, D. Boarding echoes come first and follow port order S → C → Q; post-impact echoes (tilted/helping/chaos) follow; the lifeboat escape is last.[[END_REVEAL]]
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
Name: Skoog, Master. Harald
Pclass: 3
Age: 4
Sex: male
Fare: 27.9
Embarked: S
```
**Card 2**
```
Name: Nysten, Miss. Anna Sofia
Pclass: 3
Age: 22
Sex: female
Fare: 7.75
Embarked: S
```
**Card 3**
```
Name: Moss, Mr. Albert Johan
Pclass: 3
Age: 31
Sex: male
Fare: 7.78
Embarked: S
```
**Card 4**
```
Name: Wilhelms, Mr. Charles
Pclass: 2
Age: 31
Sex: male
Fare: 13.0
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
    The Captain has created a list of 20 suspects. Can you decipher the letter and
    obtain the identity of the suspect before they get away?!
    
    

**Task:** Decode the encrypted letter and select the name from the list of suspects.

### Possible suspects 

![Suspect Table](./assets/images\suspect_table.png)

### Letters from the Stowaway 

**Plaintext Letter**```
R.M.S. TITANIC
MARCONI WIRELESS SERVICE
APRIL 12, 1912
Dear Friend,
Life aboard this magnificent ship feels like living in paradise.
Each morning begins with breakfast served at elegant dining rooms where delectable cuisine awaits us all alongside delightful conversations over coffee breaks by the grand piano tunes echoing through our corridors.
 
The afternoon is filled to a brim, as we wander across decks adorned with stunning artwork and lush gardens. Gentle strolls on deck offer breathtaking views of endless ocean horizons.
In evenings comes relaxation time; warm firesides await where family stories are shared while children play games that captivate every heart aboard this grand vessel.
Life here truly feels like floating through a luxurious dream as we sail across the great blue sea with nothing but wonder around us. 
Warmest regards,
A Passenger on Board the Titanic```
**Encrypted Letter**```
R.M.S. TITANIC
MARCONI WIRELESS SERVICE
APRIL 12, 1912
It's a bit cramped here in third class! Dear Reader,
I am aboard The Titanic today experiencing an extraordinary journey across the North Atlantic Ocean.
Life onboard this magnificent vessel offers unparalleled luxury with grand dining rooms adorned in exquisite crystal chandeliers; spacious suites featuring marble bathrooms fitted with gold-plated fixtures, opulent bedrooms equipped to accommodate six people comfortably and elegantly furnished. 
The ship is bustling as passengers excitedly explore every nook of The Titanic's vast facilities including the elegant lounge where one can indulge themselves while sipping champagne or enjoying a classic French meal prepared by our world-renowned chefs.
We also have access to an array of entertainment options such as opulent theaters, art galleries featuring renowned works and even indoor swimming pools with heated waters for relaxation. 
I cannot wait until we arrive in New York City on this majestic ship!
Sincerely,
A Passenger aboard The Titanic```
### A Mysterious Code 

![Encoded Alphabet Grid](./assets/images\encoded_alphabet_img.png)

![Puzzle Cipher](./assets/images\bill_cipher_img.png)

### A Strange Sound 
![Morse Alphabet](./assets/images\morse_code_alphabet.jpg)

[[PLAY_SOUND]]./assets/audio\morse.wav[[END_SOUND]]
> **Letters from a Stowaway:** [[REVEAL_HINT]]Caeser Cipher with key: 24[[END_HINT]] **A Mysterious Code Hint:** [[REVEAL_HINT]]![Plaintext Alphabet Grid](./assets/images\plaintext_alphabet_img.png)[[END_HINT]] **A Strange Sound Hint:** [[REVEAL_HINT]]--   .-   .-..   .   [[END_HINT]]
> **Final Answer:** [[REVEAL_ANSWER]]The alias of the Guest from the Deep is: Saundercock, Mr. William Henry[[END_REVEAL]]---
## Game End

Congratulations! You've collected all 5 coordinate fragments, restarted the time machine, and successfully escaped from 1912 at the moment the Titanic sank.
