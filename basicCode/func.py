def loss(a, b):
    if not isinstance(a, (int, float)):  # 参数类型检查
        print(a + "不是数字")
    else:
        print(b)
    if not isinstance(b, (int,)):  # 注意第二个参数是一个tuple，单个值要有,
        return  # 等价于 return None
    return a, a+b, b  # 返回多个值


a, ab, b = loss(520, 1314)
print(a, ab, b)
