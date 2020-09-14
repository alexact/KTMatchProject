import pandas as pd
from Model.data_model import DataModel


class DataService:
    def __init__(self):
        self.data = DataModel( ).data( )

    def generation_df_impact_frecuency(self):
        """
        :return:Retorna el dataFrame de la encuesta donde están los puntajes de impacto y de frecuencia para cada variable
        """
        new_df = pd.DataFrame(self.data)
        return new_df

    def generation_df_frecuency(self, start_col, data_upload):
        """
        :param start_col: si el archivo tiene información adicional antes de las columnas se comienza con el
        indicador de columna
        :param data_upload: Recibe el dataframe cargado desde el upload
        :return: Retorna el dataFrame de la encuesta donde están los puntajes de impacto para cada variable
        """
        if type(data_upload) is str:
            data_upload = pd.DataFrame(self.data)
        list_title = list(DataModel( ).file_variables_title( ))
        full_set_df = data_upload
        new_df = pd.DataFrame( )
        # Se suma uno porque el inicio de la columna empieza por impacto y luego la frecuencia
        new_df[list_title[0]] = full_set_df.iloc[:, start_col+1]
        for col in range(len(list_title) - 1):
            start_col = start_col + 2
            new_df[list_title[col + 1]] = full_set_df.iloc[:, start_col + 1]
        return new_df

    def generation_df_impact(self, start_col, data_upload):
        """
        :param start_col: si el archivo tiene información adicional antes de las columnas se comienza con el
        indicador de columna
        :param data_upload: Recibe el dataframe cargado desde el upload
        :return:Retorna el dataFrame de la encuesta donde están los puntajes de frecuencia para cada variable
        teniendo en cuenta que en el archivo se intercalan por columna del excel cada varibale
        impactov1|FrecV1|ImpactoV2|FrecV2|impactov3|FrecV3|ImpactoV4|FrecV4
        """
        if type(data_upload) is str:
            data_upload = pd.DataFrame(self.data)
        list_title = list(DataModel( ).file_variables_title( ))
        full_set_df = data_upload
        new_df = pd.DataFrame( )
        new_df[list_title[0]] = full_set_df.iloc[:, start_col]
        for col in range(len(list_title) - 1):
            start_col = start_col + 1
            new_df[list_title[col + 1]] = full_set_df.iloc[:, start_col + 1]
        return new_df

    def gerenation_df_severity(self, start_col, data_upload):
        """
        Crea un nuevo dataFrame donde las columnas a utilizar son la severdidad= impactoV1 * frecuenciaV1 de cada variable(Vn)
        :param start_col: indica de la encuesta en que posición de columna empiezan las variables a tratar
        :param data_upload:Recibe decodificado la tabla de valores del archivo csv
        :return:
        """
        if type(data_upload) is str:
            data_upload = pd.DataFrame(self.data)
        list_title = list(DataModel().file_variables_title( ))
        full_set_df = data_upload
        new_df = pd.DataFrame( )
        new_df[list_title[0]] = full_set_df.iloc[:, start_col] * full_set_df.iloc[:, (start_col - 1) + 2]
        for col in range(len(list_title) - 1):
            start_col = start_col + 1
            new_df[list_title[col + 1]] = full_set_df.iloc[:, start_col + 1] * full_set_df.iloc[:, start_col + 2]
        return new_df

    def frecuency_table(self, new_df):
        """
        :param new_df: dataFrame a analizar
        :return: dataFrame con la información de una tabla de frecuencias(max,min,media,moda,percentiles)
        """
        df = pd.DataFrame(new_df.describe( ))
        return df

    def shape(self, new_df):
        """
        :param new_df: dataFrame a analizar
        :return: Tupla con las dimensiones del dataframe (fila, columna)
        """
        return new_df.shape( )

    def title(self):
        """
        :return: Lista de titulos predeterminados de un archivo inicial del programa antes de cargar el usuario uno
        """
        df = pd.DataFrame(DataModel().file_variables_title( ))
        return df

    def generate_titles(self):
        """
        :return: lista de titulos inciales convertidos en dataframe
        """
        titles = []
        df_titles = DataService( ).title( )
        for i in df_titles:
            titles.append({'label': i, 'value': i})
        return titles

    def correlation_pearson_pairs(self, df):
        """
        :param df: dataFrame de severidad
        :return: dataframe con los coeficientes de correolación de pearson
        """
        return df.corr(method='pearson')

    def gerenation_df_severitySVM(self, data, df_severity):
        """
        :param data: archivo cargado desde el upload en DataFrame
        :param df_severity: dataframe generado para severidad a partir del archivo cargado
        :return: la unión entre el df_severity y la ultima columna de la data (variable Y)
        """
        pd.DataFrame(data)
        df_severity[data.iloc[:,-1].name]=data.iloc[:,-1].tolist()
        return df_severity

