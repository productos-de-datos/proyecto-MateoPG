"""
Transforms the hourly data into monthly data using a monthly mean
"""
# pylint: disable=import-outside-toplevel
def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    import pandas as pd
    clean_base = pd.read_csv('data_lake/cleansed/precios-horarios.csv',
                     index_col=None, header=0)
    clean_base['Fecha'] = pd.to_datetime(clean_base['Fecha'], format='%Y-%m-%d')
    df_ano_mes_agrupada = clean_base.groupby(clean_base['Fecha'].dt.to_period('M'))[
        'Precio'].mean().reset_index()
    df_ano_mes_agrupada['Fecha'] = pd.to_datetime(
        df_ano_mes_agrupada['Fecha'].astype(str), format='%Y-%m')

    df_ano_mes_agrupada.to_csv(
        'data_lake/business/precios-mensuales.csv', index=None)
#raise NotImplementedError("Implementar esta función")
if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
