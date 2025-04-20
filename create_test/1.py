from yandex_testing_lesson import is_palindrom


def test_reverse():
    test_data = (
        (42, None),
        (['a', 'b', 'c'], None),
        ('', True),
        ('aba', True),
        ('a', True),
        ('abc', 'False'))

    for input_s, correct_output_s in test_data:
        try:
            output_s = is_palindrom(input_s)
        except TypeError:
            if correct_output_s is None:
                continue
            if type(input_s) == str:
                print('NO')
                return False
        except Exception:
            print("NO")
            return False
        else:
            if output_s != correct_output_s:
                print("NO")
                return False
    print("YES")
    return True
