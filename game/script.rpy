# Start
label start:
    jump intro

menu choose_date_1:
    mz "Please choose who you want to go on a date with."

    "Play fortnite with Punished Hanami":
        jump date_hanami

    "Go to the hot tub with Shizuha Kibashi":
        jump date_shizuha

    "Hang out with Stone":
        jump date_stone

label date_hanami:
    $ ph_date = True
    $ sh_missing = True

    stop music fadeout 1.0
    play music "audio/chugjug.mp3" fadein 2.0
    jump ph_date

label date_shizuha:
    $ sh_date = True
    $ st_missing = True

    stop music fadeout 1.0
    jump sh_date

label date_stone:
    $ st_date = True
    $ ph_missing = True

    stop music fadeout 1.0
    play music "audio/yoshi.mp3" fadein 2.0
    jump st_date

label hub_2:
    scene bg warped
    with dissolve

    play music "audio/zucchini.mp3" fadein 2.0

    if ph_missing != True:
        show hanami base at ph_intro_three
    if sh_missing != True:
        show shizuha base at sh_intro_two
    if st_missing != True:
        show stone base at st_intro_three
    with easeinright

    if ph_missing and sh_missing:
        st "Where do you think the other two went?"
        mc "Well, Hanami usually has baseball practice at this time."
        mc "Which means Shizuha is probably cleaning the temple."
        st "Hey."
        st "Since it's just us now."
        st "Maybe we could-"
        mc "Hey look it's Zucchini."
        jump zucc_return

    if sh_missing and st_missing:
        ph "Hellooo?"
        ph "Mom, stone, where are youuu?"
        mc "Maybe Shizuha dropped Stone in her bathtub."
        ph "Dude,"
        ph "what the hell."
        jump zucc_return

    if ph_missing and st_missing:
        sh "Looks like Hanami's still missing."
        mc "Don't worry, we'll find her."
        mc "But, I swear there were four of us when we started playing."
        mc "What was their name again?"
        jump zucc_return

    if ph_missing:
        st "Hey, we're back."
        sh "Wait a second..."
        sh "Hanami?"
        sh "HANAMI??" with hpunch
        mc "Shizuha, calm down."
        st "Yeah I'm sure she-"
        sh "Shut up stone!"
        mc "Uh oh Zucchini's coming back."
        jump zucc_return

    if sh_missing:
        ph "Man that was so much fun!"
        ph "I can't wait to tell mom about i-"
        ph "Hey."
        ph "Stone."
        st "Yes?"
        ph "Has my mom come back yet?"
        st "I don't know. I came back when you two did."
        mc "Hm, maybe Zucchini saw her."
        jump zucc_return

    if st_missing:
        ph "Oh, we're back."
        sh "Not all of us."
        mc "Where's Stone?"
        ph "Who?"
        mc "Oh god, here comes Zucchini again."
        jump zucc_return

label zucc_return:
    show zuck base at mz_intro_two
    with easeinbottom
    mz "Welcome back to the plaza!"
    jump choose_date_2

menu choose_date_2:
    mz "Would you like to go on another date, or find a friend?"

    "Play fortnite with Punished Hanami" if ph_missing != True and ph_date != True:
        jump date_hanami
    
    "Go to the hot tub with Shizuha Kibashi" if sh_missing != True and sh_date != True:
        jump date_shizuha

    "Hang out with Stone" if st_missing != True and st_date != True:
        jump date_stone

    "Find My Friend":
        if ph_missing != True:
            hide hanami base
        if sh_missing != True:
            hide shizuha base
        if st_missing != True:
            hide stone base
        with easeoutleft
        
        show zuck base at center
        with ease

        jump find_my_friend

    "Enough of the dates!":
        jump end_game

label end_game:
    return
