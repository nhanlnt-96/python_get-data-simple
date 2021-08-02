import subprocess
import re
import html


# get data
def getData(number):
    f = open("./data.txt", "bw")

    i = 2000001
    end = 2000000 + number + 1

    while i in range(end):
        id_number = "0" + str(i)

        data = subprocess.check_output(f'curl -F "SoBaoDanh={id_number}" diemthi.hcm.edu.vn/Home/Show', shell=True)

        f.write(data)
        i += 1
    f.close()


def dataHandle():
    # open file
    f = open("./data.txt", "r")
    r = open("./tag-replace.txt", "r")

    # split line string
    tag = r.read()
    tag_list = tag.splitlines()

    # read file
    data = f.read()

    # replace tag in file
    for tag_item in tag_list:
        data = data.replace(tag_item, "")

    # close file
    f.close()
    r.close()

    # replace spaces in file
    data = html.unescape(re.sub(r"\s+", " ", data))
    data = data.replace("thi", "thi\n")
    data = data.replace("Họ", "\nHọ")

    # overwrite to file
    f = open("./data.txt", "w")
    f.write(data)
    f.close()


def startProgram():
    print('''
    [1]. Get data
    [2]. Data handle
    [3]. Exit
    ''')

    option = int(input('Enter option: '))

    if option == 1:
        number = int(input('How many id number you want to get: '))
        getData(number)
        startProgram()
    elif option == 2:
        dataHandle()
        print('done')
        startProgram()
    else:
        exit()


startProgram()
