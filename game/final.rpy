label final:
    "*Обратная дорога заняла на меньше времени.*"
    "*Геннадий высадил вас у здания, а сам парковать машину.*"
    play sound door6
    $ renpy.pause(3.0, hard=True)
    play music work_b fadein 1.0
    "*Вы вернулись в свой кабинет, включили компьютер и стали заполнять отчет о выезде.*"
    "*Вы тратите какое-то время на заполнение отчета.*"
    "*Вы почти закончили, осталось только указать правильный порядок посещенных объектов.*"
    call schulte_game_screen

    show proj_w with fade
    call screen results_screen

    return

label game_end:
    scene black with Dissolve(1.0)
    show text _("Спасибо за игру!") at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    return