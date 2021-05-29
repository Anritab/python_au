import matplotlib.pyplot as plt


def string_to_dictionary(keys, line):
    d = dict()
    values = (line.strip('\n')).split(',')
    i = 0
    for key in keys:
        d[key] = values[i]
        i += 1
    return d


def read_from_file(file):
    array = []
    f = open(file, 'r')
    all_lines = f.readlines()
    keys = (all_lines[0].strip('\n')).split(',')
    for line in all_lines[1:]:
        d = string_to_dictionary(keys, line)
        array.append(d)
    f.close()
    return array


def sort_list_of_dict(list_of_dict, key):
    result = sorted(list_of_dict, key=lambda k: k[key])
    return result


def filter_list_of_dict(list_of_dict, key, value):
    result = list(filter(lambda x: value in x[key], list_of_dict))
    return result


def plotting(list_of_dict, x1, y_axis, title):
    x = []
    y = []

    sorted_list = sort_list_of_dict(list_of_dict, x1)

    for dic in sorted_list:
        x.append(dic[x1])
        y.append(int(dic[y_axis]))

    plt.title(title)
    plt.plot(x, y, color='blue', marker='o')
    plt.show()
def print_all_plot(list_of_dict, num_resource, num_staff):
    for i in range(1, num_resource+1):
        filt_resource_list = filter_list_of_dict(list_of_dict, 'resource', str(i))
        for j in range(1, num_staff+1):
            filtered_list = filter_list_of_dict(filt_resource_list, 'staff_id', str(j))
            plotting(filtered_list, 'data', 'count', 'resource ' + str(i) + ' staff_id ' + str(j))
        if num_staff == 0:
            filtered_list = filt_resource_list
            plotting(filtered_list, 'data', 'count', 'resource ' + str(i))
def print_sum_plot(list_of_dict, source, num_source, num_param):
    for i in range(1, num_source+1):
        filtered_list = filter_list_of_dict(list_of_dict, source, str(i))
        sorted_filtered_list = sort_list_of_dict(filtered_list, 'data')
        sum_list_of_dict = []
        keys = list(list_of_dict[0])
        j = 0
        sum_count = 0
        for dic in sorted_filtered_list:
            if j < num_param:
                sum_count += int(dic[keys[3]])
                j += 1
            if j == num_param:
                d = dict()
                d['data'] = dic['data']
                d['count'] = sum_count
                sum_list_of_dict.append(d)
                sum_count = 0
                j = 0
        plotting(sum_list_of_dict, 'data', 'count', source + ' ' + str(i))
def main():
    file = 'count.txt'
    list_of_dict = read_from_file(file)
    print_all_plot(list_of_dict, 2, 2)
if __name__ == '__main__':
    main()
