def transform_crypto_data(df):
    df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume']]
    df.columns = [col.upper() for col in df.columns]
    return df