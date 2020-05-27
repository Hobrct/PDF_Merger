import os
import fitz


def merge(name, pdf_file):  # 合并pdf
    pdfout = fitz.open(pdf_file[0])
    toc = [[1, pdf_file[0].split(".")[0], 1]]  # 目录
    for pdf in pdf_file[1:]:
        p = fitz.open(pdf)
        toc.append([1, pdf.split(".")[0], len(pdfout) + 1])
        pdfout.insertPDF(p)
        pdftocs = p.getToC()
        for pdftoc in pdftocs:
            pdftoc[0] += 1  # 原pdf目录级数加一
            toc.append(pdftoc)
        pdfout.setToC(toc)
    pdfout.save(name + '.pdf')
    print("输出到{}".format(os.getcwd() + '\\' + name + '.pdf'))


def display_pdf_file(pdf_file):  # 显示pdf文件
    print("该目录下的pdf文件：")
    for i in range(len(pdf_file)):
        print('[{}]{}'.format(i + 1, pdf_file[i]))


if __name__ == "__main__":  # 主函数
    dirs = os.listdir('./')
    print('请选择要合并的pdf文件夹：')
    for i in range(len(dirs)):
        print('[{}]{}'.format(i + 1, dirs[i]))
    d = dirs[int(input()) - 1]
    try:
        os.chdir(d)
    except IOError as e:
        print("出现错误！" + e)
        print("该文件可能不为文件夹。")
    dirs = os.listdir('./')
    pdf_file = []
    for file in dirs:
        if file.split('.')[1] == 'pdf':
            pdf_file.append(file)
    display_pdf_file(pdf_file)

    while 1:  # 开始操作输入循环
        print("请输入要进行的操作：")
        print("[0]开始合并")
        print("[1]调换顺序")
        print("[2]插入位置")
        print("[3]移出列表")
        print("[4]文件名截取")
        index = int(input())
        if index == 0:  # 合并
            merge(input("请输入输出pdf的文件名"), pdf_file)
            break
        elif index == 1:  # 调换
            a = int(input("请输入序号一："))
            b = int(input("请输入序号二："))
            a = a - 1
            b = b - 1
            if 1 <= a <= len(pdf_file) and 1 <= b <= len(pdf_file):
                temp = pdf_file[a]
                pdf_file[a] = pdf_file[b]
                pdf_file[b] = temp
                display_pdf_file(pdf_file)
            else:
                print("序号溢出")
        elif index == 2:  #  插入
            a = int(input("请输入要更换位置的序号："))
            b = int(input("请输入要插入的位置序号"))
            if 1 <= a <= len(pdf_file) and 1 <= b <= len(pdf_file):
                pdf_file.insert(b - 1, pdf_file.pop(a - 1))
                display_pdf_file(pdf_file)
            else:
                print("序号溢出")
        elif index == 3:  # 移除
            a = int(input("请输入要移除的文件序号："))
            if 1 <= a <= len(pdf_file):
                pdf_file.pop(a - 1)
                display_pdf_file(pdf_file)
            else:
                print("序号溢出")
        elif index == 4:  # 截取
            print("请输入截取形式，格式为：前/后+数字")
            print("例如，前3表示截去前面三位字符")
            a = input()
            b = int(input("请输入截取的开始序号："))
            c = int(input("请输入截取的结束序号："))
            if 1 <= b <= len(pdf_file) and 1 <= c <= len(pdf_file):
                if a[0] == "前":
                    for i in range(b - 1, c):
                        os.rename(pdf_file[i], pdf_file[i][int(a[1]):])
                        pdf_file[i] = pdf_file[i][int(a[1]):]
                    display_pdf_file(pdf_file)
                elif a[0] == "后":
                    for i in range(b - 1, c):
                        os.rename(pdf_file[i], pdf_file[i][:-int(a[1])] - 4)
                        pdf_file[i] = pdf_file[i][:-int(a[1]) - 4]
                    display_pdf_file(pdf_file)
                else:
                    print("输入有误")
            else:
                print("序号溢出")
