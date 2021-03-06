def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```
    #
    
    """
    import os
    #
    os.makedirs(os.path.join("data_lake", "business", "reports", "figures" ), exist_ok=True) 
    os.makedirs(os.path.join("data_lake", "landing" ), exist_ok=True) 
    os.makedirs(os.path.join("data_lake", "raw" ), exist_ok=True) 
    os.makedirs(os.path.join("data_lake", "cleansed" ), exist_ok=True)
    os.makedirs(os.path.join("data_lake", "business" ), exist_ok=True)
    os.makedirs(os.path.join("data_lake", "business" , "features" ), exist_ok=True)
    os.makedirs(os.path.join("data_lake", "business", "forecasts" ), exist_ok=True)
    
    return(True)

    
if __name__ == "__main__":
    import doctest
    create_data_lake()
    doctest.testmod()
