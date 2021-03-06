
"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


def ingest_data():
    """Ingeste los datos externos a la c
apa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    #
    #
    import requests
    import os
    os.system("pip install  lxml")
    import lxml.html
    #
    html = requests.get("https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/")
    doc = lxml.html.fromstring(html.content)
    urls=doc.xpath("//a/text()")
    print(urls)
    
    #
    os.chdir(os.path.join("data_lake", "landing" )) 
    for probably_a_url_to_xlsx_file in urls:
        import re
        
        if re.search("xls(.){,1}", probably_a_url_to_xlsx_file):
            file_url = "https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}?raw=true".format(probably_a_url_to_xlsx_file)
            #print(file_url)
            
            #
            response = requests.get(file_url)
            open( probably_a_url_to_xlsx_file, "wb").write(response.content)
#ingest_data()

if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
