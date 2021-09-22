import poems
import random


def blackbird():
    place = input("Type a place: ").lower()
    object = input("Type an object: ").lower()
    body_part = input("Type a body part: ").lower()
    number = input("Type a number: ").lower()
    fruit = input("Type a fruit: ").lower()
    size = input("Type a size: ").lower()
    season = input("Type a season: ").lower()
    dance = input("Type a dance: ").lower()
    adjective = input("Type an adjective: ").lower()

    pure_poem = f"""
    I
    Among twenty snowy {place},   
    The only moving {object}   
    Was the {body_part} of the blackbird.   

    II
    I was of {number} minds,   
    Like a {fruit}tree   
    In which there are three {size} blackbirds.   

    III
    The blackbird whirled in the {season} winds.   
    It was a small part of the {dance}.   

    IV
    A {adjective} man and a woman   
    Are one.   
    A man and a woman and a blackbird   
    Are one. 
    """
    return print(pure_poem)

def road_not_taken():
    color = input("Type a color: ").lower()
    expression = input("Type an expression: ").lower()
    number = input("Type a number: ").lower()
    direction = input("Type a direction: ").lower()
    area = input("Type an area: ").lower()
    verb = input("Type a verb: ").lower()
    feeling = input("Type a season: ").lower()
    noun = input("Type a noun: ").lower()
    day_period = input("Type a day period: ").lower()

    pure_poem = f"""
    Two roads diverged in a {color} wood,
    And {expression} I could not travel both
    And be {number} traveler, long I stood
    And looked {direction} one as far as I could
    To where it bent in the {area};

    Then {verb} the other, as just as fair,
    And having perhaps the better claim,
    Because it was {feeling} and wanted wear;
    Though as for that the {noun} there
    Had worn them really about the same,

    And both that {day_period} equally lay
    In leaves no step had trodden black.
    """
    return print(pure_poem)

def daddy():
    bad = input("Type a bad action: ").lower()
    color = input("Type an color: ").lower()
    body_part = input("Type a body_part: ").lower()
    number = input("Type a number: ").lower()
    verb = input("Type an verb: ").lower()
    family = input("Type a family member: ").lower()
    feeling = input("Type a season: ").lower()
    noun = input("Type a noun: ").lower()
    object = input("Type a object: ").lower()
    size = input("Type a size: ").lower()

    pure_poem = f"""
    You do not {bad}, you do not do   
    Any more, {color} shoe
    In which I have lived like a {body_part}   
    For {number} years, poor and white,   
    Barely daring to {verb} or Achoo.
    
    {family}, I have had to kill you.   
    You died before I had {feeling} time——
    Marble-heavy, a bag full of {noun},   
    Ghastly {object} with one gray toe   
    {size} as a Frisco seal
    
    And a head in the freakish Atlantic   
    Where it pours bean green over blue  
    """
    return print(pure_poem)


def harlem():
    verb = input("Type an verb: ").lower()
    fruit = input("Type a fruit: ").lower()
    adjective = input("Type an adjective: ").lower()
    body_part = input("Type a body_part: ").lower()
    food = input("Type a food: ").lower()
    taste = input("Type a taste: ").lower()
    feeling = input("Type a season: ").lower()
    object = input("Type a object: ").lower()
    size = input("Type a size: ").lower()

    pure_poem = f"""
    What happens to a dream deferred?

      Does it {verb}
      like a {fruit} in the sun?
      Or fester like a {adjective} sore—
      And then do {body_part} run?
      Does it stink like rotten {food}?
      Or crust and sugar over—
      like a {taste} sweet?

      Maybe the {object} just sags
      like a {feeling} load.

      Or does it explode, {size}? 
    """
    return print(pure_poem)


def start(game_poem):
    if poem == poems.blackbird:
        return blackbird()
    elif poem == poems.road_not_taken:
        return road_not_taken()
    elif poem == poems.daddy:
        return daddy()
    elif poem == poems.harlem:
        return harlem()
    else:
        print("Poem not found")

status = input('Are you ready to create your own Rondeau poem adaptation??! Answer "yes" or "no" ').lower()
if status == "yes":
    should_continue = True
    while should_continue:
        poem = random.choice(poems.all_poems)
        start(poem)
        progress = input("Would you like to another Rondeau Prime Poem game? True or False").lower()
        if progress == "true":
            print ("Great, Keep it up")
        elif progress == "false":
            print("Thanks for gaming with us <3 Good bye")
            should_continue == False
        else:
            print("Your input is not valid. Game over")



