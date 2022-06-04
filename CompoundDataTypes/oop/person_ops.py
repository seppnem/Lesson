def save_person(list, name, tckn, age):
    t = (name, tckn, age)
    list.append(t)


def display_names(list):
    for p in list:
        print(p[0])


def avg_age(list):
    total = 0
    for p in list:
        total += p[2]

    return total / len(list)




def main():
    person_data_list = []
    save_person(person_data_list, "Onur", 125874565, 38)
    save_person(person_data_list, "Sebnem", 125874565, 38)
    print(person_data_list)
    display_names(person_data_list)
    print(avg_age(person_data_list))

    person_data_list2 = []
    save_person(person_data_list2, "ayse", 1231548, 60)
    display_names(person_data_list2)
    print(avg_age(person_data_list2))

if __name__ == '__main__':
    main()