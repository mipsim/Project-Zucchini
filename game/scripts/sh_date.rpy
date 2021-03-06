label sh_date:
    #[BLACK]
    scene bg black
    with dissolve

    "I breathe a sigh of relief after finishing the last mandated ad to pay for my Meta Eats™ driver’s health benefits."

    #[FLOWER BOUQUET POPS UP AND LIGHTS UP]
    show bouquet at tran_bouquet
    with dissolve

    "I couldn’t afford to tip them today because I had to pick up a bouquet of Meta Flowers™."
    "It would have been cheaper to get the low poly variety, but she’s a queen and she deserves the high resolution."

    #[FLOWER BOUQUET DARKENS]
    hide bouquet
    show bouquet shaded at tran_bouquet
    with dissolve
    
    play sound "audio/streamstart.mp3"
    "Oh?"
    "The familiar chime of her stream starting rings and the notification takes up most of my HUD."
    "I instantly swipe at it to be transported to her audience box."

    #[BLACK FADES, FLOWERS DISAPPEAR]
    #[STREAM OVERLAY, HOT TUB BACKGROUND]
    scene bg streamer
    hide bouquet shaded
    with dissolve

    show streamtitle
    with easeintop
    show streamoverlay0
    with easeintop

    play music "audio/batterup.mp3" fadein 2.0

    "Today's the day!"

    hide streamoverlay0
    show streamoverlay1
    "My Meta TV™ hot tub date with my favorite streamer Shizuha!"
    hide streamoverlay1
    show streamoverlay2
    "I had to use my mom's ethereum wallet to get enough channel points to redeem the hot tub stream."

    #[SHIZUHA POPS IN BOTTOM RIGHT CORNER, DO A FUNNY LITTLE PANNING HER UP FROM THE BOTTOM OF THE FRAME IF POSSIBLE]
    #[HAPPY SPRITE]
    show shizuha_happy at st_intro_two
    with easeinbottom
    hide streamoverlay2
    show streamoverlay3
    sh "Ohayo darlings it's your favorite miko mommy!" with vpunch

    #[NEUTRAL SPRITE]
    hide shizuha_happy
    show shizuha_neutral at st_intro_two

    hide streamoverlay3
    show streamoverlay4
    sh "Are any of my cuties in the chat tonight?"
    hide streamoverlay4
    show streamoverlay5
    "I have to let her know I’m here!"
    "What should I write in chat though?"

    jump sh_choice_1

menu sh_choice_1:
    #ALL LEAD TO THE SAME DIALOGUE
    "What should I write in chat though?"

    "Call her mommy":
        hide streamoverlay5
        show streamoverlay6
        mc "{i}shizuhasimp{/i}: hi mommy!"
        jump sh_date_2

    "Say something funny":
        hide streamoverlay5
        show streamoverlay6
        mc "{i}shizuhasimp{/i}: POGGERS"
        jump sh_date_2

    "Send an emote":
        hide streamoverlay5
        show streamoverlay6
        with None
        show beachuangy
        with easeintop
        mc "{i}shizuhasimp{/i}: *spawn beachuAngy emote*"
        hide beachuangy
        with easeoutbottom
        jump sh_date_2

