def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score
    import pandas as pd
    import pickle

    df = pd.read_csv(
        'data_lake/business/features/precios-diarios.csv', index_col=None, header=0)

    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y-%m-%d')
    df['year'], df['month'], df['day'] = df['Fecha'].dt.year, df['Fecha'].dt.month, df['Fecha'].dt.day

    x = df.copy().drop('Fecha', axis=1)
    y = x.pop('Precio')

    x_train = x[:round(x.shape[0]*0.75)]
    x_test = x[round(x.shape[0]*0.75):]
    y_train = y[:round(x.shape[0]*0.75)]
    y_test = y[round(x.shape[0]*0.75):]

    regression = LinearRegression()
    regression.fit(x_train, y_train)

    pickle.dump(regression, open('src/models/precios-diarios.pkl', 'wb'))

    return
    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
