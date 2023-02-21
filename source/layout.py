import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc


def sidebar() -> html.Div:
    """ Contains the layer of the left sidebar"""
    div = html.Div(
        className="sidebar container",
        children=[]
        )
    return div


def content_bar() -> html.Div:
    """ Contains the layer of the content"""
    div = html.Div(
        className="content container",
        children=[]
        )
    return div


def main_layout(app: Dash) -> html.Div:
    """ Contains the outer layer of the layout"""
    div = html.Div(
        className="main_body",
        children=[
            sidebar(),
            content_bar(),
            ]
        )

    return div
