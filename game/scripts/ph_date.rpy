label ph_date:
    scene bg black
    with dissolve

    # Music Call
    play music "audio/disc_call.mp3"
    #sy "*Discord call received*"
    sy "Incoming call from {i}Xx_BunnyPunter_69{/i}"
    
    # SFX Join
    stop music
    play sound "audio/disc_join.mp3"
    ph "Hey hey join this server, and add me on Fortnite, {i}Xx_BunnyPunter_69{/i} okay?"
    sy "AR notifications stream onto your HUD, the last being a game invite"

    scene bg select
    with dissolve
    play music "audio/fokehs.mp3" fadein 2.0
    show hanami_speak
    with easeinright

    ph "*Splashing*"
    who "Ohayo darlings it’s your favorite Miko Mommy!"
    ph "Sorry thats my fucking streamer roommate, where is-"

    # SFX Join
    play sound "audio/disc_join.mp3"
    #sy "*Discord call join*"

    hide hanami_speak
    show kousuke_speak
    ks "Hellooo??"
    hide kousuke_speak
    show hanami_speak
    ph "Yeah Kousuke we can hear you."
    hide hanami_speak
    show kousuke_speak
    ks "Hello, guys?"
    hide kousuke_speak
    show hanami_speak
    ph "YES!! WE CAN-" with vpunch
    hide hanami_speak
    show kousuke_speak
    ks "I can’t hear, hold-"
    
    # SFX Leave
    play sound "audio/disc_leave.mp3"
    #sy "*Discord call leave*"
    
    hide kousuke_speak
    show hanami_speak
    ph "Oh my god."
    mc "Is he okay?"
    ph "Not really, the technological revolution hit him pretty hard."
    ph "He hasn’t been the same ever since mom sold the family shrine to a memecoin stock exchange."
    ph "They bulldozed it to build a datacenter."
    
    # SFX Join
    play sound "audio/disc_join.mp3"
    #sy "*Discord call join*"
    
    hide hanami_speak
    show kousuke_speak
    ks "Okay everyone, I re-plugged in my mic."
    hide kousuke_speak
    show hanami_speak
    ph "Yeah good, you figured out technology."
    ph "JOIN THE GAME ALREADY!" with vpunch
    hide hanami_speak
    show kousuke_speak
    ks "Hang on!! There’s popups. Which ones of these are traffic lights…"
    hide kousuke_speak
    show hanami_speak
    ph "Jesus christ, somebody installed an ”I am human” virus on his setup."
    ph "Everytime some bot needs to pass off as human it routes the captcha to his screen."
    ph "And for SOME REASON he doesn’t clear it, HE JUST  DOES THE CAPTCHAS!" with vpunch
    hide hanami_speak
    show kousuke_speak
    ks "You seem upset, but I can identify sailboats in a matter of seconds. I think you’re just jealous."
    hide kousuke_speak
    show hanami_speak
    ph "..."
    sy "Kousuke's avatar appears and the matchmaking symbol instantly ignites."
    
    stop music fadeout 1.0
   
    scene bg dropping
    with dissolve
    show hanami_speak
    with easeinright

    play music "audio/shizuhafight.mp3" fadein 2.0

    mc "So…do you play this game often?"
    ph "Yeah I have like 2,000 hours."
    ph "Where we droppin boys?"
    mc "Uhh, I don’t know how to play this game. You pick."
    ph "I can land anywhere, it doesn’t matter to me."
    mc "We are literally about to hit the ground."
    ph "Where the fuck are you going Kousuke?"
    hide hanami_speak
    show kousuke_speak
    ks "To the mountains, where I can be alone…"
    hide kousuke_speak
    show hanami_speak
    ph "KOUSUKE THATS A-" with vpunch
    play sound "audio/sizzle.ogg"
    sy "*Kousuke tried to swim in lava*"
    ph "Volcano."
    hide hanami_speak
    show kousuke_speak
    ks "It’s alright. This thing is saying I can mint VBucks to respawn!"

    scene bg fortnite
    with dissolve
    show hanami_speak
    with easeinright

    ph "Okay, you. Grab guns in that house!"
    mc "I can’t find anything!"
    sy "*Footsteps nearby*"
    mc "Shit! Hanami HELP!" with vpunch
    ph "Get down!!" with vpunch
    sy "{i}Xx_BunnyPunter_69{/i} downed {i}xXEveningCapeXx{/i}"
    sy "{i}xXEveningCapeXx{/i} left the game"
    mc "Shut up! Drink this chug jug!"
    hide hanami_speak
    show kousuke_speak
    ks "I’m almost back from the gulag everyone!"
    mc "Why is that one spinning?"
    hide kousuke_speak
    show hanami_speak
    ph "FU-" with hpunch
    sy "{i}Groovy-Bot{/i} downed {i}Xx_BunnyPunter_69{/i}"
    sy "{i}Groovy-Bot{/i} downed {i}ShizuhaSimp{/i}"
    hide hanami_speak
    show kousuke_speak
    ks "I’m running to you!"
    hide kousuke_speak
    show hanami_speak
    ph "KOUSUKE REVIVE ME KOUSUKE REVIVE ME NOW I’M DOWN" with vpunch
    sy "{i}Groovy-Bot{/i} downed {i}jojusoju{/i}"
    hide hanami_speak
    show kousuke_speak
    ks "What happened, I’m crawling on the floor?"
    hide kousuke_speak
    show hanami_speak
    ph "Ugh, how are there even cheaters in this game???"
    mc "It was nice playing with you Hanami-"
    sy "{i}Xx_BunnyPunter_69{/i} left the game"
    mc "Oh, ok."

    stop music fadeout 1.0
    jump end_ph_date

label end_ph_date:
    jump hub_2