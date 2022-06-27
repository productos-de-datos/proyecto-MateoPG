"""
This functions builds, train and store the model in a pickle file"""
# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-with
def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score
    import pandas as pd
    import pickle

    base = pd.read_csv(
        'data_lake/business/features/precios-diarios.csv', index_col=None, header=0)

    base['Fecha'] = pd.to_datetime(base['Fecha'], format='%Y-%m-%d')
    base['year'], base['month'], base['day'] = \
        base['Fecha'].dt.year, base['Fecha'].dt.month, base['Fecha'].dt.day

    x_total = base.copy().drop('Fecha', axis=1)
    y_total = x_total.pop('Precio')

    x_train = x_total[:round(x_total.shape[0]*0.75)]
    x_test = x_total[round(x_total.shape[0]*0.75):]
    y_train = y_total[:round(x_total.shape[0]*0.75)]
    y_test = y_total[round(x_total.shape[0]*0.75):]

    regression = LinearRegression()
    regression.fit(x_train, y_train)

    r2_score(y_test,regression.predict(x_test))

    pickle.dump(regression, open('src/models/precios-diarios.pkl', 'wb'))

#raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
