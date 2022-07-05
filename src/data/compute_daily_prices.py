def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    #
    import os
    import pandas as pd
    import numpy as np
    
    #
    # (navegar a raiz del proyecto)
    #
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    #os.chdir(dir_path)
    #os.chdir("..")
    #os.chdir("..")
    
    #
    # (leer precios diarios)
    #
    hourly_prices=pd.read_csv(os.path.join("data_lake","cleansed","precios-horarios.csv" ),header=0)
    
    #
    # (loop sobre las fechas)
    #
    an=hourly_prices.groupby('fecha').mean()
    an.drop(columns="hora", inplace=True)
    
    #
    an.to_csv( os.path.join("data_lake","business", "precios-diarios.csv"))



if __name__ == "__main__":
    import doctest
    compute_daily_prices()
    doctest.testmod()
