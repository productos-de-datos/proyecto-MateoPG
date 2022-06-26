def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    import os

    os.mkdir("./data_lake")

    dir = ["landing", "raw", "cleansed", "business"]
    subdir_business = ["reports", "features", "forecasts"]
    subdir_business_reports = ["figures"]

    [os.mkdir(os.path.join("data_lake/", each_dir)) for each_dir in dir]
    [os.mkdir(os.path.join("data_lake/business/", each_dir))
     for each_dir in subdir_business]
    [os.mkdir(os.path.join("data_lake/business/reports/", each_dir))
     for each_dir in subdir_business_reports]

    return


create_data_lake()

#raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
