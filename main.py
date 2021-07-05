import copy
import json
import math

import cv2
import numpy as np
import pandas as pd

import processing_dataset
from model_traectory import trajectory


def startFisrtModel():
    data = []
    with open("data.txt", "r") as input:
        i = 0
        try:
            for line in input:
                data.append(float(line))
                i += 1
                if i > 4: raise ValueError
        except ValueError:
            print("Bad input")
    start_coordinates = [int(data[0]), int(data[1])]

    with open("final_coordinates.txt", "w") as output:
        end_coordinates_f = trajectory.make_coordinates1(*data)
        end_coordinates = [int(i) for i in end_coordinates_f]
        output.write(str(tuple(end_coordinates_f)))
    visualisation([[start_coordinates, end_coordinates]], "First model")
    pass


def angle(vector1, vector2):
    x1, y1 = vector1
    x2, y2 = vector2
    inner_product = x1 * x2 + y1 * y2
    len1 = math.hypot(x1, y1)
    len2 = math.hypot(x2, y2)
    return math.acos(inner_product / (len1 * len2))


def distance(vector1, vector2):
    x1, y1 = vector1
    x2, y2 = vector2
    return math.hypot(x1 - x2, y1 - y2)


def jsonStartmodel(json_file='data.json', dataset_file='coordinates.csv'):
    data = processing_dataset.read_data(dataset_file)
    with open(json_file, 'r') as f:
        config = json.load(f)

    end_points_model = []
    data["start"] = [[float(j) for j in i] for i in data["start"]]

    coordinates = pd.read_csv(dataset_file)

    for start_point, end_point, alpha in zip(data["start"], data['end'],
                                             data["angele"]):
        end_point_model = trajectory.make_coordinates2(*start_point, alpha,
                                                       config['power'], config[
                                                           'friction force'])
        end_points_model.append(end_point_model)
    coordinates['model coordinates x'] = [i[0] for i in end_points_model]
    coordinates['model coordinates y'] = [i[1] for i in end_points_model]
    print(coordinates)

    points = []
    for i in zip(data["start"] + data["start"],
                 data["end"] + end_points_model):
        points.append(i)
    print(data["start"], data["end"])
    visualisation(points, "xxx")

    '''    
    with open("final_coordinates2.txt", "w") as output:
        end_coordinates_f = trajectory.make_coordinates2(*data, coefs)
        end_coordinates = [int(i) for i in end_coordinates_f]
        output.write(str(tuple(end_coordinates_f)))
    end_coordinates_second = [int(i) for i in end_coordinate_second]
    visualisation([[start_coordinates, end_coordinates], [start_coordinates,
                                                          end_coordinates_second]],
    '''


def startSecondModel():
    coefs = []
    data = []
    with open("data2.txt", "r") as input:
        try:
            i = 0
            for line in input:
                if i < 4:
                    data.append(float(line))
                else:
                    coefs.append(float(line))
                i += 1
                if i > 8: raise ValueError
        except ValueError:
            print("Bad input")
    start_coordinates = [int(data[0]), int(data[1])]

    with open("final_coordinates2.txt", "w") as output:
        end_coordinates_f = trajectory.make_coordinates2(*data, coefs)
        end_coordinates = [int(i) for i in end_coordinates_f]
        output.write(str(tuple(end_coordinates_f)))
    visualisation([[start_coordinates, end_coordinates]], "Second model")
    pass


def start():
    coefs = []
    data = []
    with open("data2.txt", "r") as input:
        try:
            i = 0
            for line in input:
                if i < 4:
                    data.append(float(line))
                else:
                    coefs.append(float(line))
                i += 1
                if i > 8: raise ValueError
        except ValueError:
            print("Bad input")
    start_coordinates = [int(data[0]), int(data[1])]
    end_coordinate_second = trajectory.make_coordinates1(*data)
    with open("final_coordinates2.txt", "w") as output:
        end_coordinates_f = trajectory.make_coordinates2(*data, coefs)
        end_coordinates = [int(i) for i in end_coordinates_f]
        output.write(str(tuple(end_coordinates_f)))
    end_coordinates_second = [int(i) for i in end_coordinate_second]
    visualisation([[start_coordinates, end_coordinates], [start_coordinates,
                                                          end_coordinates_second]],
                  "Second model")
    pass