label sh_date_2:
    #[MAD SPRITE]
    hide shizuha_neutral
    show shizuha_mad at st_intro_two
    hide streamoverlay6
    show streamoverlay7
    sh "No dicks in chat {i}milkersfan98{/i}!" with hpunch

    #[HAPPY SPRITE]
    hide shizuha_mad
    show shizuha_happy at st_intro_two
    hide streamoverlay7
    show streamoverlay8
    hide streamtitle
    show streamtitle2
    sh "Thank you for the tier three sub {i}sussyxbaka{/i}!"
    hide streamoverlay8
    show streamoverlay9
    hide shizuha_happy
    show shizuha_smug at st_intro_two
    sh "Aww that’s so funny {i}shizuh{/i}–"

    #[SURPRISE SPRITE]
    hide shizuha_smug
    show shizuha_surprised at st_intro_two
    hide streamoverlay9
    show streamoverlay10
    play sound "audio/yooo.mp3"
    "All of a sudden, a 100 Dogecoin donation rolls in!" with vpunch
    hide streamoverlay10
    show streamoverlay11
    hide shizuha_surprised
    show shizuha_extrasmug at st_intro_two
    sh "Daww {i}basebussy{/i} thank you for the 100 Dogecoins!"
    hide streamoverlay11
    show streamoverlay12
    hide shizuha_extrasmug
    show shizuha_surprised at st_intro_two
    sh "You didn’t have to do that! You’re so nice can we get a shizuhaHeart spam in chat?"
    hide streamoverlay12
    show streamoverlay13
    "Damn him she was just about to say my name on stream!" with vpunch

    #[NEUTRAL SPRITE]
    hide shizuha_surprised
    show shizuha_happy at st_intro_two
    hide streamoverlay13
    show streamoverlay14
    sh "Today we have a very special stream!"
    hide streamoverlay14
    show streamoverlay15
    hide shizuha_happy
    show shizuha_neutral at st_intro_two
    sh "Sponsored by ChonkersHQ and of course, NordVPN."
    hide streamoverlay15
    show streamoverlay16
    sh "Check my link in the bio for 10 percent off your ninth month!"
    hide streamoverlay16
    show streamoverlay17
    hide shizuha_neutral
    show shizuha_surprised at st_intro_two
    sh "Is {i}shizuhasimp{/i} on my stream tonight?"

    hide streamoverlay17
    with easeouttop
    show shizuha_surprised at center
    with ease

    "Wait that’s me!"

    #[HAPPY SPRITE]
    hide shizuha_surprised
    show shizuha_happy
    sh "We had our first 50 billion point redemption last night, which means we’re having a hot tub date stream!"

    play sound "audio/streamstart.mp3"
    "You see a ping pop up on your HUD. It’s an invite to her Meta Space™! No cap, no kizzy, on god no way you decline this!"
    jump sh_choice_2

menu sh_choice_2:
    "What should I do?"

    "Decline?":
        hide shizuha_happy
        show shizuha_surprised
        sh "Oh? Okay then."
        sh "Guess someone else can join me in the hot tub then."
        sh "See ya loser."
        sy "Date failed. Returning to Plaza."
        $ sh_date = False
        $ st_missing = False
        jump end_sh_date

    "Accept of course!":
        jump sh_date_3

label sh_date_3:
    mc "This is so exciting, I’ve never been in a girl’s Meta Space™ before!"

    #[SMUG SPRITE]
    hide shizuha_happy
    show shizuha_smug
    sh "Aha of course not, you nerd loser."
    mc "Wait what did you just say?"

    #[HAPPY SPRITE]
    hide shizuha_smug
    show shizuha_happy
    sh "I’m so happy one of my longest watching viewers is finally on my stream!"
    "Oh that must have just been background noise. That’s so silly of me."
    hide shizuha_happy
    show shizuha_surprised
    sh "Oh wow is that a 5 star Gucci fanny pack on your avatar???"
    "Fuck yeah, I knew it was worth swiping for 30 rolls on the Gucciverse collab."
    mc "Yeah! Isn’t it cool? I think the devs only released like 3 of these!"

    #[NEUTRAL SPRITE]
    hide shizuha_surprised
    show shizuha_neutral
    "Her eyes shifted into a sudden squint, boring holes through my avatar."
    sh "Oh! That’s very...nice! That’s a weird coincidence. I think one of my friends has the same bag."
    "Weird. I thought this’d be her first time gazing upon one of these babies."
    hide shizuha_neutral
    show shizuha_smug
    sh "Why don’t we get started with the date tonight?"
    "She snaps her fingers and my avatar gets moved into the hot tub."

    scene bg streamertub
    with dissolve
    show streamtitle2
    with easeintop
    hide shizuha_smug
    show shizuha_extrasmug at st_intro_two
    with easeinbottom

    "Wow. It’s unnervingly warm. Not even going to question how my headset is doing that"
    sh "You’re probably going to see a heftier than usual heating bill this month by the way."
    "That explains it all."
    mc "I won’t be able to pay for next month’s sub at this rate!"

    #[SMUG]
    hide shizuha_extrasmug
    show shizuha_smug at st_intro_two
    sh "You’d better start tightening that belt then."
    mc "So what do you like doing outside of streaming Shizuha?"

    #[HAPPY]
    hide shizuha_smug
    show shizuha_happy at st_intro_two
    sh "Well in my free time, believe it or not, I practice a lot of kendo."
    mc "I have a friend who does that too! She’s actually a big fan of yours and copied your avatar too."

    #[SMUG]
    hide shizuha_happy
    show shizuha_smug at st_intro_two
    sh "She sounds spiffy! It’d be cool if I could meet her, especially if she’s a viewer."
    "It would be funny to see two Shizuha avatars fighting each other."

    #[SURPRISE]
    hide shizuha_smug
    show shizuha_surprised at st_intro_two
    who "KOUSUKE REVIVE ME KOUSUKE REVIVE ME NOW IM DOWN!" with vpunch
    mc "What was that??"

    hide shizuha_surprised
    show shizuha_sad at st_intro_two
    sh "Oh that was just my da– mn roommate! She’s been really invested in this new Fortnite game mode."
    mc "Oh fair enough. Sounded weirdly familiar though."

    #[HAPPY]
    hide shizuha_sad
    show shizuha_happy at st_intro_two
    sh "Do you happen to have any pets? I’ve got some bunnies that I take care of at home!"
    mc "Well, I do have a crab now. My cousin brought it home one day from a beach trip."
    
    hide shizuha_happy
    show shizuha_surprised at st_intro_two
    sh "Wait a crab? How do you even take care of a crab?"
    mc "I’m not really sure honestly. It kinda just waddles around and occasionally presents me with random bits and bobs."
    sh "Must have been one strange beach tri–"

    #[SUDDEN BLACK]
    stop music fadeout 1.0

    hide streamtitle2
    hide shizuha base
    scene bg black

    "Shit, did I get disconnected?"
    mc "Hello?"

    #[FADE IN FROM BLACK]
    #[STREAM OVERLAY DISAPPEARS, HOT TUB STAYS]
    scene bg streamertub
    with dissolve

    #[REPLACE SPRITE WITH NORMAL IMAGE, NOT VTUBER]
    show shizuha base at st_intro_two
    sh "Whoops, looks like my internet died for a second there."

    #[BRING BACK VTUBER, SURPRISE SPRITE]
    hide shizuha base
    show shizuha_surprised at st_intro_two

    play music "audio/giantmiko.mp3" fadein 2.0
    sh "AH–" with vpunch
    mc "Wait, no way! Your avatar..."

    jump sh_choice_3

