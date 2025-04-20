from yandex_testing_lesson import is_correct_mobile_phone_number_ru
 
 
def test_is_correct_mobile_phone_number_ru():
    test_cases = [
        # корректные номера
        ("8(900)1234567", True),
        ("+7 900 1234567", True),
        ("+7-900-123-45-67", True),
        ("212121212123", False),
        ("+7900(122)12-22", False),
    ]
 
    for number, expected_result in test_cases:
        result = is_correct_mobile_phone_number_ru(number)
        if result == expected_result:
            continue
        else:
            print('NO')
            return
 
    print("YES")  # все тесты пройдены
 
 
test_is_correct_mobile_phone_number_ru()
