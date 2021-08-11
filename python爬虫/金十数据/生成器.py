
# 问题 下面函数为直接返回列表，请将其改为生成器
# def get_max_num(arr: list):
#     """
#     :param arr: 二维数组，eg: [[1,2,3],[4,5,6]]
#     :return:
#     """
#     return [max(_) for _ in arr]
# result=get_max_num([[1,2,3],[4,5,6]])
# print(result)

# # 方法1 把一个列表生成式的[]改成()，创建了一个generator
# def get_max_num(arr: list):
#     """
#     :param arr: 二维数组，eg: [[1,2,3],[4,5,6]]
#     :return:
#     """
#     return (max(_) for _ in arr)
# result=get_max_num([[1,2,3],[4,5,6]])
# print(result)
# print(list(result))

# 方法2 函数添加yield关键字
def get_max_num(arr: list):
    """
    :param arr: 二维数组，eg: [[1,2,3],[4,5,6]]
    :return:
    """
    yield [max(_) for _ in arr]
result=get_max_num([[1,2,3],[4,5,6]])
print(result)
