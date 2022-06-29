"""
This function does the forecast and save it in csv format
"""
# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-with
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
    from sklearn.metrics import r2_score

    base = pd.read_csv(
        'data_lake/business/features/precios-diarios.csv', index_col=None, header=0)
    final_db = base.copy()

    base['Fecha'] = pd.to_datetime(base['Fecha'], format='%Y-%m-%d')
    base['year'], base['month'], base['day'] = \
        base['Fecha'].dt.year, base['Fecha'].dt.month, base['Fecha'].dt.day

    x_total = base.copy().drop('Fecha', axis=1)
    y_total = x_total.pop('Precio')

    regression = pickle.load(open('src/models/precios-diarios.pkl', 'rb'))
    prediction = regression.predict(x_total)

    r2_score(y_total,regression.predict(x_total))

    final_db['Prediction'] = prediction

    final_db.to_csv(
        'data_lake/business/forecasts/precios-diarios.csv', index=None)
#raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()
