import random
import string


def getFinalList(total, ret):
    list_all = [i for i in range(1, total + 1)]
    ret_list = []
    for i in range(ret):
        index = random.randint(0, len(list_all) - 1)
        ret_list.append(list_all[index])
        list_all.remove(list_all[index])
    return ret_list


def getFinalListV2(total, ret):
    list_all = [i for i in range(1, total + 1)]
    random.shuffle(list_all)
    return list_all[0:ret]


def getFinalCards(ret):
    card_index = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    card_flowers = "♠♥♦♣"
    card_list = []
    for card_flower in card_flowers:
        for index in card_index:
            card_list.append(card_flower + index)
    card_list.append("大王")
    card_list.append("小王")
    random.shuffle(card_list)
    return card_list[0:ret], card_list[ret:ret + 17], card_list[ret + 17:]


def getPassWorld(ret):
    all_charts = list(string.ascii_letters + string.digits)  # 将字母、数字转为list
    random.shuffle(all_charts)  # 打乱顺序
    return "".join(all_charts[0:ret])


def getPassWorldV2(ret):
    all_charts = list(string.ascii_letters + string.digits)  # 将字母、数字转为list
    return "".join(random.sample(all_charts, ret))  # 打乱顺序


if __name__ == '__main__':
    print(getFinalList(35, 7))
    print(getFinalListV2(35, 7))
    for i in getFinalCards(17):
        print(i)
    print(getPassWorld(7))
    print(getPassWorldV2(7))
