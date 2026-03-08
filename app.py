# app.py
# Main Streamlit Dashboard

import streamlit as st
import pandas as pd
from utils.analysis import (
    load_data, get_kpis, sales_by_category,
    sales_by_region, monthly_sales_trend,
    top_cities, profit_by_category, filter_data
)
from charts import (
    bar_chart_category, line_chart_monthly,
    pie_chart_region, bar_chart_cities,
    bar_chart_profit, scatter_sales_profit
)

# ══════════════════════════════════════════
# PAGE CONFIG
# ══════════════════════════════════════════
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# ══════════════════════════════════════════
# CUSTOM CSS
# ══════════════════════════════════════════
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .kpi-card {
    background: linear-gradient(135deg, #1e3a5f, #2E86AB);
    padding: 10px 5px;
    border-radius: 12px;
    text-align: center;
    color: white;
    margin: 3px;
}
.kpi-value {
    font-size: 20px;
    font-weight: bold;
    color: #00d4ff;
}
.kpi-label {
    font-size: 11px;
    color: #aaaaaa;
    margin-top: 3px;
}
    </style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════
# LOAD DATA
# ══════════════════════════════════════════
df = load_data()

# ══════════════════════════════════════════
# SIDEBAR FILTERS
# ══════════════════════════════════════════
st.sidebar.image(
    "https://img.icons8.com/color/96/combo-chart--v2.png",
    width=80
)
st.sidebar.title("📊 Dashboard Filters")
st.sidebar.markdown("---")

# Region filter
all_regions = sorted(df['Region'].unique().tolist())
selected_regions = st.sidebar.multiselect(
    "🌍 Select Region",
    options=all_regions,
    default=all_regions
)

# Category filter
all_categories = sorted(df['Category'].unique().tolist())
selected_categories = st.sidebar.multiselect(
    "📦 Select Category",
    options=all_categories,
    default=all_categories
)

# Year filter
all_years = sorted(df['Year'].unique().tolist())
selected_years = st.sidebar.multiselect(
    "📅 Select Year",
    options=all_years,
    default=all_years
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Total Records:**")
st.sidebar.info(f"📋 {len(df)} orders loaded")

# Apply filters
df_filtered = filter_data(df, selected_regions, selected_categories, selected_years)

# ══════════════════════════════════════════
# MAIN DASHBOARD TITLE
# ══════════════════════════════════════════
st.title("📊 Superstore Sales Dashboard")
st.markdown("Interactive analysis of sales, profit and orders across regions and categories.")
st.markdown("---")

# ══════════════════════════════════════════
# KPI CARDS ROW
# ══════════════════════════════════════════
kpis = get_kpis(df_filtered)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">${kpis['Total Sales']:,.0f}</div>
            <div class="kpi-label">💰 Total Sales</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">${kpis['Total Profit']:,.0f}</div>
            <div class="kpi-label">📈 Total Profit</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{kpis['Total Orders']:,}</div>
            <div class="kpi-label">🛒 Total Orders</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{kpis['Total Quantity']:,}</div>
            <div class="kpi-label">📦 Total Quantity</div>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">${kpis['Avg Order Value']:,.0f}</div>
            <div class="kpi-label">🎯 Avg Order Value</div>
        </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{kpis['Profit Margin']}%</div>
            <div class="kpi-label">💹 Profit Margin</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ══════════════════════════════════════════
# ROW 1 — Bar Chart + Pie Chart
# ══════════════════════════════════════════
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        bar_chart_category(sales_by_category(df_filtered)),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        pie_chart_region(sales_by_region(df_filtered)),
        use_container_width=True
    )

# ══════════════════════════════════════════
# ROW 2 — Line Chart (full width)
# ══════════════════════════════════════════
st.plotly_chart(
    line_chart_monthly(monthly_sales_trend(df_filtered)),
    use_container_width=True
)

# ══════════════════════════════════════════
# ROW 3 — Top Cities + Profit Chart
# ══════════════════════════════════════════
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        bar_chart_cities(top_cities(df_filtered)),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        bar_chart_profit(profit_by_category(df_filtered)),
        use_container_width=True
    )

# ══════════════════════════════════════════
# ROW 4 — Scatter Plot (full width)
# ══════════════════════════════════════════
st.plotly_chart(
    scatter_sales_profit(df_filtered),
    use_container_width=True
)

# ══════════════════════════════════════════
# DATA TABLE
# ══════════════════════════════════════════
st.markdown("---")
st.subheader("📋 Raw Data Table")

st.dataframe(
    df_filtered[[
        'Order ID', 'Order Date', 'Region',
        'Category', 'Sub-Category', 'Sales',
        'Profit', 'Quantity', 'Discount'
    ]].sort_values('Order Date', ascending=False),
    use_container_width=True,
    height=300
)

st.markdown("---")
st.caption("📊 Data Analysis Dashboard | Built with Python, Pandas & Streamlit")
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**🛠️ Built With**")
    st.markdown("Python • Pandas • Plotly • Streamlit")
with col2:
    st.markdown("**📊 Dataset**")
    st.markdown("Superstore Sales • 1000 Records • 2021-2023")
with col3:
    st.markdown("**👨‍💻 Project**")
    st.markdown("Data Analysis Dashboard • BTech Project")