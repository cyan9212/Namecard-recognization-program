
def extractInfo(outText):
    info = ["name", "tel", "email"]
    str = outText.splitlines()
    print(str)
    for i in str:
        if i.find("010") != -1 or i.find("02") != -1 or i.find("031") != -1:
            if info[1] != "tel":
                break
            i = i.split(" ")
            temp = ""
            flag = 0
            for j in i:
                if flag == 0:
                    if j.find("010") != -1 or j.find("02") != -1 or j.find("031") != -1:
                        temp = temp+j
                        flag = 1
                        if len(temp) >= 10:
                            info[1] = temp
                            break
                        temp = temp + "-"
                    continue

                if flag == 1:
                    if j.find("0") != -1 or j.find("1") != -1 or j.find("2") != -1 or j.find("3") != -1 or j.find("4") != -1 or j.find("5") != -1 or j.find("6") != -1 or j.find("7") != -1 or j.find("8") != -1 or j.find("9") != -1:
                        temp = temp + j
                        if len(temp) >= 10:
                            info[1] = temp
                            break
                        temp = temp + "-"

        elif i.find("@") != -1:
            i = i.split(" ")
            for j in i:
                if j.find("@") != -1:
                    info[2] = j
        elif len(i) == 3:
            if info[0] == "name":
                info[0] = i
        else:
            if info[0] != "name":
                continue
            i = i.split(" ")
            flag = 0
            temp = ""
            for j in i:
                if len(j) == 1:
                    flag += 1
                    temp = temp + j
                else:
                    flag = 0
                    temp = ""
                if flag == 3:
                    info[0] = temp
                    break

    if info[0] == "name":
        info[0] = "-"
    if info[1] == "tel":
        info[1] = "-"
    if info[2] == "e-mail":
        info[2] = "-"
    return info
