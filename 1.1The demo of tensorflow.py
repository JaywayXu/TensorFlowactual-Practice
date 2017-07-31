"""这是介绍tensorflow基本用法的伪函数"""
import tensorflow as tf

b = tf.Variable(tf.zeros([100]))  # 生成100维的向量初始值是0
W = tf.Variable(tf.random_uniform([784, 100], -1, 1))  # 生成784*100随机矩阵W
"""Outputs random values from a uniform distribution.The generated values follow a uniform distribution in the range
`[minval, maxval)`. The lower bound `minval` is included in the range, while the upper bound `maxval` is excluded."""
x = tf.placeholder(name="X")  # 输入的Placeholder
relu = tf.nn.relu(tf.matmul(W, x)+b)  # ReLu(Wx+b)
C = [...]  # 根据Relu函数的结果计算Cost
s = tf.Session()
for step in range(0, 10):
    #  input =...construct 100-D input array... input是输入的100维的向量
    result = s.run(C, feed_dict={x: input})  # 获取Cost,将输入值input填充到x中
    print(step, result)