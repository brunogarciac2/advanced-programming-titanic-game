import pandas as pd
import matplotlib.pyplot as plt
import json, os, re, random
import string
from PIL import Image, ImageDraw, ImageFont
import seaborn as sns

def generate_challenge_5(df):
    """Generate Challenge 5: Find The Saboteur"""
    
    # Setup directories
    images_dir = "./hint"
    
    # PARTITION AGES INTO GROUPS FOR RIDDLE
    # _____________________________________________________________________________________
    def AddAgeGroupColumn(Df: pd.DataFrame) -> pd.DataFrame:
        GroupsForAge, Labels = [0, 12, 19, 39, 59, 120], ["child", "teen", "young_adult", "midlife", "elder"]
        Df = Df[Df["Age"].notna()].copy()
        Df["AgeGroup"] = pd.cut(Df["Age"], bins=GroupsForAge, labels=Labels, include_lowest=True, right=True)
        return Df
    
    Df = AddAgeGroupColumn(df)

    # PICKING 6 PASSENGERS
    # _____________________________________________________________________________________
    def PickDifferentiablePassengers(Df: pd.DataFrame, Seed=None) -> pd.DataFrame:
        RequiredCols = ["AgeGroup", "Sex", "Pclass"]; Filtered = Df.dropna(subset=RequiredCols).copy()
        Shuffled = Filtered.sample(frac=1, random_state=Seed); ChosenRows, SeenCombos = [], set()
        ClassCounts, TargetPerClass, TargetTotal = {1: 0, 2: 0, 3: 0}, 2, 6
        for _, Row in Shuffled.iterrows():
            PassengerClassValue = int(Row["Pclass"])
            if PassengerClassValue not in ClassCounts or ClassCounts[PassengerClassValue] >= TargetPerClass: continue
            Combo = (Row["AgeGroup"], Row["Sex"], PassengerClassValue)
            if Combo in SeenCombos: continue
            SeenCombos.add(Combo); ChosenRows.append(Row); ClassCounts[PassengerClassValue] += 1
            if len(ChosenRows) == TargetTotal: break
        if len(ChosenRows) < TargetTotal or any(C != TargetPerClass for C in ClassCounts.values()):
            raise ValueError("Could not find 6 passengers with 2 from each class and unique (AgeGroup, Sex, Pclass).")
        return pd.DataFrame(ChosenRows)

    SeedNumber = random.randint(0, 320000)
    Passengers = PickDifferentiablePassengers(Df, Seed=SeedNumber)
    Output = []
    for _, Row in Passengers.iterrows():
        Output.append({"Name": Row["Name"], "Pclass": int(Row["Pclass"]), "Age": float(Row["Age"]), "AgeGroup": str(Row["AgeGroup"]), "Sex": Row["Sex"]})

    # CLUE TEXT
    # _____________________________________________________________________________________
    Imposter = random.choice(Output)
    RiddlesForAge = {"old": "Their eyes have watched more years than the calendar dares to count, yet they still sparkle.",
        "middle": "They stand at life's midpoint with yesterday's wisdom in their pocket and tomorrow's plans in their hand.",
        "teen": "They've left childhood behind, but the future still stretches wide and bright before them.",
        "child": "They've only taken a handful of trips around the sun, yet every moment feels like an adventure."}

    RiddlesForClass = {1: "Their voyage begins at the top, with velvet paths and silver service guiding their way.",
        2: "Not the highest deck nor the lowest, yet their journey runs smooth and steady.",
        3: "Their rooms are small, their fare humble, but their dreams stretch farther than the horizon."}

    RiddlesForGender = {"male": "He travels with a calm certainty, his past and hopes woven into every step.",
        "female": "She moves with quiet intention, her soft confidence carrying echoes of her past."}
    
    Key1 = {"child":"child","teen":"teen","young_adult":"teen","midlife":"middle","elder":"old"}[Imposter["AgeGroup"]]
    imposterriddles = {
        "Age Riddle Answer": RiddlesForAge[Key1],
        "Passenger Class Riddle Answer": RiddlesForClass[Imposter["Pclass"]],
        "Gender Riddle Answer": RiddlesForGender[Imposter["Sex"]]}

    # REDACT THE SENTENCES 
    # _____________________________________________________________________________________
    ListOfRedactedWords = {"Age Riddle Answer": [],"Passenger Class Riddle Answer": [],"Gender Riddle Answer": []}
    GenderPronounToBeRemoved = {"he", "him", "his", "she", "her", "hers"}
    
    def RiddleRedactor(sentence, WordRedactList, dropProb=0.6, minLen=4, isGender=False):
        def CutWord(match):
            word = match.group(0)
            if isGender and word.lower() in GenderPronounToBeRemoved:
                WordRedactList.append(word)
                return "___"
            elif isGender:
                if len(word) >= minLen and random.random() < 0.4:
                    WordRedactList.append(word)
                    return "___"
            else:
                if len(word) >= minLen and random.random() < dropProb:
                    WordRedactList.append(word)
                    return "___"
            return word
        return re.sub(r"[A-Za-z]+", CutWord, sentence) 

    RedactedRiddles = {}
    for riddleName, riddleText in imposterriddles.items():
        RedactedRiddles[riddleName] = RiddleRedactor(
            riddleText,
            ListOfRedactedWords[riddleName],
            dropProb=0.6,
            minLen=4,
            isGender=(riddleName == "Gender Riddle Answer")
        )
    
    RiddleKeys = list(imposterriddles.keys())
    Headings = ["Anagram Riddle", "WordSearch Riddle", "Graph Riddle"]
    random.shuffle(RiddleKeys)
    random.shuffle(Headings)

    AssignedMasked = {}
    AssignedRedacted = {}
    HeadingToRiddleName = {}
    
    for heading, key in zip(Headings, RiddleKeys):
        AssignedMasked[heading] = RedactedRiddles[key]
        AssignedRedacted[heading] = ListOfRedactedWords[key]
        HeadingToRiddleName[heading] = key

    # CLUE TEXT Graph
    # _____________________________________________________________________________________
    RiddlesForAge_Graph = {
        "old": "Their survival bar on the graph barely rises—almost the lowest of all the age groups.",
        "middle": "Their survival sits somewhere in the middle of the graph, neither notably high nor low.",
        "teen": "Their bar is higher than many adults, but not as strong as the youngest group.",
        "child": "Their survival bar stands among the tallest, nearly reaching the top of the chart."
    }

    RiddlesForClass_Graph = {
        1: "On the chart, their survival bar reaches one of the highest positions compared to all others.",
        2: "Their bar sits in the middle not the highest, not the lowest—steadily between the extremes.",
        3: "Their survival bar is among the shortest, nearly touching the bottom of the graph."
    }

    RiddlesForGender_Graph = {
        "male": "Their bar drops sharply downward the lowest of all the groups on the chart.",
        "female": "Their bar rises dramatically high, clearly towering over the opposite group."
    }

    GraphHintLookup = {
        "Age Riddle Answer": RiddlesForAge_Graph,
        "Passenger Class Riddle Answer": RiddlesForClass_Graph,
        "Gender Riddle Answer": RiddlesForGender_Graph
    }

    # WordSearch Code
    # _____________________________________________________________________________________
    WordSearchWords = AssignedRedacted["WordSearch Riddle"]

    def PrepareWords(Words):
        return [Word.strip().upper() for Word in Words]

    def CreateGrid(Words, Size=15):
        Grid = [[None for _ in range(Size)] for _ in range(Size)]
        Directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        PlacedWordsInfo = []

        for Word in Words:
            Placed = False
            Attempts = 0
            MaxAttempts = 100

            while not Placed and Attempts < MaxAttempts:
                Row = random.randint(0, Size - 1)
                Col = random.randint(0, Size - 1)
                Dr, Dc = random.choice(Directions)
                EndRow = Row + Dr * (len(Word) - 1)
                EndCol = Col + Dc * (len(Word) - 1)

                if 0 <= EndRow < Size and 0 <= EndCol < Size:
                    CanPlace = True
                    for I, Letter in enumerate(Word):
                        R = Row + Dr * I
                        C = Col + Dc * I
                        if Grid[R][C] is not None and Grid[R][C] != Letter:
                            CanPlace = False
                            break

                    if CanPlace:
                        Positions = []
                        for I, Letter in enumerate(Word):
                            R = Row + Dr * I
                            C = Col + Dc * I
                            Grid[R][C] = Letter
                            Positions.append((R, C))
                        Placed = True
                        PlacedWordsInfo.append({
                            "word": Word,
                            "positions": Positions,
                            "start": (Row, Col),
                            "direction": (Dr, Dc),
                        })
                Attempts += 1

        for I in range(Size):
            for J in range(Size):
                if Grid[I][J] is None:
                    Grid[I][J] = random.choice(string.ascii_uppercase)

        return Grid, PlacedWordsInfo

    def CreatePuzzleImage(Grid, WordsToFind):
        Size = len(Grid)
        CellSize = 50
        Padding = 40
        HeaderHeight = 100
        FooterHeight = 100
        GridSize = Size * CellSize
        ImgWidth = GridSize + 2 * Padding
        ImgHeight = GridSize + HeaderHeight + FooterHeight
        Img = Image.new("RGB", (ImgWidth, ImgHeight), "white")
        Draw = ImageDraw.Draw(Img)

        try:
            TitleFont = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 34)
            TextFont = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 16)
            GridFont = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 28)
        except:
            TitleFont = ImageFont.load_default()
            TextFont = ImageFont.load_default()
            GridFont = ImageFont.load_default()

        Title = "Find the Hidden Words To Fill In The Blanks"
        Box = Draw.textbbox((0, 0), Title, font=TitleFont)
        TitleWidth = Box[2] - Box[0]
        Draw.text(((ImgWidth - TitleWidth) // 2, 30), Title, fill="black", font=TitleFont)
        TitleHeight = Box[3] - Box[1]
        UnderlineY = 30 + TitleHeight + 12
        Draw.line((Padding, UnderlineY, ImgWidth - Padding, UnderlineY), fill="#3498db", width=4)
        GridStartY = HeaderHeight
        Draw.rectangle([Padding, GridStartY, Padding + GridSize, GridStartY + GridSize], outline="black", width=2)

        for I in range(Size + 1):
            Y = GridStartY + I * CellSize
            Draw.line([Padding, Y, Padding + GridSize, Y], fill="gray", width=1)
            X = Padding + I * CellSize
            Draw.line([X, GridStartY, X, GridStartY + GridSize], fill="gray", width=1)

        for I in range(Size):
            for J in range(Size):
                Letter = Grid[I][J]
                XPos = Padding + J * CellSize + CellSize // 2
                YPos = GridStartY + I * CellSize + CellSize // 2
                Box = Draw.textbbox((0, 0), Letter, font=GridFont)
                Ww = Box[2] - Box[0]
                Hh = Box[3] - Box[1]
                Draw.text((XPos - Ww // 2, YPos - Hh // 2 - 5), Letter, fill="black", font=GridFont)

        FooterY = GridStartY + GridSize + 30
        MaxWidth = ImgWidth - 2 * Padding
        ClueWords = []
        for Word in WordsToFind:
            Temp = str(Word).strip()
            if not Temp:
                continue
            ClueWords.append(Temp[0] + " " + " ".join("_" for _ in range(len(Temp) - 1)))

        Lines = []
        CurrentLine = ""
        for Idx, Clue in enumerate(ClueWords):
            Sep = "   " if CurrentLine else ""
            TestLine = CurrentLine + Sep + Clue
            Box = Draw.textbbox((0, 0), TestLine, font=TextFont)
            if Box[2] - Box[0] <= MaxWidth:
                CurrentLine = TestLine
            else:
                Lines.append(CurrentLine)
                CurrentLine = Clue
        if CurrentLine:
            Lines.append(CurrentLine)

        for I, Line in enumerate(Lines):
            Box = Draw.textbbox((0, 0), Line, font=TextFont)
            Ww = Box[2] - Box[0]
            Draw.text(((ImgWidth - Ww) // 2, FooterY + I * 25), Line, fill="darkgreen", font=TextFont)

        return Img

    def CreateSolutionImage(Grid, PlacedWordsInfo):
        Size = len(Grid)
        CellSize = 50
        Padding = 40
        HeaderHeight = 100
        FooterHeight = 100
        GridSize = Size * CellSize
        ImgWidth = GridSize + 2 * Padding
        ImgHeight = GridSize + HeaderHeight + FooterHeight
        Img = Image.new("RGB", (ImgWidth, ImgHeight), "white")
        Draw = ImageDraw.Draw(Img)

        try:
            TitleFont = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 34)
            TextFont = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 16)
            GridFont = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 28)
        except:
            TitleFont = ImageFont.load_default()
            TextFont = ImageFont.load_default()
            GridFont = ImageFont.load_default()

        Title = "Solution"
        Box = Draw.textbbox((0, 0), Title, font=TitleFont)
        TitleWidth = Box[2] - Box[0]
        Draw.text(((ImgWidth - TitleWidth) // 2, 30), Title, fill="darkred", font=TitleFont)
        TitleHeight = Box[3] - Box[1]
        UnderlineY = 30 + TitleHeight + 12
        Draw.line((Padding, UnderlineY, ImgWidth - Padding, UnderlineY), fill="red", width=4)
        GridStartY = HeaderHeight
        Draw.rectangle([Padding, GridStartY, Padding + GridSize, GridStartY + GridSize], outline="black", width=2)

        for I in range(Size + 1):
            Y = GridStartY + I * CellSize
            Draw.line([Padding, Y, Padding + GridSize, Y], fill="gray", width=1)
            X = Padding + I * CellSize
            Draw.line([X, GridStartY, X, GridStartY + GridSize], fill="gray", width=1)

        ColorList = ["yellow", "lightgreen", "lightblue", "lightcoral", "plum",
            "lightyellow", "lightcyan", "lavender", "peachpuff", "mistyrose"]

        for Idx, WordInfo in enumerate(PlacedWordsInfo):
            TheColor = ColorList[Idx % len(ColorList)]
            for Row, Col in WordInfo["positions"]:
                Temp1 = Padding + Col * CellSize + 2
                Temp2 = GridStartY + Row * CellSize + 2
                Temp3 = Temp1 + CellSize - 4
                Temp4 = Temp2 + CellSize - 4
                Draw.rectangle([Temp1, Temp2, Temp3, Temp4], fill=TheColor, outline=None)

        for I in range(Size + 1):
            Y = GridStartY + I * CellSize
            Draw.line([Padding, Y, Padding + GridSize, Y], fill="gray", width=1)
            X = Padding + I * CellSize
            Draw.line([X, GridStartY, X, GridStartY + GridSize], fill="gray", width=1)

        for I in range(Size):
            for J in range(Size):
                Letter = Grid[I][J]
                XPos = Padding + J * CellSize + CellSize // 2
                YPos = GridStartY + I * CellSize + CellSize // 2
                Box = Draw.textbbox((0, 0), Letter, font=GridFont)
                Ww = Box[2] - Box[0]
                Hh = Box[3] - Box[1]
                Draw.text((XPos - Ww // 2, YPos - Hh // 2 - 5), Letter, fill="black", font=GridFont)

        FooterY = GridStartY + GridSize + 30
        MaxWidth = ImgWidth - 2 * Padding
        WordsFound = [W["word"] for W in PlacedWordsInfo]
        Lines = []
        CurrentLine = "Hidden Words: "

        for Idx, Word in enumerate(WordsFound):
            Sep = ", " if Idx > 0 else ""
            TestLine = CurrentLine + Sep + Word
            Box = Draw.textbbox((0, 0), TestLine, font=TextFont)
            if Box[2] - Box[0] <= MaxWidth:
                CurrentLine = TestLine
            else:
                Lines.append(CurrentLine)
                CurrentLine = Word
        if CurrentLine:
            Lines.append(CurrentLine)

        for I, Line in enumerate(Lines):
            Box = Draw.textbbox((0, 0), Line, font=TextFont)
            Ww = Box[2] - Box[0]
            Draw.text(((ImgWidth - Ww) // 2, FooterY + I * 25), Line, fill="darkgreen", font=TextFont)

        return Img

    # Generate WordSearch
    Words = PrepareWords(WordSearchWords)
    Grid, PlacedWordsInfo = CreateGrid(Words, Size=15)
    PlacedWords = [W["word"] for W in PlacedWordsInfo]
    PuzzleImage = CreatePuzzleImage(Grid, PlacedWords)
    SolutionImage = CreateSolutionImage(Grid, PlacedWordsInfo)
    
    # Save WordSearch images
    wordsearch_puzzle_path = os.path.join(images_dir, "wordsearch_puzzle.png")
    wordsearch_solution_path = os.path.join(images_dir, "wordsearch_solution.png")
    PuzzleImage.save(wordsearch_puzzle_path)
    SolutionImage.save(wordsearch_solution_path)

    # Riddle Anagram Code
    # _____________________________________________________________________________________
    AnagramWords = AssignedRedacted["Anagram Riddle"]
    FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"

    def scramble_word(Word):
        if len(Word) <= 1:
            return Word
        Shuffled = list(Word)
        Original = Word
        for I in range(100):
            random.shuffle(Shuffled)
            Result = "".join(Shuffled)
            if Result != Original:
                return Result
        return "".join(Shuffled)

    def CreateWordImage(Words, Title, Filename, font_size=28):
        W, Pad, Gap = 1000, 70, 28
        try:
            Fnt = ImageFont.truetype(FONT_PATH, font_size)
            TitleFnt = ImageFont.truetype(FONT_PATH, font_size + 18)
        except:
            Fnt, TitleFnt = ImageFont.load_default(), ImageFont.load_default()
        
        TitleSpace = font_size + 42
        LineH = font_size + Gap
        H = Pad * 2 + TitleSpace + len(Words) * LineH
        Img = Image.new("RGB", (W, H), "#f9fbff")
        Draw = ImageDraw.Draw(Img)
        Tb = Draw.textbbox((0, 0), Title, font=TitleFnt)
        TitleX = (W - (Tb[2] - Tb[0])) // 2
        Draw.text((TitleX, Pad), Title, fill="#1f3b57", font=TitleFnt)
        YLine = Pad + TitleSpace - 26
        Draw.line((Pad, YLine, W - Pad, YLine), fill="#3498db", width=4)
        CurrY = Pad + TitleSpace + 12
        for Num, Word in enumerate(Words):
            Draw.text((Pad + 30, CurrY), f"{Num + 1}. {Word}", fill="#34495e", font=Fnt)
            CurrY += LineH
        Img.save(Filename)

    Words = [str(W).strip() for W in AnagramWords if str(W).strip()]
    Scrambled = [scramble_word(W) for W in Words]
    
    anagram_puzzle_path = os.path.join(images_dir, "anagram_puzzle.png")
    anagram_solution_path = os.path.join(images_dir, "anagram_solution.png")
    
    CreateWordImage(Scrambled, "Unscramble Words To Fill In The Blanks", anagram_puzzle_path)
    CreateWordImage(Words, "Solution", anagram_solution_path)

    # Riddle Graph Generator
    # _____________________________________________________________________________________
    def GenerateSurvivalGraph(RiddleName, DataDf):
        sns.set_theme(style="whitegrid", context="talk")
        Fig, Ax = plt.subplots(figsize=(10, 6))
        Blue = "#4C72B0"
        Orange = "#DD8452"

        if RiddleName == "Age Riddle Answer":
            SurvivalByAge = DataDf.groupby("AgeGroup")["Survived"].mean().sort_values()
            Colors = [Blue if Val < 0.5 else Orange for Val in SurvivalByAge.values]
            Bars = sns.barplot(x=SurvivalByAge.index, y=SurvivalByAge.values, palette=Colors, ax=Ax, edgecolor="None", errorbar=None)
            Ax.set_xlabel("Age Group", fontsize=12, fontweight="bold")
            Ax.set_ylabel("Survival Rate", fontsize=12, fontweight="bold")
            Ax.set_title("Titanic Survival Rates by Age Group", fontsize=14, fontweight="bold")
            Ax.set_ylim(0, 1)
            Ax.grid(axis="y", alpha=0.3, linestyle="--")
            Ax.set_axisbelow(True)
            for Bar in Bars.patches:
                Height = Bar.get_height()
                Ax.text(Bar.get_x() + Bar.get_width() / 2.0, Height + 0.02, f"{Height:.1%}", ha="center", va="bottom", fontweight="bold")
            plt.xticks(rotation=15)

        elif RiddleName == "Passenger Class Riddle Answer":
            SurvivalByClass = DataDf.groupby("Pclass")["Survived"].mean().sort_values()
            Colors = [Blue if Val < 0.5 else Orange for Val in SurvivalByClass.values]
            ClassLabels = [f"Class {int(C)}" for C in SurvivalByClass.index]
            Bars = sns.barplot(x=ClassLabels, y=SurvivalByClass.values, palette=Colors, ax=Ax, edgecolor="None", errorbar=None)
            Ax.set_xlabel("Passenger Class", fontsize=12, fontweight="bold")
            Ax.set_ylabel("Survival Rate", fontsize=12, fontweight="bold")
            Ax.set_title("Titanic Survival Rates by Passenger Class", fontsize=14, fontweight="bold")
            Ax.set_ylim(0, 1)
            Ax.grid(axis="y", alpha=0.3, linestyle="--")
            Ax.set_axisbelow(True)
            for Bar in Bars.patches:
                Height = Bar.get_height()
                Ax.text(Bar.get_x() + Bar.get_width() / 2.0, Height + 0.02, f"{Height:.1%}", ha="center", va="bottom", fontweight="bold")
            plt.xticks(rotation=15)

        elif RiddleName == "Gender Riddle Answer":
            SurvivalByGender = DataDf.groupby("Sex")["Survived"].mean().sort_values()
            Colors = [Blue if Val < 0.5 else Orange for Val in SurvivalByGender.values]
            GenderLabels = [S.capitalize() for S in SurvivalByGender.index]
            Bars = sns.barplot(x=GenderLabels, y=SurvivalByGender.values, palette=Colors, ax=Ax, edgecolor="None", errorbar=None)
            Ax.set_xlabel("Gender", fontsize=12, fontweight="bold")
            Ax.set_ylabel("Survival Rate", fontsize=12, fontweight="bold")
            Ax.set_title("Titanic Survival Rates by Gender", fontsize=14, fontweight="bold")
            Ax.set_ylim(0, 1)
            Ax.grid(axis="y", alpha=0.3, linestyle="--")
            Ax.set_axisbelow(True)
            for Bar in Bars.patches:
                Height = Bar.get_height()
                Ax.text(Bar.get_x() + Bar.get_width() / 2.0, Height + 0.02, f"{Height:.1%}", ha="center", va="bottom", fontweight="bold")
            plt.xticks(rotation=0)

        sns.despine(ax=Ax)
        plt.tight_layout()
        return Fig

    GraphRiddleName = HeadingToRiddleName.get("Graph Riddle")
    graph_puzzle_path = os.path.join(images_dir, "graph_puzzle.png")
    
    if GraphRiddleName in ["Age Riddle Answer", "Passenger Class Riddle Answer", "Gender Riddle Answer"]:
        Fig = GenerateSurvivalGraph(GraphRiddleName, Df)
        Fig.savefig(graph_puzzle_path, dpi=300, bbox_inches="tight")
        plt.close(Fig)

    # This if For Update HeadingMeta with actual paths
    HeadingMeta = {
        "Anagram Riddle": {
            "link_key": "Anagram Link",
            "solution_link_key": "Anagram Solution Link",
            "url": anagram_puzzle_path,
            "solution_url": anagram_solution_path
        },
        "WordSearch Riddle": {
            "link_key": "WordSearch Link",
            "solution_link_key": "WordSearch Solution Link",
            "url": wordsearch_puzzle_path,
            "solution_url": wordsearch_solution_path
        },
        "Graph Riddle": {
            "link_key": "Graph Link",
            "solution_link_key": "Graph Solution Link",
            "url": graph_puzzle_path,
            "solution_url": graph_puzzle_path
        }
    }

    def GetGraphHint(riddleName, imposter):
        if riddleName == "Age Riddle Answer":
            ageGroupMapping = {"child":"child","teen":"teen","young_adult":"teen","midlife":"middle","elder":"old"}
            mappedAgeGroup = ageGroupMapping.get(imposter["AgeGroup"], imposter["AgeGroup"])
            return RiddlesForAge_Graph[mappedAgeGroup]
        elif riddleName == "Passenger Class Riddle Answer":
            return RiddlesForClass_Graph[imposter["Pclass"]]
        elif riddleName == "Gender Riddle Answer":
            return RiddlesForGender_Graph[imposter["Sex"].lower()]
        return ""

    def GetGraphAnswer(riddleName, imposter):
        if riddleName == "Age Riddle Answer":
            return imposter["AgeGroup"]
        elif riddleName == "Passenger Class Riddle Answer":
            return imposter["Pclass"]
        elif riddleName == "Gender Riddle Answer":
            return imposter["Sex"]
        return None

    def GetHintSentence(riddleName, imposter):
        if riddleName == "Age Riddle Answer":
            return f"This hints the imposter's AgeGroup is {imposter['AgeGroup']}."
        elif riddleName == "Passenger Class Riddle Answer":
            return f"This hints the imposter's Pclass is {imposter['Pclass']}."
        elif riddleName == "Gender Riddle Answer":
            return f"This hints the imposter's Sex is {imposter['Sex']}."
        return ""
    
    # This is For Building Riddle Clues with the image paths
    RiddleClues = []
    for HeadingName in Headings:
        RiddleName = HeadingToRiddleName[HeadingName]

        if HeadingName == "Graph Riddle":
            ClueText = GetGraphHint(RiddleName, Imposter)
            AnswerText = GetGraphAnswer(RiddleName, Imposter)
        else:
            ClueText = AssignedMasked[HeadingName]
            AnswerText = imposterriddles[RiddleName]
            hint_sentence = GetHintSentence(RiddleName, Imposter)
            if hint_sentence:
                AnswerText = f"{AnswerText} {hint_sentence}"

        ClueEntry = {
            "Heading": HeadingName,
            "Clue": ClueText,
            "Answer": AnswerText
        }

        MetaInfo = HeadingMeta.get(HeadingName)
        if MetaInfo:
            ClueEntry[MetaInfo["link_key"]] = MetaInfo["url"]
            ClueEntry[MetaInfo["solution_link_key"]] = MetaInfo.get("solution_url", MetaInfo["url"])

        RiddleClues.append(ClueEntry)

    # JSON STRUCTURE Here
    SaboteurJson = {
        "id": 5,
        "title": "Challenge 5: Find The Saboteur",
        "story": (
            "A saboteur hides among six Titanic passengers. Their identity is concealed within riddles, "
            "each missing key information. Reconstruct the clues to reveal who they really are."
        ),
        "instructions": (
            "Complete the word search, anagrams, and graph hint to restore the clues. "
            "Each passenger has three attributes: AgeGroup, Pclass, and Sex. Use the solved clues "
            "to determine which passenger is the saboteur."
        ),
        "passengers": Output,
        "Riddle_Clues": RiddleClues,
        "saboteur": {
            "Name": Imposter["Name"],
            "Pclass": Imposter["Pclass"],
            "Age": Imposter["Age"],
            "AgeGroup": Imposter["AgeGroup"],
            "Sex": Imposter["Sex"],
            "NoteForEscapeRoomRunner": "The saboteur don't show players."
        }
    }
    

    return SaboteurJson
