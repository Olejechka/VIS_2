screen ct_ui():
    tag mini_game

    if h_reason == "Магнит":
        add "ct_m.png":
            pos (0.65, 0.2)
    elif h_reason == "Перемычка":
        add "ct_p.png":
            pos (0.65, 0.2)
    else:
        add "ct.png":
            pos (0.65, 0.2)

    text " ".join(str(h_counter)) size 28 xalign 0.74 yalign 0.355 color "#ffffff"

    fixed:
        xsize 1000
        ysize 600
        xalign 0.05
        yalign 0.38

        frame:
            background "otch.png"
            padding (5, 5)

        vbox:
            spacing 10
            yalign 0.1
            xalign 0.5
            text "Показания счетчиков по электроэнергии должны записываться" size 22  xalign 0.5 color "#000"
            text "пятизначными цифровыми до запятой например 00001 или 124442." size 22 xalign 0.5 color "#000"
            text "Записи ведуться по каждому счетчику в отдельности." size 22 xalign 0.5 color "#000"

        # Дом № - выпадающий список
        vbox:
            spacing 25
            yalign 0.3
            xalign 0.5
            hbox:
                spacing 15

                text "Дом №" size 20 color "#000"

                textbutton "[us_number] ▼":
                    action house_dropdown
                    xsize 100
                    background Solid("#ffffff")
                    text_size 18
                    text_color "#000"
                    padding (10, 5)
                    align (0.5, 0.5)

        # Собственник Ф.И.О. - выпадающий список
        vbox:
            spacing 25
            yalign 0.4
            xalign 0.12

            hbox:
                spacing 15

                text "Собсвтенник Ф.И.О.:" size 20 color "#000"

                textbutton "[us_name] ▼":
                    action name_dropdown
                    xsize 256
                    background Solid("#ffffff")
                    text_size 16
                    text_color "#000"
                    padding (10, 5)
                    align (0.5, 0.5)

        # Показание счетчика - ручной ввод
        vbox:
            spacing 25
            yalign 0.5
            xalign 0.1

            hbox:
                spacing 15

                text "Показание счетчика" size 20 color "#000"

                frame:
                   xsize 80
                   ysize 40
                   background Solid("#ffffff")
                   padding (10, 10)
                   input:
                        id "counter_input"
                        length 5
                        value VariableInputValue("us_counter")
                        allow "0123456789"
                        size 14
                        align (0.5, 0.5)
                        text_align 0.5
                        color "#000"

        # Требования - выпадающий список (Да/Нет)
        vbox:
            spacing 25
            yalign 0.6
            xalign 0.09
            hbox:
                spacing 15

                text "Требования соблюдены?" size 20 color "#000"

                textbutton "[us_fault] ▼":
                    action fault_dropdown
                    xsize 80
                    background Solid("#ffffff")
                    text_size 16
                    text_color "#000"
                    padding (10, 5)
                    align (0.5, 0.5)

        # Почему? - выпадающий список
        vbox:
            spacing 25
            yalign 0.7
            xalign 0.13
            hbox:
                spacing 15

                text "Почему?" size 20 color "#000"

                textbutton "[us_reason] ▼":
                    action reason_dropdown
                    xsize 400
                    background Solid("#ffffff")
                    text_size 16
                    text_color "#000"
                    padding (10, 5)
                    align (0.5, 0.5)

        hbox:
            spacing 200
            xalign 0.5
            yalign 0.8
            text "месяц: июль." size 22 color "#000"
            text "проверяющие: Ганнадий Ч.А  [surname] [name[:1].upper()].[otch[:1].upper() + '.' if otch else '']" size 22 color "#000"

        hbox:
            spacing 20
            xalign 0.5
            yalign 0.9

            textbutton "Подтвердить":
                action Return(True)
                xsize 200
                background Solid("#6CB0D8")
                text_size 25
                text_color "#fff"
                padding (15, 10)

        textbutton "Назад" action Return(False) xalign 0.95 yalign 0.95



label ct_lb:
    # Дефолтными значениями
    $ us_number = 1
    $ us_name = "Иванов И.И."
    $ us_counter = "00000"
    $ us_fault = "Нет"
    $ us_reason = "Нарушений не обнаружено"

    python:
        # 1. Список номеров домов (1-9)
        house_dropdown = DropDown(
            _("1"), SetVariable("us_number", "1"),
            _("2"), SetVariable("us_number", "2"),
            _("3"), SetVariable("us_number", "3"),
            _("4"), SetVariable("us_number", "4"),
            _("5"), SetVariable("us_number", "5"),
            _("6"), SetVariable("us_number", "6"),
            _("7"), SetVariable("us_number", "7"),
            _("8"), SetVariable("us_number", "8"),
            _("9"), SetVariable("us_number", "9"),
            modal=True
        )

        # 2. Список ФИО собственников (можно добавить сколько нужно)
        name_dropdown = DropDown(
            _("ФАМИЛИЯ А.И."), SetVariable("us_name", "ФАМИЛИЯ А.И."),
            _("Арсеньев В.А."), SetVariable("us_name", "Арсеньев В.А."),
            _("КАРЕНИНА А.А."), SetVariable("us_name", "КАРЕНИНА А.А."),
            _("Алексеев Р.Е."), SetVariable("us_name", "Алексеев Р.Е."),
            _("Мазайхин И.С."), SetVariable("us_name", "Мазайхин И.С."),
            _("Книжная О.Э."), SetVariable("us_name", "Книжная О.Э."),
            _("Грозный И.В."), SetVariable("us_name", "Грозный И.В."),
            _("Романов Е.Г."), SetVariable("us_name", "Романов Е.Г."),
            modal=True
        )

        # 3. Список требований (Да/Нет)
        fault_dropdown = DropDown(
            _("Да"), SetVariable("us_fault", "Да"),
            _("Нет"), SetVariable("us_fault", "Нет"),
            modal=True
        )

        # 4. Список причин
        reason_dropdown = DropDown(
            _("Нарушений не обнаружено"), SetVariable("us_reason", "Нарушений не обнаружено"),
            _("Наброс"), SetVariable("us_reason", "Наброс"),
            _("Перемычка"), SetVariable("us_reason", "Перемычка"),
            _("Магнит"), SetVariable("us_reason", "Магнит"),
            modal=True
        )

    show black_i with fade
    call screen ct_ui()
    hide black_i with fade

    if _return:
        python:
            if us_number == h_number:
                ct_schet += 1
            if us_name == h_name:
                ct_schet += 1
            if us_counter == h_counter:
                ct_schet += 1
            if us_fault == h_fault:
                ct_schet += 1
            if us_reason == h_reason:
                ct_schet += 1

            ct += 1
            renpy.notify("Верно")
            if curr_lock == "h1":
                c_h1 = True
            elif curr_lock == "h3":
                c_h3 = True
            elif curr_lock == "h5":
                c_h5 = True
            elif curr_lock == "h6":
                c_h6 = True
            elif curr_lock == "h8":
                c_h8 = True
            elif curr_lock == "h9":
                c_h9 = True



    return