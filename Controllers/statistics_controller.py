import base64
import io

import pandas as pd
from Layouts.upload_component import not_succesfull_upload, succesfull_upload
from Model.data_model import DataModel as data
from Model.data_service import Statistics

s = Statistics( )


# Gestiona la data proveniente del archivo excel

def initialization():
    if not hasattr(initialization, "df_data"):
        initialization.df_data = s.gerenation_df_severity(0, "")
        initialization.df_frecuency = initialization.df_data
        initialization.df_impact = initialization.df_data
        initialization.df_data_frecuency = initialization.df_data

class StatisticsController( ):
    titles_frec = []
    titles_dropdown = []
    titles_heatmap = []

    def __init__(self):
        self.evaluate_data( )

    # Se está reiniciando los valores de las variables para la tabla
    def evaluate_data(self):

        initialization( )
        if not initialization.df_data.empty and 'Title' not in initialization.df_frecuency:
            initialization.df_frecuency.insert(0, 'Title', ["Count", "Mean", "Std", 'Min', '25%', '50%', '75%', "Max"])
            self.titles_frec = []
            self.titles_dropdown = []
        if self.titles_frec == []:
            self.titles_frec.append({'name': 'Title', 'id': 'title'})
            for i in list(initialization.df_frecuency):
                self.titles_frec.append({'name': i, 'id': i})
                self.titles_dropdown.append({'label': i, 'value': i})

    def get_allData(self, data_upload):
        df = s.gerenation_df_severity(6, data_upload)
        return df

    def generate_statistics(self, data_upload):
        """
        :param data_upload: Recibe decodificado la tabla de valores del archivo csv
        :return:Retorna la tabla de frecuencias con los maximos, minimos, media entre otros.
        """
        initialization.df_data = s.gerenation_df_severity(0, data_upload)
        initialization.df_frecuency = s.frecuency_table(initialization.df_data)
        initialization.df_impact = s.generation_df_impact(0, data_upload)
        # print("IMPACTO ",initialization.df_impact)
        initialization.df_data_frecuency =s.generation_df_frecuency(0, data_upload)
        # print("FRECUENCIAAA ", initialization.df_data_frecuency)
        self.evaluate_data( )

    def get_graphs_dispersion(self, nameX, nameY):
        """
        :param nameX: nombre selecciona
        :param nameY:
        :return:
        """
        df = StatisticsController.get_allData(data.df_X)
        df_dispersion = pd.merge(df[nameX], df[nameY], left_on=nameX, right_on=nameY)
        return df_dispersion

    def parse_contents(self, contents, filename, date):
        """
        :param contents: contenido en base 64
        :param filename: Nombre del archivo
        :param date: Fecha
        :return:Retorna un Div del contenido del archivo
        """
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)

        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                df_X = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
                self.generate_statistics(df_X)

            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                df_X = pd.read_excel(io.BytesIO(decoded))
                self.generate_statistics(df_X)

        except Exception as e:
            print(e)
            return not_succesfull_upload( )

        return succesfull_upload(filename, date)

    def get_correlation(self):
        if not initialization.df_data.empty:
            df = Statistics().correlation_pearson_pairs(initialization.df_data)
            return df
