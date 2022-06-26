"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
import luigi
from luigi import Task, LocalTarget


class data_ingestion(Task):

    def output(self):
        return LocalTarget('data_lake/landing/result.txt')

    def run(self):
        from ingest_data import ingest_data
        with self.output().open('w') as files_ingested:
            ingest_data()


class data_transformation(Task):
    def requires(self):
        return data_ingestion()

    def output(self):
        return LocalTarget('data_lake/raw/results2.txt')

    def run(self):
        from transform_data import transform_data
        with self.output().open('w') as files_transformed:
            transform_data()


class pricing_schedule_table_creation(Task):
    def requires(self):
        return data_transformation()

    def output(self):
        return LocalTarget('data_lake/cleansed/result3.txt')

    def run(self):
        from clean_data import clean_data
        with self.output().open('w') as table_created:
            clean_data()


class mean_daily_prices(Task):
    def requires(self):
        return pricing_schedule_table_creation()

    def output(self):
        return LocalTarget('data_lake/business/result4.txt')

    def run(self):
        from compute_daily_prices import compute_daily_prices
        with self.output().open('w') as daily_prices:
            compute_daily_prices()


class mean_monthly_prices(Task):
    def requires(self):
        return mean_daily_prices()

    def output(self):
        return LocalTarget('data_lake/business/result5.txt')

    def run(self):
        from compute_monthly_prices import compute_monthly_prices
        with self.output().open('w') as monthly_prices:
            compute_monthly_prices()


if __name__ == "__main__":

    luigi.run(['mean_monthly_prices', '--local-scheduler'])

    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
