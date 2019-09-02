import os

import xlrd
import xlwt
from xlutils.copy import copy

path_i = os.getcwd()
path = path_i. replace('\\','/')+'/'
pathout=path+'生成的文件/'
#path='D:/py/py办公自动化/py操作excel/'
source_file='评教表excel模版.xls'
source_data='000需制作数据.xls'


##读取数据来源文件
data_excel=xlrd.open_workbook(path+source_data)
table=data_excel.sheet_by_index(0)
#all_data=[]

def write_excel(teacher_name,class_name,date_time,lesson_name):
    #读取格式模板文件
    tem_excel=xlrd.open_workbook(path+source_file,formatting_info=True)
    # tem_sheet=tem_excel.sheet_by_index(0)
    ###设置格式
    style=xlwt.XFStyle()
    ##字体
    font=xlwt.Font()
    font.name='仿宋_GB2312'
    font.bold=False
    font.height=280  #字体大小x20
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
    alignment.horz=xlwt.Alignment.HORZ_LEFT
    alignment.vert=xlwt.Alignment.VERT_CENTER
    alignment.wrap=1
    style.alignment=alignment

    #写入

    new_excel=copy(tem_excel)
    new_sheet=new_excel.get_sheet(0)

    #写入四个内容
    new_sheet.write(1,1,teacher_name,style)
    new_sheet.write(1,4,class_name,style)
    new_sheet.write(1,8,date_time,style)
    new_sheet.write(2,1,lesson_name,style)
    #保存文件

    new_excel.save(pathout+teacher_name+date_time+'.xls')
    print(pathout+teacher_name+date_time+'.xls'+'生成完毕')

for n in range(1,table.nrows):
    class_name=table.cell_value(n,0)
    date_time=table.cell_value(n,1)
    teacher_name=table.cell_value(n,2)
    lesson_name=table.cell_value(n,3)
    #print(class_name,date_time,teacher_name,lesson_name)
    #data={'class_name':class_name,'date_time':date_time,'teacher_name':teacher_name,'lesson_name':lesson_name}
    #all_data.append(data)
    write_excel(teacher_name,class_name,date_time,lesson_name)
