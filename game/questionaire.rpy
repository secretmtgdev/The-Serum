# Fire is < 0, water is > 0
label round_1: 
    $ ranking += ask_questions(generic_questions)
    return

label round_2:
    $ score_phrase = "hot headed" if ranking < 0 else "cool and collected"
    $ element = "fire" if ranking < 0 else "water"
    $ realm = entities[element]
    "Interesting your tendancies lean toward being [score_phrase]..."
    "Let's dive a little deeper into your personality, shall we? I hope you're ready..."
    
    # fire based questions
    if ranking < 0:
        $ ranking = abs(ranking)
        $ ranking += ask_questions(fire_based_questions)
        call fire_base
    else:
        $ ranking += ask_questions(water_based_questions)
        call water_base
    "Congrats [character_name] on your new companion [familiar[name]]"
    return

label round_3:
    "Once again, congrats [character_name] on making it this far...Now it is time to attain your stats..."
    "**machine whirring**"

    $ stats = generate_stats()
    "**machine stops**"
    
    call current_player_stats
    "Getting details on your familiar..."
    
    call familiar_details
    return

label fire_base:
    $ familiar = get_familiar(ranking, realm)
    return

label water_base:
    $ familiar = get_familiar(ranking, realm)
    return