menu sh_choice_3:
    "What should I do?"

    "It’s so kind of you to share your avatar with your fans!":
        hide shizuha_surprised
        show shizuha_sad at st_intro_two
        sh "I have no idea what you're talking about."
        sh "But, I do know that the hot tub date stream is now officially over."
        sh "Feel free to get out of here immediately."
        sy "Date failed. Returning to Plaza."
        $ sh_date = False
        $ st_missing = False
        jump end_sh_date

    "You must be my friend Sh1zuha!":
        jump sh_date_4

label sh_date_4:
    sh "W-wuh who’s that?"
    mc "Look I might be dumb enough to have paid for a damn hot tub date, but I can see clearly when things are this obvious!"
    hide shizuha_surprised
    show shizuha_sad at st_intro_two
    sh "N-no…"
    mc "The name! The eerily similar everything! Have you been lying to me this whole time?"
    
    #[NEUTRAL]
    hide shizuha_sad
    show shizuha_neutral at st_intro_two
    sh "I wasn’t lying to you…but I did know who you were when I saw your bag, so I played along."
    mc "Well I hope you had fun messing with me."
    hide shizuha_neutral
    show shizuha_sad at st_intro_two
    sh "I just didn’t want you to realize it was me behind the cute persona."
    sh "The Kibashi family has a reputation to uphold, you know?"
    sh "It’s weird, but it makes me happy to relax sometimes."
    mc "You’re usually so stone faced with me and Hanami and Stone, so I couldn’t put two and two together."
    
    #[EXTRASMUG]
    hide shizuha_sad
    show shizuha_extrasmug at st_intro_two
    sh "Well the stream’s over now and there’s no more secrets. How about we just play some {i}Choke Slam{/i} now?"
    mc "We’re talking about the game right?"

    #[SMUG, SLOW ZOOM FACE]
    show shizuha_extrasmug at st_intro_two:
        yalign 0.7
        ease 0.5 zoom 2.0

    #[SLOW FADE TO BLACK]
    jump end_sh_date

label end_sh_date:
    scene bg black
    with dissolve

    stop music fadeout 1.0

    jump hub_2