def normalize_name(input):

    for symbol in input:

        if symbol == "_":

           input = input.replace(symbol, " ")

    for symbol in input:
        
        if symbol.isalpha() == False and symbol.isdigit() == False and symbol != " ":

                 input = input.replace(symbol, "")

    input = input.strip().lower().replace(" ", "_")

    return input

def cumsum(number_list):

    sum_list = []
    current_sum = 0

    for number in number_list:

        current_sum += number
        sum_list.append(current_sum)

    return sum_list