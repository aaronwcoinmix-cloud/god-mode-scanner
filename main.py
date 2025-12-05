#!/usr/bin/env python3
"""
God Mode Crypto Scanner - 主程序
"""

import ccxt
import pandas as pd
import numpy as np
import time
import logging
from datetime import datetime
import os

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CryptoScreener:
    def __init__(self):
        self.exchange = ccxt.binance()
        
    def run(self):
        print("=" * 50)
        print("🚀 God Mode Crypto Scanner 启动")
        print("=" * 50)
        
        try:
            # 获取交易对
            markets = self.exchange.load_markets()
            symbols = [s for s in markets if s.endswith('/USDT')]
            
            print(f"📊 找到 {len(symbols)} 个USDT交易对")
            print("开始分析前20个高流动性品种...")
            
            results = []
            for symbol in symbols[:20]:  # 只分析前20个
                try:
                    # 获取K线数据
                    ohlcv = self.exchange.fetch_ohlcv(symbol, '1h', limit=100)
                    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                    
                    # 计算简单评分
                    score = self.calculate_score(df)
                    
                    if score > 50:  # 只保留评分>50的
                        results.append({
                            'symbol': symbol.replace('/', ''),
                            'score': score,
                            'price': df['close'].iloc[-1],
                            'change_24h': self.get_24h_change(df)
                        })
                        
                    print(f"✓ 分析完成: {symbol} - 评分: {score}")
                    
                except Exception as e:
                    print(f"✗ 分析失败 {symbol}: {str(e)[:50]}")
                
                time.sleep(0.1)  # 避免请求过快
            
            # 输出结果
            if results:
                results.sort(key=lambda x: x['score'], reverse=True)
                
                print("\n" + "=" * 50)
                print("🏆 今日推荐品种:")
                print("=" * 50)
                
                for i, r in enumerate(results[:10], 1):
                    print(f"{i}. {r['symbol']}")
                    print(f"   评分: {r['score']:.0f}/100 | 价格: ${r['price']:.4f}")
                    print(f"   24h变化: {r['change_24h']:+.2f}%")
                    print()
                
                # 保存结果
                self.save_results(results)
            else:
                print("⚠️ 今日未找到符合条件的品种")
                
        except Exception as e:
            logger.error(f"运行失败: {e}")
            
    def calculate_score(self, df):
        """简化评分函数"""
        if len(df) < 20:
            return 0
            
        score = 0
        
        # 1. 阳线加分
        if df['close'].iloc[-1] > df['open'].iloc[-1]:
            score += 20
            
        # 2. 成交量放大加分
        avg_volume = df['volume'].rolling(20).mean().iloc[-1]
        if df['volume'].iloc[-1] > avg_volume * 1.5:
            score += 30
            
        # 3. 趋势判断
        sma20 = df['close'].rolling(20).mean().iloc[-1]
        if df['close'].iloc[-1] > sma20:
            score += 30
            
        # 4. 波动性判断
        high_low_range = (df['high'] - df['low']) / df['low'] * 100
        if high_low_range.iloc[-1] > 1.0:  # 波动大于1%
            score += 20
            
        return min(score, 100)
    
    def get_24h_change(self, df):
        """计算24小时变化"""
        if len(df) < 24:
            return 0
        return ((df['close'].iloc[-1] - df['close'].iloc[-24]) / df['close'].iloc[-24] * 100)
    
    def save_results(self, results):
        """保存结果到文件"""
        import json
        
        data = {
            'timestamp': datetime.now().isoformat(),
            'results': results
        }
        
        with open('scan_results.json', 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"📁 结果已保存到: scan_results.json")

if __name__ == "__main__":
    screener = CryptoScreener()
    screener.run()
