init python: 
    import random
    def ask_questions(questions_and_answers):
        round_score = 0
        
        # [Question, (response, score)]
        for i in range(len(questions_and_answers)):
            narrator(questions_and_answers[i][0], interact=False)
            ans_score = renpy.display_menu(questions_and_answers[i][1])
            round_score += ans_score
        return round_score

    def get_character_name():
        character_name = renpy.input("Please enter a name:", length=32);
        character_name = character_name.strip()
        return character_name

    def generate_stats():
        attack_boost = 5 if game_manager.element == "fire" else 0
        speed_boost = 5 if game_manager.element == "water" else 0
        return {
            "hp": random.randrange(1, 20, 1),
            "attack": random.randrange(1, 20, 1) + attack_boost,
            "speed": random.randrange(1, 20, 1) + speed_boost
        }
    
    def get_familiar(ranking, dict):
        idx = 0 if ranking > 11 else 1
        return dict["familiars"][idx]

define audio.machine = "audio/sfx/machine.wav"

label start:
    play music "audio/music/ambient.mp3" fadein 2 fadeout 2
    call initialize_variables
    call narrator_intro
    show question_room
    call round_1
    call round_2
    call round_3
    stop music
    return

label narrator_intro:
    scene space_1 with Dissolve(background_fade_rate)
    "Welcome...uhmm...what's your name exactly?" with Dissolve(text_fade_rate)
    $ pause_rate

    $ player.name = get_character_name()    

    scene space_2 with Dissolve(background_fade_rate)
    "Well [player.name], I truly hope that you have found your journey up to this point fruitful and rewarding.
    Savor this moment while you can, for now you are about to embark on a journey beyond 
    your wildest imagination." with Dissolve(text_fade_rate)
    $ pause_rate

    scene space_3 with Dissolve(background_fade_rate)
    "You will have your fill of lust, gluttony, greed, sloth, wrath, envy,
    and pride. So I hope that you're ready..." with Dissolve(text_fade_rate)
    $ pause_rate

    scene space_4 with Dissolve(background_fade_rate)
    "First thing's first though..." with Dissolve(text_fade_rate)
    $ pause_rate

    scene space_5 with Dissolve(background_fade_rate)
    "Before you embark, you must go through a series of questions in order to determine 
    your familiar." with Dissolve(text_fade_rate)
    $ pause_rate
    return

## Choices at this point are Basan or Istumade
label fire_path: 
    return

## Choices at this point are Kappa or Wani
label water_path: 
    return