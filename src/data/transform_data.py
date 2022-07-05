def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    #
    
    #
    import os
    import pandas as pd
    os.system("pip install  openpyxl")
    os.system("pip install  xlrd")

    #
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    os.chdir("..")
    os.chdir("..")
    _,_,files=list(os.walk(os.path.join("data_lake", "landing" )))[0]
    
    #
    for a_file in files:
        #
        new_df=pd.read_excel(os.path.join("data_lake", "landing", a_file ), header=None)
        first_col=list(new_df.iloc[:, 0])
        print(a_file )
        header_row=[i for i in range(len(new_df.index)) if str(first_col[i]).lower()=="fecha" ][0]
        new_df=pd.read_excel(os.path.join("data_lake", "landing", a_file ), header=header_row)  
        #
        # schema normalization (preserve well formed files)
        #
        import re
        schema_cols=[c for c in new_df.columns if re.search("(.echa)|(^[0-9]+$)", str(c))]
        new_df=new_df[schema_cols]
        new_df.columns=[c.lower() for c in new_df.columns]
        #return(new_df)
        new_file_name=os.path.join("data_lake", "raw", a_file.replace(".xlsx", ".csv"))
        new_df.to_csv(new_file_name, index=False)


if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
