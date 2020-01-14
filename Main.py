import Parsing

if __name__ == '__main__':
    # 目标路径
    path = '.\\source\\武汉大学教务系统_files'
    # 解析网页获取表格
    table = Parsing.get_table(path)
    print(table)