"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.

"""

import os
#
# (navegar a raiz del proyecto)
#
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
os.chdir("..")
os.chdir("..")
os.chdir(os.path.join("src", "data"))
print(os.getcwd())


#
import luigi
from luigi import Task, LocalTarget
import os
import pandas as pd
#
from ingest_data import ingest_data
from transform_data import transform_data
from  clean_data import clean_data
from compute_daily_prices import compute_daily_prices
from compute_monthly_prices import compute_monthly_prices


#
#
class pipeline_until_clean_data(Task):
    
    def output(self):
        return LocalTarget(os.path.join("data_lake","cleansed","precios-horarios.csv" ))
    def run(self):
        ingest_data()
        transform_data()
        clean_data()
#
#
class Compute_daily_prices(Task):
    def requires (self):
        return pipeline_until_clean_data()
    def output(self):
        return LocalTarget(os.path.join("data_lake","business","precios-diarios.csv"))
    def run(self):
        compute_daily_prices()
#
class Compute_monthly_prices(Task):
    def requires (self):
        return pipeline_until_clean_data()
    def output(self):
        return LocalTarget(os.path.join("data_lake","business","precios-mensuales.csv"))
    def run(self):
        compute_monthly_prices()

#
class Pipeline(Task):

    def requires(self):
        return [
            Compute_daily_prices(),
            Compute_monthly_prices(),
        ]

#
#
if __name__ == "__main__":
    import doctest
    luigi.run(['Pipeline','--local-scheduler'])
    doctest.testmod()
