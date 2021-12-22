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