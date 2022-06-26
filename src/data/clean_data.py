def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    import pandas as pd
    import glob

    path = glob.glob(r'data_lake/raw/*.csv')

    for i, file in enumerate(path):
        if i == 0:
            df = pd.read_csv(file, index_col=None, header=0)
            df_hours = df.iloc[:, :25]
            df_hours.columns = ['Fecha']+[('0'+str(i))[:2] for i in range(24)]
            converted_df = df_hours.melt(
                id_vars='Fecha', var_name='Hora', value_name='Precio')
            temp_df = converted_df
        else:
            df = pd.read_csv(file, index_col=None, header=0)
            df_hours = df.iloc[:, :25]
            df_hours.columns = ['Fecha']+[('0'+str(i))[:2] for i in range(24)]
            converted_df = df_hours.melt(
                id_vars='Fecha', var_name='Hora', value_name='Precio')
            temp_df = pd.concat([temp_df, converted_df])
    temp_df.to_csv('data_lake/cleansed/precios-horarios.csv', index=None)

    return
    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
