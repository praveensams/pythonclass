from os import path

while True:

    while path.isfile("Feb"):
        print("File is there")
    else:
        print("End of loop")


    while not path.isfile("Feb"):
        print("File is not there")
    else:
        print("End of loop")

