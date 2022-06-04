def read_file_content(filename):
    with open(filename, "r") as file:
        content = file.read()
    return content


def get_word_list(content: str):
    """
    [['hello', 5], ['world', 2]]
    :param content: str
    :return: List(List)
    """
    specialChars = ".()*?!%+-,;:-@"
    for ch in specialChars:
        content = content.replace(ch, " ")

    word_lst = content.split()  # ["hello", "world"]
    for i in range(len(word_lst)):
        if word_lst[i].isupper():
            word_lst[i] = word_lst[i].lower()

    return word_lst


def get_word_count_dict(word_lst):
    d = {}
    for word in word_lst:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d


def get_freq_avg(dct):
    return sum(dct.values()) / len(dct)


def words_below_average(dct: dict, avg: float) -> tuple:
    lst = []  # empty list
    for k, v in dct.items():  #t = ("Dhoby", 3)   k = t[0]  v = t[1]     k, v = t   k, v = ("Dhoby", 3)
        if v < avg:
            lst.append(k)
    return tuple(lst)


def main():
    con = read_file_content("input.txt")
    print(con)
    lst = get_word_list(con)
    print(lst)
    word_counts = get_word_count_dict(lst)
    print(word_counts)
    avg = get_freq_avg(word_counts)
    print(avg)
    print(words_below_average(word_counts, avg))



# main()


if __name__ == '__main__':
    main()
