screen results_screen():
    modal True

    frame:
        xalign 0.5
        yalign 0.0
        xpadding 50
        ypadding 50
        background Solid("#ffffffaa")

        vbox:
            spacing 10
            xalign 0.5

            label _("Сотрудник [surname] [name] [otch]") xalign 0.5

            # Должность
            $ position = ""
            if schet < 45:
                $ position = "Стажер"
            elif schet <= 80:
                $ position = "Сотрудник"
            else:
                $ position = "Детектив"

            label _("Должность: [position]") xalign 0.5

            label _("Результаты дня") xalign 0.5

            vbox:
                spacing 10
                xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 40
                    text "Первая часть:"
                    text "Очки: [kr_schet]"

                hbox:
                    xalign 0.5
                    spacing 40
                    text "Вторая часть:"
                    text "Очки: [ct_schet]"

                hbox:
                    xalign 0.5
                    spacing 40
                    text "Третья часть:"
                    text "Очки: [sh_schet]"

                add Solid("#000000") size (400, 2) xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 40
                    text "Всего:"
                    text "[schet]"

            textbutton _("Завершить"):
                xalign 0.5
                action [Hide("results_screen"), Jump("game_end")]