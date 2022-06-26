def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    df = pd.read_csv(
        'data_lake/business/features/precios-diarios.csv', index_col=None, header=0)

    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y-%m-%d')
    df['year'], df['month'], df['day'] = df['Fecha'].dt.year, df['Fecha'].dt.month, df['Fecha'].dt.day

    x = df.copy().drop('Fecha', axis=1)
    y = x.pop('Precio')

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()
