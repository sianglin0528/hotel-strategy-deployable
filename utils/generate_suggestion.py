
def generate_suggestion(latest_forecast):
    rate = latest_forecast['yhat']
    if rate < 0.5:
        return "⚠️ 預測住房率偏低，建議降價或增加促銷活動。"
    elif rate > 0.8:
        return "✅ 預測住房率良好，可考慮適度提高價格以增加收益。"
    else:
        return "➖ 預測住房率穩定，維持現有策略即可。"
