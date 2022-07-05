def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    
    #
    import pandas as pd
    import os
    #
    from sklearn.model_selection import train_test_split
    from sklearn import linear_model
    import numpy as np
    import pickle
    
    #
    # (navegar a raiz del proyecto)
    #
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    os.chdir("..")
    os.chdir("..")
    
    #
    # (cargar variables para entrenar el modelo)
    #
    features_df = pd.read_csv(os.path.join("data_lake","business", "features", "precios_diarios.csv"))

    #
    # (entrenar regresion lineal)
    #
    import re
    x_vars= [c for c in features_df.columns if re.search( "^x",c) ]
    X = features_df[x_vars].to_numpy()
    y = np.array(features_df['precio']).reshape(-1, 1)
    #
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=33
    )
    linear_model = linear_model.LinearRegression()
    linear_model_fit = linear_model.fit(X_train, y_train)
    pickle.dump( linear_model_fit , open(
        os.path.join("src","models", "precios-diarios.pkl"), "wb"     
        ))

    return(True)


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
