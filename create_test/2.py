from yandex_testing_lesson import is_prime 


def test_reverse():
    test_data = (
        (1, None),
        (4, False),
        (10, False),
        (3, True),
        (0, None),
        (3, True),
        (23, True),
        (2, True),
        (5, True),
        (823, True))

    for input_s, correct_output_s in test_data:
        try:
            output_s = is_prime(input_s)
        except TypeError:
            if correct_output_s is None:
                continue
        except ValueError:
            if correct_output_s is None:
                continue
        except Exception as e:
            print("NO")
            print(e)
            return False
        else:
            if output_s != correct_output_s:
                print("NO")
                print(output_s, correct_output_s, input_s)
                return
    print("YES")


test_reverse()