def visualisation(Points,
                  name_model: str):
    color = (255, 255, 255)
    ball_color = [116, 1, 55]
    trajectory_color = (123, 100, 200)
    another_trajectory_color = (200, 100, 123)
    and_another_one_trajectory_color = (100, 100, 50)
    thickness = 3
    window_name = 'Image'
    field_size = [660, 960]
    cache = Points
    center = [i / 2 for i in field_size]

    Points = [[[int(k * 100 + c) for k, c in zip(j, center[::-1])] for j in i]
              for i in cache]

    img = np.zeros((*field_size, 3), np.uint8) + (
        np.uint8(10), np.uint(150), np.uint(15))
    img = img.astype(np.uint8)
    bord = 30
    border = [(bord, bord), (field_size[1] - bord, bord),
              (field_size[1] - bord, field_size[0] - bord),
              (bord, field_size[0] - bord)]
    points_sz = len(Points)

    for i in range(4):
        img = cv2.line(img, border[i], border[(i + 1) % 4], color, thickness)

    center_coordinates = (field_size[1] // 2, field_size[0] // 2)
    radius = 50
    img = cv2.circle(img, center_coordinates, radius, color, thickness)
    dot_radius = 8
    img = cv2.circle(img, center_coordinates, dot_radius, color, -1)
    img = cv2.line(img, (field_size[1] // 2, bord), (field_size[1] // 2,
                                                     field_size[0] - bord),
                   color, thickness)
    font = cv2.FONT_HERSHEY_SIMPLEX
    i = 0
    print(points_sz)
    for i in range(points_sz // 2):
        img1 = copy.copy(img)
        points_e = Points[i]
        points_m = Points[points_sz + i - points_sz // 2]

        img1 = cv2.circle(img1, points_e[0], 5, ball_color, -1)
        img1 = cv2.circle(img1, points_e[1], 5, ball_color, -1)
        img1 = cv2.arrowedLine(img1, points_e[0], points_e[1],
                               trajectory_color, 2, tipLength=0.1)
        img1 = cv2.putText(img1, str(tuple(points_e[0])), points_e[0], font,
                           0.5,
                           (150, 10, 0), 1, cv2.LINE_AA)
        img1 = cv2.putText(img1, str(tuple(points_e[1])), points_e[1], font,
                           0.5,
                           (150, 10, 0), 1, cv2.LINE_AA)

        img1 = cv2.circle(img1, points_m[0], 5, ball_color, -1)
        img1 = cv2.circle(img1, points_m[1], 5, ball_color, -1)
        img1 = cv2.arrowedLine(img1, points_m[0], points_m[1],
                               another_trajectory_color, 2, tipLength=0.1)
        img1 = cv2.putText(img1, str(tuple(points_m[0])), points_m[0], font,
                           0.5,
                           (150, 10, 0), 1, cv2.LINE_AA)
        img1 = cv2.putText(img1, str(tuple(points_m[1])), points_m[1], font,
                           0.5,
                           (150, 10, 0), 1, cv2.LINE_AA)
        img1 = cv2.putText(img1, "Deflection angle is " + str(angle(
            points_m[1], points_e[1])), [50, 50], font, 0.5, (150, 10, 0), 1,
                           cv2.LINE_AA)
        img1 = cv2.putText(img1, "Deviation " + str(distance(points_m[1],
                                                             points_e[1])),
                           [50, 80], font, 0.5, (150, 10, 0), 1,
                           cv2.LINE_AA)

        # img1 = cv2.arrowedLine(img1, points_e, points_m,
        #                      and_another_one_trajectory_color, 2,
        #                      tipLength=0.1)
        cv2.imshow(name_model, img1)
        cv2.waitKey()

    '''for i in range(points_sz // 2):
        point_m = Points[i][1]
        point_e = Points[points_sz + i - points_sz // 2][1]
        img = cv2.arrowedLine(img, point_e, point_m,
                              trajectory_color, 2, tipLength=0.1 )
     '''

    # print (img[0][0][0])
    cv2.imshow(name_model, img)
    cv2.waitKey()

    pass


if __name__ == '__main__':
    # startFisrtModel()
    # startSecondModel()
    # start()
    jsonStartmodel()
