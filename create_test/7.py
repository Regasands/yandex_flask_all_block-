def strip_punctuation_ru(arg):
    punctuations = '''!()—[]{};:'",<>./?@#$%^&*_~'''
    str_ = ''
    try:
        for elem in arg:
            if elem not in punctuations:
                str_ += elem
            else:
                str_ += ' '
        str_ = str_.replace(' - ', ' ')
        str_ = str_.strip()
        last_arg = str_[0]
        end_str = last_arg
        for e in str_[1:]:
            if e == last_arg and e in ['\t', ' ', '\n']:
                continue
            end_str += e
            last_arg = e
                
        return end_str
    except Exception:
        return ''


a = input()
print(strip_punctuation_ru(a))
