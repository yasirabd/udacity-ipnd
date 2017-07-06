# IPND Stage 2 Final Project

# Titles for the story
titles = ["A Bunny Story", "Kites", "The Cat"]

# A Bunny Story fill-in-the-blanks and its corresponding answers.
bunny_story = "Once there was an ugly __1__ named Kevin. He was __2__ and nobody liked him. One day there was a Bhutan Marathon and the ugly bunny __3__ it. He got a __4__ and then everybody liked him. He made lots of new __5__ and lived happily ever after."
bunny_answers = ["bunny", "ugly", "won", "medal", "friends"]

# Kites story fill-in-the-blanks and its corresponding answers
kites_story = "There was once a boy called Sam. He was very __1__. He lived with his __2__ named Sigrid. One day he found __3__ gold coins and __4__ silver coins. Then he went and bought some paper and crayons, made __5__ kites and sold them. Then he took the money and bought a wardrobe, a car, a black dress for his mom and lots of gifts for his house and became very __6__."
kites_answers = ["poor", "mother", "50", "25", "1000", "rich"]

# The Cat story fill-in-the-blanks and its corresponding answers
cat_story = "Once upon a time there was a __1__ named Susan. She __2__ cats. She __3__ had a cat before but one day she got a cat for her now and then. The cat's name was Harry. Susan loved Harry. She __4__ with it and __5__ it sooo much. Her __6__ named Robb, disliked the cat but her mom loved it. Susan __7__ it and loved it so much. They all lived very ever after."
cat_answers = ["girl", "loved", "never", "slept", "loved", "dad", "pet"]

def load_fib_category():
    """
    Asks the user for a category and load that data.

    Args:
        none.
    Returns:
        print title and story that are selected.
        return function guess_check to check the correct answer.
    """
    category = raw_input("\nPlease select a category for the story (bunny, kites, cat): ")
    if category.lower() == "bunny":
        print "\n" + titles[0]
        print "\n" + bunny_story
        return guess_check(titles[0], bunny_story, bunny_answers)
    if category.lower() == "kites":
        print "\n" + titles[1]
        print "\n" + kites_story
        return guess_check(titles[1], kites_story, kites_answers)
    if category.lower() == "cat":
        print "\n" + titles[2]
        print "\n" + cat_story
        return guess_check(titles[2], cat_story, cat_answers)
    else:
        print "You selected an invalid category!"
        return load_fib_category()

def guess_check(title, prompt, answers):
    """
    Asks the user for a guess. If correct, moves to the next blank.

    Prompts the user to fill in the first blank. Displays the updated
    fill-in-the-blank when the user inputs the correct answer and prompts them
    to fill in the next blank. Prompts the user to try again when their guess
    is incorrect.

    Args:
        title (str) : the title for the story selected.
        prompt (str) : the story.
        answers (list of str) : list of the answer.
    Returns:
        print 'Good job' if the answer is right and continue the loop.
        print 'Try again' if the answer is wrong and return the loop.
        print 'Congratulations,...' if you completed the story.
    """
    idx = 1
    while idx <= len(answers):
        user_input = raw_input("\nWhat is the answer to __" + str(idx) + "__? ")
        if user_input == answers[idx-1]:
            print "Good job!" + "\n"
            idx += 1
            prompt = prompt.replace("__" + str(idx-1) + "__", user_input)
            print title + "\n\n" + prompt
        else:
            print "Try again.\n" + "\n" + title + "\n\n" + prompt
    print "Congratulations, you have filled in all of the blanks!"

def play_game():
    """
    Plays a full game of fill-in-the-blanks.

    Displays the chosen empty fill-in-the-blank. Ask the user if want to play
    another round. If 'yes' selected, continue the game.

    Args:
        none.
    Returns:
        if 'yes' selected, continue the game.
        if 'no' selected, stop the game.
    """
    load_fib_category()
    yes = ['yes', 'YES', 'y', 'Y']
    no = ['no', 'NO', 'n', 'N']

    user_input = raw_input("Would you play another round? (yes/no) : ")
    if user_input in yes:
        play_game()
    else:
        print "Thanks for playing!"

play_game()
