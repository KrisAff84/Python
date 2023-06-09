# Function in which only unique values will be returned

def unique(value_list):
    final_list = []
    for value in value_list:
        if value not in final_list:
            final_list.append(value)
    return final_list


print(unique([5, 5, 7, 8, 9, 5, 4, 5, 8, 7, 2, 1, 5, 2, 1]))




