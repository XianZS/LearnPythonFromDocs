res = [x for x in range(1, 10)]
# print(res)

# range(start_index,end_index,step)
# 起始下标（可选参数,default=0）
# 终止下标（必选参数）
# 步长（可选参数,step=1）
# 左闭右开区间（包含起始下标指向的元素，但是不包含终止下标指向的元素）
some = [x for x in range(1, 101, 3)]

# L = len(some)
# for index in range(L):
#     print(index, some[index])

# for child in enumerate(some, start=0):
#     print(child)
#
news = range(10)
print(news, type(news), sum(news))
