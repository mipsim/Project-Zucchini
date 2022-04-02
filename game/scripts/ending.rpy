label ending:

    if ph_missing and sh_missing and st_missing:
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
    mz "Come back soon! I'll be waiting."

    jump end_game

label end_game_mark:

    "Mark"