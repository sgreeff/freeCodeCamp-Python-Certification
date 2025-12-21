def create_character(character_name, strength, intelligence, charisma):
    full_dot = '●'
    empty_dot = '○'

    if not isinstance(character_name,str):
        return 'The character name should be a string'
    if character_name == "":
        return 'The character should have a name'
    if len(character_name) > 10:
        return 'The character name is too long'
    if " " in character_name:
        return 'The character name should not contain spaces'
    