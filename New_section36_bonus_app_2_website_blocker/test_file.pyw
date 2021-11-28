import time


while True:
    with open('counter.txt', 'r+') as file:
        data = file.readlines()
        if not data:
            file.write('1')
        else:
            file.seek(0)
            file.truncate()
            print(data)
            data.append(str(int(data[len(data) - 1]) + 1))
            print("data after modification : ", data)
            for number in data:
                file.write(str(number).strip() + "\n")

    time.sleep(10)