from CompoundDataTypes.files.word_count_in_file import get_word_list, read_file_content


def eval_input(lst1, lst2):
    ops = input("Enter ops [ins -> intersection of doc, un -> merge two files]")
    s1 = set(lst1)
    s2 = set(lst2)
    if ops == "ins":
        res = s1.intersection(s2)
        return tuple(res)
    elif ops == "un":
        res = s1.union(s2)
        return tuple(res)
    else:
        print("ınvalid OPS [ins -> intersection of doc, un -> merge two files]")
        return ()  # empty


def main():
    while True:
        try:
            file1 = input("Enter a file name")
            file2 = input("Enter a file name")

            content1 = read_file_content(file1)
            content2 = read_file_content(file2)
            break
        except FileNotFoundError as fne:
            print("İnvalid file names", fne.filename)

    word_list1 = get_word_list(content1)
    word_list2 = get_word_list(content2)

    res = eval_input(word_list1, word_list2)

    print(res)


if __name__ == '__main__':
    main()
