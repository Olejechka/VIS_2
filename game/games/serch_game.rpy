screen search:
    tag menu
    modal True

    # Выбор фона в зависимости от curr_lock
    if curr_lock == "h1":
        add "der4" at right
        use h1_s

    elif curr_lock == "h2":
        add "bober"
        use h2_s

    elif curr_lock == "h3":
        add "der5" at center
        use h3_s

    elif curr_lock == "h4":
        add "der6" at right
        use h4_s

    elif curr_lock == "h5":
        add "d_k" at center
        use h5_s

    elif curr_lock == "h6":
        add "dead_dom" at left
        use h6_s

    elif curr_lock == "h7":
        add "kd" at center
        use h7_s

    elif curr_lock == "h8":
        add "d_b" at center
        use h8_s

    elif curr_lock == "h9":
        add "d_h" at center
        use h9_s

    else:
        # Фон по умолчанию
        add "default_background"
        text "Некорректное значение curr_lock" align (0.5, 0.5)

    # Общая кнопка "Назад" для всех экранов
    textbutton "Назад" action Return() xalign 0.95 yalign 0.95 text_color "#FFFFFF" text_hover_color "#67B4D2"

screen h1_s():
    imagemap:
        ground Null()

        imagebutton:
            idle Null()
            hover Null()
            xoffset 570
            yoffset 710
            xsize 180
            ysize 190
            action [
                Show("pop", message="изношенные походные сапоги."),
                Play("sound", "audio/select_click.mp3")
            ]

        imagebutton:
            idle Null()
            hover Null()
            xoffset 1150
            yoffset 900
            xsize 200
            ysize 200
            action [
                Show("pop", message="Раскладной стул. Удобно ходить с таким на рыбалку."),
                Play("sound", "audio/select_click.mp3")
            ]

        imagebutton:
            idle Null()
            hover Null()
            xoffset 1350
            yoffset 835
            xsize 535
            ysize 250
            action [
                Show("pop", message="Большой самодельный стол."),
                Play("sound", "audio/select_click.mp3")
            ]

        # Подсветка областей (для отладки)
        #add "#ff00ff40" at Transform(xoffset=570, yoffset=710, xsize=180, ysize=190)
        #add "#00ffff40" at Transform(xoffset=1150, yoffset=900, xsize=200, ysize=200)
        #add "#00ffff40" at Transform(xoffset=1350, yoffset=835, xsize=535, ysize=250)


screen h2_s():
    imagemap:
        ground Null()

        imagebutton:
            idle Null()
            hover Null()
            xoffset 0
            yoffset 0
            xsize 1920
            ysize 1080
            action [
                Show("pop", message="'Закрыто'"),
                Play("sound", "audio/select_click.mp3")
            ]

        # Подсветка областей
        #add "#ff000040" at Transform(xoffset=0, yoffset=0, xsize=1920, ysize=1080)




screen h3_s():
    imagemap:
        ground Null()

        imagebutton:
            idle Null()
            hover Null()
            xoffset 1260
            yoffset 810
            xsize 420
            ysize 150
            action [
                Show("pop", message="Клумба с необычными цветами."),
                Play("sound", "audio/select_click.mp3")
            ]

        imagebutton:
            idle Null()
            hover Null()
            xoffset 75
            yoffset 570
            xsize 210
            ysize 230
            action [
                Show("pop", message="С таким инструментом всегда нужно быть осторожнее."),
                Play("sound", "audio/select_click.mp3")
            ]

        imagebutton:
            idle Null()
            hover Null()
            xoffset 0
            yoffset 460
            xsize 265
            ysize 100
            action [
                Show("pop", message="Ухоженные грядки."),
                Play("sound", "audio/select_click.mp3")
            ]

        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=0, yoffset=460, xsize=265, ysize=100)
        #add "#ffff0040" at Transform(xoffset=1260, yoffset=810, xsize=420, ysize=150)
        #add "#ff00ff40" at Transform(xoffset=75, yoffset=570, xsize=210, ysize=230)

screen h4_s():
    imagemap:
        ground Null()

        imagebutton:
            idle Null()
            hover Null()
            xoffset 0
            yoffset 620
            xsize 20
            ysize 90
            action [
                Show("pop", message="'Осторожно Злая собака'"),
                Play("sound", "audio/select_click.mp3"),
                SetVariable("found_bedroom_key", True)
            ]

        imagebutton:
            idle Null()
            hover Null()
            xoffset 200
            yoffset 540
            xsize 455
            ysize 540
            action [
                Show("pop", message="Калитку можно открыть."),
                Play("sound", "audio/select_click.mp3"),
                SetVariable("found_bedroom_diary", True)
            ]

        imagebutton:
            idle Null()
            hover Null()
            xoffset 0
            yoffset 0
            xsize 1920
            ysize 540
            action [
                Show("pop", message="Хозяев участка не видно."),
                Play("sound", "audio/select_click.mp3"),
                SetVariable("found_bedroom_diary", True)
            ]

        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=0, yoffset=620, xsize=20, ysize=90)
        #add "#ff00ff40" at Transform(xoffset=200, yoffset=540, xsize=455, ysize=540)
        #add "#ff00ff40" at Transform(xoffset=0, yoffset=0, xsize=1920, ysize=540)

