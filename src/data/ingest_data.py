"""
This funtion downloads the information and save it in the same format obtained.
"""
# pylint: disable=consider-using-f-string
# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-with
# pylint: disable=line-too-long
def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.
    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.
    """
    import requests
    url_base = "https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/"

    for year in range(1995, 2022):
        if year in [2016, 2017]:
            url = url_base+"{}.xls?raw=true".format(
                year)
            response = requests.get(url, allow_redirects=True)
            open('data_lake/landing/{}.xls'.format(year),
                 "wb").write(response.content)
        else:
            url = url_base+"{}.xlsx?raw=true".format(
                year)
            response = requests.get(url, allow_redirects=True)
            open('data_lake/landing/{}.xlsx'.format(year),
                 "wb").write(response.content)
if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
