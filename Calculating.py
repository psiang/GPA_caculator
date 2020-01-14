import types
import pandas as pd


def get_gpa(x):
    if type(x) is not float:
        x = float(x)
    if x >= 90:
        return 4.0
    elif x >= 85:
        return 3.7
    elif x >= 82:
        return 3.3
    elif x >= 78:
        return 3.0
    elif x >= 75:
        return 2.7
    elif x >= 72:
        return 2.3
    elif x >= 68:
        return 2.0
    elif x >= 64:
        return 1.5
    elif x >= 60:
        return 1.0
    else:
        return 0


def calculate(table):
    # '专业必修', '专业选修', '公共必修', '公共选修', '总分'
    zb = [0.0, 0.0, 0.0]
    zx = [0.0, 0.0, 0.0]
    gb = [0.0, 0.0, 0.0]
    gx = [0.0, 0.0, 0.0]
    zf = [0.0, 0.0, 0.0]
    for index, row in table.iterrows():
        # 出了成绩才计入，根据分类进行累加
        if row['成绩'] != '':
            credit = float(row['学分'])
            gpa = get_gpa(row['成绩'])
            score = float(row['成绩'])
            zf[0] += credit
            zf[1] += gpa * credit
            zf[2] += score * credit
            if row['课程类型'] == '专业必修':
                zb[0] += credit
                zb[1] += gpa * credit
                zb[2] += score * credit
            elif row['课程类型'] == '专业选修':
                zx[0] += credit
                zx[1] += gpa * credit
                zx[2] += score * credit
            elif row['课程类型'] == '公共必修' or row['课程类型'] == '通识教育必修':
                gb[0] += credit
                gb[1] += gpa * credit
                gb[2] += score * credit
            elif row['课程类型'] == '公共选修' or row['课程类型'] == '通识教育选修':
                gx[0] += credit
                gx[1] += gpa * credit
                gx[2] += score * credit
    # 除去分母算平均
    if zf[0] != 0:
        zf[1] /= zf[0]
        zf[2] /= zf[0]
    if zb[0] != 0:
        zb[1] /= zb[0]
        zb[2] /= zb[0]
    if zx[0] != 0:
        zx[1] /= zx[0]
        zx[2] /= zx[0]
    if gb[0] != 0:
        gb[1] /= gb[0]
        gb[2] /= gb[0]
    if gx[0] != 0:
        gx[1] /= gx[0]
        gx[2] /= gx[0]
    # 生成表格返回
    list_table = [zb, zx, gb, gx, zf]
    df_table = pd.DataFrame(list_table, columns=['学分', '平均GPA', '平均分'],
                            index=['专业必修', '专业选修', '公共必修', '公共选修', '合计总分'])
    return df_table
