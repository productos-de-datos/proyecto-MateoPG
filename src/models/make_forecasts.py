def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    import pandas as pd
    import pickle
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score

    df = pd.read_csv(
        'data_lake/business/features/precios-diarios.csv', index_col=None, header=0)

    final_db = df.copy()

    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y-%m-%d')
    df['year'], df['month'], df['day'] = df['Fecha'].dt.year, df['Fecha'].dt.month, df['Fecha'].dt.day

    x = df.copy().drop('Fecha', axis=1)
    y = x.pop('Precio')

    regression = pickle.load(open('src/models/precios-diarios.pkl', 'rb'))
    prediction = regression.predict(x)

    final_db['Prediction'] = prediction

    final_db.to_csv(
        'data_lake/business/forecasts/precios-diarios.csv', index=None)

    return
    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()
