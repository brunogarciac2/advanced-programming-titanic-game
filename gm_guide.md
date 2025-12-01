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
name: Nosworthy, Mr. Richard Cater
Pclass: 1
Age: 21.0
Sex: male
Fare: 3.55
Embarked: S
```
**Card 2**
```
name: Holm, Mr. John Fredrik Alexander
Pclass: 3
Age: 43.0
Sex: male
Fare: 6.45
Embarked: S
```
**Card 3**
```
name: Cor, Mr. Liudevit
Pclass: 3
Age: 19.0
Sex: male
Fare: 7.9
Embarked: S
```
**Card 4**
```
name: Lulic, Mr. Nikola
Pclass: 3
Age: 27.0
Sex: male
Fare: 8.66
Embarked: S
```
**Card 5**
```
name: Butt, Major. Archibald Willingham
Pclass: 1
Age: 45.0
Sex: male
Fare: 26.55
Embarked: S
```
**Card 6**
```
name: Harris, Mr. Henry Birkhardt
Pclass: 1
Age: 45.0
Sex: male
Fare: 83.47
Embarked: S
```

---
### GM Guide

> **Hint:** GM Hint: Refer to the box plot above. The forged card has a fare that doesn't match its class - either much higher or much lower than typical for that class. Players should compare each card's fare with the distribution shown in the chart for that card's class.
> **Answer:** [[REVEAL_ANSWER]]The forged card: 1st class (Pclass=1) but paying £3.55, which is much lower than typical 1st class fares (£5.00-512.33). **(In this game, this card is Card 1)**[[END_REVEAL]]
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

- Echo A: Lanterns sway as the deck tilts; Moubarek steadies a stranger amid rising alarm.
- Echo B: Smith boards at Queenstown (Q); a third-class ticket rustles in hand.
- Echo C: Beesley boards at Southampton (S); a second-class ticket rustles in hand.
- Echo D: In the final chaos, Heininen finds space in a lifeboat and slips into the night.
- Echo E: Lurette boards at Cherbourg (C); a first-class ticket rustles in hand.

**Task:** Arrange the echoes (A–E) in correct chronological order.

---
### GM Guide

> **Answer:** [[REVEAL_ANSWER]]Correct order: C, E, B, A, D. Boarding echoes come first and follow port order S → C → Q; post-impact echoes (tilted/helping/chaos) follow; the lifeboat escape is last.[[END_REVEAL]]
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
Name: Emir, Mr. Farred Chehab
Pclass: 3
Age: 32
Sex: male
Fare: 7.22
Embarked: C
```
**Card 2**
```
Name: McCormack, Mr. Thomas Joseph
Pclass: 3
Age: 27
Sex: male
Fare: 7.75
Embarked: Q
```
**Card 3**
```
Name: Cumings, Mrs. John Bradley (Florence Briggs Thayer)
Pclass: 1
Age: 38
Sex: female
Fare: 71.28
Embarked: C
```
**Card 4**
```
Name: Flynn, Mr. James
Pclass: 3
Age: 48
Sex: male
Fare: 7.75
Embarked: Q
```

---
### GM Guide

> **Hint:** Use the survival charts above to infer the 4-digit lifeboat code.
> **Answer:** [[REVEAL_ANSWER]]0110[[END_REVEAL]]
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
Dear Reader,
Life aboard our magnificent vessel, The Titanic, was nothing less than extraordinary as we sailed through crystal-clear waters under an endless azure sky.
Our daily routine included enjoying the lavish onboard amenities such as luxurious dining halls serving gourmet meals prepared by skilled chefs; elegant lounges filled with conversation and laughter echoing off polished floors. Families gathered in cozy suites while young travelers marveled at interactive exhibits designed to educate them about our journey across oceans, all surrounded by sumptuous decor that spoke of opulence.
Evenings were reserved for entertainment as performers showcased stunning dances on decks adorned with glittering lights or captivated audiences during captivating plays told through vivid set designs. We also took time each day aboard the ship's swimming pool and gymnasium to maintain a healthy balance amidst our travels, all while basking in an atmosphere of comfort that made every moment feel like paradise.
As we sailed onward towards distant shores filled with promise for new adventures yet unknown, life on board The Titanic was nothing short of spectacular.```
**Encrypted Letter**```
R.M.S. TITANIC
MARCONI WIRELESS SERVICE
APRIL 12, 1912
It's a bit cramped here in third class! Dear Friend,
I hope this message finds you well.
Life aboard The Titanic has been an extraordinary experience so far! From dawn until dusk we spend our days enjoying luxurious amenities that cater to every whimâ€”fine dining with delectable meals prepared by skilled chefs, relaxing in the opulent suites furnished with plush carpets and elegant decor. Guests can unwind at lavish spas offering massages or soak up sunrises on deck while taking advantage of state-of-the-art entertainment options like live performances.
The ship is equipped with modern conveniences including Wi-Fi throughout its vast corridors so passengers are always connected to friends, family members back home as well as the latest news and events. The staff go out of their way ensuring our comfort from room service attendants offering delicious meals at every meal all day long right up until midnight on certain nights.
We have also been treated with endless entertainment choices such as Broadway shows or exciting sports like tennis matches taking place just a few steps away! With so many activities to enjoy, itâ€™s easy not wanting even think about getting bored during our time aboard!
Life onboard The Titanic is truly beyond anything I could ever imagine before arriving here. We are fortunate enough that we have access to such luxury and comfort while traveling across the world.
Warm regards,
Someone on board The Titanic```
### A Mysterious Code 

![Encoded Alphabet Grid](./assets/images\encoded_alphabet_img.png)

![Puzzle Cipher](./assets/images\bill_cipher_img.png)

### A Strange Sound 
![Morse Alphabet](./assets/images\morse_code_alphabet.jpg)

[[PLAY_SOUND]]./assets/audio\morse.wav[[END_SOUND]]
> **Letters from a Stowaway:** [[REVEAL_HINT]]Caeser Cipher with key: 4[[END_HINT]] **A Mysterious Code Hint:** [[REVEAL_HINT]]![Plaintext Alphabet Grid](./assets/images\plaintext_alphabet_img.png)[[END_HINT]] **A Strange Sound Hint:** [[REVEAL_HINT]]--   .-   .-..   .   [[END_HINT]]
> **Final Answer:** [[REVEAL_ANSWER]]The alias of the Guest from the Deep is: Allen, Mr. William Henry[[END_REVEAL]]---
## Game End

Congratulations! You've collected all 5 coordinate fragments, restarted the time machine, and successfully escaped from 1912 at the moment the Titanic sank.
