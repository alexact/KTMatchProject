import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


class Description:
    def description_frec_table(self):
        """
        :return:Retorna la visualización descripción para la estadística básica para la tabla de frecuencias
        """
        return dbc.Card([
            dbc.CardHeader("Tips"),
            dbc.CardBody(
                dbc.Row([
                    dbc.Col([
                        html.H1('Tabla de frecuencia', className="card-title"),
                        html.P(
                            'En ella puedes verificar cual es la media, la desviación, los máximos y minimos de los datos.'),
                        html.H3('Qué es 25%, 50% y 75%  ?', className="card-subtitle"),
                        html.P('Son percentiles y permite saber cómo está situado un valor en función de una muestra.',
                               className="card-text"),
                        html.P('Se divide el 100% de la muestra en 3, dando como resultado 25%, 50% y 75%.',
                               className="card-text"),
                        html.P('El 50% es la mediana.', className="card-text"),
                    ]),
                    dbc.Col([
                        html.Br( ),
                        html.Br( ),
                        html.H3('Interpretación:', className="card-subtitle"),
                        html.P(
                            '- El 25% de los trabajadores consideran que para la variable "Disinterest" existe una severidad de...',
                            className="card-text"),
                        html.P(
                            '- El 50% de los trabajadores consideran que para la variable "Disinterest" existe una severidad de...',
                            className="card-text"),
                        html.P(
                            '- El 75% de los trabajadores consideran que para la variable "Disinterest" existe una severidad de...',
                            className="card-text")
                    ])
                ])
            )
        ], color="success", inverse=True, style={"width": "100%", 'marginTop': '30px', 'marginBottom': '30px'})

    def description_scatter_plot(self):
        """
        :return:Retorna la visualización de la descripción para la estadística básica para la gráfica de correlación
        """
        return dbc.Card([
            dbc.CardHeader("Tips"),
            dbc.CardBody(
                [html.Div([
                    html.H1('Gráfica de dispersión', className="card-title"),
                    html.P(
                        'Nos ayuda a identificar entre dos variables de estudio '
                        'que tan dispersos se encuentran los datos unos de otros así como la relación que tienen esas dos varibales'),
                    html.P(
                        'Cambia con la lista desplegable las variables'),
                    html.H3('Comportamiento a analizar', className="card-subtitle"),
                    html.Br( ),
                    html.P('¿Los puntos de la gráfica denotan una tendencia?',
                           className="card-text"),
                    html.P('¿Los puntos de la gráfica se concentran en una zona especifica?',
                           className="card-text"),
                    html.H3('Interpretación:', className="card-subtitle"),
                    html.Br( ),
                    html.P(
                        '- El que los puntos de la gráfica tengan un comportamiento similar significa que se acercan'
                        ' a comportarse de manera normal lo que hace posible usar la estadística para su estudio',
                        className="card-text"),
                    html.P(
                        'Al medir la severidad= Impacto x Fecuencia, entre dos variables se relacionan los puntajes de '
                        'significa que de acuerdo a la información de la encuesta:',
                        className="card-text"),
                    html.P(
                        '   - A medida que aumenta la variable X, la variable Y se ve afectada de manera proporcional, '
                        '   inversamente proporcional, no se define un comportamiento',
                        className="card-text")
                ])]
            )
        ], color="info", inverse=True, style={"width": "100%", 'marginTop': '30px', 'justify': 'center'}, )

    def heatmap_plot(self):
        """
        :return:Retorna el tip para el mapa de calor de correlación de las variables
        """
        return dbc.Card([
            dbc.CardHeader("Tips"),
            dbc.CardBody(
                dbc.Row([
                    dbc.Col([
                        html.H1('Mapa de calor - Correlación entre variables', className="card-title"),
                        html.P(
                            'Nos muestra que tanta incidencia tiene positiva o negativamente una variable sobre otra'),
                        html.P(
                            'los colores representan los valores enre 1 y -1 para la correlación de Pearson'),
                        html.H3('Comportamiento a analizar', className="card-subtitle"),
                        html.Br( ),
                        html.P('¿Cuáles son las variables que tienen los colores más cercanos a 1 o -1 '
                               'sin tenere en cuenta la diagonal donde se une la misma variable desde el eje X y Y?',
                               className="card-text"),
                        html.P('¿Tiene lógica en el proceso de negocio esta correlación?',
                               className="card-text"),
                    ]),
                    dbc.Col([
                        html.H3('Interpretación:', className="card-subtitle"),
                        html.Br( ),
                        html.P(
                            '- Si los colores se acercan a 1 significa que tiene una correlación positiva',
                            className="card-text"),
                        html.P(
                            '- Si los colores se acercan a 0 significa que tienen muy poca correlación',
                            className="card-text"),
                        html.P(
                            '- Si los colores se acercan a -1 significa que tiene una correlación negativa',
                            className="card-text"),
                        html.P(
                            'Analizar si aquellas variables se pueden convertir en la causa de su correlación',
                            className="card-text")
                    ])]
                ))
        ], color="secondary", inverse=True
        )

    def collapse_graph_description(self):
        """
        :return:Despliega el tip para las graficas de dispersión
        """
        collapse = html.Div(
            [
                dbc.Button(
                    "Abrir tip 1",
                    id="collapse-button",
                    className="mb-3",
                    color="info",
                ),
                dbc.Collapse(
                    [
                        self.description_scatter_plot( )
                    ], id="collapse"
                ),
            ],
        )
        return collapse

    def description_about_app(self):
        """
        :return:Retorna la visualización de las intrucciones para el aplicativo
        """
        return dbc.Card([
            dbc.CardHeader("Sobre KTMath"),
            dbc.CardBody(
                [html.Div([
                    html.H1('Como usar KtMath', className="card-title"),
                    html.Br( ),
                    html.H2('Gestión del conocimiento con inteligencia matemática'),
                    html.Ol('- Fugas en transferencia de conocimiento en tu empresa?'),
                    html.Ol('- Conoces las causas?'),
                    html.Ol('- Quisieras reconocer de manera cuantitativa este tipo de problemáticas?'),
                    html.Ol('- Generar un control de la gestión del conocimiento'),
                    html.Br( ),
                    html.H2('¿Qué es KTmat?', className="card-subtitle"),
                    html.P('KTmat es una herramienta diseñada para facilitar a las empresas y a '
                           'personas dedicadas a la gestión del conocimiento el diagnostico de problematicas '
                           'que se encuentran en la transferencia de conocimiento utilizando herramientas estadísticas'
                           ' y de machine learning para mejorar su precisión.',
                           className="card-text"),
                    html.Br( ),
                    html.H2('¿Qué proceso realiza KTmat?', className="card-subtitle"),
                    html.P('A partir de información recolectada por medio de encuestas que cumplen una estructura '
                           'especifica de la que se extraen las posibles problemáticas de la empresa, *KTmat* utiliza'
                           ' herramientas estadisticas para filtrar dichas variables y encontrar su correlación para p'
                           'osteriormente evaluar por medio del algoritmo de machine learning llamada Maquina de vectores'
                           ' de soporte si la empresa tiene o no gestión del conocimiento y si las variables generan un '
                           'patrón definido.', className="card-text"),
                    html.Br( ),
                    html.H2('¿En que información se basa KTmat?', className="card-subtitle"),
                    html.P('KTmat se basa en un conjunto de variables',
                           className="card-text"),
                ])]
            )
        ], color="info", inverse=True, style={"width": "100%", 'marginTop': '30px', 'justify': 'center'}, )

    def description_instruction(self):
        """
        :return:Retorna la visualización de las intrucciones para el aplicativo
        """
        return dbc.Card([
            dbc.CardHeader("Paso a paso"),
            dbc.CardBody(
                [html.Div([
                    html.H1('Como usar KtMath', className="card-title"),
                    html.Br( ),
                    html.Ol('1. Selecciona una de las dos pestañas para analizar los datos, se recomienda comenzar con '
                            '"Cuál es la estadística?" y posteriormente con "Algoritmo SVM"'),
                    html.Ol(
                        '2. Cargue un archivo en formato .csv que cumpla con las condiciones en la barra de carga para la'
                        'pestaña seleccionada'),
                    html.Ol('3. analice las graficas y tablas de acuerdo a los tips'),
                    html.Ol('4. Seleccione las distintas variables en pares de su archivo para analizar el comportamiento'),
                    html.Br( ),
                    html.H3('Archivo base', className="card-subtitle"),
                    html.Br( ),
                    html.P(
                        'El archivo base en formato csv tendrá en la primera fila las variables que se identifican como '
                        'problemas que afectan la transferencia de conocimiento siendo la ultima de ellas la que define si'
                        'la empresa tiene o no gestión del conocimiento. Cada variable se repetirá dos veces teniendo el nombre'
                        'de la variable seguido de nombreVariable_Impacto, nombreVariable_frecuencia'
                        'Las otras filas serán los resultados de la encuesta realizada donde cada columna tendrá valores de 0 a 5'
                        'excepto en la ultima columna que tendrá valores entre SI, No, No sé, como se muestra en la imagen',
                        className="card-text"),
                    html.Br( ),
                    html.H3('Pestaña ¿Cuál es la estadística?', className="card-subtitle"),
                    html.P('En esta pestaña existen 3 tipos de gráficas y una tabla de frecuencia.',
                           className="card-text"),
                    html.P(
                        'La gráfica de dispersión y el diagrama de barras permitirá reconocer el comportamiento de las variables'
                        ' analizando por pares, la tabla de frecuencia mostrará los valores maximos, minimos, la media de cada variables'
                        'y los percentiles. Por último, la grafica de correlación represantada en un mapa de calor permitirá entender la'
                        'relación entre variables y su dependencia',
                        className="card-text"),
                    html.Br( ),
                    html.H3('Pestaña Algoritmo SVM', className="card-subtitle"),
                    html.P(
                        'En esta pestaña se encuentra el análisis por mapa de calor de dos variables, en esta gráfica se verá la clasificación'
                        'dentro del hiperplano y se visualizará cuales datos tanto del porcentaje utilizado para probar como el de entrenamiento'
                        ' se encuentra como parte del porcentaje de error de la clasificación',
                        className="card-text"),
                ])]
            )
        ], color="light", inverse=False, style={"width": "100%", 'marginTop': '30px', 'justify': 'center'}, )
