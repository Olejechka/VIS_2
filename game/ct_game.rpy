screen ct_ui():
    tag mini_game

    fixed:
        xsize 1400
        ysize 800
        xalign 0.5
        yalign 0.5

        frame:
            background "otch.png"
            padding (5, 5)

        vbox:
            spacing 25
            yalign 0.1
            xalign 0.5
            text "Показания счетчиков по электроэнергии должны записываться" size 22  xalign 0.5 color "#000"
            text "пятизначными цифровыми до запятой например 00001 или 124442." size 22 xalign 0.5 color "#000"
            text "Записи ведуться по каждому счетчику в отдельности." size 22 xalign 0.5 color "#000"

        vbox:
            spacing 25
            yalign 0.3
            xalign 0.5
            hbox:
                spacing 15

                text "Дом №" size 20 color "#000"

                frame:
                    xsize 40
                    ysize 40
                    background Solid("#ffffff")
                    padding (10, 10)
                    input:
                        id "number_input"
                        length 2
                        default us_number
                        allow "0123456789"
                        size 14
                        align (0.5, 0.5)
                        text_align 0.5
                        color "#000"
        vbox:
            spacing 25
            yalign 0.4
            xalign 0.12

            hbox:
                spacing 15

                text "Собсвтенник Ф.И.О.:" size 20 color "#000"

                frame:
                   xsize 256
                   ysize 40
                   background Solid("#ffffff")
                   padding (10, 10)
                   input:
                        id "name_input"
                        length 256
                        default us_name
                        size 14
                        align (0.1, 0.1)
                        text_align 0.5
                        color "#000"

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
                        id "name_input"
                        length 5
                        default us_name
                        size 14
                        align (0.5, 0.5)
                        text_align 0.5
                        color "#000"

        vbox:
            spacing 25
            yalign 0.6
            xalign 0.09
            hbox:
                spacing 15

                text "Требования" size 20 color "#000"

                frame:
                   xsize 40
                   ysize 40
                   background Solid("#ffffff")
                   padding (10, 10)
                   input:
                        id "fault_input"
                        length 1
                        default us_fault
                        allow "0123456789"
                        size 14
                        align (0.5, 0.5)
                        text_align 0.5
                        color "#000"

        vbox:
            spacing 25
            yalign 0.7
            xalign 0.13
            hbox:
                spacing 15

                text "Почему?" size 20 color "#000"

                frame:
                   xsize 400
                   ysize 40
                   background Solid("#ffffff")
                   padding (10, 10)
                   input:
                        id "fault_input"
                        length 512
                        default us_fault
                        allow "0123456789"
                        size 14
                        align (0.1, 0.1)
                        text_align 0.5
                        color "#000"

        hbox:
            spacing 200
            xalign 0.5
            yalign 0.8
            text "месяц: июль." size 22 color "#000"
            text "проверяющие: Ганнадий Ч.А  [surname] Е.Б." size 22 color "#000"

        hbox:
            spacing 20
            xalign 0.5
            yalign 0.9

            textbutton "Подтвердить":
                action [
                    Return({"next": True})
                ]
                xsize 200
                background Solid("#6CB0D8")
                text_size 25
                text_color "#fff"
                padding (15, 10)


label ct_lb:
    define us_number = 1
    define us_name = "Grigory"
    define us_fault = 0



    define h_number = 1
    define name = "Grigory"
    define fault = 0

    call screen ct_ui()

    #if h_number == us_number and name == us_name and fault == us_fault:
    #    $ schet += 1

    return