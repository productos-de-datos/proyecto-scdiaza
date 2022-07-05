def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    
    #
    import pandas as pd
    import pickle
    import os
    import re
    
    #
    # (navegar a raiz del proyecto)
    #
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    os.chdir("..")
    os.chdir("..")
    
    #
    a_estimar=pd.read_csv(os.path.join("data_lake", "business", "features", "precios-diarios.csv"))
    a_estimar['fecha'] = pd.to_datetime(a_estimar['fecha'], format='%Y-%m-%d')

    #
    x_vars= [c for c in a_estimar.columns if re.search( "^x",c) ]
    X = a_estimar[x_vars].to_numpy()

    #
    with open(os.path.join("src", "models", "precios-diarios.pkl"), 'rb') as model_source:
        prices_model = pickle.load(model_source)
 
    #
    a_estimar['pred_precio'] = prices_model.predict(X)
    answer = a_estimar[['fecha', 'precio', 'pred_precio']]
    answer.to_csv(os.path.join("data_lake", "business", "forecasts", "precios-diarios.csv"), index=False)


if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()
