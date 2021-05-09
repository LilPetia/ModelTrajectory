import cv2
import numpy as np

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
        end_coordinates = [int(i)for i in end_coordinates_f]
        output.write(str(tuple(end_coordinates_f)))
    visualisation(start_coordinates,end_coordinates, "First model")
    pass


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
        end_coordinates_f = trajectory.make_coordinates2( *data, coefs)
        end_coordinates = [int(i)for i in end_coordinates_f ]
        output.write(str(tuple(end_coordinates_f)))
    visualisation(start_coordinates, end_coordinates, "Second model")
    pass


def visualisation(start_point: [int, int], end_point: [int, int],
                  name_model:str):
    color = (255, 255, 255)
    ball_coolor = (4, 4, 4)
    trajectory_color = (43, 0, 0)
    thickness = 3
    window_name = 'Image'
    field_size = [512, 700]
    img = np.zeros((*field_size, 3)) + (0, 100, 0)
    bord = 30
    border = [(bord, bord), (field_size[1] - bord, bord),
              (field_size[1] - bord, field_size[0] - bord),
              (bord, field_size[0] - bord)]
    # cv2.namedWindow('xxx', cv2.WINDOW_AUTOSIZE)
    for i in range(4):
        img = cv2.line(img, border[i], border[(i + 1) % 4], color, thickness)

    center_coordinates = (field_size[1] // 2, field_size[0] // 2)
    radius = 50
    img = cv2.circle(img, center_coordinates, radius, color, thickness)
    dot_radius = 8
    img = cv2.circle(img, center_coordinates, dot_radius, color, -1)
    # centerLine
    img = cv2.line(img, (field_size[1] // 2, bord), (field_size[1] // 2,
    field_size[0] - bord), color, thickness)
    # arrow
    img = cv2.circle(img, start_point, dot_radius, color, -1)
    img = cv2.circle(img, end_point, dot_radius, color, -1)
    img = cv2.arrowedLine(img, start_point, end_point,
                            trajectory_color, 5)

    cv2.imshow(name_model, img)
    cv2.waitKey()

    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    startFisrtModel()
    startSecondModel()
