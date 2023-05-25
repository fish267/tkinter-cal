# !/usr/bin/env python
# -*-coding:utf-8 -*-
import csv
import random

"""
# File       : exam_plan.py
# Time       ：2023/5/25 17:30
# Author     ：shiheng.fsh
# version    ：python 3.6
# Description：考场安排脚本
"""


def random_sample(n):
    ret = ''
    for ele in random.sample('abcdefghijklmnopqrstuvwxyz', n):
        ret += ele
    return ret


def generate_name_list(examiner_count):
    '''
    生成测试数据用的，模拟名单
    :param examiner_count: 每个单位考官数量
    :return: 生成名单 examiner_list.csv
    '''

    header = ('编号', '类型', '性别', '姓名', '单位', '部职别', '电话')
    with open('examiner_list.csv', 'w') as f:
        examiner_file = csv.writer(f)
        examiner_file.writerow(header)
        # 定义好每列的变量
        code, examiner_type, sex, name, company, company_detail, tel = '', '', '', '', '', '', ''
        # 3个单位, 随机生成数据, 30%主考, 至少6个女的
        for i in range(3):
            for k in range(examiner_count):
                if k % 3 == 0:
                    examiner_type = '主考'
                else:
                    examiner_type = '监考'
                if k < 6:
                    sex = '女'
                else:
                    sex = '男'
                name = '姓名' + random_sample(5)
                company = '单位' + str(i)
                company_detail = company + random_sample(7)
                tel = '186' + random_sample(6)
                code = str(i) + str(k)
                row_detail = (code, examiner_type, sex, name, company, company_detail, tel)
                examiner_file.writerow(row_detail)
                print(row_detail)


def pick_main_examinor(name_list_detail, exam_plan_detail, input_examiner_type, input_sex, main_examinor=None,
                       sub_examinor=None):
    '''
    选主考官
    :param name_list_detail:  内存中的名单
    :param exam_plan_detail:  考场计划安排
    :return:
    '''

    candidate_group = []
    for ele in name_list_detail:
        code, examiner_type, sex, name, company, company_detail, tel = ele[0], ele[1], ele[2], ele[3], ele[4], ele[5], \
                                                                       ele[6]
        if input_sex == sex and input_examiner_type == examiner_type:
            if main_examinor:
                if main_examinor[4] != company:
                    if sub_examinor:
                        if sub_examinor[4] != company:
                            candidate_group.append(ele)
                    else:
                        candidate_group.append(ele)
            else:
                candidate_group.append(ele)

    # 随机取一个元素
    pick_element = ''
    flag = True
    while flag:
        pick_element = candidate_group[random.randint(0, len(candidate_group) - 1)]
        for ele in exam_plan_detail:
            if ele[6] == pick_element[0]:
                flag = True
                break
        flag = False

    new_name_list = []
    for element in name_list_detail:
        if pick_element[0] != element[0]:
            new_name_list.append(element)

    print(pick_element)
    return pick_element, new_name_list


def generate_diff_info(main_examiner):
    print(main_examiner[6])
    return main_examiner[3], main_examiner[5], main_examiner[6][:-1], main_examiner[0]


