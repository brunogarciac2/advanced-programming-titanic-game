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
name: Flynn, Mr. John
Pclass: 3
Age: nan
Sex: male
Fare: 6.95
Embarked: Q
```
**Card 2**
```
name: Pavlovic, Mr. Stefo
Pclass: 3
Age: 32.0
Sex: male
Fare: 7.9
Embarked: S
```
**Card 3**
```
name: Braund, Mr. Owen Harris
Pclass: 3
Age: 22.0
Sex: male
Fare: 513.59
Embarked: S
```
**Card 4**
```
name: Pears, Mrs. Thomas (Edith Wearne)
Pclass: 1
Age: 22.0
Sex: female
Fare: 66.6
Embarked: S
```
**Card 5**
```
name: Denkoff, Mr. Mitto
Pclass: 3
Age: nan
Sex: male
Fare: 7.9
Embarked: S
```
**Card 6**
```
name: Caldwell, Mrs. Albert Francis (Sylvia Mae Harbaugh)
Pclass: 2
Age: 22.0
Sex: female
Fare: 29.0
Embarked: S
```

---
### GM Guide

> **Hint:** GM Hint: Refer to the box plot above. The forged card has a fare that doesn't match its class - either much higher or much lower than typical for that class. Players should compare each card's fare with the distribution shown in the chart for that card's class.
> **Answer:** [[REVEAL_ANSWER]]The forged card: 3rd class (Pclass=3) but paying £513.59, which is much higher than typical 3rd class fares (£4.01-69.55). **(In this game, this card is Card 3)**[[END_REVEAL]]
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
Name: Doharr, Mr. Tannous
Pclass: 3
Age: 50
Sex: male
Fare: 7.23
Embarked: C
```
**Card 2**
```
Name: Moen, Mr. Sigurd Hansen
Pclass: 3
Age: 25
Sex: male
Fare: 7.65
Embarked: S
```
**Card 3**
```
Name: Vovk, Mr. Janko
Pclass: 3
Age: 22
Sex: male
Fare: 7.9
Embarked: S
```
**Card 4**
```
Name: Backstrom, Mrs. Karl Alfred (Maria Mathilda Gustafsson)
Pclass: 3
Age: 33
Sex: female
Fare: 15.85
Embarked: S
```

---
### GM Guide

> **Hint:** Use the survival charts above to infer the 4-digit lifeboat code.
> **Answer:** [[REVEAL_ANSWER]]0001[[END_REVEAL]]
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

|     | Name                                            |   Pclass | Sex    |   Age |   Survived |

|----:|:------------------------------------------------|---------:|:-------|------:|-----------:|

| 532 | Elias, Mr. Joseph Jr                            |        3 | male   |    17 |          0 |

| 109 | Moran, Miss. Bertha                             |        3 | female |   nan |          1 |

| 342 | Collander, Mr. Erik Gustaf                      |        2 | male   |    28 |          0 |

| 589 | Murdlin, Mr. Joseph                             |        3 | male   |   nan |          0 |

| 376 | Landergren, Miss. Aurora Adelia                 |        3 | female |    22 |          1 |

| 246 | Lindahl, Miss. Agda Thorilda Viktoria           |        3 | female |    25 |          0 |

|  68 | Andersson, Miss. Erna Alexandra                 |        3 | female |    17 |          1 |

| 626 | Kirkland, Rev. Charles Leonard                  |        2 | male   |    57 |          0 |

| 231 | Larsson, Mr. Bengt Edvin                        |        3 | male   |    29 |          0 |

|  11 | Bonnell, Miss. Elizabeth                        |        1 | female |    58 |          1 |

| 338 | Dahl, Mr. Karl Edwart                           |        3 | male   |    45 |          1 |

| 145 | Nicholls, Mr. Joseph Charles                    |        2 | male   |    19 |          0 |

| 194 | Brown, Mrs. James Joseph (Margaret Tobin)       |        1 | female |    44 |          1 |

| 719 | Johnson, Mr. Malkolm Joackim                    |        3 | male   |    33 |          0 |

| 866 | Duran y More, Miss. Asuncion                    |        2 | female |    27 |          1 |

| 512 | McGough, Mr. James Robert                       |        1 | male   |    36 |          1 |

| 617 | Lobb, Mrs. William Arthur (Cordelia K Stanlick) |        3 | female |    26 |          0 |

| 533 | Peter, Mrs. Catherine (Catherine Rizk)          |        3 | female |   nan |          1 |

| 258 | Ward, Miss. Anna                                |        1 | female |    35 |          1 |

|  77 | Moutal, Mr. Rahamin Haim                        |        3 | male   |   nan |          0 |

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
[[PLAY_SOUND]]sound.mp3[[END_SOUND]]
---
## Game End

Congratulations! You've collected all 5 coordinate fragments, restarted the time machine, and successfully escaped from 1912 at the moment the Titanic sank.
