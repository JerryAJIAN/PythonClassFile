# author:ASUS
# datetime:2020/10/19 下午 05:25
# software: PyCharm
# UserName:ASUS 
# OS DATE: 2020/10/19 
# ProjetName: PythonClassFile
# scripts:
#初始：
letters = [
  '7', 'u', 'b', 'u', 'r', 'l', 'n', ' ', '5', 'o',
  'j', 'c', '3', '7', '1', 'x', 'd', 'x', 'm', '8',
  'a', 'v', 'f', 'd', 'z', 'z', 'd', 'l', 'v', 'o',
  'q', 'j', 'u', '2', 'o', 'l', 'v', '6', 'i', 'o',
  'i', '5', '9', 'b', 'c', 'i', 's', 'a', 'i', '2',
  '!', '8', 's', 't', '9', 'r', 'x', 'w', 'j', '1',
  '5', '5', '3', 'm', '9', '6', 'r', 'w', '9', 'd',
  'd', 'r', 'y', '3', 'p', 'h', 'f', '9', '1', 'b',
  'w', 'u', 'c', 'e', 'r', '3', 'i', 'i', 'x', '7',
  'x', '2', 'n', 'p', 'a', '4', 'b', 'f', 'w', ' '
]
Answer=[]
# 按照提示来动手破解信件吧！
# 1 列表 letters 尾部追加 '!'
letters.insert(-1,'!')

# 2 取出列表 letters 中第 7 到 9 个元素（包含 7 和 9）

letters[7:10]
# 3 列表 answer 尾部追加 letters 列表里字符 'x' 的次数（需要转换成字符串类型）
Answer.append(str(letters.count('x')))
# 4 列表 answer 尾部追加 letters 列表中最后一个元素
Answer.append(letters[-1])
# 5 将列表 answer 和列表 letters 中最后的三个元素拼接在一起
Answer=Answer+letters[-3:]
# 6 打印结果
print(''.join(Answer))
print("1840610913 简高林")