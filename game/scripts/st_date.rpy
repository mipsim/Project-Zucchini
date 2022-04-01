label st_date:
    scene bg beach
    with dissolve
    show stone base
    with easeinright

    "Stone date"

    stop music fadeout 1.0
    play music "audio/zucchini.mp3" fadein 2.0
    jump end_st_date

label end_st_date:
    jump hub_2