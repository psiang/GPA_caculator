import Calculating
import Parsing

if __name__ == '__main__':
    # 目标路径
    path = '.\\source\\武汉大学教务系统_files'
    # 解析网页获取表格
    score_table = Parsing.get_table(path)
    # 计算平均GPA
    GPA_table = Calculating.calculate(score_table)
    print(GPA_table)