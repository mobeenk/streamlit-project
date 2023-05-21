import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder

def render_html(value):
    return f"<strong>{value}</strong>"

data = [
    {"name": "John", "age": 28, "city": "New York"},
    {"name": "Jane", "age": 35, "city": "Boston"},
    {"name": "Bill", "age": 42, "city": "Los Angeles"},
]

options = GridOptionsBuilder.from_dataframe(data)
options = options.build()

# set the cell renderer for the 'name' column
options.columnDefs[0].cellRenderer = "renderHtml"

grid_result = AgGrid(
    data,
    gridOptions=options,
    cell_renderer={
        "renderHtml": {"renderer": f"<strong>wwwww</strong>"}
    }
)
