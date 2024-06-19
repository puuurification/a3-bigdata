import dash
import dash_bootstrap_components as dbc
# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output, State

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots


df_gdp = pd.read_csv('data/GDP_interpolated.csv')
df_obesity = pd.read_csv('data/obesity-cleaned.csv')

country_gdp = df_gdp.Country.unique().tolist()
region_gdp = df_gdp.Region.unique().tolist()
year_gdp = df_gdp.year.unique().tolist()

country_obesity = df_obesity.Country.unique().tolist()
year_obesity = df_obesity.year.unique().tolist()
sex_obesity = df_obesity.Sex.dropna().unique().tolist()

mean_male = round(df_obesity[df_obesity['Sex'] == 'Male'].describe().loc["mean","Obesity"],2)
std_male = round(df_obesity[df_obesity['Sex'] == 'Male'].describe().loc["std","Obesity"],2)
mean_female = round(df_obesity[df_obesity['Sex'] == 'Female'].describe().loc["mean","Obesity"],2)
std_female = round(df_obesity[df_obesity['Sex'] == 'Female'].describe().loc["std","Obesity"],2)

max_year = df_gdp.year.max()
df_last_year = df_gdp[df_gdp['year'] == max_year]
max_gdp = df_last_year.loc[df_last_year['GDP_pp_cumsum_diff'].idxmax()]

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

SIDEBAR_STYLE = {
    "position": "fixed",
    "padding": "1rem 2rem",
}


sidebar = html.Div(
    [
        dbc.Row(
            [
                html.H5('Dashboard',
                        style={'margin-top': '12px', 'margin-left': '24px'})
                ],
            style={"height": "5vh"},
            className='bg-primary text-white font-italic'
            ),
        dbc.Row(
            [
                html.Div([
                    html.H6('GDP',
                        style={'margin-top': '12px'}),
                    html.P('Country',
                           style={'margin-top': '8px', 'margin-bottom': '4px'},
                           className='font-weight-bold'),
                    dcc.Dropdown(id='country-gdp-dropdown', multi=True,
                                 options=[{'label': x, 'value': x}
                                          for x in country_gdp],
                                 style={'width': '320px'}
                                 ),
                    html.P('Region',
                           style={'margin-top': '16px', 'margin-bottom': '4px'},
                           className='font-weight-bold'),
                    dcc.Dropdown(id='region-gdp-dropdown', multi=False,
                                 options=[{'label': x, 'value': x}
                                          for x in region_gdp],
                                 style={'width': '320px'}
                                 ),
                    html.Button(id='gdp-button', n_clicks=0, children='apply',
                                style={'margin-top': '16px'},
                                className='bg-dark text-white'),
                    html.Hr()
                    ]
                    )
                ],
            style={'height': '30vh', 'margin': '8px'}),
        dbc.Row(
            [
                html.Div([
                    html.H6('OBESITY',
                        style={'margin-top': '12px'}),
                    html.P('Country',
                           style={'margin-top': '8px', 'margin-bottom': '4px'},
                           className='font-weight-bold'),
                    dcc.Dropdown(id='country-obesity-dropdown', multi=True,
                                 options=[{'label': x, 'value': x}
                                          for x in country_obesity],
                                 style={'width': '320px'}
                                 ),
                    html.P('Sex',
                           style={'margin-top': '16px', 'margin-bottom': '4px'},
                           className='font-weight-bold'),
                    dcc.Dropdown(id='sex-obesity-dropdown', multi=True,
                                 options=[{'label': x, 'value': x}
                                          for x in sex_obesity],
                                 style={'width': '320px'}
                                 ),
                    html.Button(id='obesity-button', n_clicks=0, children='apply',
                                style={'margin-top': '16px'},
                                className='bg-dark text-white'),
                    html.Hr()
                    ]
                    )
                ],
            style={'height': '30vh', 'margin': '8px'}),
        dbc.Row(
            [
                html.Div([])
                ],
            style={'height': '35vh', 'margin': '8px'}),
        ],
        style=SIDEBAR_STYLE,
    )

@app.callback(
    Output('region-gdp-dropdown', 'disabled'),
    Input('country-gdp-dropdown', 'value'),
    prevent_initial_call=True
)
def set_region_options(value):
    if value is None or len(value) == 0:
        return False
    else:
        return True
    
@app.callback(
    Output('country-gdp-dropdown', 'disabled'),
    Input('region-gdp-dropdown', 'value'),
    prevent_initial_call=True
)
def set_country_options(value):
    if value is None or len(value) == 0:
        return False
    else:
        return True
    
content = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div([
                            dbc.Card(
                                [
                                dbc.CardHeader("Media Obesidade Masculina"),
                                dbc.CardBody(
                                    [
                                        html.H4(f"{mean_male}", className="card-title"),
                                    ]
                                )
                            ],
                            style={"width": "15rem","text-align": "center", "height": "10rem"},
                            )
                                      ])
                        ]),
                dbc.Col(
                    [
                        html.Div([
                            dbc.Card(
                                [
                                dbc.CardHeader("Desvio Padrão Obesidade Masculina"),
                                dbc.CardBody(
                                    [
                                        html.H4(f"{std_male}", className="card-title")
                                    ]
                                )
                            ],
                            style={"width": "15rem","text-align": "center", "height": "10rem"},
                            )
                                      ])
                        ]),
                dbc.Col(
                    [
                        html.Div([
                            dbc.Card(
                                [
                                dbc.CardHeader("Media Obesidade Feminina"),
                                dbc.CardBody(
                                    [
                                        html.H4(f"{mean_female}", className="card-title")
                                    ]
                                )
                            ],
                            style={"width": "15rem","text-align": "center", "height": "10rem"},
                            )
                                      ])
                        ]),
                dbc.Col(
                    [
                        html.Div([
                            dbc.Card(
                                [
                                dbc.CardHeader("Desvio Padrão Obesidade Feminina"),
                                dbc.CardBody(
                                    [
                                        html.H4(f"{std_female}", className="card-title")
                                    ]
                                )
                            ],
                            style={"width": "15rem","text-align": "center", "height": "10rem"},
                            )
                                      ])
                        ]),
                dbc.Col(
                    [
                        html.Div([
                            dbc.Card(
                                [
                                dbc.CardHeader("Maior Crecimento de PIB"),
                                dbc.CardBody(
                                    [
                                        html.H4(f"{max_gdp.iloc[6]}", className="card-title"),
                                        html.P(f"{max_gdp.iloc[1]}", className="card-text"),
                                    ]
                                )
                            ],
                            style={"width": "15rem","text-align": "center", "height": "10rem"},
                            )
                                      ])
                        ])
            ],
            style={'height': '20vh',
                   'margin-top': '16px', 'margin-left': '8px',
                   'margin-bottom': '8px', 'margin-right': '8px'}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div([
                            dcc.Graph(id="line1-chart",
                                      className='bg-light')])
                        ])
            ],
            style={'height': '50vh', 'margin': '8px'}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div([
                            dcc.Graph(id='bar1-chart',
                                      className='bg-light')])
                    ])
            ],
            style={'height': '50vh', 'margin': '8px'}
            ),
            dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div([
                            dcc.Graph(id='line2-chart',
                                      className='bg-light')])
                    ])
            ],
            style={'height': '50vh', 'margin': '8px'}
            ),
            dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div([
                            dcc.Graph(id='line3-chart',
                                      className='bg-light')])
                    ])
            ],
            style={'height': '50vh', 'margin': '8px'}
            ),
            dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div([
                            dcc.Graph(id='line4-chart',
                                      className='bg-light')])
                    ])
            ],
            style={'height': '50vh', 'margin': '8px'}
            ),
            dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div([
                            dcc.Graph(id='bar2-chart',
                                      className='bg-light')])
                    ])
            ],
            style={'height': '50vh', 'margin': '8px'}
            )
        ]
    )

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(sidebar, width=3, className='bg-light'),
                dbc.Col(content, width=9)
                ]
            ),
        ],
    fluid=True
    )

@app.callback(Output('line1-chart', 'figure'),
              Input('obesity-button', 'n_clicks'),
              State('country-obesity-dropdown', 'value'),
              State('sex-obesity-dropdown', 'value'),
              )
def update_bar(n_clicks, country_value,sex_value):
    if country_value in ([], None) and sex_value in ([], None):
        fig_line = px.line(title='Obesidade')
    else:
        line_df = df_obesity
        if country_value not in ([], None):
            line_df = line_df[line_df['Country'].isin(country_value)]
        if sex_value not in ([], None):
            line_df = line_df[line_df['Sex'].isin(sex_value)]

        fig_line = px.line(line_df, x="year", y="Obesity", color="Country", facet_row="Sex", markers=True, title='Obesidade')

    return fig_line

@app.callback(Output('bar1-chart', 'figure'),
              Input('obesity-button', 'n_clicks'),
              State('country-obesity-dropdown', 'value'),
              State('sex-obesity-dropdown', 'value'),
              )
