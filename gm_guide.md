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
name: Smith, Mr. Thomas
Pclass: 3
Age: nan
Sex: male
Fare: 7.75
Embarked: Q
```
**Card 2**
```
name: Bailey, Mr. Percy Andrew
Pclass: 2
Age: 18.0
Sex: male
Fare: 11.5
Embarked: S
```
**Card 3**
```
name: Bonnell, Miss. Elizabeth
Pclass: 1
Age: 58.0
Sex: female
Fare: 26.55
Embarked: S
```
**Card 4**
```
name: Beane, Mrs. Edward (Ethel Clarke)
Pclass: 2
Age: 19.0
Sex: female
Fare: 7.39
Embarked: S
```
**Card 5**
```
name: Nicola-Yarred, Master. Elias
Pclass: 3
Age: 12.0
Sex: male
Fare: 11.24
Embarked: C
```
**Card 6**
```
name: Barton, Mr. David John
Pclass: 3
Age: 22.0
Sex: male
Fare: 8.05
Embarked: S
```

---
### GM Guide

> **Hint:** GM Hint: Refer to the box plot above. The forged card has a fare that doesn't match its class - either much higher or much lower than typical for that class. Players should compare each card's fare with the distribution shown in the chart for that card's class.
> **Answer:** [[REVEAL_ANSWER]]The forged card: 2nd class (Pclass=2) but paying £7.39, which is much lower than typical 2nd class fares (£10.50-73.50). **(In this game, this card is Card 4)**[[END_REVEAL]]
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

- Echo A: Lanterns sway as the deck tilts; Tornquist steadies a stranger amid rising alarm.
- Echo B: Burke boards at Queenstown (Q); a third-class ticket rustles in hand.
- Echo C: In the final chaos, Karun finds space in a lifeboat and slips into the night.
- Echo D: Meyer boards at Southampton (S); a second-class ticket rustles in hand.
- Echo E: Rothschild boards at Cherbourg (C); a first-class ticket rustles in hand.

**Task:** Arrange the echoes (A–E) in correct chronological order.

---
### GM Guide

> **Answer:** [[REVEAL_ANSWER]]Correct order: D, E, B, A, C. Boarding echoes come first and follow port order S → C → Q; post-impact echoes (tilted/helping/chaos) follow; the lifeboat escape is last.[[END_REVEAL]]
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
Name: Garside, Miss. Ethel
Pclass: 2
Age: 34
Sex: female
Fare: 13.0
Embarked: S
```
**Card 2**
```
Name: Bazzani, Miss. Albina
Pclass: 1
Age: 32
Sex: female
Fare: 76.29
Embarked: C
```
**Card 3**
```
Name: Hart, Miss. Eva Miriam
Pclass: 2
Age: 7
Sex: female
Fare: 26.25
Embarked: S
```
**Card 4**
```
Name: Rekic, Mr. Tido
Pclass: 3
Age: 38
Sex: male
Fare: 7.9
Embarked: S
```

---
### GM Guide

> **Hint:** Use the survival charts above to infer the 4-digit lifeboat code.
> **Answer:** [[REVEAL_ANSWER]]1110[[END_REVEAL]]
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

![Suspect Table](./challenge_4_puzzle_images\suspect_table.png)

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

![Encoded Alphabet Grid](./challenge_4_puzzle_images\encoded_alphabet_img.png)

![Puzzle Cipher](./challenge_4_puzzle_images\bill_cipher_img.png)

### A Strange Sound 
![Morse Alphabet](./challenge_4_puzzle_images\morse_code_alphabet.jpg)

[[PLAY_SOUND]]morse.wav[[END_SOUND]]
> **Letters from a Stowaway:** [[REVEAL_HINT]]Caeser Cipher with key: 11[[END_HINT]] **A Mysterious Code Hint:** [[REVEAL_HINT]]![Plaintext Alphabet Grid](./challenge_4_puzzle_images\plaintext_alphabet_img.png)[[END_HINT]] **A Strange Sound Hint:** [[REVEAL_HINT]]..-.   .   --   .-   .-..   .   [[END_HINT]]
> **Final Answer:** [[REVEAL_ANSWER]]The alias of the Guest from the Deep is: McDermott, Miss. Brigdet Delia[[END_REVEAL]]---
## Game End

Congratulations! You've collected all 5 coordinate fragments, restarted the time machine, and successfully escaped from 1912 at the moment the Titanic sank.
