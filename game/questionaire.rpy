# Fire is < 0, water is > 0
label round_1: 
    $ ranking += ask_questions(generic_questions)
    return

label round_2:
    $ score_phrase = "hot headed" if ranking < 0 else "cool and collected"
    $ element = "fire" if ranking < 0 else "water"

    "Interesting your tendancies lean toward being [score_phrase]..."
    "Let's dive a little deeper into your personality, shall we? I hope you're ready..."
    # fire based questions
    if ranking < 0:
        $ ranking += ask_questions(fire_based_questions)
    else:
        $ ranking += ask_questions(water_based_questions)
    return

label round_3:
    "Congrats on making it this far...Now it is time to attain your stats..."
    "**machine whirring**"
    $ stats = generate_stats()
    "**machine stops**"
    """
    Current stats:\n
    Health: [stats[hp]]\n
    Attack: [stats[attack]]\n
    Speed: [stats[speed]]
    """
    return