from model_traectory import trajectory




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = []
    with open("data.txt","r") as input:
        for line in input:
            data.append(float(line))
    with open("final_coordinates.txt", "w") as output:
        output.write(str(tuple(trajectory.make_coordinates(*data))))


