# 定义步行和公交的时间
a = 15  # 步行到公交站的时间（分钟）
b = 75  # 公交车行驶时间（1小时15分钟 = 75分钟）
c = a + b  # 总通勤时间（分钟）

# 定义驾车和步行的时间
d = 90  # 驾车时间（1小时30分钟 = 90分钟）
e = 5   # 停车后步行时间（分钟）
f = d + e  # 总通勤时间（分钟）

# 比较两种通勤方式的时间
if c < f:
    quicker_method = "公交更快"
elif c > f:
    quicker_method = "驾车更快"
else:
    quicker_method = "两者时间相同"

# 输出结果
print(f"公交通勤时间: {c} 分钟")
print(f"驾车通勤时间: {f} 分钟")
print(f"更快的方式是: {quicker_method}")
# 定义布尔变量
X = True
Y = False

# 定义 W 变量（X 和 Y 的逻辑与）
W = X and Y

# 输出 W 的值
print(f"X = {X}, Y = {Y}, W = X and Y = {W}")

# 生成 X 和 Y 的真值表
truth_table = [
    (False, False, False and False),
    (False, True, False and True),
    (True, False, True and False),
    (True, True, True and True)
]

# 打印真值表
print("Truth Table for W (X and Y):")
print("X     Y     W")
for row in truth_table:
    print(f"{row[0]}  {row[1]}  {row[2]}")

# 真值表的内容：
# X     Y     W
# False False False
# False True  False
# True  False False
# True  True  True
