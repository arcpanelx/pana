#__Author__: Panax Wong
# encoding utf=8
# 定义展示系统功能的函数
def showUI():
    print("= " * 8,end="")
    print("  学员管理系统  ",end="")
    print("= " * 8,end="")
    print("")
    print(" 1.查看学员信息  ",end="")
    print(" 2.添加学员信息   ",end="")
    print(" 3.删除学员信息")
    print(" 4.修改学员信息  ",end="")
    print(" 5.退出管理系统",)
    print("= " * 23)

# 定义一个列表，用来存储学员信息
students = []

while True:
    # 展示可选择的功能
    showUI()

    # 提示用户进行功能选择
    key = input("请选择功能数字序号：")

    # 根据用户选择，运行相关功能
    if key == "1":
        print("您选择了查看学员信息")
        # 输出学员信息
        print("- " * 23)
        print("|id      |name       |age        |classid")
        for temp in students:
            print("%s      %s        %s         %s" % (temp['id'], temp['name'], temp['age'], temp['classid']))
        print("- " * 23)
    elif key == "2":
        print("您选择了添加学员信息功能")
        id = input("请输入学员学号(学号不可重复)：")
        name = input("请输入学员姓名：")
        age = input("请输入学员年龄:")
        classid = input("请输入学员的班级:")

        # 验证学号是否唯一
        i = 0
        leap = 0
        for temp in students:
            if temp['id'] == id:
                leap = 1
                break
            else:
                i = i + 1
        if leap == 1:
            print("您输入学号重复，添加失败！")
            break
        else:
            # 定义一个字典，存放单个学员信息
            stuInfo = {}
            stuInfo['name'] = name
            stuInfo['id'] = id
            stuInfo['age'] = age
            stuInfo['classid'] = classid

            # 将单个学员信息存入列表
            students.append(stuInfo)
            print("添加成功！")
    elif key == "3":
        print("您选择了删除学员功能")
        delId = input("请输入要删除的学员学号:")
        i = 0
        leap = 0
        for temp in students:
            if temp['id'] == delId:
                leap = 1
                break
            else:
                i = i + 1
        if leap == 0:
            print("没有此学生学号，删除失败！")
        else:
            del students[i]
            print("删除成功！")

    elif key == "4":
        print("您已选择修改学员信息功能")
        alterId = input("请输入你要修改学员的学号:")
        # 检查学号是否存在，然后再修改信息
        i = 0
        leap = 0
        for temp in students:
            if temp['id'] == alterId:
                leap = 1
                break
            else:
                i = i + 1
        if leap == 1:
            while True:
                alterNum = int(input(" 1.修改学号\n 2.修改姓名 \n 3.修改年龄 \n 4.修改班级 \n 5.退出修改\n"))
                if alterNum == 1:
                    newId = input("输入更改后的学号:")
                    # 修改后的学号要验证是否唯一
                    i = 0
                    leap1 = 0
                    for temp1 in students:
                        if temp1['id'] == newId:
                            leap1 = 1
                            break
                        else:
                            i = i + 1
                    if leap1 == 1:
                        print("输入学号不可重复，修改失败！")
                    else:
                        temp['id'] = newId
                        print("学号修改成功")
                elif alterNum == 2:
                    newName = input("输入更改后的姓名:")
                    temp['name'] = newName
                    print("姓名修改成功")
                elif alterNum == 3:
                    newAge = input("输入更改后的年龄:")
                    temp['age'] = newAge
                    print("年龄修改成功")
                elif alterNum == 4:
                    newClass = input("输入更改后的班级:")
                    temp['classid'] = newClass
                    print("班级修改成功")
                elif alterNum == 5:
                    break
                else:
                    print("输入错误请重新输入")
        else:
            print("没有此学号，修改失败！")
    elif key == "5":
        # 退出功能
        quitconfirm = input("亲，真的要退出么？😭~~(>_<)~~😭（请回复yes或者no）")
        if quitconfirm == 'yes':
            print("您已退出本系统，欢迎下次再次使用，谢谢")
            break;
        else:
            print("您输入的信息有误，请核实！")

    else:
        print("您再瞅瞅，输入的东东有误吧，要输入的是1到5的数字，本系统才支持哦")




