import re


def separate_words_and_numbers(x: str) -> str:
    """Отделить цифры от букв в слове."""
    result = ""
    for i in range(1, len(x)):
        prev = x[i-1]
        cur = x[i]
        if (not prev.isdigit() and prev != " ") and cur.isdigit():
            result += " "
        if result == "":
            result += prev
        result += cur
    return result


def split_digit_with_unit(x: str):
    """Добавить пробел перед единицами измерения."""
    result = []
    pat = re.compile("\d[г|рул|р|шт|гр]")
    words = [w.lower() for w in x.split()]
    for word in words:
        m = pat.search(word)
        if m:
            word = word[:m.start()+1]+" " + word[m.start() +
                                                 1:m.end()+1] + word[m.end()+1:]
        result.append(word)
    return " ".join(result)


remove_nX_temp = re.compile(r"\d[ХxХх]")


def remove_nX(x: str):
    """Убрать записи вида 1х,2X и тд."""
    return remove_nX_temp.sub(" ", x)


remove_service_char_pat = re.compile("[\,\.\*\:\-\d]")


def remove_service_char(x):
    """Убрать спецсимволы."""
    return remove_service_char_pat.sub(" ", x)


general_words = ['вес', 'глобус']


def remove_general_words(x):
    """Убрать общие слова для всех позиций в чеке."""
    pattern = "|".join(general_words)
    return re.sub(pattern, " ", x)


units = ('г', 'рул', 'р', "шт", "гр")


def remove_unit_whitespace(x: str):
    """Убрать единицы измерения, где разделить пробел."""
    words = [w.lower() for w in x.split()]
    result = []
    i, j = 0, 1
    while j < len(words):
        prev = words[i]
        cur = words[j]

        if prev.isdigit() and cur in (units):
            i += 2
            j += 2
            continue
        result.append(prev)
        i += 1
        j += 1
    if words[-1] not in units:
        result.append(words[-1])
    return " ".join(result)
