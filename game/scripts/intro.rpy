label intro:
    scene bg black
    with dissolve

    show zuck base
    with easeinbottom
    
    play music "audio/zucchini.mp3"
    
    mz "Hi, I’m Mark Zucchini-berg."
    mz "Welcome to the {i}Metaverse{i}!"
    mz "Here at Meta we are committed to connecting you to the people you really care about."
    mz "To do so we developed a new patented peer evaluation n’ interconnection system."
    mz "Haven’t talked to a friend in weeks?"
    mz "Don’t worry about it."
    mz "We’ll remove them from your personal space for you."
    mz "This way you can avoid those awkward conversations about how you never see each other anymore."
    mz "If you still care about them, don’t worry."
    mz "The procedure to get them back is quite simple."
    #mz "Just go to the Settings Menu and click the “Find My Friend” button."
    mz "When you're in the Plaza, click the “Find My Friend” button."
    #mz "It’ll prompt you to enter the friend’s full legal name."
    mz "Find My Friend will prompt you to enter your missing friend’s full legal name."
    mz "Don’t worry if you can’t remember their name off the top of your head."
    mz "They probably weren’t that good of a friend anyways."
    mz "In order to ensure the security and privacy of all our users, we’ve now added a questionnaire to the Find My Friend functionality."
    #mz "After entering their full legal name you’ll answer a series of short questions."
    mz "After entering their full legal name, you’ll answer a short verification question related to that friend."
    #mz "Don’t worry, there’s nothing on here that good friends wouldn’t know about each other."
    mz "Don’t worry, there’s nothing that good friends wouldn’t know about each other."
    mz "Just simple questions like:"
    mz "“What's their favorite color?”"
    mz "“What foods do they like to eat?”"
    mz "“What were they doing between the times of 5p.m. and 7p.m. on Sunday, March 20th?”"
    mz "Here at Meta we are all about giving you the experience you deserve,"
    mz "with the people you really care about."
    mz "Welcome,"
    mz "to the Metaverse."

    jump hub_1

label hub_1:
    scene bg warped

    hide zuck base
    with dissolve

    "Wow! I'm finally here in the Metaverse."
    "..."
    "....."
    "Kinda looks like shit."

    who "Hey! Looks like you finally got here."
    mc "Hanami is that you?"

    show hanami base
    with easeinright

    ph "That's {i}Punished{/i} Hanami to you."
    mc "..."
    ph "This skin cost me a lot of V-Bucks okay!"
    ph "You better not make fun of it."
    mc "I'll try my hardest."

    show stone base at st_intro_one
    show hanami base at ph_intro_one
    with easeinright

    st "Hey guys, sorry I'm late. It was kinda hard to get the headset on."
    st "I get the feeling it wasn't made with stones in mind."
    st "They really need to work on their accessibility."
    mc "Oh, Shizuha! You're finally here."

    show hanami base at ph_intro_two
    show stone base at st_intro_two
    show shizuha_mad at sh_intro_one
    with easeinright

    sh "Yeah, the ID system to get in this game is pretty strict."
    sh "So it took me a while to get all of my documents."
    ph "Well, now that we're all here, what should we do?"

    show shizuha_mad at sh_intro_two
    show hanami base at ph_intro_three
    show stone base at st_intro_three
    show zuck base at mz_intro_two
    with easeinleft
    hide shizuha_mad
    show shizuha_neutral at sh_intro_two

    mz "Did someone just ask for a tour of our Metaverse featureset?"
    ph "Ummm...no I think we're okay."
    mz "If you would like to stop the feature tour, please say \"STOP\" or another action you would li-"
    ph "STOP!" with hpunch
    hide shizuha_neutral
    show shizuha_surprised at sh_intro_two
    sh "STO;P" with hpunch
    hide shizuha_surprised
    show shizuha_neutral at sh_intro_two
    st "Stop."
    mc "Uh...no thank you Mark. We'd really just like to be left all alone for now."
    mz "You have selected the \"All Alone\" entertainment package."
    mz "I will now split you off for a date with that \"Special Someone\"."
    
    jump choose_date_1