label st_date:
    scene bg black
    with dissolve
    
    "So I guess this is where I’m meeting Stone today."
    "If that even {i}is{/i} their real name…"
    "Honestly, I never really knew them well in person. They’re just someone my other friends introduced me to in Meta."
    "Still, might as well try to get to know them."
    "Besides, I don’t mind waiting on a nice tropical island."
    "They should be arriving any second no-"
    mc "OW!"

    play music "audio/yoshi.mp3" fadein 2.0
    scene bg beach
    with dissolve
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
    sy "Date failed. Returning to plaza."

    jump end_st_date

label st_1_2:
    mc "Your name…suits you…very well."
    hide stone base
    show stone_blush
    st "Oh. Uhhhh…Thank you."
    "Are they blushing? I really can’t tell with someone as stone-faced as…well…a stone."
    hide stone_blushe
    show stone base
    st "Anyway, sorry about dropping on your head. I tend to lose myself when I’m rocking to some tunes."
    mc "Um. That’s okay."
    st "So, now that we’re here, how should we start this date?"
    mc "Uh...I dunno. Icebreakers?"
    st "Oh. Right. How could that have slipped my mind?"
    st "I guess that’s just what happens with someone as hard-headed as me."
    "Hard-headed…"
    "At this point it’s just sinking in that I am dating a literal rock…"
    "How did my life lead to this moment?"
    "I can totally feel the world judging me at this very moment."
    st "Okay so…what questions should we ask each other?"
    "Are people staring at us?"
    "Oh God people are totally staring at us. Aren’t they?"
    st "Oh right. Meta’s Find My Friend System has a built-in questionnaire. That will do."
    st "So…what genre of music do you like to listen to?"
    mc "..."
    st "Oh y-you don’t need to answer if you don’t want to. I can answer first."
    st "Ahem, so…my favorite genre of music is-"
    mc "I can’t do this."
    st "Huh?"
    mc "I have better things to do than dating a freaking rock…"
    mc "I’m out."
    st "...what?"
    mc "Byeeeeeee."

    stop music fadeout 1.0
    play music "audio/zucchini.mp3" fadein 2.0
    jump end_st_date

label end_st_date:
    jump hub_2