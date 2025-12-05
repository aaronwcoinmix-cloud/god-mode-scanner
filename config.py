# ==========================================
# 📝 God Mode 筛选器配置文件
# 您可以在这里修改设置
# ==========================================

# 🏦 交易所设置
EXCHANGE = "binance"      # 使用币安交易所
TIMEFRAME = "1h"         # 使用1小时K线图
LOOKBACK_DAYS = 30       # 分析最近30天数据

# 📊 筛选标准
MIN_VOLUME_USDT = 1000000  # 最小成交量100万美元
MIN_PRICE = 0.01           # 最低价格0.01美元
TOP_N_RESULTS = 20         # 显示前20个结果

# 🎯 策略参数
USE_GREEN_CANDLE = True   # 是否要求阳线（收盘>开盘）
USE_RSI_HOOK = True       # 是否要求RSI拐头向上
ADX_THRESHOLD = 20        # ADX最小阈值
RSI_MAX_LIMIT = 65        # RSI最大限制
MAX_STOP_LOSS_PCT = 5.0   # 最大止损百分比

# 🔔 通知设置（可选）
TELEGRAM_ENABLED = False   # 是否启用Telegram通知
# 如果需要Telegram通知，请在下面填写：
# TELEGRAM_BOT_TOKEN = "您的机器人Token"
# TELEGRAM_CHAT_ID = "您的Chat ID"

# 📁 文件保存
OUTPUT_DIR = "output"     # 结果保存目录
