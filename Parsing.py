from bs4 import BeautifulSoup
import pandas as pd


def get_table(path):
    # 设置网页地址
    urls = path + '\\武汉大学教务系统_files\\Svlt_QueryStuScore.html'
    # 解析网页
    wb_data = open(urls, 'r').read()
    soup = BeautifulSoup(wb_data, 'lxml')
    # 找到成绩表格
    soup_table = soup.find_all('table')[0]
    # 找到成绩表
    soup_scores = soup_table.find_all('tr')[1:];

    # 课程名 课程类型 通识课类型 课程属性 学分 教师名 授课学院 学习类型 学年 学期 成绩
    names = []
    types = []
    general_types = []
    general_attrs = []
    credit = []
    teachers = []
    faculties = []
    learn_types = []
    years = []
    semesters = []
    scores = []
    # 处理统计每一条成绩
    for soup_score in soup_scores:
        cols = soup_score.find_all("td");
        # 获取课程名
        names.append(cols[0].text.strip(' '))
        # 获取课程类型
        types.append(cols[1].find("span").get_text())
        # 获取通识课类型
        general_types.append(cols[2].get_text())
        # 获取课程属性
        if cols[3].find("span"):
            general_attrs.append(cols[3].find("span").get_text().strip(' '))
        else:
            general_attrs.append('')
        # 获取学分
        credit.append(cols[4].get_text())
        # 获取教师名
        teachers.append(cols[5].get_text())
        # 获取授课学院
        faculties.append(cols[6].get_text())
        # 获取学习类型
        learn_types.append(cols[7].get_text())
        # 获取学年
        years.append(cols[8].get_text())
        # 获取学期
        semesters.append(cols[9].get_text())
        # 获取成绩
        scores.append(cols[10].get_text())

    dic_table = {'课程名': names, '课程类型': types, '通识课类型': general_types, '课程属性': general_attrs,
                 '学分': credit, '教师名': teachers, '授课学院': faculties, '学习类型': learn_types,
                 '学年': years, '学期': semesters, '成绩': scores}
    df_table = pd.DataFrame(dic_table)
    return df_table
