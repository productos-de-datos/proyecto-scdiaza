def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    #
    import os
    import pandas as pd
    
    #
    # (navegar a raiz del proyecto)
    #
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    os.chdir("..")
    os.chdir("..")
    
    #
    # (enumerar archivos anuales)
    #
    _,_,files=list(os.walk(os.path.join("data_lake", "raw" )))[0]
    daily_data_paths= [os.path.join("data_lake", "raw", f )  for f in  files]
    
    #
    # (leer archivos anuales)
    #
    
    daily_dataframes=[pd.read_csv(p,header=0) for p in daily_data_paths]
    
    #
    # (reshape info diaria en info horaria->formato largo)
    #
    
    #
    def data_diaria_en_data_horaria(daily_data):
        #daily_data=pd.read_csv('data_lake\\raw\\2007.csv',header=None)
        assert int(len(daily_data.columns))==int(25), print(daily_data.head())
        #daily_data.rename(columns={1:"fecha"}, inplace=True)
        import re
        #return(daily_data)
        value_cols=[c for c in daily_data.columns if bool(re.search("[0-9]",str(c)))]
        #
        hourly_data = daily_data.melt(id_vars='fecha', 
                                      value_vars=value_cols,   
                                      var_name="hora",
                                      value_name="precio")
        return(hourly_data)
    hourly_dataframes=[data_diaria_en_data_horaria(df) for df in daily_dataframes]
    
    #
    # (single global dataframe)
    #
    hourly_data=pd.concat(hourly_dataframes, ignore_index=True)
    hourly_data.to_csv( os.path.join("data_lake","cleansed","precios-horarios.csv"),index=False)
    print("201")
clean_data()

if __name__ == "__main__":
    import doctest    
    doctest.testmod()
