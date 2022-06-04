from CompoundDataTypes.similarity_of_doc.sim import get_similarity


def test_get_word_count_list():
    from CompoundDataTypes.similarity_of_doc.sim import get_word_count_list
    content = "hello world- hello mars jupyter:"
    lst = get_word_count_list(content)
    print(lst)



def main():
    content1 = input("Enter content of first doc.")
    content2 = input("Enter content of second doc.")

    s = get_similarity(content1, content2)

    print("Similarity of two doc is", s)


main()
#test_get_word_count_list()
