import pandas as pd
import dash
from dash import dash_table
import dash_bootstrap_components as dbc
from dash import html


df = pd.read_csv('dbms.csv')

app = dash.Dash(__name__)

app.layout = dbc.Container([

    dbc.Row([

        dbc.Col([
            dbc.Card([
                dbc.CardBody([

                    html.Div([
                        html.H1(children="Data Table", className="saldash",
                                style={'color': '#00361c', 'text-align': 'center'
                                       })
                    ])

                ])
            ]),
        ], width=14),
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([

                    html.Div([

                        dash_table.DataTable(
                            id='datatable-interactivity',
                            columns=[
                                {"lead_fname": i, "id": i, "deletable": False, "selectable": True, "hideable": True}

                                if i == "lead_fname" or i == "id" or i == "lead_email" or i == "lead_phone" or i == "lead_pincode"

                                   or i == "partner_access_id" or i == "timestamp" or i == "order_id" or i == "invoice_url" or i == "order_status"

                                   or i == "order_delivery_date" or i == "api_method" or i == "flag" or i == "Direct/Converted"

                                else {"lead_fname": i, "id": i, "deletable": False, "selectable": True}

                                for i in df.columns
                            ],
                            data=df.to_dict('records'),  # the contents of the table
                            editable=False,  # allow editing of data inside all cells
                            filter_action="native",  # allow filtering of data by user ('native') or not ('none')
                            sort_action="native",  # enables data to be sorted per-column by user or not ('none')
                            sort_mode="multi",  # sort across 'multi' or 'single' columns
                            column_selectable="multi",  # allow users to select 'multi' or 'single' columns
                            row_selectable="multi",  # allow users to select 'multi' or 'single' rows
                            row_deletable=False,  # choose if user can delete a row (True) or not (False)
                            selected_columns=[],  # ids of columns that user selects
                            selected_rows=[],  # indices of rows that user selects
                            page_action="native",  # all data is passed to the table up-front or not ('none')
                            page_current=0,  # page number that user is on
                            page_size=15,

                            # number of rows visible per page
                            style_cell={  # ensure adequate header width when text is shorter than cell's text
                                'minWidth': 95, 'maxWidth': 95, 'width': 95
                            },

                            style_cell_conditional=[  # align text columns to left. By default they are aligned to right
                                {
                                    'if': {'column_id': c},
                                    'textAlign': 'left'
                                } for c in ['STATE', 'CITY', 'PRODUCT', 'CATEGORY', 'Direct/Converted']
                            ],
                            style_data={  # overflow cells' content into multiple lines
                                'whiteSpace': 'normal'
                            }
                        ),
                    ]),
                ])
            ]),
        ], width=14),

    ]),
])

if __name__ == '__main__':
    app.run_server(debug=False)