## модуль содержит класс DropBox (выпадающий список), улучшенный и доработанный

## КАК ПОЛЬЗОВАТЬСЯ:

# создать класс DropBox, в котором будут чередоваться названия пунктов и соответствующие им action
# если убрать modal=True, то при открытом списке можно кликать по другим виджетам, по quick_menu, например
# textbutton _("Выпадающий список ▼") action DropDown(
    # _("Строка 1"), Function(renpy.notify, "Строка 1"),
    # _("Строка 2"), Function(renpy.notify, "Строка 2"),
    # _("Строка 3"), Function(renpy.notify, "Строка 3"),
    # modal=True
    # )

# в параметрах можно указать xsize или width - ширину строк в выпадающем окошке
# или указать popup=True, тогда получится контекстное меню, привязанное к курсору мышки:
# screen test:
    # key "mouseup_3" action DropDown(
        # _("Настройки"), ShowMenu("preferences"),
        # _("Сохранить"), ShowMenu("save"),
        # _("Загрузить"), ShowMenu("load"),
        # _("Выход"), Quit(),
        # popup=True)

# ширина строк контекстного меню
define dropbox_popup_xsize = config.screen_width // 8

# фон, затемняющий экран позади модального списка
define dropbox_modal_background = "gui/overlay/confirm.png"

# по умолчанию списки модальные
define dropbox_default_modal = True

# по умолчанию списки прикрепляются к кнопкам
define dropbox_default_popup = False

# оформление зависит от настроек из gui.rpy, но можно поменять на своё
init -1:
    # стопка
    style dropbox_vbox is vbox:
        spacing 0

    # пункт
    style dropbox_button is button:
        background gui.text_color
        hover_background gui.hover_color
        selected_background gui.hover_color
        selected_hover_background gui.hover_color

    # текст пункта
    style dropbox_button_text is button_text:
        color gui.idle_color
        hover_color gui.text_color
        selected_color gui.text_color
        selected_hover_color gui.text_color

    # фон списка
    style dropbox_frame is empty


    # появление/исчезание затемнения за модальным списком
    transform dropbox_bg_at(t=.25):
        alpha 0

        on show:
            linear t alpha 1

        on hide:
            linear t alpha 0

    # появление/исчезание самого списка
    transform dropbox_at(t=.1):
        yzoom 0

        on show:
            linear t yzoom 1

        on hide:
            linear t yzoom 0

## ДАЛЕЕ ЛУЧШЕ НИЧЕГО НЕ МЕНЯТЬ

init -1 python:
    # класс разворачивающегося списка
    @renpy.pure
    class DropDown(Action):
        def __init__(self, *args, **kwargs):
            labels = args[0::2]
            actions = args[1::2]
            self.entries = list(zip(labels, actions))

            # если контекстное меню и не указаны другие размеры
            if kwargs.get("popup", dropbox_default_popup) and not (kwargs.get("width", None) or kwargs.get("xsize", None)):
                # то будет ширина из настроек
                kwargs["width"] = dropbox_popup_xsize

            self.kwargs = kwargs

        def __call__(self):
            renpy.capture_focus("dropdown")

            self.kwargs["current_w"] = self.kwargs.get("current_w", dropbox_xsize(**self.kwargs))

            if self.kwargs.get("modal", dropbox_default_modal):
                renpy.show_screen("dropdown_m", entries=self.entries, **self.kwargs)

            else:
                renpy.show_screen("dropdown_n", entries=self.entries, **self.kwargs)

            renpy.restart_interaction()

    # позиция окошка зависит от параметров на входе типа popup (привязать к курсору)
    # или pos, xpos, ypos - задать точные координаты, если флаг popup сброшен
    def dropbox_pos(**kwargs):
        if kwargs.get("popup", dropbox_default_popup):
            x, y = renpy.get_mouse_pos()
            x, y = int(x), int(y)

        else:
            x, y, w, h = focus()
            y += h
            xx, yy = kwargs.get("pos", (x, y))
            x, y = kwargs.get("xpos", xx), kwargs.get("ypos", yy)

        return x, y

    # координаты и размеры виджета, на котором установлен фокус
    def focus():
        x, y, w, h = renpy.focus_coordinates()

        if None in (x, y, w, h): return 0, 0, 0, 0

        return int(x), int(y), int(w), int(h)

    # ширина зависит от виджета с фокусом, а если такого нет, то от параметров на входе
    def dropbox_xsize(**kwargs):
        w = kwargs.get("xysize", (None, None))[0]
        w = kwargs.get("xsize", w) or kwargs.get("width", w)

        if w is None: w = focus()[2] or kwargs["current_w"]

        w = w or dropbox_popup_xsize

        return w

    def dropbox_get_size():
        d = renpy.get_widget("dropdown", "db")

        if d:
            w, h = renpy.render(d, config.screen_width, config.screen_height, 0, 0).get_size()

            return int(w), int(h)

        return None, None

    def dropbox_ysize(**kwargs):
        h = kwargs.get("xysize", (None, None))[1]
        h = kwargs.get("ysize", h) or kwargs.get("height", h)

        return h or dropbox_get_size()[1]

# выпадающий список
screen dropdown_n(entries, **kwargs):
    zorder 111
    use dropdown(entries, **kwargs)

# выпадающий список
screen dropdown_m(entries, **kwargs):
    modal True
    zorder 111

    button:
        action NullAction()
        style "empty"
        xfill True
        yfill True

        # фон, затемняющий экран позади списка
        if dropbox_modal_background and kwargs.get("modal", dropbox_default_modal):
            background dropbox_modal_background
            at dropbox_bg_at

    use dropdown(entries, **kwargs)

# выпадающий список
screen dropdown(entries, **kwargs):
    zorder 111

    # отмена
    dismiss:
        action Hide()

    default pos = dropbox_pos(**kwargs)

    # пустая рамка, чтобы выставить положение
    frame style "empty":
        at dropbox_at

        pos pos
        focus "dropdown"
        style_prefix "dropbox"

        frame:
            # скролл, если не помещаются все пункты
            viewport:
                mousewheel True
                draggable True
                pagekeys True

                if dropbox_xsize(**kwargs):
                    xsize dropbox_xsize(**kwargs)

                if dropbox_ysize(**kwargs):
                    ysize dropbox_ysize(**kwargs)

                yfill False

                # стопка
                vbox:
                    id "db"

                    # все пункты
                    for i in range(len(entries)):
                        $ label, action = entries[i]

                        # пункт
                        textbutton label:
                            # ширина строк
                            xsize dropbox_xsize(**kwargs)
                            action Hide(), action
