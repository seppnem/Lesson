def get_word_count_list(content:str):
    """
    [['hello', 5], ['world', 2]]
    :param content: str
    :return: List(List)
    """
    specialChars = ".()*?!%+-,;:-"
    for ch in specialChars:
        content = content.replace(ch, "")

    #str content   "hello world"

    word_lst = content.split() #["hello", "world"]

    word_counts = []

    for word in word_lst:
        result = linear_search(word_counts, word)
        if result == -1:
            word_counts.append([word, 1])
        else:
            word_counts[result][1] = word_counts[result][1] + 1

    return word_counts


def linear_search(word_count, word):
    for i, [w, c] in enumerate(word_count): #unpack ["hello", 1]
        if w == word:
            return i

    return -1






def align_list(first, second):
    """
    second da olup first olmayan kelimeleri first ekleyecek 0 değeriyle ekledik
    :param first:
    :param second:
    :return:
    """
    for word, c in second:
        res = linear_search(first, word)
        if res == -1:
            first.append([word, 0])



def sort_by_word(lst):
    lst.sort(key=lambda ls : ls[0])


def calculate_similarity(first, second):
    total = 0
    for i in range(len(first)):
        total += first[i][1] * second[i][1]

    return total / len(first)


def get_similarity(con1, con2):
    first = get_word_count_list(con1)
    second = get_word_count_list(con2)

    first_a = align_list(first, second)
    second_a = align_list(second, first)

    sort_by_word(first_a)
    sort_by_word(second_a)

    return calculate_similarity(first_a, second_a)
