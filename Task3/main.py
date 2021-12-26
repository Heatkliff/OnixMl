import csv
import json


def f1(x):
    return x / (x + 100)


def f2(x):
    return 1 / x


def f3(x):
    return 20 * (f1(x) + f2(x)) / x


if __name__ == "__main__":
    step1 = [(f1(x), f2(x)) for x in range(5, 90)]
    step2 = [f3(x) for x in range(5, 90)]
    step3 = {x: [f1(x), f2(x), f3(x)] for x in range(5, 90)}
    # step4
    with open("step4.csv", 'w') as step4:
        step4_writer = csv.writer(step4, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for x, results in step3.items():
            step4_writer.writerow([x, results[0], results[1], results[2]])

    # step5
    with open("step4.csv", 'r') as step4:
        step4_writer = csv.reader(step4, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # step5 = [row for row in step4_writer]
        step5 = list(filter(lambda row: row != [], step4_writer))

    # step6
    if step5:
        with open("step6.csv", 'w') as step6:
            json.dump(step5, step6)
