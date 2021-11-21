# WAF with two input params list and object
# check if object is in list if not append in list


def check_object(obj_list, obj):
    if obj not in obj_list:
        obj_list.append(obj)
    return obj_list


sample = [1, 2, 3]

new_list = check_object(sample, 3)

print(new_list)
