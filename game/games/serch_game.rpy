screen search:
    tag menu
    modal True

    # Выбор фона в зависимости от curr_lock
    if curr_lock == "h1":
        add "office"  # Фоновое изображение офиса
        use search_office

    elif curr_lock == "h2":
        add "kitchen"  # Фоновое изображение кухни
        use search_kitchen

    elif curr_lock == "h3":
        add "bedroom"  # Фоновое изображение спальни
        use search_bedroom

    else:
        # Фон по умолчанию
        add "default_background"
        text "Некорректное значение curr_lock" align (0.5, 0.5)

    # Общая кнопка "Назад" для всех экранов
    textbutton "Назад" action Return() xalign 0.95 yalign 0.95



# Мини-игра для офиса
screen search_office():
    imagemap:
        ground Null()  # Фон уже добавлен в основном экране

        # Кнопки для офиса
        imagebutton:
            idle Null()
            hover Null()
            xoffset 300
            yoffset 200
            xsize 220
            ysize 220
            action [
                Show("pop", message="Excel таблица."),
                Play("sound", "audio/select_click.mp3"),
                # Дополнительные действия для этой кнопки
                SetVariable("found_office_item1", True)
            ]

        imagebutton:
            idle Null()
            hover Null()
            xoffset 100
            yoffset 400
            xsize 160
            ysize 160
            action [
                Show("pop", message="Фирма Apple."),
                Play("sound", "audio/select_click.mp3"),
                SetVariable("found_office_item2", True)
            ]

        # Добавить больше кнопок для офиса...

        # Подсветка областей (для отладки)
        add "#ff00ff40" at Transform(xoffset=300, yoffset=200, xsize=220, ysize=220)
        add "#00ffff40" at Transform(xoffset=100, yoffset=400, xsize=160, ysize=160)



# Мини-игра для кухни
screen search_kitchen():
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
                Show("pop", message="Найдена сковородка."),
                Play("sound", "audio/select_click.mp3"),
                SetVariable("found_kitchen_item1", True)
            ]

        imagebutton:
            idle Null()
            hover Null()
            xoffset 400
            yoffset 300
            xsize 120
            ysize 120
            action [
                Show("pop", message="Кофеварка."),
                Play("sound", "audio/select_click.mp3"),
                SetVariable("found_kitchen_item2", True)
            ]

        # Подсветка областей
        add "#ff000040" at Transform(xoffset=150, yoffset=150, xsize=180, ysize=180)
        add "#00ff0040" at Transform(xoffset=400, yoffset=300, xsize=120, ysize=120)



# Мини-игра для спальни
screen search_bedroom():
    imagemap:
        ground Null()

        # Кнопки для спальни
        imagebutton:
            idle Null()
            hover Null()
            xoffset 200
            yoffset 250
            xsize 200
            ysize 150
            action [
                Show("pop", message="Ключ под подушкой."),
                Play("sound", "audio/select_click.mp3"),
                SetVariable("found_bedroom_key", True)
            ]

        imagebutton:
            idle Null()
            hover Null()
            xoffset 50
            yoffset 100
            xsize 100
            ysize 100
            action [
                Show("pop", message="Старый дневник."),
                Play("sound", "audio/select_click.mp3"),
                SetVariable("found_bedroom_diary", True)
            ]

        # Подсветка областей
        add "#ffff0040" at Transform(xoffset=200, yoffset=250, xsize=200, ysize=150)
        add "#ff00ff40" at Transform(xoffset=50, yoffset=100, xsize=100, ysize=100)



# Всплывающее окно (общее для всех)
screen pop(message):
    zorder 100
    frame:
        xalign 0.5
        yalign 0.1
        xpadding 30
        ypadding 20
        background "#000000CC"

        text "Заполнено: [message]" size 24 color "#FFFFFF"

    # Автоматическое скрытие через 2 секунды
    timer 2.0 action Hide("pop")