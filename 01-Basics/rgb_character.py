#initialize and create character function skeleton
def create_character(character_name, strength, intelligence, charisma):
    full_dot = '●'
    empty_dot = '○'

    #character name validation logic
    if not isinstance(character_name,str):
        return 'The character name should be a string'
    if character_name == "":
        return 'The character should have a name'
    if len(character_name) > 10:
        return 'The character name is too long'
    if " " in character_name:
        return 'The character name should not contain spaces'
    
    #stat type and range validation
    if not isinstance(strength,int) or not isinstance(intelligence,int) or not isinstance(charisma,int):
        return 'All stats should be integers'
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    
    #total point allocation validation
    sum_of_stats = strength + intelligence + charisma
    if sum_of_stats > 7 or sum_of_stats < 7:
        return 'The character should start with 7 points'

    return (
        # visual stat bars and multiline return
        f"{character_name}\nSTR {full_dot * strength}{empty_dot * (10 - strength)}\nINT {full_dot*intelligence}{empty_dot* (10 - intelligence)}\nCHA {full_dot*charisma}{empty_dot* (10 - charisma)}"
    )

print(create_character('ren', 4, 2, 1))
"""OUTPUT TEST:
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○"""

"""Teacher Notes:

Defensive Programming: Validation Sequence
Notice the order of the if statements in the code. This is called "Early Exit" or "Guard Clauses."

---The Logic: We check for the "easiest" errors first (Is it a string? Is it empty?).

---Efficiency: If the name is an integer, the function stops immediately. It doesn't waste "energy" checking if the stats add up to 7 because the input is already invalid.
"""
