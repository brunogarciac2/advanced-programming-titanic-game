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
name: Ringhini, Mr. Sante
Pclass: 1
Age: 22.0
Sex: male
Fare: 135.63
Embarked: C
```
**Card 2**
```
name: Givard, Mr. Hans Kristensen
Pclass: 2
Age: 30.0
Sex: male
Fare: 13.0
Embarked: S
```
**Card 3**
```
name: Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)
Pclass: 3
Age: 38.0
Sex: female
Fare: 31.39
Embarked: S
```
**Card 4**
```
name: Salkjelsvik, Miss. Anna Kristine
Pclass: 3
Age: 21.0
Sex: female
Fare: 7.65
Embarked: S
```
**Card 5**
```
name: Jermyn, Miss. Annie
Pclass: 2
Age: nan
Sex: female
Fare: 92.03
Embarked: Q
```
**Card 6**
```
name: Kiernan, Mr. Philip
Pclass: 3
Age: nan
Sex: male
Fare: 7.75
Embarked: Q
```

---
### GM Guide

> **Hint:** GM Hint: Refer to the box plot above. The forged card has a fare that doesn't match its class - either much higher or much lower than typical for that class. Players should compare each card's fare with the distribution shown in the chart for that card's class.
> **Answer:** [[REVEAL_ANSWER]]The forged card: 2nd class (Pclass=2) but paying £92.03, which doesn't match typical 2nd class fares (£10.50-73.50). **(In this game, this card is Card 5)**[[END_REVEAL]]
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
Name: Butt, Major. Archibald Willingham
Pclass: 1
Age: 45
Sex: male
Fare: 26.55
Embarked: S
```
**Card 2**
```
Name: Madsen, Mr. Fridtjof Arne
Pclass: 3
Age: 24
Sex: male
Fare: 7.14
Embarked: S
```
**Card 3**
```
Name: Coutts, Master. Eden Leslie "Neville"
Pclass: 3
Age: 9
Sex: male
Fare: 15.9
Embarked: S
```
**Card 4**
```
Name: Jarvis, Mr. John Denzil
Pclass: 2
Age: 47
Sex: male
Fare: 15.0
Embarked: S
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
    The Captain has created a list of 10 suspects. Can you decipher the letter and
    obtain the identity of the suspect before they get away?!
    
    

**Task:** Decode the encrypted letter and select the name from the list of suspects.

### Possible suspects 

|     | Name                                                |   Pclass | Sex    |   Age |   Survived |

|----:|:----------------------------------------------------|---------:|:-------|------:|-----------:|

| 506 | Quick, Mrs. Frederick Charles (Jane Richards)       |        2 | female |    33 |          1 |

| 886 | Montvila, Rev. Juozas                               |        2 | male   |    27 |          0 |

| 101 | Petroff, Mr. Pastcho ("Pentcho")                    |        3 | male   |   nan |          0 |

| 359 | Mockler, Miss. Helen Mary "Ellie"                   |        3 | female |   nan |          1 |

| 850 | Andersson, Master. Sigvard Harald Elias             |        3 | male   |     4 |          0 |

| 515 | Walker, Mr. William Anderson                        |        1 | male   |    47 |          0 |

| 808 | Meyer, Mr. August                                   |        2 | male   |    39 |          0 |

| 131 | Coelho, Mr. Domingos Fernandeo                      |        3 | male   |    20 |          0 |

| 852 | Boulos, Miss. Nourelain                             |        3 | female |     9 |          0 |

| 600 | Jacobsohn, Mrs. Sidney Samuel (Amy Frances Christy) |        2 | female |    24 |          1 |

| 611 | Jardin, Mr. Jose Neto                               |        3 | male   |   nan |          0 |

| 275 | Andrews, Miss. Kornelia Theodosia                   |        1 | female |    63 |          1 |

| 562 | Norman, Mr. Robert Douglas                          |        2 | male   |    28 |          0 |

| 617 | Lobb, Mrs. William Arthur (Cordelia K Stanlick)     |        3 | female |    26 |          0 |

| 202 | Johanson, Mr. Jakob Alfred                          |        3 | male   |    34 |          0 |

| 636 | Leinonen, Mr. Antti Gustaf                          |        3 | male   |    32 |          0 |

|  23 | Sloper, Mr. William Thompson                        |        1 | male   |    28 |          1 |

| 723 | Hodges, Mr. Henry Price                             |        2 | male   |    50 |          0 |

| 257 | Cherry, Miss. Gladys                                |        1 | female |    30 |          1 |

| 745 | Crosby, Capt. Edward Gifford                        |        1 | male   |    70 |          0 |

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
