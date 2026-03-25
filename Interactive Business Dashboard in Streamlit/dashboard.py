import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

# ─── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Global Superstore Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── CUSTOM CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }
    .main { background-color: #0f1117; }
    .block-container { padding: 2rem 2rem 2rem 2rem; }

    h1, h2, h3 { font-family: 'Syne', sans-serif !important; }

    .kpi-card {
        background: linear-gradient(135deg, #1e2130 0%, #252a3d 100%);
        border: 1px solid #2e3450;
        border-radius: 16px;
        padding: 24px 28px;
        text-align: center;
        box-shadow: 0 4px 24px rgba(0,0,0,0.3);
        transition: transform 0.2s;
    }
    .kpi-card:hover { transform: translateY(-3px); }
    .kpi-label {
        font-size: 13px;
        font-weight: 500;
        color: #8892b0;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    .kpi-value {
        font-family: 'Syne', sans-serif;
        font-size: 32px;
        font-weight: 800;
        color: #e6f1ff;
    }
    .kpi-delta {
        font-size: 13px;
        color: #64ffda;
        margin-top: 6px;
    }
    .section-title {
        font-family: 'Syne', sans-serif;
        font-size: 20px;
        font-weight: 700;
        color: #ccd6f6;
        margin: 32px 0 16px 0;
        padding-left: 12px;
        border-left: 4px solid #64ffda;
    }
    .sidebar-title {
        font-family: 'Syne', sans-serif;
        font-size: 22px;
        font-weight: 800;
        color: #64ffda;
        margin-bottom: 4px;
    }
    .dashboard-header {
        background: linear-gradient(135deg, #1e2130, #252a3d);
        border-radius: 20px;
        padding: 32px 40px;
        margin-bottom: 32px;
        border: 1px solid #2e3450;
    }
    .stSelectbox > div > div { background-color: #1e2130; color: #ccd6f6; }
</style>
""", unsafe_allow_html=True)

# ─── LOAD & CLEAN DATA ─────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("Global_Superstore2.csv", encoding='latin1')
    # Standardise column names
    df.columns = df.columns.str.strip()

    # Parse dates
    for col in ['Order Date', 'Ship Date']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')

    # Drop rows with missing critical fields
    df.dropna(subset=['Sales', 'Profit'], inplace=True)

    # Ensure numeric
    df['Sales']    = pd.to_numeric(df['Sales'],    errors='coerce').fillna(0)
    df['Profit']   = pd.to_numeric(df['Profit'],   errors='coerce').fillna(0)
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0)
    df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce').fillna(0)

    # Derived columns
    df['Year']          = df['Order Date'].dt.year
    df['Month']         = df['Order Date'].dt.to_period('M').astype(str)
    df['Profit Margin'] = (df['Profit'] / df['Sales'].replace(0, np.nan)) * 100

    return df

df = load_data()

# ─── SIDEBAR FILTERS ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-title">🌍 Global Superstore</div>', unsafe_allow_html=True)
    st.markdown("**Interactive Business Dashboard**")
    st.markdown("---")

    st.markdown("### 🔍 Filters")

    regions = ['All'] + sorted(df['Region'].dropna().unique().tolist())
    selected_region = st.selectbox("Region", regions)

    categories = ['All'] + sorted(df['Category'].dropna().unique().tolist())
    selected_category = st.selectbox("Category", categories)

    if selected_category != 'All':
        sub_cats = ['All'] + sorted(df[df['Category'] == selected_category]['Sub-Category'].dropna().unique().tolist())
    else:
        sub_cats = ['All'] + sorted(df['Sub-Category'].dropna().unique().tolist())
    selected_subcat = st.selectbox("Sub-Category", sub_cats)

    years = ['All'] + sorted(df['Year'].dropna().unique().astype(str).tolist())
    selected_year = st.selectbox("Year", years)

    st.markdown("---")
    st.markdown("### 📊 Segment")
    segments = ['All'] + sorted(df['Segment'].dropna().unique().tolist())
    selected_segment = st.selectbox("Segment", segments)

# ─── APPLY FILTERS ─────────────────────────────────────────────────────────────
filtered = df.copy()
if selected_region    != 'All': filtered = filtered[filtered['Region']       == selected_region]
if selected_category  != 'All': filtered = filtered[filtered['Category']     == selected_category]
if selected_subcat    != 'All': filtered = filtered[filtered['Sub-Category'] == selected_subcat]
if selected_year      != 'All': filtered = filtered[filtered['Year']         == int(selected_year)]
if selected_segment   != 'All': filtered = filtered[filtered['Segment']      == selected_segment]

# ─── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="dashboard-header">
    <h1 style="font-family:'Syne',sans-serif;font-size:36px;font-weight:800;color:#e6f1ff;margin:0;">
        🌍 Global Superstore Dashboard
    </h1>
    <p style="color:#8892b0;margin:8px 0 0 0;font-size:15px;">
        Sales · Profit · Segment Performance — Interactive Business Intelligence
    </p>
</div>
""", unsafe_allow_html=True)

# ─── KPI CARDS ─────────────────────────────────────────────────────────────────
total_sales    = filtered['Sales'].sum()
total_profit   = filtered['Profit'].sum()
total_orders   = filtered['Order ID'].nunique()
avg_margin     = filtered['Profit Margin'].mean()
total_qty      = filtered['Quantity'].sum()

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">💰 Total Sales</div>
        <div class="kpi-value">${total_sales:,.0f}</div>
    </div>""", unsafe_allow_html=True)

with k2:
    color = "#64ffda" if total_profit >= 0 else "#ff6b6b"
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">📈 Total Profit</div>
        <div class="kpi-value" style="color:{color};">${total_profit:,.0f}</div>
    </div>""", unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">🛒 Total Orders</div>
        <div class="kpi-value">{total_orders:,}</div>
    </div>""", unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">📦 Units Sold</div>
        <div class="kpi-value">{total_qty:,.0f}</div>
    </div>""", unsafe_allow_html=True)

with k5:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">🎯 Avg Margin</div>
        <div class="kpi-value">{avg_margin:.1f}%</div>
    </div>""", unsafe_allow_html=True)

# ─── ROW 1: Sales Over Time + Sales by Region ──────────────────────────────────
st.markdown('<div class="section-title">Sales & Profit Trends</div>', unsafe_allow_html=True)
c1, c2 = st.columns([3, 2])

with c1:
    monthly = filtered.groupby('Month')[['Sales', 'Profit']].sum().reset_index()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=monthly['Month'], y=monthly['Sales'],
                             name='Sales', line=dict(color='#64ffda', width=2.5),
                             fill='tozeroy', fillcolor='rgba(100,255,218,0.08)'))
    fig.add_trace(go.Scatter(x=monthly['Month'], y=monthly['Profit'],
                             name='Profit', line=dict(color='#f7c59f', width=2),
                             fill='tozeroy', fillcolor='rgba(247,197,159,0.06)'))
    fig.update_layout(
        title='Monthly Sales & Profit', paper_bgcolor='#1e2130', plot_bgcolor='#1e2130',
        font=dict(color='#ccd6f6'), legend=dict(bgcolor='#252a3d'),
        xaxis=dict(showgrid=False, tickangle=45),
        yaxis=dict(gridcolor='#2e3450'), margin=dict(t=40, b=10)
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    region_sales = filtered.groupby('Region')['Sales'].sum().reset_index().sort_values('Sales', ascending=True)
    fig2 = px.bar(region_sales, x='Sales', y='Region', orientation='h',
                  color='Sales', color_continuous_scale='Teal',
                  title='Sales by Region')
    fig2.update_layout(paper_bgcolor='#1e2130', plot_bgcolor='#1e2130',
                       font=dict(color='#ccd6f6'), coloraxis_showscale=False,
                       xaxis=dict(gridcolor='#2e3450'), yaxis=dict(showgrid=False),
                       margin=dict(t=40, b=10))
    st.plotly_chart(fig2, use_container_width=True)

# ─── ROW 2: Category Breakdown + Segment Pie ───────────────────────────────────
st.markdown('<div class="section-title">Category & Segment Analysis</div>', unsafe_allow_html=True)
c3, c4 = st.columns(2)

with c3:
    cat_data = filtered.groupby(['Category', 'Sub-Category'])['Sales'].sum().reset_index()
    fig3 = px.treemap(cat_data, path=['Category', 'Sub-Category'], values='Sales',
                      color='Sales', color_continuous_scale='Teal',
                      title='Sales by Category & Sub-Category')
    fig3.update_layout(paper_bgcolor='#1e2130', font=dict(color='#ccd6f6'),
                       margin=dict(t=40, b=10))
    st.plotly_chart(fig3, use_container_width=True)

with c4:
    seg_data = filtered.groupby('Segment')[['Sales', 'Profit']].sum().reset_index()
    fig4 = px.pie(seg_data, names='Segment', values='Sales',
                  color_discrete_sequence=['#64ffda', '#f7c59f', '#ff6b9d'],
                  title='Sales Distribution by Segment', hole=0.45)
    fig4.update_layout(paper_bgcolor='#1e2130', font=dict(color='#ccd6f6'),
                       legend=dict(bgcolor='#252a3d'), margin=dict(t=40, b=10))
    st.plotly_chart(fig4, use_container_width=True)

# ─── ROW 3: Top 5 Customers + Profit by Category ──────────────────────────────
st.markdown('<div class="section-title">Top Customers & Profitability</div>', unsafe_allow_html=True)
c5, c6 = st.columns(2)

with c5:
    top_customers = (filtered.groupby('Customer Name')['Sales']
                     .sum().reset_index()
                     .sort_values('Sales', ascending=False).head(5))
    fig5 = px.bar(top_customers, x='Customer Name', y='Sales',
                  color='Sales', color_continuous_scale='Teal',
                  title='Top 5 Customers by Sales', text_auto='.2s')
    fig5.update_layout(paper_bgcolor='#1e2130', plot_bgcolor='#1e2130',
                       font=dict(color='#ccd6f6'), coloraxis_showscale=False,
                       xaxis=dict(showgrid=False), yaxis=dict(gridcolor='#2e3450'),
                       margin=dict(t=40, b=10))
    fig5.update_traces(textfont_color='#e6f1ff')
    st.plotly_chart(fig5, use_container_width=True)

with c6:
    profit_cat = filtered.groupby('Category')[['Sales', 'Profit']].sum().reset_index()
    profit_cat['Margin %'] = (profit_cat['Profit'] / profit_cat['Sales']) * 100
    fig6 = px.bar(profit_cat, x='Category', y=['Sales', 'Profit'],
                  barmode='group', title='Sales vs Profit by Category',
                  color_discrete_sequence=['#64ffda', '#f7c59f'])
    fig6.update_layout(paper_bgcolor='#1e2130', plot_bgcolor='#1e2130',
                       font=dict(color='#ccd6f6'), legend=dict(bgcolor='#252a3d'),
                       xaxis=dict(showgrid=False), yaxis=dict(gridcolor='#2e3450'),
                       margin=dict(t=40, b=10))
    st.plotly_chart(fig6, use_container_width=True)

# ─── ROW 4: Profit Margin by Sub-Category ─────────────────────────────────────
st.markdown('<div class="section-title">Profit Margin by Sub-Category</div>', unsafe_allow_html=True)

subcat_margin = (filtered.groupby('Sub-Category')
                 .apply(lambda x: (x['Profit'].sum() / x['Sales'].sum()) * 100)
                 .reset_index(name='Margin %')
                 .sort_values('Margin %', ascending=True))

colors = ['#ff6b6b' if v < 0 else '#64ffda' for v in subcat_margin['Margin %']]
fig7 = go.Figure(go.Bar(
    x=subcat_margin['Margin %'], y=subcat_margin['Sub-Category'],
    orientation='h', marker_color=colors,
    text=subcat_margin['Margin %'].round(1).astype(str) + '%',
    textposition='outside'
))
fig7.update_layout(
    title='Profit Margin % by Sub-Category',
    paper_bgcolor='#1e2130', plot_bgcolor='#1e2130',
    font=dict(color='#ccd6f6'), height=420,
    xaxis=dict(gridcolor='#2e3450', zeroline=True, zerolinecolor='rgba(255,255,255,0.27)'),
    yaxis=dict(showgrid=False), margin=dict(t=40, b=10)
)
st.plotly_chart(fig7, use_container_width=True)

# ─── RAW DATA TABLE ────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">📋 Raw Data</div>', unsafe_allow_html=True)
with st.expander("Click to view filtered dataset"):
    st.dataframe(
        filtered[['Order ID','Order Date','Customer Name','Segment','Region',
                  'Category','Sub-Category','Sales','Profit','Quantity','Discount']],
        use_container_width=True, height=300
    )

st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:#8892b0;font-size:13px;'>"
    "Global Superstore Dashboard · Built with Streamlit & Plotly</p>",
    unsafe_allow_html=True
)
