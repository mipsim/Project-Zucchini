label find_my_friend:
    mz "Who would you like to find?"

    python: # Player types in name of Character
        search_name = renpy.input("Enter first and last name (case insensitive)", length=32)
        search_name = search_name.strip()

    if search_name == "Hanami Kibashi" or search_name == "hanami kibashi":
        # Add Hanami back to the pool of available characters
        # Then go play a short reunion that's cut short by the zucc
        # back again to the hub_2
        $ ph_missing = False

        show hanami base at center
        with easeinright

        play sound "audio/friendfound.mp3"

        st "Yo! I'm not in the Spirit Realm anym-"
        hide hanami base
        with easeoutleft

        mz "Congratulations on finding Hanami Kibashi!"
        jump after_search

    if search_name == "Shizuha Kibashi" or search_name == "shizuha kibashi":
        $ sh_missing = False

        show shizuha_happy at center
        with easeinright

        play sound "audio/friendfound.mp3"

        sh "Aw, I knew you could never forget m-"
        hide shizuha_happy
        with easeoutleft

        mz "Congratulations on finding Shizuha Kibashi!"
        jump after_search

    if search_name == "Stone" or search_name == "stone":
        $ st_missing = False

        show stone base at center
        with easeinright

        play sound "audio/friendfound.mp3"

        st "I'm back! Thank y-"
        hide stone base
        with easeoutleft

        mz "Congratulations on finding Stone!"
        jump after_search

    if search_name == "Mark Zucchiniberg" or search_name == "mark zucchiniberg":
        mz "Oh, don't worry about me. I'd never leave you on your own."
        jump after_search

    if search_name == "Metaverse Zucciniberg" or search_name == "metaverse zucciniberg":
        # Seems like nothing happened but the background get's weird and true ending is ready to go
        scene bg warpedb
        with dissolve and hpunch
        jump after_search

    mz "Sorry, we can't find who you're looking for."
    jump after_search

menu after_search:
    "What would you like to do next?"

    "Search again":
        jump find_my_friend

    "Return to Plaza":
        jump hub_2