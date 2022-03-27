define mz = Character("Mark Zucchini-Berg")
define ph = Character("Punished Hanami")
define who = Character("???")

# ATL
transform zoom_dissolve:
    xalign 0.5 yalign 1.0
    alpha .0 zoom .75
    linear .25 alpha 1.0 zoom 1.0
    on hide:
        xalign 0.5 yalign 1.0
        alpha 1.0 zoom 1.0
        linear .25 alpha .0 zoom .75

label start:
    scene bg select
    show zuck base at zoom_dissolve
    play music "audio/gates.mp3" fadein 2.0

    mz "Hi, I’m mark zucchini-berg."
    mz "Welcome to the metaverse."
    mz "Here at meta we are committed to connecting you to the people you really care about."
    mz "To do so we developed a new patented peer evaluation n’ interconnection system."
    mz "Haven’t talked to a friend in weeks?"
    mz "Don’t worry about it."
    mz "We’ll remove them from your personal space for you."
    mz "This way you can avoid those awkward conversations about how you never see each other anymore."
    mz "If you still care about them, don’t worry."
    mz "The procedure to get them back is quite simple."
    mz "Just go to the settings menu and click the “Find my friend” button."
    mz "It’ll prompt you to enter the friend’s full legal name."
    mz "Don’t worry if you can’t remember their name off the top of your head."
    mz "They probably weren’t that good of a friend anyways."
    mz "In order to ensure the security and privacy of all our users we’ve now added a questionnaire to the find my friend functionality."
    mz "After entering their full legal name you’ll answer a series of short questions."
    mz "Don’t worry, there’s nothing on here that good friends wouldn’t know about each other."
    mz "Just simple questions like:"
    mz "“What is their favorite color?”"
    mz "“What foods do they like to eat?”"
    mz "“What were they doing between the times of 5p.m. and 7p.m. on sunday march 20th?”"
    mz "Here at meta we are all about giving you the experience you deserve,"
    mz "with the people you really care about."
    mz "Welcome,"
    mz "to the metaverse."

    python:
        povname = renpy.input("First, what is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Eli"

    mz "Ah, nice to meet you [povname]."

    jump choice_end

menu choice_end:
    "What will you do?"

    "Could you repeat that please?":
        jump start

    "I'm looking for Hanami Kibashi":
        jump route_ph

    "F the metaverse I'm out":
        jump end_game

label route_ph:
    hide zuck base
    scene bg dropping
    play music "audio/chugjug.mp3" fadein 2.0

    who "There you are!"
    who "So, where are we dropping?"
    povname "Huh?"
    who "Ooo, let's go there!"
    povname "Wait, don't touch m-"
    "The next thing I know we're falling out of the Party Bus."

    scene bg fortnite
    show hanami base at zoom_dissolve
    ph "Nice landing [povname]!"
    ph "Let's get going, before they take all the good loot."

    jump end_game

label end_game:
    return
