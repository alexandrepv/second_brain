import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

if __name__ == "__main__":

    data = pd.read_csv("avocado.csv")
    data = data.query("type == 'conventional' and region == 'Albany'")
    data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
    data.sort_values("Date", inplace=True)

    app = dash.Dash(__name__)
    app.run_server(debug=True)