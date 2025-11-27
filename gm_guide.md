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
name: Turja, Miss. Anna Sofia
Pclass: 3
Age: 18.0
Sex: female
Fare: 9.84
Embarked: S
```
**Card 2**
```
name: Slemen, Mr. Richard James
Pclass: 2
Age: 35.0
Sex: male
Fare: 10.5
Embarked: S
```
**Card 3**
```
name: Markun, Mr. Johann
Pclass: 3
Age: 33.0
Sex: male
Fare: 7.9
Embarked: S
```
**Card 4**
```
name: Hagland, Mr. Konrad Mathias Reiersen
Pclass: 3
Age: nan
Sex: male
Fare: 19.97
Embarked: S
```
**Card 5**
```
name: Dean, Master. Bertram Vere
Pclass: 1
Age: 1.0
Sex: male
Fare: 9.29
Embarked: S
```
**Card 6**
```
name: Uruchurtu, Don. Manuel E
Pclass: 1
Age: 40.0
Sex: male
Fare: 27.72
Embarked: C
```

---
### GM Guide

> **Hint:** GM Hint: Refer to the box plot above. The forged card has a fare that doesn't match its class - either much higher or much lower than typical for that class. Players should compare each card's fare with the distribution shown in the chart for that card's class.
> **Answer:** [[REVEAL_ANSWER]]The forged card: 1st class (Pclass=1) but paying £9.29, which is much lower than typical 1st class fares (£5.00-512.33). **(In this game, this card is Card 5)**[[END_REVEAL]]
> **Obtain:** **Temporal Coordinate Fragment 1** hidden under the forged card.

---
## Decipher the Lifeboat Code

**Story:** The lifeboat lock requires a 4-digit code based on passengers' survival predictions.

**Task:** Predict which of the 4 passengers survived (1) or perished (0). Use the survival clues provided.

### Passenger Cards (Show to Players)

**Card 1**
```
Name: Webber, Miss. Susan
Pclass: 2
Age: 32
Sex: female
Fare: 13.0
Embarked: S
```
**Card 2**
```
Name: Rugg, Miss. Emily
Pclass: 2
Age: 21
Sex: female
Fare: 10.5
Embarked: S
```
**Card 3**
```
Name: Clarke, Mrs. Charles V (Ada Maria Winfield)
Pclass: 2
Age: 28
Sex: female
Fare: 26.0
Embarked: S
```
**Card 4**
```
Name: Baxter, Mr. Quigg Edmond
Pclass: 1
Age: 24
Sex: male
Fare: 247.52
Embarked: C
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
    The Captain has created a list of 10 suspects. Can you decipher the letter and
    obtain the identity of the suspect before they get away?!
    
    

**Task:** Decode the encrypted letter and select the name from the list of suspects.

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
### Possible suspects 

|     | Name                                                     |   Pclass | Sex    |   Age |   Survived |

|----:|:---------------------------------------------------------|---------:|:-------|------:|-----------:|

| 590 | Rintamaki, Mr. Matti                                     |        3 | male   |  35   |          0 |

| 319 | Spedden, Mrs. Frederic Oakley (Margaretta Corning Stone) |        1 | female |  40   |          1 |

| 507 | Bradley, Mr. George ("George Arthur Brayton")            |        1 | male   | nan   |          1 |

| 748 | Marvin, Mr. Daniel Warner                                |        1 | male   |  19   |          0 |

| 156 | Gilnagh, Miss. Katherine "Katie"                         |        3 | female |  16   |          1 |

| 148 | Navratil, Mr. Michel ("Louis M Hoffman")                 |        2 | male   |  36.5 |          0 |

| 541 | Andersson, Miss. Ingeborg Constanzia                     |        3 | female |   9   |          0 |

| 173 | Sivola, Mr. Antti Wilhelm                                |        3 | male   |  21   |          0 |

| 279 | Abbott, Mrs. Stanton (Rosa Hunt)                         |        3 | female |  35   |          1 |

| 701 | Silverthorne, Mr. Spencer Victor                         |        1 | male   |  35   |          1 |

| 657 | Bourke, Mrs. John (Catherine)                            |        3 | female |  32   |          0 |

| 474 | Strandberg, Miss. Ida Sofia                              |        3 | female |  22   |          0 |

| 652 | Kalvik, Mr. Johannes Halvorsen                           |        3 | male   |  21   |          0 |

| 843 | Lemberopolous, Mr. Peter L                               |        3 | male   |  34.5 |          0 |

| 713 | Larsson, Mr. August Viktor                               |        3 | male   |  29   |          0 |

| 480 | Goodwin, Master. Harold Victor                           |        3 | male   |   9   |          0 |

| 292 | Levy, Mr. Rene Jacques                                   |        2 | male   |  36   |          0 |

| 304 | Williams, Mr. Howard Hugh "Harry"                        |        3 | male   | nan   |          0 |

| 233 | Asplund, Miss. Lillian Gertrud                           |        3 | female |   5   |          1 |

| 253 | Lobb, Mr. William Arthur                                 |        3 | male   |  30   |          0 |

###  

---
## Game End

Congratulations! You've collected all 5 coordinate fragments, restarted the time machine, and successfully escaped from 1912 at the moment the Titanic sank.
