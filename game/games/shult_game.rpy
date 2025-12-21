init python:
    import random

    class SchulteGame:
        def __init__(self, grid_size=5, rounds=3):
            self.grid_size = grid_size
            self.rounds = rounds
            self.current_round = 1
            self.round_scores = []
            self.current_score = 0
            self.create_grid()

        def create_grid(self):
            total_cells = self.grid_size * self.grid_size
            numbers = list(range(1, total_cells + 1))
            random.shuffle(numbers)

            self.grid = []
            for i in range(self.grid_size):
                row = numbers[i*self.grid_size:(i+1)*self.grid_size]
                self.grid.append(row)

            self.expected_number = 1
            self.current_score = 0

        def click_cell(self, value):
            if value == self.expected_number:
                self.current_score += 1
                self.expected_number += 1

                if self.expected_number > self.grid_size * self.grid_size:
                    self.round_scores.append(self.current_score)

                    if self.current_round < self.rounds:
                        self.current_round += 1
                        self.create_grid()
                        return "next_round"
                    else:
                        return "game_over"

                return "correct"
            else:
                self.round_scores.append(self.current_score)

                if self.current_round < self.rounds:
                    self.current_round += 1
                    self.create_grid()
                    return "wrong_next"
                else:
                    return "game_over"

screen schulte_game_ui(schulte_game, show_rules=False):
    tag mini_game

    fixed:
        xsize 800
        ysize 700
        xalign 0.55
        yalign 0.65

        frame:
            background Solid("#6CB0D8")
            padding (5, 5)
            frame:
                background Solid("#f0f0f0")
                padding (30, 30)

        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5

            if show_rules:
                text "Тест Шульте" size 32 xalign 0.5 color "#000"

                vbox:
                    spacing 15
                    xalign 0.5
                    xsize 600

                    text "• Вам будет дана таблица 5x5 с числами от 1 до 25" size 22 color "#000"
                    text "• Вам необходимо последовательно находить числа от 1 до 25" size 22 color "#000"
                    text "• Кликайте по числам в порядке возрастания: 1, 2, 3, ... 25" size 22 color "#000"
                    text "• Каждое правильно найденное число даёт 1 очко" size 22 color "#000"
                    text "• При ошибке раунд немедленно заканчивается" size 22 color "#000"
                    text "• Всего  3 раунда" size 22 color "#000"
                    text "• Будьте внимательны!" size 22 color "#000"

                textbutton "Начать тест":
                    action [
                        Return({"start": True})
                    ]
                    keysym "input_enter"
                    xalign 0.5
                    xsize 300
                    background Solid("#6CB0D8")
                    text_size 28
                    text_color "#fff"
                    padding (15, 10)

            else:
                vbox:
                    spacing 20
                    xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing 25

                        vbox:
                            spacing 5
                            text "ТЕСТ ШУЛЬТЕ" size 28 color "#000" xalign 0.5
                            text "Раунд: [schulte_game.current_round] из [schulte_game.rounds]" size 22 color "#555" xalign 0.5

                        vbox:
                            spacing 5
                            text "Очки в раунде:" size 24 color "#000" xalign 0.5
                            frame:
                                background Solid("#ffffff")
                                padding (20, 10)
                                xalign 0.5
                                text str(schulte_game.current_score) + " из 25" size 36 color "#6CB0D8" xalign 0.5

                    text "Найдите: [schulte_game.expected_number]" size 26 color "#000" xalign 0.5

                    frame:
                        background Solid("#ffffff")
                        padding (20, 20)
                        xalign 0.5

                        grid 5 5:
                            xalign 0.5
                            yalign 0.5
                            spacing 5

                            for i in range(5):
                                for j in range(5):
                                    $ cell_value = schulte_game.grid[i][j]
                                    $ is_found = cell_value < schulte_game.expected_number

                                    button:
                                        if is_found:
                                            background Solid("#6CB0D8")
                                            hover_background Solid("#4A8CB0")
                                        else:
                                            background Solid("#f0f0f0")
                                            hover_background Solid("#d0d0d0")

                                        xsize 80
                                        ysize 80
                                        action [
                                            Return({"click": cell_value})
                                        ]

                                        if is_found:
                                            text str(cell_value):
                                                size 28
                                                color "#ffffff"
                                                align (0.5, 0.5)
                                        else:
                                            text str(cell_value):
                                                size 28
                                                color "#000000"
                                                align (0.5, 0.5)

