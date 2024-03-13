import os
import psycopg2
import plotly.graph_objs as go

# Database connection parameters
db_params = {
    'dbname': os.environ.get('DB_NAME', 'mmmaaa'),
    'user': os.environ.get('DB_USER', 'mmmaaa'),
    'password': os.environ.get('DB_PASSWORD', 'Maal97900'),
    'host': os.environ.get('DB_HOST', 'localhost'),
    'port': os.environ.get('DB_PORT', 5432),
}

# Connect to the database
conn = psycopg2.connect(**db_params)

# Query data from the database
cursor = conn.cursor()
cursor.execute("SELECT time, red FROM ryb")
data = cursor.fetchall()

# Separate x and y values
x_values = [row[0] for row in data]
y_values = [row[1] for row in data]

# Create a Plotly scatter plot
fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='markers'))

# Customize the layout (optional)
fig.update_layout(title='Loads', xaxis_title='Time', yaxis_title='Loads')

# Save the chart as an HTML file
fig.write_html('chart.html')
