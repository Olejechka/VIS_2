init python:
    import random

    class SchulteGame:
        def __init__(self, grid_size=5, rounds=3):
            self.grid_size = grid_size
            self.rounds = rounds
            self.current_round = 0
            self.correct_numbers = []
            self.create_grid()

        def create_grid(self):
            total_cells = self.grid_size * self.grid_size
            numbers = list(range(1, total_cells + 1))
            random.shuffle(numbers)

            self.grid = []
            for i in range(self.grid_size):
                row = numbers[i*self.grid_size:(i+1)*self.grid_size]
                self.grid.append(row)

            self.correct_numbers = []

        def click_cell(self, value):
            expected_number = len(self.correct_numbers) + 1

            if value == expected_number:
                self.correct_numbers.append(value)

                if len(self.correct_numbers) == self.grid_size * self.grid_size:
                    self.current_round += 1
                    if self.current_round < self.rounds:
                        self.create_grid()
                        return True
                    else:
                        return False
                return "correct"
            else:
                self.correct_numbers = []
                return "wrong"

screen schulte_game_ui(schulte_game, show_rules=False):
    tag mini_game

    fixed:
        xsize 800
        ysize 600
        xalign 0.5
        yalign 0.5

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

                    text "• Перед вами таблица 5×5 со случайными числами от 1 до 25" size 22 color "#000"
                    text "• Вам нужно последовательно находить числа от 1 до 25" size 22 color "#000"
                    text "• Кликайте по числам в порядке возрастания: 1, 2, 3, ... 25" size 22 color "#000"
                    text "• Правильно нажатые числа подсвечиваются голубым" size 22 color "#000"
                    text "• При ошибке подсветка сбрасывается, начинайте снова с 1" size 22 color "#000"
                    text "• Всего будет 3 раунда" size 22 color "#000"
                    text "• В каждом раунде новая случайная таблица" size 22 color "#000"
                    text "• Результат: количество правильно пройденных чисел" size 22 color "#000"

                textbutton "Начать тест Шульте":
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
                        spacing 50

                        vbox:
                            spacing 5
                            text "ТЕСТ ШУЛЬТЕ" size 28 color "#000" xalign 0.5
                            text "Раунд: [schulte_game.current_round + 1] из [schulte_game.rounds]" size 22 color "#555" xalign 0.5

                        vbox:
                            spacing 5
                            text "Правильно найдено:" size 24 color "#000" xalign 0.5
                            frame:
                                background Solid("#ffffff")
                                padding (20, 10)
                                xalign 0.5
                                if len(schulte_game.correct_numbers) > 0:
                                    text str(len(schulte_game.correct_numbers)) + " чисел" size 36 color "#6CB0D8" xalign 0.5
                                else:
                                    text "Начинайте с 1" size 24 color "#555" xalign 0.5

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
                                    $ is_correct = cell_value in schulte_game.correct_numbers

                                    button:
                                        if is_correct:
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

                                        if is_correct:
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
    $ round_scores = []
    call screen schulte_game_ui(schulte_game, show_rules=True)

    if not _return.get("start", False):
        return

    while schulte_game.current_round < rounds:
        call screen schulte_game_ui(schulte_game, show_rules=False)

        $ result = _return.get("click", None)

        if result is not None:
            $ click_result = schulte_game.click_cell(result)

            if click_result == "correct":
                pass

            elif click_result == "wrong":
                pass

            elif click_result == True:
                $ last_score = len(schulte_game.correct_numbers)
                $ round_scores.append(last_score)

                if schulte_game.current_round < rounds:
                    centered "Раунд [schulte_game.current_round] завершен! Вы нашли все 25 чисел!"
                    centered "Следующий раунд начинается..."

            elif click_result == False:
                $ last_score = len(schulte_game.correct_numbers)
                $ round_scores.append(last_score)
                jump schulte_game_complete

    label schulte_game_complete:

    $ total_found = sum(round_scores)
    $ max_possible = rounds * 25
    $ average_found = round(total_found / rounds, 1) if rounds > 0 else 0

    $ best_round = max(round_scores) if round_scores else 0

    if best_round == 25:
        $ grade = "Отличный результат! Вы нашли все числа без ошибок."
        $ grade_color = "#2E7D32"
    elif best_round >= 20:
        $ grade = "Очень хороший результат! Отличная концентрация."
        $ grade_color = "#6CB0D8"
    elif best_round >= 15:
        $ grade = "Хороший результат. Внимание на хорошем уровне."
        $ grade_color = "#8BC34A"
    elif best_round >= 10:
        $ grade = "Средний результат. Рекомендуется тренировать внимание."
        $ grade_color = "#FF9800"
    else:
        $ grade = "Низкий результат. Стоит уделить больше времени тренировке внимания."
        $ grade_color = "#C62828"

    centered "Тест Шульте завершён!"

    show screen schulte_results_screen(round_scores, total_found, average_found, max_possible, best_round, grade, grade_color)
    pause

    hide screen schulte_results_screen

    return

screen schulte_results_screen(round_scores, total_found, average_found, max_possible, best_round, grade, grade_color):
    modal True
    zorder 200

    fixed:
        xsize 700
        ysize 550
        xalign 0.5
        yalign 0.5

        frame:
            background Solid("#6CB0D8")
            padding (5, 5)
            frame:
                background Solid("#f0f0f0")
                padding (30, 30)

                vbox:
                    spacing 25
                    xalign 0.5

                    text "РЕЗУЛЬТАТЫ ТЕСТА ШУЛЬТЕ" size 32 xalign 0.5 color "#000"

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
                                    text "Всего найдено:" size 22 color "#000" xalign 0.5
                                    text "[total_found] из [max_possible]" size 36 color "#6CB0D8" xalign 0.5

                                vbox:
                                    spacing 5
                                    text "Лучший раунд:" size 22 color "#000" xalign 0.5
                                    text "[best_round] из 25" size 36 color "#2E7D32" xalign 0.5

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