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