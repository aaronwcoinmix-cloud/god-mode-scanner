# God Mode Plus 策略配置
# 对应您的Pine Script参数

# ===== 基础参数 =====
USE_BTC_FILTER = True        # 启用 BTC 情绪过滤
USE_GREEN_CANDLE = True      # 只在阳线买入
USE_RSI_HOOK = True          # RSI 拐头向上
USE_ADX_FILTER = True        # 启用 ADX 过滤 (>20)
ADX_THRESHOLD = 20           # ADX 阈值
USE_RSI_FILTER = True        # 启用 RSI 超买过滤 (<65)
RSI_MAX_LIMIT = 65           # RSI 最大值
MAX_STOP_LOSS_PCT = 5.0      # 最大止损硬顶 (%)

# ===== Peaks 参数 =====
PEAKS_PD = 22                # Peaks周期
PEAKS_MULT = 2.0             # Peaks乘数
PEAKS_LB = 20                # Peaks回看

# ===== MF Distribution 参数 =====
RMA_Y_PERIOD_TOP = 3         # RMA 'Y' Period
TM2_MULTIPLIER_TOP = 10.0    # TM2 Multiplier
EMA_TM3_LEN_TOP = 5          # TM3 EMA Length
HIGH_LOOKBACK_TM4 = 30       # TM4 Lookback
TM3_HIGH_LOOKBACK_TM5 = 30   # TM5 Lookback
HIGH_LOOKBACK_TM6 = 60       # TM6 Lookback
EMA_TM7_LEN_TOP = 3          # TM7 EMA Length
TM8_SCALE_NUM_TOP = 10.0     # TM8 Numerator
TM8_SCALE_DENOM_TOP = 618.0  # TM8 Denominator
TOPS_ALERT_THRESHOLD = 0.1   # Alert Threshold
TOPS_CONFIRMATION_BARS = 2   # Confirmation Bars

# ===== S/R 参数 =====
SR_PRD = 10                  # S/R周期

# ===== Trend Rider 参数 =====
TR_PD = 22                   # Trend Rider周期

# ===== VPC 参数 =====
VPC_LEN = 20                 # VPC长度
