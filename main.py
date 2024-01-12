from input import input_1, input_2
from numpy import prod
def find_variations(data):
    variations = []
    data = [(int(k), v) for k, v in data.items()]
    for i in range(len(data)):
        counter = 0
        for j in range(data[i][0] + 1):
            distance = j * (data[i][0] - j)
            if distance > data[i][1]:
                counter += 1

        variations.append(counter)
    print(prod(variations))

if __name__ == '__main__':
    find_variations(input_1)
    find_variations(input_2)
