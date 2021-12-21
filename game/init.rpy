label initialize_variables:
    call initialize_game_speeds
    call initialize_images
    call initialize_entities
    $ ranking = 0
    call initialize_questions
    # Water elements:
    #     Koromodako - Octopus yokai which lives in between Kyoto & Fukui
    #     Mizuchi - Dangerous water dragon
    #     Moryo - Water demons which eat corpses
    # Fire elements:
    #     Janjanbi - Drifting fireballs
    #     Kechibi - Fireballs with human faces
    #     Kosenjobi - Fireballs that float over former battlefields
    #     Hakanohi - Fire that sprouts from base of graves
    #     Hitodama - Fireball ghost that appears upon death (spirit)
    return

label initialize_game_speeds:
    $ text_fade_rate = 1
    $ background_fade_rate = 1.5
    $ pause_rate = 0.5

label initialize_images:
    # Generic backgrounds
    image question_room = im.Scale("bg open_space.jpg", 1920, 1080)

    # splashscreen backgrounds 
    image space_1 = im.Scale("bg space_1.jpg", 1920, 1080)
    image space_2 = im.Scale("bg space_2.jpg", 1920, 1080)
    image space_3 = im.Scale("bg space_3.jpg", 1920, 1080)
    image space_4 = im.Scale("bg space_4.jpg", 1920, 1080)
    image space_5 = im.Scale("bg space_5.jpg", 1920, 1080)
    return

label initialize_entities:
    $ entities = {
        "water": {
            "familiars": [],
            "god": "Susanoo, God of Seas and Storms",
            "monsters": ["Kappa", "Wani"]
        },
        "fire": {
            "familiars": [],
            "god": "Kojin, God of Fire",
            "monsters": ["Basan, Fowl of Fire", "Itsumade, Bird of Flame"]
        }
    }
    $ character_name = ""
    $ element = ""
    $ stats = {}
    return

label initialize_questions:
    $ generic_questions = [
        ["Do you like Angels or Demons?", [("Demons", -1), ("Angels", 1)]],
        ["Do actions speak louder than words?", [("Yes", -1), ("No", 1)]],
        ["Are you a night or day person?", [("Night", -1), ("Day", 1)]],
        ["Does success outweigh ones happiness?", [("Yes", -1), ("No", 1)]],
        ["Would you rather be cherished or respected?", [("Respected", -1), ("Cherished", 1)]],
        ["Are you a 'spur of the moment' kind of person or do you like to calculate consequences?", [("Spur of the moment", -1), ("Calculative", 1)]],
        ["Do you prefer to be heard or listen?", [("Be heard", -1), ("Listen", 1)]]
    ]
    $ fire_based_questions = [
    ]
    $ water_based_questions = [
    ]