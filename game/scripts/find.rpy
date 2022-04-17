label find_my_friend:
    mz "Who would you like to find?"

    python: # Player types in name of Character
        search_name = renpy.input("First, enter your missing friend's full legal name (case insensitive)", length=32)
        search_name = search_name.strip()

    # [Hanami]
    if search_name == "Punished Hanami" or search_name == "punished hanami" or search_name == "Hanami" or search_name == "hanami":
        sy "Sorry, we can't find who you're looking for."
        sy "We suggest: Try using their full legal name, not the nickname they ask you to call them!"
        jump after_search

    if search_name == "Hanami Kibashi" or search_name == "hanami kibashi":
        if ph_missing != True:
            show hanami base
            with easeinright
            ph "Hey um, I'm right here?"
            sy "This friend was not in need of finding."
            hide hanami base
            with easeoutleft

            jump after_search

        sy "User found! Proceeding with friend verification question:"

        show trafficaptcha at tran_captcha
        with easeintop
        "Q: How many traffic lights are in this picture?"

        jump test_hanami

    # [Shizuha]
    if search_name == "shizuha" or search_name == "sh1zuha" or search_name == "kibashi" or search_name == "Shizuha" or search_name == "Sh1zuha" or search_name == "Kibashi":
        sy "Sorry, we can't find who you're looking for."
        sy "We suggest: Try using their full name, first and last. But make sure you figure it out and read it carefully."
        sy "Have you watched their stream?"
        jump after_search

    if search_name == "shizuha kibashi" or search_name == "Shizuha Kibashi":
        sy "Sorry, we can't find who you're looking for."
        sy "We suggest: Check your spelling! You may be looking for someone with a similar name."
        jump after_search

    if search_name == "Sh1zuha Kibashi" or search_name == "sh1zuha kibashi":
        if sh_missing != True:
            show shizuha_mad
            with easeinright
            sh "Thanks, but I'm already here."
            sy "This friend was not in need of finding."
            hide shizuha_mad
            with easeoutleft
            
            jump after_search

        sy "User found! Proceeding with friend verification question:"
        jump test_shizuha

    # [Stone]
    if search_name == "stone stone" or search_name == "rock" or search_name == "stone rock" or search_name == "Stone Stone" or search_name == "Rock" or search_name == "Stone Rock":
        sy "Sorry, we can't find who you're looking for."
        sy "We suggest: Try using just their name, don't get fancy."
        jump after_search

    if search_name == "Stone" or search_name == "stone":
        if st_missing != True:
            show stone base
            with easeinright
            st "Huh?"
            sy "This friend was not in need of finding."
            hide stone base
            with easeoutleft
            
            jump after_search

        sy "User found! Proceeding with friend verification question:"
        jump test_stone

    # [Mark 1]
    if search_name == "Mark Zucchiniberg" or search_name == "mark zucchiniberg":
        mz "Oh, don't worry about me. I'd never leave you on your own."
        jump after_search

    # [Mark 2]
    if search_name == "Plaza Zucchiniberg" or search_name == "plaza zucchiniberg":
        scene bg warpedb
        $ pl_found = True 
        with dissolve and hpunch
        jump after_search

    sy "Sorry, we can't find who you're looking for."
    jump after_search

menu test_hanami:
    "Q: How many traffic lights are in this picture?"

    "A: 0":
        hide trafficaptcha
        with easeoutbottom
        "We're sorry, but that was incorrect." with hpunch
        jump after_search
    "B: 7":
        hide trafficaptcha
        with easeoutbottom
        "We're sorry, but that was incorrect." with hpunch
        jump after_search
    "C: 6":
        hide trafficaptcha
        with easeoutbottom
        "We're sorry, but that was incorrect." with hpunch
        jump after_search
    "D: 2 fuckin many":
        hide trafficaptcha
        with easeoutbottom
        "Correct!"
        jump found_hanami

menu test_shizuha:
    "Q: Who is their favorite tier 3 sub?"

    "A: shizuhasimp":
        "We're sorry, but that was incorrect." with hpunch
        jump after_search
    "B: basebussy":
        "Correct!"
        jump found_shizuha
    "C: eveningcape":
        "We're sorry, but that was incorrect." with hpunch
        jump after_search
    "D: grainy":
        "We're sorry, but that was incorrect." with hpunch
        jump after_search
    
menu test_stone:
    "Q: What is Stone's favorite music genre?"

    "A: Rock":
        "Correct!"
        jump found_stone
    "B: Pop":
        "We're sorry, but that was incorrect." with hpunch
        jump after_search
    "C: Orchestral":
        "We're sorry, but that was incorrect." with hpunch
        jump after_search
    "D: Shinto-era":
        "We're sorry, but that was incorrect." with hpunch
        jump after_search

label found_hanami:
    $ ph_missing = False

    show hanami base at center
    with easeinright

    play sound "audio/friendfound.mp3"

    ph "Yo! I'm not in the Spirit Realm anym-"
    hide hanami base
    with easeoutleft

    mz "Congratulations on finding Hanami Kibashi!"
    jump after_search    

label found_shizuha:
    $ sh_missing = False

    show shizuha_happy at center
    with easeinright

    play sound "audio/friendfound.mp3"

    sh "Aw, I knew you could never forget m-"
    hide shizuha_happy
    with easeoutleft

    mz "Congratulations on finding Sh1zuha Kibashi!"
    jump after_search

label found_stone:
    $ st_missing = False

    show stone base at center
    with easeinright

    play sound "audio/friendfound.mp3"

    st "I'm back! Thank y-"
    hide stone base
    with easeoutleft

    mz "Congratulations on finding Stone!"
    jump after_search

menu after_search:
    sy "What would you like to do next?"

    "Search again":
        jump find_my_friend

    "Return to Plaza":
        jump hub_2