def update_bar(n_clicks, country_value,sex_value):
    if country_value in ([], None) and sex_value in ([], None):
        fig_line = px.bar(title='Taxa de aumento de índices de obesidade no período completo')
    else:
        max_year = df_obesity.year.max()
        line_df = df_obesity.query(f"year == {max_year}")
        if country_value not in ([], None):
            line_df = line_df[line_df['Country'].isin(country_value)]
        if sex_value not in ([], None):
            line_df = line_df[line_df['Sex'].isin(sex_value)]

        fig_line = make_subplots(rows=3, cols=1)

        for index,sex in enumerate(line_df.Sex.unique().tolist()):
            df_filtered = line_df[line_df["Sex"] == sex]
            fig_line.append_trace(go.Bar(
            x=df_filtered.Country.tolist(),
            y=df_filtered.obesity_cumsum_diff.tolist(),
            name = sex
            ), row=index+1, col=1)

        fig_line.update_layout(title_text="Taxa de aumento de índices de obesidade no período completo")

    return fig_line

@app.callback(Output('line2-chart', 'figure'),
              Input('obesity-button', 'n_clicks'),
              State('country-obesity-dropdown', 'value'),
              State('sex-obesity-dropdown', 'value'),
              )
def update_bar(n_clicks, country_value,sex_value):
    if country_value in ([], None) and sex_value in ([], None):
        fig_line = px.line(title='Taxa de aumento de índices de obesidade')
    else:
        line_df = df_obesity
        if country_value not in ([], None):
            line_df = line_df[line_df['Country'].isin(country_value)]
        if sex_value not in ([], None):
            line_df = line_df[line_df['Sex'].isin(sex_value)]

        fig_line = px.line(line_df, x="year", y="obesity_diff", color="Country", facet_row="Sex", markers=True, title='Taxa de aumento de índices de obesidade')

    return fig_line

@app.callback(Output('line3-chart', 'figure'),
              Input('gdp-button', 'n_clicks'),
              State('country-gdp-dropdown', 'value'),
              State('region-gdp-dropdown', 'value'),
              )
def update_bar(n_clicks, country_value,region_value):
    if country_value in ([], None) and region_value == None:
        fig_line = px.line(title='PIB per capita')
    else:
        line_df = df_gdp
        if country_value not in ([], None):
            line_df = line_df[line_df['Country'].isin(country_value)]
        if region_value != None:
            line_df = line_df[line_df['Region'] == region_value]

        fig_line = px.line(line_df,
                        x="year",
                        y="GDP_pp",
                        color="Country",
                        title='PIB per capita',
                        markers=True)

    return fig_line

@app.callback(Output('bar2-chart', 'figure'),
              Input('gdp-button', 'n_clicks'),
              State('country-gdp-dropdown', 'value'),
              State('region-gdp-dropdown', 'value'),
              )
def update_bar(n_clicks, country_value,region_value):
    if country_value in ([], None) and region_value == None:
        fig_line = px.bar(title='Taxa de aumento de índices de PIB no período completo')
    else:
        max_year = df_gdp.year.max()
        line_df = df_gdp.query(f"year == {max_year}")
        if country_value not in ([], None):
            line_df = line_df[line_df['Country'].isin(country_value)]
        if region_value != None:
            line_df = line_df[line_df['Region'] == region_value]

        fig_line = px.bar(line_df,
                        x="Country",
                        y="GDP_pp_cumsum_diff",
                        color="Country",
                        title='Taxa de aumento de índices de PIB no período completo')

    return fig_line

@app.callback(Output('line4-chart', 'figure'),
              Input('gdp-button', 'n_clicks'),
              State('country-gdp-dropdown', 'value'),
              State('region-gdp-dropdown', 'value'),
              )
def update_bar(n_clicks, country_value,region_value):
    if country_value in ([], None) and region_value == None:
        fig_line = px.line(title='Taxa de aumento de indice PIB')
    else:
        line_df = df_gdp
        if country_value not in ([], None):
            line_df = line_df[line_df['Country'].isin(country_value)]
        if region_value != None:
            line_df = line_df[line_df['Region'] == region_value]

        fig_line = px.line(line_df,
                        x="year",
                        y="GDP_pp_diff",
                        color="Country",
                        title='Taxa de aumento de indice PIB',
                        markers=True)

    return fig_line

if __name__ == "__main__":
    app.run_server(debug=True, port=1234)