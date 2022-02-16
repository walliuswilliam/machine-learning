import random
import math
import matplotlib.pyplot as plt

centers = {1: [(2, 2), (-2, -2)], 2: [(2, -2), (-2, 2)]}

def calculate_distance(initial_point, ending_point):
    x = ending_point[0] - initial_point[0]
    y = ending_point[1] - initial_point[1]
    return (x ** 2 + y ** 2) ** 0.5


def find_closest_center(point, point_type):
    possible_centers = []

    for key in centers:
        if point_type == key:
            possible_centers = centers[key]

    min_distance = 100000
    closest_center = (100, 100)

    for center in possible_centers:
        distance = calculate_distance(point, center)

        if distance < min_distance:
            min_distance = distance
            closest_center = center

    return closest_center

def probability(x):
    return 2 ** (-1 * x)

def create_random_dataset(data_set_size,return_dict=False):
    num_points = 0
    point_data = {1: [], 2: []}

    while num_points < data_set_size:
        x = random.uniform(-4, 4)
        y = random.uniform(-4, 4)

        point_type = 1

        if num_points < data_set_size / 2:
            point_type = 2

        closest_center = find_closest_center((x, y), point_type)

        distance = calculate_distance((x, y), closest_center)

        if probability(distance) >= random.uniform(0, 1):
            point_data[point_type].append((x, y))
            num_points += 1

    if return_dict:
        return point_data

    point_list = [[],[]]
    for point in point_data[1]:
      point_list[0].append(point)
      point_list[1].append(1)
    for point in point_data[2]:
      point_list[0].append(point)
      point_list[1].append(2)

    return point_list

if __name__ == "__main__":
  dataset = create_random_dataset(200,return_dict=True)
  for i in range(100):
    plt.plot([dataset[1][i][0]], [dataset[1][i][1]], marker='x', color='red')
    plt.plot([dataset[2][i][0]], [dataset[2][i][1]], marker='o', color='blue')

  plt.savefig('datasets/semi_random.png')