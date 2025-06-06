import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='🍚南宁美食地图')

# 餐厅数据
data = pd.DataFrame({
    "月份":['01月','02月','03月','04月','05月','06月','07月','08月','09月','10月','11月','12月']
    "餐厅": ["星艺荟塔斯汀", "麦当劳",  "好友缘","小放肆烤肉", "李嬢拌粉"],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
    "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
    "人均消费(元)": [25, 40, 25, 35, 20],
    "位置X": [22.853973, 22.843103, 22.834317, 22.814946, 22.821271],
    "位置Y": [108.222505, 108.267250, 108.284567, 108.321104, 108.357652]
})



df = pd.DataFrame(data)

index = pd.Series([1, 2, 3,], name='序号')

df.index = index
st.header("门店数据")
# 使用write()方法展示数据框
st.write(df)
st.header("不同类型餐厅价格")
st.line_chart(df, x='餐厅')


# 修改df，用月份列作为df的索引，替换原有的索引
df.set_index('月份', inplace=True)

st.subheader("设置y参数")
# 通过y参数筛选只显示1号门店的数据
st.line_chart(df, y='人均消费(元)')
