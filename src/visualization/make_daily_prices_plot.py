def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    #
    # 
    import os
    import pandas as pd
    import plotly.express as px 
    import matplotlib.pyplot as plt
    
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
    # (leer precios diarios)
    #
    daily_prices=pd.read_csv(os.path.join("data_lake","business", "precios-diarios.csv" ),header=0)
    #return(daily_prices)
    #
    # (grafico de linea precios diarios)
    #
    #
    plt.figure(figsize=(24,18))
    #
    plot = daily_prices.plot(x="fecha" , y=["precio"], kind="line")
    #
    plt.tick_params(axis='x',labelsize=15,rotation=45)
    #plt.tight_layout()
    #
    plt.savefig(os.path.join("data_lake","business","reports","figures","daily_prices.png" ))

if __name__ == "__main__":
    import doctest
    make_daily_prices_plot()
    doctest.testmod()
