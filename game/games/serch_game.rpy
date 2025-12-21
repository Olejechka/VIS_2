screen search:
    tag menu
    modal True

    # Выбор фона в зависимости от curr_lock
    if curr_lock == "h1":
        add "der4" at right
        use h1_s

    elif curr_lock == "h2":
        add "der"
        use h2_s

    elif curr_lock == "h3":
        add "der5" at center
        use h3_s

    elif curr_lock == "h4":
        add "der6" at right
        use h4_s

    else:
        # Фон по умолчанию
        add "default_background"
        text "Некорректное значение curr_lock" align (0.5, 0.5)

    # Общая кнопка "Назад" для всех экранов
    textbutton "Назад" action Return() xalign 0.95 yalign 0.95



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
                Show("pop", message="изношенные оходные сапоги."),
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

        # Кнопки для кухни
        imagebutton:
            idle Null()
            hover Null()
            xoffset 150
            yoffset 150
            xsize 180
            ysize 180
            action [
                Show("pop", message="--"),
                Play("sound", "audio/select_click.mp3")
            ]

        imagebutton:
            idle Null()
            hover Null()
            xoffset 400
            yoffset 300
            xsize 120
            ysize 120
            action [
                Show("pop", message="--."),
                Play("sound", "audio/select_click.mp3")
            ]

        # Подсветка областей
        add "#ff000040" at Transform(xoffset=150, yoffset=150, xsize=180, ysize=180)
        add "#00ff0040" at Transform(xoffset=400, yoffset=300, xsize=120, ysize=120)



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
                Show("pop", message="Калитка открыта."),
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

    # Горячие клавиши
    key "K_RETURN" action Hide("pop_simple")
    key "K_SPACE" action Hide("pop_simple")