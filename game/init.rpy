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
            "familiars": [
                {
                    "name": "Water byte", 
                    "ability": {
                        "name": "Douse",
                        "description": "Renders the enemy immobile for 2 turns",
                        "cost": 2
                    }
                },
                {
                    "name": "Ice byte",
                    "ability": 
                    {
                        "name": "Freeze",
                        "description": "Renders the enemy immobile for 1 turn",
                        "cost": 1
                    }
                }],
            "god": "Susanoo, God of Seas and Storms",
            "monsters": ["Kappa", "Wani"]
        },
        "fire": {
            "familiars": [
                {
                    "name": "Fire byte", 
                    "ability": 
                    {
                        "name": "Burn",
                        "description": "Enemy takes an additional 2 damage each turn",
                        "cost": 2
                    }, 
                },
                { 
                    "name": "Spark byte",
                    "ability": {
                        "name": "Jolt",
                        "description": "Enemy takes an additional 1 damage each turn",
                        "cost": 1
                    }
                }],
            "god": "Kojin, God of Fire",
            "monsters": ["Basan, Fowl of Fire", "Itsumade, Bird of Flame"]
        }
    }
    return

label initialize_character:
    $ character_name = ""
    $ element = ""
    $ stats = {}
    $ realm = ""
    return

label initialize_questions:
    $ generic_questions = [
        ["Do actions speak louder than words?", [("Yes", -1), ("No", 1)]],
        ["Are you a night or day person?", [("Night", -1), ("Day", 1)]],
        ["Does success outweigh ones happiness?", [("Yes", -1), ("No", 1)]],
        ["Would you rather be cherished or respected?", [("Respected", -1), ("Cherished", 1)]],
        ["Are you a 'spur of the moment' kind of person or do you like to calculate consequences?", [("Spur of the moment", -1), ("Calculative", 1)]],
        ["Do you prefer to be heard or listen?", [("Be heard", -1), ("Listen", 1)]],
        ["If someone who betrayed you were to have unfortunate events befall them, what would you feel?", [("Pride", -1), ("Pity", 1)]],
        ["Do you ever find yourself envious of others for things that they have?", [("Yes", -1), ("No", 1)]],
        ["If you suddenly became wealthy, would you...", [("Keep it all", -1), ("Share the wealth", 1)]],
    ]
    $ fire_based_questions = [
        ["If you saw a fire, what would you do?", [("Fan the flames", 1), ("Stem the fire",0.5)]],
        ["Do you often find yourself in a spiteful mood?", [("Yes", 1), ("No",0.5)]],
        ["High...", [("Heaven", 1), ("Tide",0.5)]],
        ["Fire or lava?", [("Lava", 1), ("Fire",0.5)]],
        ["Which animal would win in a fight?", [("Raccoon", 1), ("Honey Badger",0.5)]]
    ]
    $ water_based_questions = [
        ["If your boat start sinking, what would you do?", [("Jump ship and swim", 1), ("Attempt to patch the boat with duct tape",0.5)]],
        ["Do you often find yourself in relaxed state?", [("Yes", 1), ("No",0.5)]],
        ["High...", [("Tide", 1), ("Noon",0.5)]],
        ["Water or ice?", [("Ice", 1), ("Water",0.5)]],
        ["Which animal would win in a fight?", [("Polar bear", 1), ("Walrus",0.5)]]
    ]