screen h5_s():
    imagemap:
        ground Null()

        imagebutton:
            idle Null()
            hover Null()
            xoffset 1180
            yoffset 730
            xsize 740
            ysize 300
            action [
                Show("pop", message="Куст с ягодами."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=1180, yoffset=730, xsize=740, ysize=300)

        imagebutton:
            idle Null()
            hover Null()
            xoffset 910
            yoffset 730
            xsize 270
            ysize 210
            action [
                Show("pop", message="Клумба с цветами."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=910, yoffset=730, xsize=270, ysize=210)

        imagebutton:
            idle Null()
            hover Null()
            xoffset 330
            yoffset 720
            xsize 260
            ysize 120
            action [
                Show("pop", message="Клумба с цветами."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ff00ff40" at Transform(xoffset=330, yoffset=720, xsize=260, ysize=120)

        imagebutton:
            idle Null()
            hover Null()
            xoffset 0
            yoffset 460
            xsize 265
            ysize 100
            action [
                Show("pop", message="Ухоженные грядки."),
                Play("sound", "audio/select_click.mp3")
            ]

screen h6_s():
    imagemap:
        ground Null()

        imagebutton:
            idle Null()
            hover Null()
            xoffset 0
            yoffset 0
            xsize 265
            ysize 100
            action [
                Show("pop", message="Наброс провода."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=0, yoffset=0, xsize=265, ysize=100)

        imagebutton:
            idle Null()
            hover Null()
            xoffset 0
            yoffset 500
            xsize 220
            ysize 520
            action [
                Show("pop", message="Уютная баня."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=0, yoffset=200, xsize=220, ysize=520)

        imagebutton:
            idle Null()
            hover Null()
            xoffset 220
            yoffset 400
            xsize 260
            ysize 160
            action [
                Show("pop", message="Шкурки животных."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ff00ff40" at Transform(xoffset=220, yoffset=400, xsize=260, ysize=160)

screen h7_s():
    imagemap:
        ground Null()

        imagebutton:
            idle Null()
            hover Null()
            xoffset 450
            yoffset 725
            xsize 150
            ysize 150
            action [
                Show("pop", message="Чебурашка."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=450, yoffset=725, xsize=125, ysize=125)

        imagebutton:
            idle Null()
            hover Null()
            xoffset 880
            yoffset 850
            xsize 125
            ysize 125
            action [
                Show("pop", message="Машинка."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=880, yoffset=850, xsize=125, ysize=125)

        imagebutton:
            idle Null()
            hover Null()
            xoffset 1180
            yoffset 730
            xsize 740
            ysize 300
            action [
                Show("pop", message="Вкусные ягоды."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=1180, yoffset=730, xsize=740, ysize=300)

        imagebutton:
            idle Null()
            hover Null()
            xoffset 0
            yoffset 460
            xsize 265
            ysize 100
            action [
                Show("pop", message="Грядки."),
                Play("sound", "audio/select_click.mp3")
            ]

screen h8_s():
    imagemap:
        ground Null()

        imagebutton:
            idle Null()
            hover Null()
            xoffset 0
            yoffset 800
            xsize 1250
            ysize 300
            action [
                Show("pop", message="Бетонная заливка."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=0, yoffset=800, xsize=1250, ysize=300)

        imagebutton:
            idle Null()
            hover Null()
            xoffset 1250
            yoffset 850
            xsize 425
            ysize 100
            action [
                Show("pop", message="Иссохшие растения."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=1250, yoffset=850, xsize=425, ysize=100)

        imagebutton:
            idle Null()
            hover Null()
            xoffset 900
            yoffset 10
            xsize 100
            ysize 50
            action [
                Show("pop", message="Камера слежения."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=900, yoffset=10, xsize=100, ysize=50)

screen h9_s():
    imagemap:
        ground Null()

        imagebutton:
            idle Null()
            hover Null()
            xoffset 0
            yoffset 400
            xsize 400
            ysize 220
            action [
                Show("pop", message="Традиционное одеяние для приведий..."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=0, yoffset=400, xsize=400, ysize=220)

        imagebutton:
            idle Null()
            hover Null()
            xoffset 900
            yoffset 650
            xsize 255
            ysize 270
            action [
                Show("pop", message="Удобная скамейка."),
                Play("sound", "audio/select_click.mp3")
            ]
        # Подсветка областей
        #add "#ffff0040" at Transform(xoffset=900, yoffset=650, xsize=255, ysize=270)

# Всплывающее
screen pop(message):
    zorder 100
    modal True

    # Затемнение фона
    add "#00000060"

    frame:
        xalign 0.5
        yalign 0.9
        xsize 700
        ysize 300
        background Frame("gui/frame.png", 12, 12)

        vbox:
            xalign 0.5
            yalign 0.5

            text message:
                size 28
                color "#000000"
                text_align 0.5
                xalign 0.5
                yalign 0.4

        textbutton " OK ":
            keysym "input_enter"
            text_size 25
            xalign 0.5
            yalign 0.9
            action Hide("pop")


