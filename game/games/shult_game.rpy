init python:
    import random
    import time

    class SchulteGame:
        def __init__(self, grid_size=3):
            self.grid_size = grid_size
            self.start_time = None
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

        def start_timer(self):
            if self.start_time is None:
                self.start_time = time.time()

        def click_cell(self, value):
            # Запускаем таймер при первом клике
            self.start_timer()

            if value == self.expected_number:
                self.current_score += 1
                self.expected_number += 1

                if self.expected_number > self.grid_size * self.grid_size:
                    # Игра завершена успешно - начисляем очки по времени
                    elapsed_time = time.time() - self.start_time
                    self.award_points_by_time(elapsed_time)
                    return "game_over_success"

                return "correct"
            else:
                return "reset"

        def reset_game(self):
            self.create_grid()

        def award_points_by_time(self, elapsed_time):
            if elapsed_time <= 15:
                points = 10
            elif elapsed_time <= 20:
                points = 5
            elif elapsed_time <= 30:
                points = 3
            else:
                points = 0

            store.sh_schet += points
            return points

screen schulte_game_ui(schulte_game, show_rules=False):
    tag mini_game

    fixed:
        xsize 500
        ysize 500
        xalign 0.5
        yalign 0.5

        frame:
            background Solid("#6CB0D8")
            padding (5, 5)
            frame:
                background Solid("#f0f0f0")
                padding (20, 20)

        vbox:
            spacing 15
            xalign 0.5
            yalign 0.5

            if show_rules:
                text "Завершениче отчета" size 30 xalign 0.5 color "#000"

                vbox:
                    spacing 10
                    xalign 0.5
                    xsize 450

                    text "• Необходимо указать посещенные локации в правильном порядке" size 18 color "#000"
                    text "• Локации представлены номерами от 1 до 9" size 18 color "#000"
                    text "• Внимательно следите за числом, которое необходимо найти" size 18 color "#000"

                textbutton "Начать":
                    action [
                        Return({"start": True})
                    ]
                    keysym "input_enter"
                    xalign 0.5
                    xsize 200
                    background Solid("#6CB0D8")
                    text_size 22
                    text_color "#fff"
                    padding (10, 6)
                    text_xalign 0.5

            else:
                vbox:
                    spacing 10
                    xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing 15

                        vbox:
                            spacing 3
                            text "Найдите:" size 18 color "#000" xalign 0.5
                            frame:
                                background Solid("#6CB0D8")
                                padding (10, 5)
                                xalign 0.5
                                text "[schulte_game.expected_number]" size 28 color "#fff" xalign 0.5

                        vbox:
                            spacing 3
                            text "Очки:" size 18 color "#000" xalign 0.5
                            frame:
                                background Solid("#ffffff")
                                padding (10, 5)
                                xalign 0.5
                                text "[schulte_game.current_score] из 9" size 22 color "#6CB0D8" xalign 0.5

                    frame:
                        background Solid("#ffffff")
                        padding (10, 10)
                        xalign 0.5

                        grid 3 3:
                            xalign 0.5
                            yalign 0.5
                            spacing 5

                            for i in range(3):
                                for j in range(3):
                                    $ cell_value = schulte_game.grid[i][j]
                                    $ is_found = cell_value < schulte_game.expected_number

                                    button:
                                        background Frame("images/button_bg.png", 10, 10)
                                        hover_background Frame("images/button_bg_hover.png", 10, 10)
                                        xsize 90
                                        ysize 90
                                        action [
                                            Return({"click": cell_value})
                                        ]

                                        if is_found:
                                            text str(cell_value):
                                                size 32
                                                color "#6CB0D8"
                                                bold True
                                                align (0.5, 0.5)
                                        else:
                                            text str(cell_value):
                                                size 32
                                                color "#000000"
                                                bold True
                                                align (0.5, 0.5)

label schulte_game_screen:
    $ schulte_game = SchulteGame(grid_size=3)

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
            elif click_result == "game_over_success":
                return
            elif click_result == "reset":
                $ schulte_game.reset_game()