# charts.py
# This file creates all interactive charts using Plotly

import plotly.express as px
import plotly.graph_objects as go

# Colour palette — used across all charts
COLORS = {
    'primary'  : '#2E86AB',   # blue
    'secondary': '#A23B72',   # purple
    'success'  : '#F18F01',   # orange
    'danger'   : '#C73E1D',   # red
    'green'    : '#3B1F2B',   # dark
    'palette'  : ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#44BBA4']
}

# ══════════════════════════════════════════
# CHART 1 — Sales by Category (Bar Chart)
# ══════════════════════════════════════════
def bar_chart_category(df_category):
    fig = px.bar(
        df_category,
        x='Category',
        y='Total Sales',
        color='Category',
        color_discrete_sequence=COLORS['palette'],
        title='💰 Sales by Category',
        text='Total Sales'
    )

    fig.update_traces(
        texttemplate='$%{text:,.0f}',  # format as $12,345
        textposition='outside'
    )

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',   # transparent background
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        title_font_size=18,
        height=400
    )

    return fig


# ══════════════════════════════════════════
# CHART 2 — Monthly Sales Trend (Line Chart)
# ══════════════════════════════════════════
def line_chart_monthly(df_monthly):
    fig = px.line(
        df_monthly,
        x='Period',
        y='Total Sales',
        color='Year',
        color_discrete_sequence=COLORS['palette'],
        title='📈 Monthly Sales Trend',
        markers=True        # show dots on each data point
    )

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title_font_size=18,
        height=400,
        xaxis_tickangle=-45  # tilt x labels so they don't overlap
    )

    return fig


# ══════════════════════════════════════════
# CHART 3 — Sales by Region (Pie Chart)
# ══════════════════════════════════════════
def pie_chart_region(df_region):
    fig = px.pie(
        df_region,
        names='Region',
        values='Total Sales',
        color_discrete_sequence=COLORS['palette'],
        title='🌍 Sales by Region',
        hole=0.4            # makes it a donut chart
    )

    fig.update_traces(
        textposition='inside',
        textinfo='percent+label'
    )

    fig.update_layout(
        title_font_size=18,
        height=400
    )

    return fig


# ══════════════════════════════════════════
# CHART 4 — Top 5 Cities (Horizontal Bar)
# ══════════════════════════════════════════
def bar_chart_cities(df_cities):
    fig = px.bar(
        df_cities,
        x='Total Sales',
        y='City',
        orientation='h',    # horizontal bars
        color='Total Sales',
        color_continuous_scale='Blues',
        title='🏙️ Top 5 Cities by Sales',
        text='Total Sales'
    )

    fig.update_traces(
        texttemplate='$%{text:,.0f}',
        textposition='outside'
    )

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title_font_size=18,
        height=400,
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'}
    )

    return fig


# ══════════════════════════════════════════
# CHART 5 — Profit by Category (Bar Chart)
# ══════════════════════════════════════════
def bar_chart_profit(df_profit):
    # Add color — green for positive, red for negative profit
    df_profit['Color'] = df_profit['Total Profit'].apply(
        lambda x: 'Profit' if x > 0 else 'Loss'
    )

    fig = px.bar(
        df_profit,
        x='Category',
        y='Total Profit',
        color='Color',
        color_discrete_map={
            'Profit': '#44BBA4',   # green
            'Loss'  : '#C73E1D'    # red
        },
        title='📊 Profit by Category',
        text='Total Profit'
    )

    fig.update_traces(
        texttemplate='$%{text:,.0f}',
        textposition='outside'
    )

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title_font_size=18,
        height=400,
        showlegend=True
    )

    return fig


# ══════════════════════════════════════════
# CHART 6 — Sales vs Profit (Scatter Plot)
# ══════════════════════════════════════════
def scatter_sales_profit(df):
    fig = px.scatter(
        df,
        x='Sales',
        y='Profit',
        color='Category',
        size='Quantity',    # bubble size = quantity
        color_discrete_sequence=COLORS['palette'],
        title='🔵 Sales vs Profit by Category',
        hover_data=['City', 'Region']  # show on hover
    )

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title_font_size=18,
        height=400
    )

    return fig