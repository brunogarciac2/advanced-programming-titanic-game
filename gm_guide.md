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
name: Cacic, Miss. Marija
Pclass: 3
Age: 30.0
Sex: female
Fare: 8.66
Embarked: S
```
**Card 2**
```
name: Funk, Miss. Annie Clemmer
Pclass: 2
Age: 38.0
Sex: female
Fare: 13.0
Embarked: S
```
**Card 3**
```
name: Partner, Mr. Austen
Pclass: 3
Age: 45.5
Sex: male
Fare: 177.16
Embarked: S
```
**Card 4**
```
name: Chapman, Mr. Charles Henry
Pclass: 2
Age: 52.0
Sex: male
Fare: 13.5
Embarked: S
```
**Card 5**
```
name: Bonnell, Miss. Elizabeth
Pclass: 1
Age: 58.0
Sex: female
Fare: 26.55
Embarked: S
```
**Card 6**
```
name: Mamee, Mr. Hanna
Pclass: 3
Age: nan
Sex: male
Fare: 7.23
Embarked: C
```

---
### GM Guide

> **Hint:** GM Hint: Refer to the box plot above. The forged card has a fare that doesn't match its class - either much higher or much lower than typical for that class. Players should compare each card's fare with the distribution shown in the chart for that card's class.
> **Answer:** [[REVEAL_ANSWER]]The forged card: 3rd class (Pclass=3) but paying £177.16, which is much higher than typical 3rd class fares (£4.01-69.55). **(In this game, this card is Card 3)**[[END_REVEAL]]
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
Name: Daniel, Mr. Robert Williams
Pclass: 1
Age: 27
Sex: male
Fare: 30.5
Embarked: S
```
**Card 2**
```
Name: Drazenoic, Mr. Jozef
Pclass: 3
Age: 33
Sex: male
Fare: 7.9
Embarked: C
```
**Card 3**
```
Name: Foreman, Mr. Benjamin Laventall
Pclass: 1
Age: 30
Sex: male
Fare: 27.75
Embarked: C
```
**Card 4**
```
Name: Adams, Mr. John
Pclass: 3
Age: 26
Sex: male
Fare: 8.05
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

|     | Name                                           |   Pclass | Sex    |   Age |   Survived |

|----:|:-----------------------------------------------|---------:|:-------|------:|-----------:|

| 878 | Laleff, Mr. Kristo                             |        3 | male   | nan   |          0 |

| 303 | Keane, Miss. Nora A                            |        2 | female | nan   |          1 |

| 643 | Foo, Mr. Choong                                |        3 | male   | nan   |          1 |

|  82 | McDermott, Miss. Brigdet Delia                 |        3 | female | nan   |          1 |

|   6 | McCarthy, Mr. Timothy J                        |        1 | male   |  54   |          0 |

| 612 | Murphy, Miss. Margaret Jane                    |        3 | female | nan   |          1 |

| 203 | Youseff, Mr. Gerious                           |        3 | male   |  45.5 |          0 |

|  40 | Ahlin, Mrs. Johan (Johanna Persdotter Larsson) |        3 | female |  40   |          0 |

| 863 | Sage, Miss. Dorothy Edith "Dolly"              |        3 | female | nan   |          0 |

| 177 | Isham, Miss. Ann Elizabeth                     |        1 | female |  50   |          0 |

|  32 | Glynn, Miss. Mary Agatha                       |        3 | female | nan   |          1 |

| 312 | Lahtinen, Mrs. William (Anna Sylfven)          |        2 | female |  26   |          0 |

| 402 | Jussila, Miss. Mari Aina                       |        3 | female |  21   |          0 |

| 715 | Soholt, Mr. Peter Andreas Lauritz Andersen     |        3 | male   |  19   |          0 |

|  80 | Waelens, Mr. Achille                           |        3 | male   |  22   |          0 |

| 115 | Pekoniemi, Mr. Edvard                          |        3 | male   |  21   |          0 |

| 215 | Newell, Miss. Madeleine                        |        1 | female |  31   |          1 |

| 201 | Sage, Mr. Frederick                            |        3 | male   | nan   |          0 |

| 567 | Palsson, Mrs. Nils (Alma Cornelia Berglund)    |        3 | female |  29   |          0 |

| 276 | Lindblom, Miss. Augusta Charlotta              |        3 | female |  45   |          0 |

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

My secret alias is Mr James Moran. It's quite comfortable here in first class!

A Guest of the Deep
```
### A Mysterious Code 

![Alphabet Grid](./challenge_4_puzzle_images\alpha_cipher_img.png)

![Puzzle Cipher](./challenge_4_puzzle_images\bill_cipher_img.png)

---
## Game End

Congratulations! You've collected all 5 coordinate fragments, restarted the time machine, and successfully escaped from 1912 at the moment the Titanic sank.
