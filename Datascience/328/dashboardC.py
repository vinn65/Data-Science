import plotly.graph_objs as go
import plotly.colors as colors
from plotly.subplots import make_subplots
import pandas as pd
import plotly.io as pio
import webbrowser

# Load Mall Customer Segmentation Data from CSV file
df = pd.read_csv('Mall_Customers.csv')

# Create scatter plot showing Annual Income vs Spending Score, with different colors for each Gender
scatter_fig = go.Figure()
for gender in df['Gender'].unique():
    df_gender = df[df['Gender'] == gender]
    scatter_fig.add_trace(go.Scatter(
        x=df_gender['Annual Income (k$)'],
        y=df_gender['Spending Score (1-100)'],
        mode='markers',
        marker=dict(
            color=colors.qualitative.Plotly[df['Gender'].unique().tolist().index(gender)],
            size=10,
            opacity=0.8
        ),
        name=gender
    ))

# Create dashboard with one row and one column
dashboard = make_subplots(rows=1, cols=1)

# Add scatter plot to dashboard
for trace in scatter_fig.data:import plotly.graph_objs as go
import plotly.colors as colors
from plotly.subplots import make_subplots
import pandas as pd
import plotly.io as pio
import webbrowser

# Load Mall Customer Segmentation Data from CSV file
df = pd.read_csv('Mall_Customers.csv')

# Create scatter plot showing Annual Income vs Spending Score, with different colors for each Gender
scatter_fig = go.Figure()
for gender in df['Gender'].unique():
    df_gender = df[df['Gender'] == gender]
    scatter_fig.add_trace(go.Scatter(
        x=df_gender['Annual Income (k$)'],
        y=df_gender['Spending Score (1-100)'],
        mode='markers',
        marker=dict(
            color=colors.qualitative.Plotly[df['Gender'].unique().tolist().index(gender)],
            size=10,
            opacity=0.8
        ),
        name=gender
    ))

# Create dashboard with one row and one column
dashboard = make_subplots(rows=1, cols=1)

# Add scatter plot to dashboard
for trace in scatter_fig.data:
    dashboard.add_trace(trace, row=1, col=1)

# Update dashboard layout
dashboard.update_layout(
    title='Mall Customer Segmentation Data Analysis Dashboard',
    height=600,
    showlegend=True,
    xaxis_title='Annual Income (k$)',
    yaxis_title='Spending Score (1-100)',
    margin=dict(l=50, r=50, t=50, b=50)
)

# Generate HTML code for dashboard
html = pio.to_html(dashboard, include_plotlyjs='cdn')

# Save dashboard to HTML file
with open('mall_customers_dashboard.html', 'w') as f:
    f.write(html)

# Open dashboard in default web browser
webbrowser.open('mall_customers_dashboard.html')

    dashboard.add_trace(trace, row=1, col=1)

# Update dashboard layout
dashboard.update_layout(
    title='Mall Customer Segmentation Data Analysis Dashboard',
    height=600,
    showlegend=True,
    xaxis_title='Annual Income (k$)',
    yaxis_title='Spending Score (1-100)',
    margin=dict(l=50, r=50, t=50, b=50)
)

# Generate HTML code for dashboard
html = pio.to_html(dashboard, include_plotlyjs='cdn')

# Save dashboard to HTML file
with open('mall_customers_dashboard.html', 'w') as f:
    f.write(html)

# Open dashboard in default web browser
webbrowser.open('mall_customers_dashboard.html')
