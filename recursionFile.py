"""
    function: 遍历目录，返回目录结构的 list
"""

import os


def scanpath(filepath, suffix):
    file_list = []
    print("开始扫描【{0}】".format(filepath))
    if not os.path.isdir(filepath):
        print("【{0}】不是目录".format(filepath))
        exit(-1)
    for filename in os.listdir(filepath):
        if os.path.isdir(filepath + "/" + filename):
            file_list.extend(scanpath(filepath + "/" + filename, suffix))
        elif filename.endswith(suffix):
            sub_filename = filepath + '/' + filename
            file_list.append(sub_filename)
            print(sub_filename)
    return file_list
