# coding = utf-8
# --*-- coding:utf-8 --*--
# python3

'''
功能：拆分每月薪资表，给每个员工单独创建表格

表格样式：
    # 需合并单元格
    A1:AC1  公司名称
    A2:AC2  年月
    A3:B3   空白
    C3:C4   当前工资合计, hidden
    D3:L3   应发工资
    M3:Q3   社保、公积金个人扣款
    R3:R4   税前工资
    S3:S4   个人所得税
    T3:T4   实发工资
    U3:AA3  公司承担社保、公积金费用
    AB3:AB4 前锦管理费
    AC3:AC4 人力成本合计

    # 不需合并单元格
    A4:     姓名
    B4:     入职日期
    D4:     基本工资
    E4:     加班工资
    F4:     保密费
    G4:     交通通讯房租补贴
    H4:     地区补助
    I4:     绩效工资
    J4:     缺勤天数, hidden
    K4:     缺勤扣款
    L4:     小计
    M4:     养老
    N4:     医保
    O4:     失保
    P4:     公积金
    Q4:     小计
    U4:     养老
    V4:     医保
    W4:     失保
    X4:     生育
    Y4:     工伤
    Z4:     公积金
    AA4:    小计

'''

import xlsxwriter   # 写入excel
import xlrd         # 读取源文件
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import formatdate
from email import encoders
import os



def wExcel(temp_filepath, user_info):
    ''''接受员工信息，然后拆分独立表单'''

    row = 4
    ncols = 30

    wb_name = temp_filepath + user_info[0] + '的工资单.xlsx'

    # 初始化新增员工薪资表格
    workbook = xlsxwriter.Workbook(wb_name)
    # workbook = xlsxwriter.Workbook('merge2.xlsx')
    worksheet = workbook.add_worksheet(user_info[0])
    worksheet.set_column('A:AD', 13)
    worksheet.set_column('D:D',None,None,{'hidden':True})
    worksheet.set_column('K:K',None,None,{'hidden':True})

    '''表格样式'''
    # 标题格式
    format01 = workbook.add_format({
        'font_name': '微软雅黑',
        'bold':     True,
        'border':   1,
        'align':    'center',
        'valign':   'vcenter',
        'font_size': 16,

    })

    # 类别格式
    format02 = workbook.add_format({
        'font_name': '微软雅黑',
        'bold':     True,
        'italic':   True,
        'border':   1,
        'align':    'center',
        'valign':   'vcenter',
        'font_size': 11,
    })

    # 内容格式
    format03 = workbook.add_format({
        'font_name': '微软雅黑',
        'bold':     True,
        'border':   1,
        'align':    'center',
        'valign':   'vcenter',
        'font_size': 9,
    })


    # 需要合并的单元格
    worksheet.merge_range('A1:AD1', '某大型互联网公司', format01)
    worksheet.merge_range('A2:AD2', '2017年5月', format02)
    worksheet.merge_range('A3:C3 ', '', format03)
    worksheet.merge_range('D3:D4 ', '当前工资合计', format03)
    worksheet.merge_range('E3:M3 ', '应发工资', format03)
    worksheet.merge_range('N3:R3 ', '社保、公积金个人扣款', format03)
    worksheet.merge_range('S3:S4 ', '税前工资', format03)
    worksheet.merge_range('T3:T4 ', '个人所得税', format03)
    worksheet.merge_range('U3:U4 ', '实发工资', format03)
    worksheet.merge_range('V3:AB3', '公司承担社保、公积金费用', format03)
    worksheet.merge_range('AC3:AC4 ', '前锦管理费', format03)
    worksheet.merge_range('AD3:AD4 ', '人力成本合计', format03)

    # 不需要合并的单元格
    worksheet.write('A4', '姓名', format03)
    worksheet.write('B4', '邮箱', format03)
    worksheet.write('C4', '入职日期', format03)
    worksheet.write('E4', '基本工资', format03)
    worksheet.write('F4', '加班工资', format03)
    worksheet.write('G4', '保密费', format03)
    worksheet.write('H4', '交通通讯房租补贴', format03)
    worksheet.write('I4', '地区补助', format03)
    worksheet.write('J4', '绩效工资', format03)
    worksheet.write('K4', '缺勤天数', format03)
    worksheet.write('L4', '缺勤扣款', format03)
    worksheet.write('M4', '小计', format03)
    worksheet.write('N4', '养老', format03)
    worksheet.write('O4', '医保', format03)
    worksheet.write('P4', '失保', format03)
    worksheet.write('Q4', '公积金', format03)
    worksheet.write('R4', '小计', format03)
    worksheet.write('V4', '养老', format03)
    worksheet.write('W4', '医保', format03)
    worksheet.write('X4', '失保', format03)
    worksheet.write('Y4', '生育', format03)
    worksheet.write('Z4', '工伤', format03)
    worksheet.write('AA4', '公积金', format03)
    worksheet.write('AB4', '小计', format03)

    for col in range(ncols):
        worksheet.write(row, col, user_info[col],format03)
    # 保存文件
    workbook.close()

    return wb_name

def sendmail(temp_file, user_mail):

    filename = format(os.path.basename(temp_file))

    msg = MIMEMultipart()

    text = '本邮件为自动发送，若有任何疑问请与人事部联系，谢谢！'
    part = MIMEText(text, 'plain', _charset='utf-8')
    msg.attach(part)

    att = MIMEMultipart(open(temp_file, 'rb').read(), 'base64', 'gb2312')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=%s' % filename
    msg.attach(att)

    msg['From'] = 'lucj@visionet.com.cn'
    msg['To'] = user_mail
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = '工资表'


    smtp = smtplib.SMTP('smtp.263.net')
    smtp.login('lucj@visionet.com.cn','Lcj921010')
    smtp.sendmail('lucj@visionet.com.cn', user_mail, msg.as_string())
    smtp.quit()


# 请在这里添加源表格
sourcefile = '/Users/Alex/GitHub/myPythonCodes/salary_table_to_single_person/money.xlsx'
temp_filepath = '/Users/Alex/tmp/'

# 加载表格和表格
wb = xlrd.open_workbook(sourcefile)
ws = wb.sheets()[0]
nrows = ws.nrows

for row in range(4,nrows):
    user_info = ws.row_values(row)
    temp_file = wExcel(temp_filepath, user_info)
    print(format(os.path.basename(temp_file)))
    # print(temp_file)
    user_mail = user_info[1]
    sendmail(temp_file, user_mail)
