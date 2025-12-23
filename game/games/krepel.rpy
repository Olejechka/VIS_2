init python:
    import random

    def start_new_mini_game_round():
        num1 = random.randint(1000, 7500)
        num2 = random.randint(100, 600)
        return num1, num2, num1 + num2

screen mini_game_ui(num1, num2, ver, r_numb, rounds, show_rules=False):
    tag mini_game
    default time_vsy = False

    fixed:
        xsize 700
        ysize 450
        xalign 0.54
        yalign 0.5

        frame:
            background Solid("#6CB0D8")
            padding (5, 5)
            frame:
                background Solid("#f0f0f0")
                padding (30, 30)

        if not show_rules:
            timer 10.0 action SetScreenVariable("time_vsy", True)

        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5

            if show_rules:
                # ПРАВИЛА
                text "Для: [surname] [name[:1].upper()].[otch[:1].upper() + '.' if otch else ''] От: Нач." size 32 xalign 0.1 color "#000"

                vbox:
                    spacing 15
                    xalign 0.5
                    xsize 550

                    text "Доброе утро, [name]." size 22 color "#000"
                    text "Разослал вам и вашим коллегам последние показания." size 22 color "#000"
                    text "Вам достался 4-ый участок." size 22 color "#000"
                    text "Рассчитайте, пожалуйста, показания до конца рабочего дня." size 22 color "#000"
                textbutton "Файл":
                    action [
                        Return({"start": True})
                    ]
                    keysym "input_enter"
                    xalign 0.9
                    xsize 100
                    background Solid("#6CB0D8")
                    text_size 28
                    text_color "#fff"
                    padding (15, 10)

            else:
                # КРЕПЕЛИН
                text "Рассчитайте показания" size 32 xalign 0.5 color "#000"

                hbox:
                    spacing 15
                    xalign 0.5
                    yalign 0.5

                    frame:
                        xsize 150
                        ysize 80
                        background Solid("#ffffff")
                        padding (10, 10)
                        text "[num1]" align (0.5, 0.5) size 36 color "#000"

                    text "+" size 36 yalign 0.5 color "#000"

                    frame:
                        xsize 150
                        ysize 80
                        background Solid("#ffffff")
                        padding (10, 10)
                        text "[num2]" align (0.5, 0.5) size 36 color "#000"

                    text "=" size 36 yalign 0.5 color "#000"

                    frame:
                        xsize 150
                        ysize 80
                        background Solid("#ffffff")
                        padding (10, 10)
                        input:
                            id "answer_input"
                            length 4
                            value VariableInputValue("us_ans")
                            allow "0123456789"
                            size 36
                            align (0.5, 0.5)
                            text_align 0.5
                            color "#000"

                text "Страница: [r_numb] из [rounds]" size 24 xalign 0.5 color "#555"

                hbox:
                    spacing 20
                    xalign 0.5

                    textbutton "Далее":
                        action [
                            SetVariable("vrem_vsy", time_vsy),
                            SetVariable("us_ans", us_ans),
                            Return({"next": True})
                        ]
                        keysym "input_enter"
                        xsize 200
                        sensitive us_ans
                        background Solid("#6CB0D8")
                        text_size 28
                        text_color "#fff"
                        padding (15, 10)

label mini_game_screen:
    $ kr_schet = 0
    $ rounds = 9
    $ r_numb = 0

    call screen mini_game_ui(0, 0, 0, 0, rounds, show_rules=True)

    if not _return.get("start", False):
        return

    while r_numb < rounds:
        $ num1, num2, ver = start_new_mini_game_round()
        $ us_ans = ""
        $ vrem_vsy = False

        call screen mini_game_ui(num1, num2, ver, r_numb + 1, rounds, show_rules=False)

        if str(us_ans) == str(ver):
            if not store.vrem_vsy:  # Уложился вовремя (≤10 сек)
                $ kr_schet += 5
            else:  # Правильно, но превысил время (>10 сек)
                $ kr_schet += 1
        $ r_numb += 1

    "Кажется в файле больше ничего не было."
    return