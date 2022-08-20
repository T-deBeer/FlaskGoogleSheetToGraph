from flask import render_template, url_for, flash, redirect
from website import app
from website.sheets import fig
import json
import plotly
import plotly.express as px


@app.route("/")
def main():
    graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dash.html', graph=graph)