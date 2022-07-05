def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    #
    import os
    import pandas as pd
    
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
    daily_prices=pd.read_csv(os.path.join("data_lake","cleansed","precios-horarios.csv" ),header=0)
    
    #
    # (loop sobre las fechas)
    #
    daily_prices["fecha"]=[str(f)[0:7] for f in daily_prices["fecha"]]
    #return(daily_prices)
    an=daily_prices.groupby('fecha').mean()
    an.drop(columns="hora", inplace=True)
    
    #
    an.to_csv( os.path.join("data_lake","business", "precios-mensuales.csv"))


if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