label schulte_game_screen:
    $ rounds = 3
    $ schulte_game = SchulteGame(rounds=rounds)

    call screen schulte_game_ui(schulte_game, show_rules=True)

    if not _return.get("start", False):
        return

    while True:
        call screen schulte_game_ui(schulte_game, show_rules=False)

        $ result = _return.get("click", None)

        if result is not None:
            $ click_result = schulte_game.click_cell(result)

            if click_result == "correct":
                pass
            elif click_result == "next_round":
                if schulte_game.current_round <= rounds:
                    centered "Раунд [schulte_game.current_round - 1] завершён! Вы нашли все 25 чисел!"
                    centered "Следующий раунд начинается..."
            elif click_result == "wrong_next":
                centered "Ошибка! Раунд [schulte_game.current_round - 1] завершён."
                centered "Следующий раунд начинается..."
            elif click_result == "game_over":
                jump schulte_game_complete

    label schulte_game_complete:

    $ total_score = sum(schulte_game.round_scores)
    $ max_possible = rounds * 25
    $ average_score = round(total_score / rounds, 1) if rounds > 0 else 0
    $ best_round = max(schulte_game.round_scores) if schulte_game.round_scores else 0

    if total_score == 75:
        $ grade = "ИДЕАЛЬНЫЙ РЕЗУЛЬТАТ! Вы нашли ВСЕ 75 чисел без единой ошибки!"
        $ grade_color = "#2E7D32"
    elif total_score >= 60:
        $ grade = "ОТЛИЧНО! Хорошая концентрация внимания."
        $ grade_color = "#6CB0D8"
    elif total_score >= 45:
        $ grade = "ХОРОШО. Внимание на хорошем уровне."
        $ grade_color = "#8BC34A"
    elif total_score >= 30:
        $ grade = "СРЕДНИЙ РЕЗУЛЬТАТ. Рекомендуется тренировать внимание."
        $ grade_color = "#FF9800"
    else:
        $ grade = "НИЗКИЙ РЕЗУЛЬТАТ. Стоит уделить больше времени тренировке внимания."
        $ grade_color = "#C62828"

    centered "Тест Шульте завершён!"

    show screen schulte_results_screen(schulte_game.round_scores, total_score, average_score, max_possible, best_round, grade, grade_color)
    pause

    hide screen schulte_results_screen

    return

screen schulte_results_screen(round_scores, total_score, average_score, max_possible, best_round, grade, grade_color):
    modal True
    zorder 200

    fixed:
        xsize 700
        ysize 300
        xalign 0.58
        yalign 0.32

        frame:
            background Solid("#6CB0D8")
            padding (5, 5)
            frame:
                background Solid("#f0f0f0")
                padding (30, 30)

                vbox:
                    spacing 10
                    xalign 0.5

                    text "РЕЗУЛЬТАТЫ ТЕСТА ШУЛЬТЕ" size 25 xalign 0.5 color "#000"

                    frame:
                        background Solid("#ffffff")
                        padding (20, 20)
                        xalign 0.5
                        xsize 500

                        vbox:
                            spacing 10
                            xalign 0.5

                            text "Результаты по раундам:" size 26 color "#000" xalign 0.5

                            for i, score in enumerate(round_scores):
                                hbox:
                                    xalign 0.5
                                    spacing 30
                                    text "Раунд [i+1]:" size 22 color "#555" xalign 0.5
                                    text "[score] из 25" size 24 color "#6CB0D8" xalign 0.5

                    # Итоговая статистика
                    frame:
                        background Solid("#ffffff")
                        padding (20, 20)
                        xalign 0.5
                        xsize 500

                        vbox:
                            spacing 15
                            xalign 0.5

                            text "Итоговый результат:" size 26 color "#000" xalign 0.5

                            hbox:
                                xalign 0.5
                                spacing 40

                                vbox:
                                    spacing 5
                                    text "Всего очков:" size 22 color "#000" xalign 0.5
                                    text "[total_score] из [max_possible]" size 36 color "#6CB0D8" xalign 0.5

                                vbox:
                                    spacing 5
                                    text "Лучший раунд:" size 22 color "#000" xalign 0.5
                                    text "[best_round] из 25" size 36 color "#2E7D32" xalign 0.5

                            hbox:
                                xalign 0.5
                                spacing 40

                                vbox:
                                    spacing 5
                                    text "Средний раунд:" size 22 color "#000" xalign 0.5
                                    text "[average_score] из 25" size 28 color "#555" xalign 0.5

                                vbox:
                                    spacing 5
                                    text "Раундов:" size 22 color "#000" xalign 0.5
                                    text "[len(round_scores)] из 3" size 28 color "#555" xalign 0.5

                            text "[grade]" size 20 color grade_color xalign 0.5 text_align 0.5

                    # Кнопка завершения
                    textbutton "Завершить тест":
                        action Return()
                        xalign 0.5
                        xsize 250
                        background Solid("#6CB0D8")
                        text_size 24
                        text_color "#fff"
                        padding (15, 10)
                        hover_background Solid("#4A8CB0")