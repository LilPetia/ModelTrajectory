from model_traectory import trajectory


def startFisrtModel():
    data = []
    with open("data.txt", "r") as input:
        i = 0
        try:
            for line in input:
                data.append(float(line))
                i += 1
                if i > 5: raise ValueError
        except ValueError:
            print("Bad input")
    with open("final_coordinates.txt", "w") as output:
        output.write(str(tuple(trajectory.make_coordinates1(*data))))
    pass


def startSecondModel():
    coefs = []
    data = []
    with open("data2.txt", "r") as input:
        try:
            i = 0
            for line in input:
                if i <= 4:
                    data.append(float(line))
                else:
                    coefs.append(float(line))
                i += 1
                if i > 9: raise ValueError
        except ValueError:
            print("Bad input")
    with open("final_coordinates2.txt", "w") as output:
        output.write(str(tuple(trajectory.make_coordinates2(*data, coefs))))

    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startFisrtModel()
    startSecondModel()
