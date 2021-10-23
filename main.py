@@ -12,13 +12,12 @@
len_bag_randint = random.randint(2,len(bag))  目的是为了取数，生成1个符号的式子，需要2个数，
生成3个运算符的式子需要4个数
create_expression函数目前只能生成整数式子，没有判断功能：判断式子是否合法——结果负值，除法有0等，只能简单生成式子
create_expression函数目前只能生成整数、真分数、带分数式子
'''


def create_expression(erange=10):
    operator = [' + ', ' - ', ' * ', ' / ']  # 符号
    end_operator = ' ='
    equation = ''  # 初始式子，为空
    bag = []  # 为随机数的空列表，随机从里面取字
    nature_step = random.randrange(1, 3)  # 随机数的间隔
@@ -32,19 +31,19 @@ def create_expression(erange=10):
        fraction_number = molecule / denominator
        fraction_number = Fraction('{}'.format(fraction_number)).limit_denominator()  # 小数转换为真分数
        bag.append(str(fraction_number))
        for i in range(4):
            denominator2 = random.randrange(1, 10)  # 分母
            molecule2 = random.randrange(1, 10)  # 分子
            denominator2, molecule2 = max(denominator2, molecule2), min(denominator2, molecule2)  # 比较大小同时交换
            fraction_number2 = denominator2 / molecule2
            fraction_number2 = Fraction('{}'.format(fraction_number2)).limit_denominator()  # 小数转换为真分数
            int_t = int(fraction_number2)
            los_t = fraction_number2 - int_t
            if (int_t != 0 and los_t != 0):
                fi_t = str(str(int_t) + "'" + str(los_t))
            else:
                fi_t = str(fraction_number2)
            bag.append(fi_t)
    for i in range(4):
        denominator2 = random.randrange(1, 10)  # 分母
        molecule2 = random.randrange(1, 10)  # 分子
        denominator2, molecule2 = max(denominator2, molecule2), min(denominator2, molecule2)  # 比较大小同时交换
        fraction_number2 = denominator2 / molecule2#对调分子分母位置以生成带分数
        fraction_number2 = Fraction('{}'.format(fraction_number2)).limit_denominator()  # 小数转换为真分数
        int_t = int(fraction_number2)
        los_t = fraction_number2 - int_t
        if (int_t != 0 and los_t != 0):
            fi_t = str(str(int_t) + "'" + str(los_t))
        else:
            fi_t = str(fraction_number2)
        bag.append(fi_t)
    len_bag_randint = random.randrange(2, 4)
    # print(len_bag_randint)
    for i in range(len_bag_randint):
@@ -53,8 +52,6 @@ def create_expression(erange=10):
        equation += bag[randint_number]
        if i < len_bag_randint - 1:
            equation += operator[randint_number % len(operator)]
        # else:
        # equation += end_operator
        bag.pop(randint_number)
    return equation

@@ -206,8 +203,33 @@ def main():
            print("[-]文件扩展名有误或路径有误！")
            print('[-]exiting')
            return

    '''测试用
    t1 = time.time()
    to_file(need=10000, erange=10)
    check_answer(e_fliepath="Exercises.txt", a_filepath="Answers.txt")
    t2= time.time()
    print('Execute time: %.2f' %(t2-t1))
    '''

'''
opt():
argparse是一个Python模块：命令行选项、参数和子命令解析器。
argparse模块可以让人轻松编写用户友好的命令行接口。
程序定义它需要的参数，然后argparse将弄清楚如何从sys.argv解析出那些参数。
'''

'''
def opt():
    parser = argparse.ArgumentParser()
    # 设置四个选项
    parser.add_argument("-n", dest="need", help="生成数量")
    parser.add_argument("-r", dest="range", help="生成范围")
    parser.add_argument("-e", dest="grade_e", help="练习文件")
    parser.add_argument("-a", dest="grade_a", help="答案文件")
    args = parser.parse_args()
    return args
'''
    ''' 
  args = opt()
    if args.range and args.need:
@@ -221,13 +243,8 @@ def main():
        check_answer(e_fliepath=e_file, a_filepath=a_flie)
    else:
        print("请检查输入的文件名信息！\n")
    t1 = time.time()
    to_file(need=10000, erange=10)
    check_answer(e_fliepath="Exercises.txt", a_filepath="Answers.txt")
    t2= time.time()
    print('Execute time: %.2f' %(t2-t1))
    '''

    '''  

if __name__ == '__main__':
    main()
