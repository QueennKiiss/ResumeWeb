"""
Main module for application launch
"""

import dash
import dash_bootstrap_components as dbc

from source import layout, callbacks

def main_app() -> None:
    """ Function to be run when app execution"""
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

    app.layout = layout.main_layout(app)
    app.config.suppress_callback_exceptions = True

    # Callback will be here
    callbacks.modify_navlink_style(app)
    callbacks.show_resume_content(app)

    app.run_server(debug=True)


if __name__ == '__main__':
    main_app()