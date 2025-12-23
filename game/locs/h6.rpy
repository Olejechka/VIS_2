define h6_v = 0
define h6_n = 0

define h6_сt = ""
define h6_f = ""
define h6_r = ""

#ДЕД МАЗАЙ
#наименование персонажа dead_0m
label h6:
    $ curr_lock = "h6"

    if ct == 6:
        r "Это был последний счетчик."
        r "Пора возвращаться на базу."
        scene black with fade
        jump final

    $ h_number = hn_6
    $ h_name = "Мазайхин И.С."

    $ h_counter = h6_сt
    $ h_fault = "Нет"
    $ h_reason = "Наброс"

    scene der5 at center
    if h6_v == 0:
       python:
            import random
            counter_value = random.randint(10000, 70000)
            h6_сt = str(counter_value).zfill(5)
       hide screen map_but
       show dead_0m at center
       "*Проходя дальше, взгляду открылся густой дым, который исходит из небольшого домика. Подойдя ближе из него вышел дедушка. *"
       show dead_0m at center
       r "Доброе утро!"
       dead_0 "Что вам нужно тут?"


       menu:
            "Мы с напарником хотели бы проверить ваш счетчик.":
                dead_0 "Чужих к себе не приглашаю. Вам стоит уйти."
                r "Поймите нам нужно выполнить свою работу, после же мы сразу исчезнем."
                dead_0 "Смотрите и проваливайте!"
            "Здравствуйте. Не подскажете, как вас зовут?":
                dead_0 "Иван Саввич Мазайхин."
                $ dead_0 = Character("Иван Саввич")
                $ h6_n = 1
                "*Мужчина всем своим видом проявлял недовольство. *"
       $ h6_v = 1
       hide fance with dissolve
       show screen map_but
       jump h6

    if h6_v == 1:
        show dead_0m at center
        menu:
            "1. Можно просто поговорить?":
                dead_0 "В темпе давайте."
                jump h6_q
            "2. Осмотреться":
                hide dead_0m with dissolve
                hide screen map_but with dissolve
                call screen search
                show dead_0m with dissolve
                show screen map_but with dissolve
            "3. Проверить счетчик" if c_h6 == False:
                hide screen map_but
                "*Переступив через ограду, можно было отправиться проверять счётчик.*"
                call ct_lb
                show screen map_but

    jump h6

label h6_q:
    menu:
         "1. Как вас зовут?":
             if h6_n == 0:
                dead_0 "Иван Саввич Мазайхин."
                $ dead_0 = Character("Иван Саввич ")
                $ h6_n = 1
             else:
                dead_0 "Кофе попей, внучок."
                r "Извините…"
             show screen map_but
         "2. Чем вы занимаетесь?":
             hide screen map_but
             dead_0 "А с чего это вдруг молодёжь переживает за досуг старика, а?"
             "*Старик слегка улыбнулся. *"
             dead_0 "Охотник я бывший, смекаете? Люблю мяса вкусного поесть да поспать хорошо. Баню вот сам построил, чтобы с удовольствием жить. Родом из деревни Малые Вежи."
             r "С вами ещё кто-то живёт?"
             dead_0 "Никакого не нажил кроме одного десятка лесных кроликов."
             show screen map_but
         "3. Не подскажете номер вашего дома?":
             hide screen map_but
             dead_0 "Ох, номер..."
             dead_0 "Вспомнил! Номер [hn_6]"
             show screen map_but
         "4. Происходит что-то интересное в деревне?":

             hide screen map_but
             dead_0 "Это ещё что за вопрос такой? Ходите тут слухи собираете. Не думали работать, а не языками чесать?"
             r "Всё же интересно узнать, чем же живёт такая глубинка."
             dead_0 "Не моё это дело - женские сплетни собирать. Сам уши не грею и вам не советую."
             show screen map_but

         "Назад":
            jump h6
    jump h6_q
