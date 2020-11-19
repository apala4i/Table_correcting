file_name = input('Input full path to file\n')


def table_edit():
    """
    fix table
    :return: corrected table
    """
    max_values_of_stroke = [-10] * 256
    max_values_of_text = [-10] * 256
    current_stroke = ['None empty value']
    input_file = open(file_name, 'r', encoding='utf-8')
    input_file.readline()
    count_of_strokes = 0
    # Read stroke of the table. replace "│" sights to -1, to
    # make them easier to work with. Finding pozition of "│" sights
    current_stroke = [-1 if i == '│' else len(i) for i
                      in input_file.readline().replace('│', ' │ ').split()]
    while len(current_stroke) > 1:
        zero_indexes = [poz for poz, element in enumerate(current_stroke)
                        if element == -1]
        for i in range(len(zero_indexes) - 1):

            # finding max length of each column
            max_values_of_stroke[i] = sum(
                current_stroke[zero_indexes[i]:zero_indexes[i + 1]]) + 1 \
                                + zero_indexes[i + 1] - zero_indexes[i]
            if max_values_of_stroke[i] > max_values_of_text[i]:
                max_values_of_text[i] = max_values_of_stroke[i]
        count_of_strokes += 1
        current_stroke = [-1 if i == '│' else len(i) for i
                          in input_file.readline().replace('│', ' │ ').split()]

    # massive with maximum length of each column and with the length of
    # maximum column count.
    len_of_max = [x for x in max_values_of_text if x > 0]

    # massive made to create a table decoration.
    table = [x * '─' for x in max_values_of_text if x > 0]

    return len_of_max, table, count_of_strokes


def table_creating():
    """
    create txt file with fixed table
    :return:
    """
    pass


def table_correcting():
    """
    main function that corrects given table and make new file with
    corrected table
    :return: fixed table
    """
    global file_name
    table_edit()
    table_creating()


print(table_edit())
