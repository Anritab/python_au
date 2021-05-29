import math
import datetime
import random
import sys
def generate_count_by_sin(n):
    step = math.pi / n
    x_data = [i * step for i in range(n)]
    return [int(10 + 40 * math.sin(x)) for x in x_data]
def generate_count_by_power(n):
    return [10 + 2 ** x for x in range(n)]
def generate_count_by_log(n):
    return [int(20 + math.log((x + 0.1)*1000)) for x in range(n)]
def generate_count_by_parabola(n):
    return [10 + x ** 2 for x in range(n)]
def generate_dates(n):
    start = datetime.datetime(2020, 1, 15)
    return [(start + datetime.timedelta(days=30 * i)).strftime('%Y-%m') for i in range(n)]
def write_to_general_file(filename, num_months, num_resource):
    generate_count = [generate_count_by_sin(num_months),
                      generate_count_by_power(num_months),
                      generate_count_by_log(num_months),
                      generate_count_by_parabola(num_months)]
    months = generate_dates(num_months) * num_resource
    resources = []
    for i in range(0, num_resource):
        resources += [str(i + 1)] * num_months

    count = []
    for i in range(0, num_resource):
        count += generate_count[random.randint(0, 3)]
    str_count = [str(c) for c in count]
    elements = list(zip(months, resources, str_count))
    random.shuffle(elements)
    f = open(filename, 'w')
    f.write('data,resource,count\n')
    f.write('\n'.join([','.join(elem) for elem in elements]))
    f.write('\n')
    f.close()
def write_to_staff_file(filename, month, res, staff):
    rand = [20, 18, 16, 14, 12, 10, 0, 0, 0, 0, 0, 0]
    null = [0] * 12
    generate_count = [generate_count_by_sin(month),
                      generate_count_by_power(month),
                      generate_count_by_log(month),
                      generate_count_by_parabola(month)]

    months = generate_dates(month) * res * staff

    resources = []
    for i in range(0, res):
        resources += [str(i + 1)] * month * staff

    staff_id = []
    for i in range(0, staff):
        staff_id += [str(i + 1)] * month
    staff_id = staff_id * res

    count = []
    for i in range(0, res * staff):
        if random.randint(0, 10) % 7 == 0:
            count += rand
        elif random.randint(1, 20) % 13 == 0:
            count += null
        else:
            count += generate_count[random.randint(0, 3)]
    str_count = [str(c) for c in count]

    elements = list(zip(months, resources, staff_id, str_count))
    random.shuffle(elements)
    f = open(filename, 'w')
    f.write('data,resource,staff_id,count\n')
    f.write('\n'.join([','.join(elem) for elem in elements]))
    f.write('\n')
    f.close()


def main():
    filename = sys.argv[1]
    num_month = int(sys.argv[2])
    num_resource = int(sys.argv[3])
    num_staff = int(sys.argv[4])
    write_to_staff_file(filename, num_month, num_resource, num_staff)


if __name__ == '__main__':
    main()
