label splashscreen:
    # Воспроизводим музыку
    play sound door6

    # Показываем логотип на 3 секунды, затем плавно исчезает
    show logo2 with fade
    pause 2.5
    hide logo2 with fade
    stop sound

    return