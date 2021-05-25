# 综合联系
'''
王者荣耀角色管理
'''
import time

print(str)
all_role = []  # 存放所有角色
print("~~~~~~~~~~~~欢迎进入王者荣耀角色管理~~~~~~~~~~~~~")
while True:
    choice = input("请选择功能:\n 1:添加角色 \n 2.删除角色 \n 3:修改角色 \n 4.查询角色 \n 5：显示所有角色 \n 6.退出系统 \n")
    # 判断
    if choice == '1':
        print('添加角色模块~~\n')
        name = input('\t角色名：')
        sex = input("\t性别：")
        job = input("\t工作：")
        # 添加到all_role
        role = [name, sex, job]
        all_role.append(role)
        print("成功添加{}到王者荣耀系统".format(name))
    elif choice == '2':
        print("删除角色模块：")
        role_name = input("输入一个角色名称:")
        for role in all_role:
            if (role[0] == role_name):
                while True:
                    sfDel = input('是否删除{}角色：Y/N:'.format(role_name))
                    if sfDel == 'Y':
                        all_role.remove(role)
                        print('删除成功')
                        break
                        pass
                    else:
                        print("取消删除");
                        break
                        pass
                pass
            pass
        else:
            print("本系统不存在{},请重新输入\n".format(role_name))
        # print("删除成功")
        # break
    elif choice == '3':
        print("修改模块：")
        role_name = input("请输入一个角色名：")
        for everyRole in all_role:
            if everyRole[0] == role_name:
                sex = input("请输入性别：")
                job = input("请输入职业：")
                while True:
                    isEdit = input("确认修改吗？Y/N:")
                    if isEdit == "Y":
                        everyRole[1] = sex
                        everyRole[1] = job
                        print("修改成功!")
                        break
                        pass
                    else:
                        print("取消成功!")
                        break
                        pass
                    pass
                pass
            pass
        else:
            print("未查询到您输入的角色")
    elif choice == '4':
        print("开始查询角色~~~")
        role_name = input("请输入角色名称：")
        for role in all_role:
            if role_name in role:
                print('{}{}{}'.format('名称'.center(10), '性别'.center(10), '职业'.center(10)))
                print(role[0].center(10), end='')
                print(role[1].center(10), end='')
                print(role[2].center(10), end='')
                print('\n')
                print("查询完成")
                break
                pass
        else:
            print("未查找到{}".format(role_name))

    elif choice == '5':
        print('显示所有角色模块')
        print('{}{}{}'.format('名称'.center(10), '性别'.center(10), '职业'.center(10)))
        for role in all_role:
            print(role[0].center(10), end='')
            print(role[1].center(10), end='')
            print(role[2].center(10), end='')
            print('\n')
    elif choice == '6':
        print("正在退出王者荣耀~~~")
        time.sleep(3)
        print("退出成功")
        break
        pass
    else:
        print('输入错误，请重新选择！')
