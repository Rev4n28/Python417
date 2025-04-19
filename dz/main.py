def nums(fn):
    def summer(*args):
        global num_list, num_sum, num_list_str
        num_list = []
        num_sum = 0
        for i in range(len(args)):
            num_list.append(args[i])
            num_sum += args[i]
            num_list_str = ", ".join([str(j) for j in num_list])
        print("Сумма чисел ", num_list_str, " = ", num_sum, sep="")
        fn(*args)

    return summer


@nums
def midler(*args):
    print("Срендее арифметическое чисел ", num_list_str, " = ", sum(num_list) / len(num_list), sep="")


midler(2, 3, 3, 4)
