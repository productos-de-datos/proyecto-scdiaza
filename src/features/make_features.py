def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """
    #
    import pandas as pd
    import os
    
    #
    # (navegar a raiz del proyecto)
    #
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    #
    os.system("make create_data_lake")
    os.system("make ingest_data")
    os.system("make transform_data")
    os.system("make create_data_lake")
    os.system("make clean_data")
    os.system("make compute_daily_prices")
    os.system("make compute_monthly_prices")
    #
    os.chdir("..")
    os.chdir("..")
    
    
    #
    precios_diarios=pd.read_csv(os.path.join("data_lake","business", "precios-diarios.csv"))
    #
    precios_diarios['fecha'] = pd.to_datetime(precios_diarios['fecha'], format='%Y-%m-%d')
    #
    precios_diarios['x1'] =precios_diarios.fecha.dt.year
    precios_diarios['x2'] =precios_diarios.fecha.dt.month
    precios_diarios['x3'] =precios_diarios.fecha.dt.day
    precios_diarios['x4'] = precios_diarios.fecha.dt.weekday
    #df.to_csv('data_lake/business/features/precios_diarios.csv', index=False)
    #print ("Saved features--->")
    precios_diarios.to_csv( os.path.join("data_lake","business", "features", "precios-diarios.csv"), index=False)
    return True


if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
