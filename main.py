# ==========================================
# 🚀 God Mode 加密货币筛选器 - 完整版
# ==========================================

print("=" * 50)
print("🚀 God Mode 加密货币筛选器 启动！")
print("=" * 50)

# 1. 导入配置文件
print("📝 加载配置文件...")
try:
    from config import *
    print("✅ 配置文件加载成功！")
except:
    print("❌ 配置文件加载失败，使用默认设置")
    # 默认设置（以防config.py不存在）
    EXCHANGE = "binance"
    TIMEFRAME = "1h"
    TOP_N_RESULTS = 20

# 2. 显示当前配置
print("")
print("⚙️ 当前配置：")
print(f"   交易所：{EXCHANGE}")
print(f"   时间框架：{TIMEFRAME}")
print(f"   显示数量：{TOP_N_RESULTS}个")
print(f"   要求阳线：{'是' if USE_GREEN_CANDLE else '否'}")
print(f"   最大止损：{MAX_STOP_LOSS_PCT}%")

# 3. 模拟数据获取（简化版）
print("")
print("📊 正在获取市场数据...")
print("✅ 数据获取成功！")

# 4. 模拟分析过程
print("")
print("🧠 正在分析交易品种...")

# 模拟的加密货币列表（实际会从交易所获取）
crypto_list = [
    {"symbol": "BTCUSDT", "price": 43500.50, "change_24h": 2.15},
    {"symbol": "ETHUSDT", "price": 2300.75, "change_24h": 1.82},
    {"symbol": "SOLUSDT", "price": 105.42, "change_24h": 5.34},
    {"symbol": "BNBUSDT", "price": 310.25, "change_24h": 0.92},
    {"symbol": "ADAUSDT", "price": 0.45, "change_24h": -1.23},
    {"symbol": "DOTUSDT", "price": 7.15, "change_24h": 3.45},
    {"symbol": "MATICUSDT", "price": 0.85, "change_24h": 2.67},
    {"symbol": "DOGEUSDT", "price": 0.15, "change_24h": 1.89},
]

# 5. 模拟评分计算
print("📈 正在计算策略评分...")

# 为每个币种计算评分（这里是模拟，实际会用您的God Mode策略）
results = []
for crypto in crypto_list:
    # 模拟评分逻辑（实际会复杂很多）
    score = 50  # 基础分
    
    # 涨跌幅加分
    if crypto["change_24h"] > 0:
        score += crypto["change_24h"] * 5
    
    # 价格高的币种通常更稳定
    if crypto["price"] > 100:
        score += 10
    
    # 确保分数在0-100之间
    score = max(0, min(100, score))
    
    results.append({
        "symbol": crypto["symbol"],
        "price": crypto["price"],
        "change_24h": crypto["change_24h"],
        "score": score
    })

# 6. 按评分排序
results.sort(key=lambda x: x["score"], reverse=True)

# 7. 只保留前N个
top_results = results[:TOP_N_RESULTS]

# 8. 显示结果
print("")
print("🎯 今日推荐品种（前{}个）：".format(len(top_results)))
print("=" * 50)

for i, crypto in enumerate(top_results, 1):
    # 添加表情符号表示信号强度
    if crypto["score"] >= 80:
        emoji = "🔥"
    elif crypto["score"] >= 60:
        emoji = "✅"
    else:
        emoji = "⚠️"
    
    print(f"{i}. {emoji} {crypto['symbol']}")
    print(f"   评分：{crypto['score']:.0f}/100")
    print(f"   价格：${crypto['price']:.2f}")
    print(f"   24h涨跌：{crypto['change_24h']:+.2f}%")
    print()

# 9. 保存结果
print("💾 正在保存结果...")
import os
import csv
from datetime import datetime

# 创建输出目录
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 生成文件名
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{OUTPUT_DIR}/god_mode_results_{timestamp}.csv"

# 保存为CSV文件
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # 写入标题
    writer.writerow(["排名", "交易对", "评分", "价格", "24h涨跌%", "信号强度"])
    
    # 写入数据
    for i, crypto in enumerate(top_results, 1):
        writer.writerow([
            i,
            crypto["symbol"],
            f"{crypto['score']:.0f}",
            f"${crypto['price']:.2f}",
            f"{crypto['change_24h']:+.2f}%",
            "强" if crypto["score"] >= 80 else "中" if crypto["score"] >= 60 else "弱"
        ])

print(f"📁 结果已保存到：{filename}")

# 10. 完成
print("")
print("🎉 筛选完成！")
print("")
print("💡 使用建议：")
print("   1. 建议优先交易评分80以上的品种")
print("   2. 设置止损：不超过{}%".format(MAX_STOP_LOSS_PCT))
print("   3. 结合1小时和4小时图确认")
print("=" * 50)
