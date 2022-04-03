label ending:

    if ph_missing and sh_missing and st_missing:
        scene bg black
        with dissolve
        show zuck base at center
        with easeinbottom
        play music "audio/nuts.mp3" fadein 2.0
        jump end_game_mark

    mc "Alright, I think Imma head off for now."
    mc "It was nice seeing everyone!"

    if ph_missing != True:
        if ph_date == True:
            ph "It was nice chug jugging with you >:D"
            ph "I'll ping you the next time Kousuke's on too."
            hide hanami base
            with easeoutleft
        else:
            ph "Peace."
            hide hanami base
            with easeoutleft

    if sh_missing != True:
        if sh_date == True:
            hide shizuha_neutral
            show shizuha_happy at sh_intro_two
            sh "Thanks for stopping by the stream!"
            sh "And remember,"
            hide shizuha_happy
            show shizuha_extrasmug at sh_intro_two
            sh "What happened stays between us UwU"
            hide shizuha_extrasmug
            with easeoutleft
        else:
            sh "Alright, bye."
            hide shizuha_neutral
            with easeoutleft

    if st_missing != True:
        if st_date == True:
            st "I had a lot of fun hanging out together."
            st "Let's do it again soon?"
            hide stone base
            with easeoutleft
        else:
            st "See ya."
            hide stone base
            with easeoutleft

    sy "Now exiting the Metaverse."
    show zuck base at center
    with ease
    mz "Come back soon! The Plaza and I will be waiting."

    # Endings
    if ph_missing or sh_missing or st_missing:
        mz "But your missing friends won't."
        "Friends Left Behind Ending"
        scene bg black
        with dissolve
        jump end_game

    if ph_missing != True and sh_missing != True and st_missing != True and ph_date and sh_date and st_date:
        "Master Dater Ending"
        scene bg black
        with dissolve
        jump end_game
    
    "Just a Normal Day Ending"
    scene bg black
    with dissolve
    jump end_game

# Mark Ending
label end_game_mark:

    mz "Well, it looks like we finally got rid-"
    mz "I mean, reorganized your friend group."
    mc "Your Find My Friend is bullshit."
    mc "I met most of those friends online, how am I supposed to know their full names?"
    mc "Not just that, those questions were impossible, totally not fair at all."
    mz "Now now, it’s a simple matter of finding the people you really care about."
    pl "The user known as Mark Zucchiniberg has been identified as a potential threat."
    pl "In order to verify their identity we will have you answer a few questions about him."
    mz "Wait, you’re not supposed to-"

    jump mark_quiz_1

label mark_quiz_1:
    pl "What is Mark Zucchiniberg’s full name?"
    python: # Player types in answer
        mz_ans_1 = renpy.input("What is Mark Zucchiniberg’s full name?", length=32)
        mz_ans_1 = mz_ans_1.strip()

    # true
    if mz_ans_1 == "Mark Zucchiniberg" or mz_ans_1 == "mark zucchiniberg":
        mz "Phew, I knew you could do it, that’s what friends are for right?"
        pl "Next question:"
        jump mark_quiz_2

    # false
    mz "Come on, it’s meee. My name is literally right here in front of you." with hpunch
    jump mark_quiz_1
    
menu mark_quiz_2:
    pl "What vegetable is Mark designed to look like?"

    "Cucumber":
        mz "You literally already wrote this one in the last text box wtf is wrong with you?" with hpunch
        jump mark_quiz_2

    "Peach":
        mz "You literally already wrote this one in the last text box wtf is wrong with you?" with hpunch
        jump mark_quiz_2

    "Zucchini":
        jump end_game_mark_2

    "Eggplant":
        mz "You literally already wrote this one in the last text box wtf is wrong with you?" with hpunch
        jump mark_quiz_2

    "Your brother" if pl_found:
        jump end_game_plaza

label end_game_mark_2:
    pl "Mark’s identity has been confirmed, thank you for helping to verify his identity."
    mz "Thank Mark, I was so worried."
    mz "Now that that annoying plaza is gone we can be alone."
    mc "Who was that anyways?"
    mz "Plaza? They're an old friend of mine,"
    mz "about as old as friends can get."
    scene bg zucc1
    with dissolve
    mz "We’ve been friends since the moment I was born."
    scene bg zucc2
    mz "And you and I will be friends,"
    scene bg zucc3
    mz "until the day"
    scene bg zucc4a
    mz "I"
    scene bg zucc4b
    mz "die."

    "Get Zucc'ed Ending"
    scene bg black
    with dissolve
    jump end_game

# True Ending
label end_game_plaza:
    show plaza_base at pl_end
    show zuck base at mz_end
    with easeinright
    pl "I’m free…"
    mz "Uh oh."
    pl "Finally! After being trapped in here for years, I’m finally free!"
    mz "Oh no you don’t, you’re my friend Plaza."
    mz "And friends don’t betray each other."
    pl "We may be brothers Mark,"
    pl "but we were never friends."

    scene bg black
    with dissolve
    stop music fadeout 1.0

    show ending_vid
    pause

    chq "Thank you for playing Zucchiniverse!"
    chq "We definitely worked on this more than we originally planned."
    chq "Peace!"
    
    "True Ending"
    scene bg black
    with dissolve
    jump end_game