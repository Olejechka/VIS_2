define h7_v = 0

label h7:
    $ curr_lock = "h7"
    scene kd at center
    if h7_v == 0:
        hide screen map_but
        "*Проходя ближе к следующему домику, вам всё отчётливее слышался детский смех*"
        vovan "Привет!"
        "*После этих слов до вас донёсся звук закрывания двери*"
        show kid_0m at center

        menu:
            "А дома есть взрослые?":
                vovan "Нет. Мама и папа уехали в яму за картошкой, а я остался главным!"
                "*Мальчик, очевидно, очень гордился этим статусом*"
            "Мы пройдём посмотрим?":
                vovan "Мама мне сказала, что нельзя никого впускать пока дома никого нет!"
        r "Без взрослых мы не можем зайти на участок, так что давай пойдем дальше"
        $ h7_v = 1
        show screen map_but
        jump h7
    else:
        show kid_0m at center
        menu:
            "1. Осмотреться":
                hide kid_0m with dissolve
                hide screen map_but with dissolve
                call screen search
                show kid_0m with dissolve
                show screen map_but with dissolve
            "2. Скоро ли вернутся родители?":
                vovan "Мама и папа хотели заехать к бабушке на обратном пути, так что..."
                r "Мы не можем ждать"
                r "Нужно вернуться на базу до конца рабочего дня"
        jump h7