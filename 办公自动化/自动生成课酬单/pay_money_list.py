from  xlutils.copy import copy
import xlrd
import xlwt
import os

path_i = os.getcwd()
path = path_i. replace('\\','/')+'/'
pathout=path+'生成的文件/'
source_file='课酬单模板.xls'
source_data='000需制作的数据.xls'
source_base='001授课人信息数据库.xls'

##读取数据来源文件
data_excel=xlrd.open_workbook(path+source_data)
table=data_excel.sheet_by_index(0)
all_data=[]

####读取人员身份证号等具体信息
person_excel=xlrd.open_workbook(path+source_base)
person_table=person_excel.sheet_by_index(0)
person_data=[]


def write_excel(teacher_name,class_name,date_time,lesson_name,money_num,p_job,p_bank,bank_num,id_num):
    #读取格式模板文件
    tem_excel=xlrd.open_workbook(path+source_file,formatting_info=True)
    # tem_sheet=tem_excel.sheet_by_index(0)
    ###设置格式
    style=xlwt.XFStyle()
    ##字体
    font=xlwt.Font()
    font.name='仿宋_GB2312'
    font.bold=False
    font.height=240  #字体大小x20
    style.font=font
    ##边框
    borders=xlwt.Borders()
    borders.top=xlwt.Borders.THIN
    borders.bottom=xlwt.Borders.THIN
    borders.left=xlwt.Borders.THIN
    borders.right=xlwt.Borders.THIN
    style.borders=borders
    ##对齐
    alignment=xlwt.Alignment()
    alignment.horz=xlwt.Alignment.HORZ_CENTER
    alignment.vert=xlwt.Alignment.VERT_CENTER
    alignment.wrap=1
    style.alignment=alignment

    #写入

    new_excel=copy(tem_excel)
    new_sheet=new_excel.get_sheet(0)

    #写入四个内容
    new_sheet.write(4,1,teacher_name,style)
    new_sheet.write(1,1,class_name,style)
    new_sheet.write(2,1,date_time,style)
    new_sheet.write(3,1,lesson_name,style)
    new_sheet.write(5,1,money_num,style)
    new_sheet.write(6,3,'\''+bank_num,style)  #避免excel自动将长数字串变格式
    new_sheet.write(7,1,p_bank,style)
    new_sheet.write(7,3,'\''+id_num,style)
    #继续写入身份证号，开户行及卡号。



    #保存文件

    new_excel.save(pathout+teacher_name+date_time+'.xls')
    print(pathout+teacher_name+date_time+'.xls'+'生成完毕')

def read_source(nrows_num):
    for n in range(1,nrows_num):
        class_name=table.cell_value(n,0)
        date_time=table.cell_value(n,1)
        teacher_name=table.cell_value(n,2)
        lesson_name=table.cell_value(n,3)
        money_num=table.cell_value(n,4)
        # print(class_name,date_time,teacher_name,lesson_name,money_num)
        data={
            'class_name':class_name,
            'date_time':date_time,
            'teacher_name':teacher_name,
            'lesson_name':lesson_name,
            'money_num':money_num,
        }
        all_data.append(data)
        # write_excel(teacher_name,class_name,date_time,lesson_name,money_num)

def read_person(rows_num):
    for n in range(1,rows_num):
        p_name=person_table.cell_value(n,0)
        p_job=person_table.cell_value(n,1)
        p_bank=person_table.cell_value(n,2)
        bank_num=person_table.cell_value(n,3)
        id_num=person_table.cell_value(n,4)
        # print(p_name,p_job,p_bank,bank_num,id_num)
        p_data={
        "p_name":p_name,
        "p_job":p_job,
        "p_bank":p_bank,
        "bank_num":bank_num,
        "id_num":id_num,
        }
        person_data.append(p_data)
read_source(table.nrows)
read_person(person_table.nrows)


for i in all_data:
    p_job=" "
    p_bank=" "
    bank_num=" "
    id_num= " "
    for j in person_data:
        if i['teacher_name']==j['p_name']:
            p_job=j['p_job']
            p_bank=j['p_bank']
            bank_num=j['bank_num']
            id_num= j['id_num']
        else:
            pass
    if id_num==" ":
        print (i['teacher_name']+'缺少身份证信息等数据')
    else:
        print(i['teacher_name']+'数据完整，生成课酬单完毕')
    write_excel(i['teacher_name'],i['class_name'],i['date_time'],i['lesson_name'],i['money_num'],p_job,p_bank,bank_num,id_num)




# print (all_data)
# print(person_data)
# print(class_name,date_time,teacher_name,lesson_name,money_num)
# print(p_name,p_job,p_bank,bank_num,id_num)



# print(person_data[0]["p_name"])
'''
取得每一个teacher_name后，都去和person_data数组里包含的字典的p_name字段匹配，
如果一致，就读取字典的条内容。
如果匹配不成功，就返回空格。
if teacher_name in person_data.values():
    print(list(person_data.keys())[list(person_data.values()).index(teacher_name)])
else:
    print('你要查询的值'+get_value+'不存在')

'''