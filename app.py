import dash
from source.layout import main_layout


def main_app() -> None:
    """ Function to be run when app execution"""
    app = dash.Dash()
    app.layout = main_layout(app)

    # Callback will be here

    app.run_server(debug=True)


if __name__ == "__main__":
    main_app()
