label st_date:
    scene bg beach
    with dissolve
    
    "So I guess this is where I’m meeting Stone today."
    "If that even {i}is{/i} their real name…"
    "Honestly, I never really knew them well in person. They’re just someone my other friends introduced me to in Meta."
    "Still, might as well try to get to know them."
    "Besides, I don’t mind waiting on a nice tropical island."
    "They should be arriving any second no-"
    mc "OW!"

    show stone base
    with easeintop
    
    "Ugh…my head…What was that?"
    "Actually, how am I even feeling pain here?"
    st "OMG I’m so sorry!"
    "I guess my date literally dropped on me…"
    mc "No problem, uh…what’s your name?"
    st "I didn’t hit you that hard, did I? It’s me. Stone."
    mc "Yeah. I can see that. But what is your {i}actual{/i} name?"
    st "That {i}is{/i} my name. It’s Stone."
    "..."
    st "..."

    jump st_choice_1

menu st_choice_1:
    "..."

    "I’m done.":
        jump st_1_1

    "I see…":
        jump st_1_2

label st_1_1:
    mc "I don’t have time for this…"
    st "Huh?"
    mc "I know how this is gonna play out. I’m not getting catfished on my first day here."
    st "Hey! Wait!"
    mc "Byeeeeeeeee."
    "Game Over"

    jump end_game

label st_1_2:
    mc "Your name…suits you…very well."

    stop music fadeout 1.0
    play music "audio/zucchini.mp3" fadein 2.0
    jump end_st_date

label end_st_date:
    jump hub_2