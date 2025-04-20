from yandex_testing_lesson import strip_punctuation_ru


def test():
    cases = [
        ("Привет, как дела?", "Привет как дела"),
        ("Это e-mail для связи!", "Это e-mail для связи"),
        ("Ну и что - подумаешь...", "Ну и что подумаешь"),
        ("Цена: 1000₽.", "Цена 1000₽")
    ]

    for inp, expected in cases:
        result = strip_punctuation_ru(inp)
        if result != expected:
            print(result, expected)
            print("NO")
            return
    print("YES")


test()

