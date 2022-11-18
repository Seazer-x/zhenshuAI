import os
from rich.progress import track


# 根据文件大小排序文件，并重命名
def sortFileBySize(dirs="../"):
    files_size = []
    files_list = []
    for top, down, files in os.walk(dirs):
        for item in track(description="[bold blue]Checking", sequence=files):
            if item.startswith("._"):
                os.remove(os.path.join(top, item))
                continue
            file_size = os.path.getsize(dirs + "/" + item)
            files_size.append(file_size)
            files_list.append(item)
    file_dict = dict(zip(files_list, files_size))
    sorted_file = sorted(file_dict.items(), key=lambda kv: (kv[1], kv[0]))
    index = 0
    for name, _ in track(description="[bold blue]Renaming", sequence=sorted_file):
        os.rename(dirs + "/" + name, dirs + "/" + str(index + 1) + "_" + name)
        index += 1


def delUselessFile(dirs="../"):
    for top, down, files in os.walk(dirs):
        for item in files:
            if item.startswith("._"):
                os.remove(os.path.join(top, item))
                continue


delUselessFile("/Volumes/Mac-vm/zhenshuAI")
# sortFileBySize("../fileTest")
