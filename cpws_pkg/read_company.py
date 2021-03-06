# coding=utf-8
import datetime


def read_company1(csv):
    company_list = []
    with open(csv, 'r') as f:
        c_list = f.readlines()
    for c in c_list:
        com = c.strip()
        if com:
            com_list = com.split(',')
            try:
                company = com_list[2]
            except Exception as e:
                with open('log/cp_log.log', 'a') as f:
                    now = str(datetime.datetime.now())
                    f.write(now + ',' + str(e) + ',' + '' +',' + '\n')
                continue
            company_list.append(company)
    return company_list


def read_company2(csv):
    company_list = []
    num = 1
    with open(csv, 'rb') as f:
        c_list = f.readlines()
    for c in c_list:
        company = c.decode("gbk").strip()
        if company:
            company_list.append(company)
        num +=1
    return company_list

if __name__ == '__main__':
    # read_company1('company/监理类公司.csv')
    read_company2("E:\zhy-数据\company_list\hunan_company.csv")