def arrange_examination(classroom_count=52):
    '''
    针对生成的examiner_list.csv，生成考场安排表
    1. 1-42 男性考场、男监考
    2. 48-53 女性考场、女监考
    3. 每个考场，1个主考、两个监考
    4. 每个考场，考官来自3个单位
    5. 剩余的人，放到名单最后

    :param classroom_count: 考场数量
    :return: 生成 exam_plan.csv 考场安排表
    '''

    name_list_detail = []
    with open('examiner_list.csv', 'r') as name_list:
        # 读取名单中的内容，放到内存中
        for ele in name_list.readlines()[1:]:
            name_list_detail.append(ele.split(','))

    header = ('考点名称', '考场名称', '类别', '性别', '姓名', '部职别', '电话', '编号')
    exam_plan_detail = []
    with open('exam_plan.csv', 'w') as f:
        exam_plan = csv.writer(f)
        exam_plan.writerow(header)
        # 安排1-42考场
        location_name, examination_name, examiner_type, sex, name, company_detail, tel, code = '', '', '', '', '', '', '', ''
        for index in range(1, 43):
            location_name = '大连考点-男'
            if index < 10:
                examination_name = 'A0' + str(index)
            else:
                examination_name = 'A' + str(index)
            sex = '男'

            examiner_type = '主考'
            main_examiner, name_list_detail = pick_main_examinor(name_list_detail, exam_plan_detail, examiner_type, sex)
            name, company_detail, tel, code = generate_diff_info(main_examiner)
            exam_plan_detail.append(main_examiner)
            insert_row = (location_name, examination_name, examiner_type, sex, name, company_detail, tel, code)
            exam_plan.writerow(insert_row)

            examiner_type = '监考'
            sub_examiner, name_list_detail = pick_main_examinor(name_list_detail, exam_plan_detail, examiner_type, sex,
                                                                main_examiner)
            exam_plan_detail.append(sub_examiner)
            name, company_detail, tel, code = generate_diff_info(sub_examiner)
            insert_row = (location_name, examination_name, examiner_type, sex, name, company_detail, tel, code)
            exam_plan.writerow(insert_row)

            sub_sub_examiner, name_list_detail = pick_main_examinor(name_list_detail, exam_plan_detail, examiner_type,
                                                                    sex, main_examiner,
                                                                    sub_examiner)
            exam_plan_detail.append(sub_sub_examiner)
            name, company_detail, tel, code = generate_diff_info(sub_sub_examiner)

            insert_row = (location_name, examination_name, examiner_type, sex, name, company_detail, tel, code)
            exam_plan.writerow(insert_row)
            print(index)

        for index in range(48, 54):
            location_name = '大连考点-女'
            if index < 10:
                examination_name = 'A0' + str(index)
            else:
                examination_name = 'A' + str(index)
            sex = '女'

            examiner_type = '主考'
            main_examiner, name_list_detail = pick_main_examinor(name_list_detail, exam_plan_detail, examiner_type, sex)
            name, company_detail, tel, code = generate_diff_info(main_examiner)
            exam_plan_detail.append(main_examiner)
            insert_row = (location_name, examination_name, examiner_type, sex, name, company_detail, tel, code)
            exam_plan.writerow(insert_row)

            examiner_type = '监考'
            sub_examiner, name_list_detail = pick_main_examinor(name_list_detail, exam_plan_detail, examiner_type, sex,
                                                                main_examiner)
            exam_plan_detail.append(sub_examiner)
            name, company_detail, tel, code = generate_diff_info(sub_examiner)
            insert_row = (location_name, examination_name, examiner_type, sex, name, company_detail, tel, code)
            exam_plan.writerow(insert_row)

            sub_sub_examiner, name_list_detail = pick_main_examinor(name_list_detail, exam_plan_detail, examiner_type,
                                                                    sex, main_examiner,
                                                                    sub_examiner)
            exam_plan_detail.append(sub_sub_examiner)
            name, company_detail, tel, code = generate_diff_info(sub_sub_examiner)

            insert_row = (location_name, examination_name, examiner_type, sex, name, company_detail, tel, code)
            exam_plan.writerow(insert_row)
            print(index)

        exam_plan.writerow('后补名单列表明细')

        for name_detail in name_list_detail:
            insert_backup_flag = True
            for plan_detail in exam_plan_detail:
                if plan_detail[-1] == name_detail[0]:
                    insert_backup_flag = False
                    break
            if insert_backup_flag:
                name_detail[6] = name_detail[6][:-1]
                name_detail.append('__')
                exam_plan.writerow(name_detail)


if __name__ == '__main__':
    # generate_name_list(60)

    arrange_examination()
