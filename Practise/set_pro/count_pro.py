from collections import Counter


def getCount(content_str):
    return Counter(content_str)


def getWordCount(content_str):
    count_dict = {}
    content_list = content_str.split(" ")
    for word in content_list:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict


if __name__ == '__main__':
    content = input("请输入要统计的内容:\n")
    print(getWordCount(content))
