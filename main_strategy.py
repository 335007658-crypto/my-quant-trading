#!/usr/bin/env python
# coding: utf-8

# In[1]:


import akshare as ak
import pandas as pd

def check_signal_real(stock_code):
    print(f"正在从 AkShare 接口抓取股票 {stock_code} 的历史行情...")

    # 【已修正】使用标准的A股历史行情接口
    # period="daily" 表示日线，adjust="" 表示不复权
    df = ak.stock_zh_a_hist(symbol=stock_code, period="daily", start_date="20250101", adjust="")

    # 计算 5日均线 和 20日均线
    df['MA5'] = df['收盘'].rolling(5).mean()
    df['MA20'] = df['收盘'].rolling(20).mean()

    # 获取最新的行情和均线数据
    latest_data = df.iloc[-1]
    current_close = latest_data['收盘']
    ma5 = latest_data['MA5']
    ma20 = latest_data['MA20']
    date = latest_data['日期']  # 东方财富接口返回的列名是“日期”

    print(f"日期: {date} | 当前收盘价: {current_close} | 5日线: {ma5:.2f} | 20日线: {ma20:.2f}")

    # 双均线策略逻辑
    if ma5 > ma20:
        return f"【买入信号】{date} 5日线超越20日线，属于主流龙头，控制回撤分批建仓！"
    else:
        return f"【观望】{date} 均线未形成金叉，继续等待时机。"

# 用真实的贵州茅台代码测试
print(check_signal_real("600519"))


# In[ ]:





# In[ ]:




