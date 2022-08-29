print("\t\tQuiz For python")
print("\tSelect answers in Variables. i.e (a, b, c, or d)\n")

# Asking user's name.
a = input("What is your name?: ")

# Welcoming the user.
print("\t\tWelcome to the Python Quiz " + a, "!!", "\n")

# Asking user to start the Quiz By Pressing any Number key.
x = float(input("Type any number to start the quiz : "))

if x >= 0:

    # initiating class
    class Question:
        def __init__(self, prompt, answer):
            self.prompt = prompt
            self.answer = answer

    # Qustions for the Quiz in the form of list.
    question_prompts = [
        "1) Python is a ?"
        "\n(a)Machine Language \n(b)Data Language \n(c)Programming Language\n(d)Speaking Language \nAnswer :",

        "2) what we use to shift on next line in Python?"
        "\n(a)(\ n) \n(b) <br>\n(c) next\n(d) new \nAnswer :",

        "3) What symbol we use for exponents in Python?"
        "\n(a) ^ \n(b)& \n(c)@ \n(d)** \nAnswer :",

        "4) Which function is used to provide output to the screen?"
        "\n(a)print() \n(b)output() \n(c)out \n(d)to \nAnswer :",

        "5) What is the correct file extension for Python files?"
        "\n(a).pyth  \n(b).json \n(c).py \n(d).pt \nAnswer :",

        "6) How do you insert Comments in Python code?"
        "\n(a)%  \n(b)# \n(c)!...! \n(d)// \nAnswer :",

        "7) How do you create a variable with the numeric value 5?"
        "\n(a)x=float(5)  \n(b)x=5 \n(c)Both are correct \n(d)Both are incorrect \nAnswer :",

        "8) What is the correct way to create a function in Python?"
        "\n(a)def myfunction():  \n(b)create myfunction(): \n(c)function() \n(d)create \nAnswer :",

        "9) Which operator is used to multiply numbers in python?"
        "\n(a)x  \n(b)* \n(c)# \n(d)** \nAnswer :",

        "10) Which operator can be used to compare two values in python?"
        "\n(a)<>  \n(b)= \n(c)>< \n(d)== \nAnswer :",

        "11) How to make a empty list of variable x in python?"
        "\n(a)x=[]   \n(b)x{} \n(c)x=list \n(d)x=() \nAnswer :",

        "12) How do you start writing an if statement in Python?"
        "\n(a)if x>y then:  \n(b)if x>y then \n(c)if (x>y) \n(d)if x>y : \nAnswer :",

        "13) How do you start writing a while loop in Python?"
        "\n(a)while x>y  \n(b)while x>y { \n(c)while (x>y) \n(d)while x>y : \nAnswer :",

        "14) How do you start writing a for loop in Python?"
        "\n(a)for x in y  \n(b)for x in y: \n(c)for x>y \n(d)for x>y: \nAnswer :",

        "15) Which statement is used to stop a loop?"
        "\n(a)stop  \n(b)return \n(c)exit \n(d)break \nAnswer :",
    ]

    # Giving answers in the form of list.
    questions = [
        Question(question_prompts[0], "c"),
        Question(question_prompts[1], "a"),
        Question(question_prompts[2], "d"),
        Question(question_prompts[3], "a"),
        Question(question_prompts[4], "c"),
        Question(question_prompts[5], "b"),
        Question(question_prompts[6], "c"),
        Question(question_prompts[7], "a"),
        Question(question_prompts[8], "b"),
        Question(question_prompts[9], "d"),
        Question(question_prompts[10], "a"),
        Question(question_prompts[11], "d"),
        Question(question_prompts[12], "d"),
        Question(question_prompts[13], "b"),
        Question(question_prompts[14], "d"),
    ]

    # Creating function for printing.

    def run_quiz(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)

            # checking answers
            if answer == question.answer:

                # Adding Scores after each question
                score += 1

            # Printing points after each Question.
            # no matter right or wrong
            print("point:"), print(score)

        # Pinting score.
        print("you got "+str(score) + "/" + str(len(questions)))

        # printing "you played well :)"
        if (score >= 7):
            print("\nYou played Well :)")

    # Run command for the whole Program.
    run_quiz(questions)

    # Printing Thank You...
    print("Thank You for playing <3\n")
