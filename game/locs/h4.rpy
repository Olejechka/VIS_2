define h4_v = 0
define h4_n = 0

label h4:
    $ curr_lock = "h4"
    scene der6 at right

    if h4_v == 0:
        hide screen map_but
        "*Вы медленно приближаетесь к дому, пока не упираетесь в окружающий его забор*"
        "*На заборе виднеется какая-то табличка*"
        "*Владельцев участка нигде не видно, да и из дома не доносится никаких звуков*"
        "*Только из-под забора с другой стороны слышно какое-то шуршание, будто что-то маленькое и живое суетится в ожидании*"
        $ h4_v = 1
        show screen map_but
        jump h4
    else:
        menu:
            "1. Попробовать позвать хозяев":
                hide screen map_but
                "*Вы окликиваете участок, в надежде, что к вам всё-таки выйдут*"
                play sound dog1
                dog "Гав"
                r "Думаю, что дома никого нет. Следует идти дальше"
                $ h4_n = 1
                show screen map_but
                jump h4
            "2. Зайти на участок":
                hide screen map_but
                show black with fade
                "*Вы осторожно открываете калитку, пока ваш напарник в недоумении смотрит на вас*"
                "*Вы делаете осторожно несколько шагов, как вдруг...*"
                play audio dog2
                show dog with hpunch
                "*Вы в панике убегаете с участка, закрывая за собой калитку*"
                hide dog with dissolve
                r "Лучше больше так не делать"
                show screen map_but
                jump h4
            "3. Осмотреться":
                hide screen map_but with dissolve
                call screen search
                show screen map_but with dissolve
    jump h4