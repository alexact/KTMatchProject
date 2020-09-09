import pandas as pd
from sklearn import datasets


class DataModel:
    x, y = datasets.make_moons(
        n_samples=200,
        noise=0.6,
        random_state=0
    )
    df_X = pd.DataFrame(datasets.make_moons(
        n_samples=200,
        noise=0.6,
        random_state=0
    ))

    def __init__(self):
        self.df_X = DataModel.df_X

    def get_df_X(self):
        return self.df_X

    def set_df_X(self, df_X):
        self.df = df_X
        return df_X

    def data(self):
        """
        Recibe el archivo en formato csv de los resultados de la encuesta
        :return: Retorna el archivo con los puntajes de las ecuestas
        """
        file = pd.read_csv('dataInit.csv',
                           encoding='unicode_escape')
        return file

    def file_variables_title(self):
        """
        Recibe el archivo en formato csv de los titulos para el nuevo DataFrame( se usa para los dropdown)
        :return: Retorna el archivo con los titulos
        """
        file = pd.read_csv('dataTituloVariables.csv',
                           encoding='unicode_escape')
        print("TYPE FILE", type(file))
        return file
