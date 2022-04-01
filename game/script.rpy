# Characters
define mc = Character("You")
define mz = Character("Mark Zucchiniberg")
define ph = Character("Punished Hanami")
define st = Character("Stone")
define sh = Character("Shizuha")
define who = Character("???")

# Variables
default ph_date = False
default ph_missing = False
default st_date = False
default st_missing = False
default sh_date = False
default sh_missing = False

# Animation
transform ph_intro_one:
    xalign -1.0

transform ph_intro_two:
    xalign -6.0

transform ph_intro_three:
    xalign -3.0

transform st_intro_one:
    xalign 0.8

transform st_intro_two:
    xalign 0.85

transform st_intro_three:
    xalign 0.9

transform sh_intro_one:
    xalign 0.6

transform sh_intro_two:
    xalign 0.7

transform mz_intro_two:
    xalign 0.1

# Opening
label start:
    scene bg select
    with dissolve

    show zuck base
    with easeinbottom
    
    play music "audio/zucchini.mp3" fadein 2.0
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
    mz "Just go to the Settings Menu and click the “Find My Friend” button."
    mz "It’ll prompt you to enter the friend’s full legal name."
    mz "Don’t worry if you can’t remember their name off the top of your head."
    mz "They probably weren’t that good of a friend anyways."
    mz "In order to ensure the security and privacy of all our users we’ve now added a questionnaire to the Find My Friend functionality."
    mz "After entering their full legal name you’ll answer a series of short questions."
    mz "Don’t worry, there’s nothing on here that good friends wouldn’t know about each other."
    mz "Just simple questions like:"
    mz "“What is their favorite color?”"
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
    ph "This skin cost me a lot of V-Bucks ok!"
    ph "You better not make fun of it."
    mc "I'll try my hardest."

    show stone base at st_intro_one
    show hanami base at ph_intro_one
    with easeinright

    st "Hey guys, sorry I'm late. It was kinda hard to get the headset on."
    st "I get the feeling it wasn't made with stones in mind."
    st "They really need to work on their accessibility."
    mc "Oh, Shizuha, you're finally here."

    show hanami base at ph_intro_two
    show stone base at st_intro_two
    show shizuha base at sh_intro_one
    with easeinright

    sh "Yeah, the ID system to get in this game is pretty strict."
    sh "So it took me a while to get all of my documents."

    ph "Well, now that we're all here, what should we do?"

    show shizuha base at sh_intro_two
    show hanami base at ph_intro_three
    show stone base at st_intro_three
    show zuck base at mz_intro_two
    with easeinleft

    mz "Did someone just ask for a tour of our Metaverse featureset?"
    ph "Ummm... no I think we're ok."
    mz "If you would like to stop the feature tour, please say \"STOP\" or another action you would li-"
    ph "STOP!" with hpunch
    sh "STO;P" with hpunch
    st "stop."
    mc "umm... no thank you mark, we'd really just like to be left alone for now."
    mz "You have selected the \"All Alone\" entertainment package."
    mz "I will now split you off for a date with that \"Special Someone\"."
    
    jump choose_date_1

menu choose_date_1:
    mz "Please choose who you want to go on a date with."

    "Play fortnite with Punished Hanami":
        jump date_hanami

    "Go to the hot tub with Shizuha Kibashi":
        jump date_shizuha

    "Hang out with Stone":
        jump date_stone

label date_hanami:
    "Hanami date"


    $ ph_date = True
    $ sh_missing = True

    jump hub_2

label date_shizuha:
    "Shizuha date"

    $ sh_date = True
    $ st_missing = True

    jump hub_2

label date_stone:
    "Stone date"

    $ st_date = True
    $ ph_missing = True

    jump hub_2

label hub_2:
    scene bg warped
    with dissolve

    if ph_missing != True:
        show hanami base at ph_intro_three
    if sh_missing != True:
        show shizuha base at sh_intro_two
    if st_missing != True:
        show stone base at st_intro_three
    with easeinbottom

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
        sh "Hanami?"
        mc "Uh oh, Stone's "
        st "Where did the other two go?"
        mc "Maybe they had to leave together?"
        mc "I know Hanami usually has baseball practice at this time."
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

        st "Yo! I'm not in the Spirit Realm anym-"
        hide hanami base
        with easeoutleft

        mz "Congratulations on finding Hanami Kibashi!"
        jump after_search

    if search_name == "Shizuha Kibashi" or search_name == "shizuha kibashi":
        $ sh_missing = False

        show shizuha base at center
        with easeinright

        sh "Aw, I knew you could never forget m-"
        hide shizuha base
        with easeoutleft

        mz "Congratulations on finding Shizuha Kibashi!"
        jump after_search

    if search_name == "Stone" or search_name == "stone":
        $ st_missing = False

        show stone base at center
        with easeinright

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

label end_game:
    return
