import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import os

# =========================================================
# PAGE CONFIG 
# =========================================================
st.set_page_config(
    page_title="FinTech Investment Dashboard",
    page_icon="📈",
    layout="wide"
)
# =========================================================
# BACKGROUND IMAGE FIX 
# =========================================================
image_path = "bg.jpeg" 

try:
    with open(image_path, "rb") as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.4)), url("data:image/jpeg;base64,{bin_str}") !important;
            background-size: cover !important;
            background-position: center !important;
            background-attachment: fixed !important;
            background-repeat: no-repeat !important;
        }}
        .stMainCard {{
            background: transparent !important;
        }}
        </style>
    """, unsafe_allow_html=True)
    
except FileNotFoundError:
    st.error(f"❌ '{image_path}'")
    st.info()

# =========================================================
# SAFE MATPLOTLIB SETTINGS
# =========================================================
plt.rcParams["figure.dpi"] = 80
plt.rcParams['text.color'] = '#1e293b'
plt.rcParams['axes.labelcolor'] = '#1e293b'
plt.rcParams['xtick.color'] = '#475569'
plt.rcParams['ytick.color'] = '#475569'

sns.set_style("darkgrid", {
    "axes.facecolor": "#f1f5f9",
    "figure.facecolor": "none",
    "grid.color": "#cbd5e1"            
})

# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("cleaned_fact_investment.csv")
    except FileNotFoundError:
        dates = pd.date_range(start="2025-01-01", periods=100, freq="D").strftime("%Y%m%d")
        df = pd.DataFrame({
            "Date_ID": np.random.choice(dates, 5000),
            "Investor_ID": [f"INV_{i}" for i in np.random.randint(1, 20, 5000)],
            "Stock_ID": [f"STK_{i}" for i in np.random.randint(1, 30, 5000)],
            "Investment_Amount": np.random.randint(10000, 500000, 5000),
            "Current_Value": np.random.randint(8000, 600000, 5000),
            "Transaction_ID": range(1, 5001)
        })
    
    
    if "Asset_Class" not in df.columns:
        df["Asset_Class"] = np.random.choice(["Equity", "Mutual Funds", "Crypto", "Bonds"], len(df))
    if "Risk_Profile" not in df.columns:
        df["Risk_Profile"] = np.random.choice(["High", "Medium", "Low"], len(df))
    if "Profit_Loss" not in df.columns:
        df["Profit_Loss"] = df["Current_Value"] - df["Investment_Amount"]
        
    return df

df = load_data()

# =========================================================
# DATA CLEANING
# =========================================================
df["Date_ID"] = df["Date_ID"].astype(str)
df["Date"] = pd.to_datetime(df["Date_ID"], format="%Y%m%d", errors="coerce")
df.dropna(inplace=True)
df = df.head(5000)

# =========================================================
# SIDEBAR CUSTOM CSS WITH PREMIUM LOGO & FILTER STYLING
# =========================================================
st.markdown(
    """
    <style>
    /* संपूर्ण साईडबारला ग्लास लूक देणे */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.45) !important;
        backdrop-filter: blur(15px) !important;
        -webkit-backdrop-filter: blur(15px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    
    [data-testid="stSidebar"] label {
        color: #334155 !important;
        font-weight: 600 !important;
        font-family: 'Segoe UI', sans-serif !important;
    }

    [data-testid="stSidebar"] div[data-baseweb="select"], 
    [data-testid="stSidebar"] div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.5) !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        border-radius: 8px !important;
    }

    /* वाढवलेला मोठा कोड-बेस्ड प्रोग्रेसिव्ह लोगो बॉक्स */
    .premium-logo-box {
        text-align: center;
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.98));
        border-radius: 20px;
        padding: 50px 25px; /* पॅडिंग वाढवले */
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-bottom: 30px;
    }
    
    .logo-icon-animation {
        font-size: 75px; /* आयकॉन साईझ मोठा केला */
        animation: pulse 2s infinite;
        margin-bottom: 10px;
    }
    
    .logo-text-main {
        font-family: 'Segoe UI', sans-serif;
        font-weight: 800;
        font-size: 32px; /* टेक्स्ट साईझ मोठा केला */
        letter-spacing: 2px;
        background: linear-gradient(135deg, #38bdf8, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .logo-tagline {
        color: #94a3b8;
        font-size: 13px; 
        font-weight: 600;
        letter-spacing: 0.8px;
        margin-top: 6px;
    }

    .live-status-pill {
        background-color: rgba(16, 185, 129, 0.2);
        color: #34d399;
        padding: 4px 16px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        display: inline-block;
        border: 1px solid rgba(16, 185, 129, 0.4);
        margin-top: 12px;
        text-transform: uppercase;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.08); }
        100% { transform: scale(1); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# INTERACTIVE SIDEBAR WITH BIGGER LOGO
# =========================================================
with st.sidebar:
    try:
        st.image("sonyy.png", use_container_width=True)
    except Exception:
        st.markdown('''
        <div class="premium-logo-box">
             <div class="logo-icon-animation">⚡</div>
             <div class="logo-text-main">FINTECH ANALYTICS</div>
             <div class="logo-tagline">AI-POWERED PORTFOLIO</div>
             <div><span class="live-status-pill">● LIVE ENGINE</span></div>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown("### 📌 Dashboard Filters")
    
    
    asset_options = ["All"] + list(df["Asset_Class"].unique())
    selected_asset = st.selectbox("Asset Class", options=asset_options, index=0)

    risk_options = ["All"] + list(df["Risk_Profile"].unique())
    selected_risk = st.selectbox("Risk Profile", options=risk_options, index=0)

    st.markdown("---")
    
    selected_investor = st.multiselect(
        "Select Investor",
        options=list(df["Investor_ID"].unique()),
        default=list(df["Investor_ID"].unique())[:10]
    )

    selected_stock = st.multiselect(
        "Select Stock",
        options=list(df["Stock_ID"].unique()),
        default=list(df["Stock_ID"].unique())[:10]
    )

    profit_status = st.radio(
        "Profit Status",
        ["All", "Profit", "Loss"]
    )

    min_date = df["Date"].min()
    max_date = df["Date"].max()

    selected_dates = st.date_input(
        "Select Date Range",
        [min_date, max_date]
    )

# =========================================================
# FILTER DATA
# =========================================================
filtered_df = df[
    (df["Investor_ID"].isin(selected_investor)) &
    (df["Stock_ID"].isin(selected_stock))
].copy()

if selected_asset != "All":
    filtered_df = filtered_df[filtered_df["Asset_Class"] == selected_asset]

if selected_risk != "All":
    filtered_df = filtered_df[filtered_df["Risk_Profile"] == selected_risk]

if profit_status == "Profit":
    filtered_df = filtered_df[filtered_df["Profit_Loss"] > 0]
elif profit_status == "Loss":
    filtered_df = filtered_df[filtered_df["Profit_Loss"] < 0]

if isinstance(selected_dates, (list, tuple)) and len(selected_dates) == 2:
    start_date, end_date = selected_dates
    filtered_df = filtered_df[
        (filtered_df["Date"] >= pd.to_datetime(start_date)) &
        (filtered_df["Date"] <= pd.to_datetime(end_date))
    ]

# =========================================================
# HEADER SECTION (📌 PERFECTLY CENTERED & ONE-LINE DESIGN)
# =========================================================
st.markdown("""
    <div style='text-align: center; padding: 15px 0px; width: 100%;'>
        <h1 style='color: #1e293b; font-weight: 800; font-family: "Segoe UI", sans-serif; margin: 0; padding: 0; white-space: nowrap; font-size: 2.8rem;'>
            FinTech Investment Portfolio Dashboard
        </h1>
        <p style='color: #475569; font-weight: 500; font-family: "Segoe UI", sans-serif; margin-top: 8px; margin-bottom: 0; font-size: 1.2rem; white-space: nowrap;'>
            AI Powered Professional Stock Market Analytics Platform
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# INTERACTIVE KPI SECTION (CLICKABLE BUTTONS WITH GLOW)
# =========================================================
st.markdown("""
<style>
    div.stButton > button {
        background: rgba(255, 255, 255, 0.45) !important;
        backdrop-filter: blur(15px) !important;
        -webkit-backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        color: #1e293b !important;
        padding: 20px !important;
        border-radius: 24px !important;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.02) !important;
        transition: all 0.3s ease-in-out !important;
        font-weight: bold !important;
        height: auto !important;
        white-space: pre-line !important;
    }

    div.stButton > button:hover {
        transform: translateY(-5px) scale(1.02) !important;
        background: rgba(255, 255, 255, 0.65) !important;
        border: 1px solid #3b82f6 !important;
        box-shadow: 0 12px 25px rgba(59, 130, 246, 0.2) !important;
        color: #2563eb !important;
    }
</style>
""", unsafe_allow_html=True)

if not filtered_df.empty:
    total_investment = filtered_df["Investment_Amount"].sum()
    current_value = filtered_df["Current_Value"].sum()
    profit_loss = filtered_df["Profit_Loss"].sum()
    transactions = filtered_df["Transaction_ID"].count()
    roi = ((current_value - total_investment) / total_investment) * 100 if total_investment != 0 else 0
else:
    total_investment, current_value, profit_loss, transactions, roi = 0, 0, 0, 0, 0

if "selected_kpi" not in st.session_state:
    st.session_state.selected_kpi = "All"

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button(f"Total Investment\n\n₹ {total_investment:,.0f}", key="btn_inv", use_container_width=True):
        st.session_state.selected_kpi = "Investment"
with col2:
    if st.button(f"Current Value\n\n₹ {current_value:,.0f}", key="btn_val", use_container_width=True):
        st.session_state.selected_kpi = "Value"
with col3:
    if st.button(f"Profit/Loss\n\n₹ {profit_loss:,.0f}", key="btn_pl", use_container_width=True):
        st.session_state.selected_kpi = "Profit_Loss"
with col4:
    if st.button(f"Transactions\n\n{transactions}", key="btn_tx", use_container_width=True):
        st.session_state.selected_kpi = "Transactions"
with col5:
    if st.button(f"ROI %\n\n{roi:.2f}%", key="btn_roi", use_container_width=True):
        st.session_state.selected_kpi = "ROI"

st.caption(f"Active View : **{st.session_state.selected_kpi}**")
st.markdown("---")

# =========================================================
# TOP CHARTS
# =========================================================
if not filtered_df.empty:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("  Top Performing Stocks")
        top_profit = filtered_df.groupby("Stock_ID")["Profit_Loss"].sum().sort_values(ascending=False).head(10)
        
        fig, ax = plt.subplots(figsize=(9, 5), facecolor="none")
        sns.barplot(x=top_profit.values, y=top_profit.index.astype(str), palette="viridis", ax=ax)
        ax.set_facecolor("none")
        
        for i, v in enumerate(top_profit.values):
            ax.text(v, i, f" ₹{v:,.0f}", color="#1e293b", va="center", fontweight='bold')
        plt.tight_layout()
        st.pyplot(fig)

    with col2:
        st.subheader("  Loss Making Stocks")
        loss_chart = filtered_df.groupby("Stock_ID")["Profit_Loss"].sum().sort_values().head(10)
        
        fig2, ax2 = plt.subplots(figsize=(9, 5), facecolor="none")
        sns.barplot(x=loss_chart.values, y=loss_chart.index.astype(str), palette="rocket", ax=ax2)
        ax2.set_facecolor("none")
        
        for i, v in enumerate(loss_chart.values):
            ax2.text(v, i, f" ₹{v:,.0f}", color="#1e293b", va="center", fontweight='bold')
        plt.tight_layout()
        st.pyplot(fig2)

    # =========================================================
    # MONTHLY TREND
    # =========================================================
    st.subheader("  Monthly Investment Trend")
    monthly_data = filtered_df.groupby(filtered_df["Date"].dt.to_period("M"))["Investment_Amount"].sum().head(12)
    monthly_data.index = monthly_data.index.astype(str)

    fig3, ax3 = plt.subplots(figsize=(12, 4), facecolor="none")
    sns.lineplot(x=monthly_data.index, y=monthly_data.values, marker="o", linewidth=4, color="#3b82f6", ax=ax3)
    ax3.set_facecolor("none")

    for i, value in enumerate(monthly_data.values):
        ax3.text(i, value, f" ₹{value:,.0f}", color="#1e293b", ha="center", va="bottom", fontweight='bold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig3)

    # =========================================================
    # PORTFOLIO ALLOCATION & TOP INVESTORS
    # =========================================================
    col1, col2 = st.columns([1, 1], gap="medium")

    with col1:
        st.subheader("  Portfolio Allocation")
        allocation = filtered_df.groupby("Stock_ID")["Investment_Amount"].sum().sort_values(ascending=False).head(5)
        
        fig4, ax4 = plt.subplots(figsize=(5, 5), facecolor="none")
        ax4.set_facecolor("none")
        
        colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(allocation)))
        
        wedges, texts, autotexts = ax4.pie(
            allocation.values, 
            labels=allocation.index.astype(str), 
            autopct="%1.1f%%", 
            startangle=140, 
            colors=colors,
            textprops=dict(color="#1e293b", weight="bold", size=10),
            wedgeprops=dict(edgecolor=(1, 1, 1, 0.6), width=0.55)
        )
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_weight('bold')
            autotext.set_size(10)
            
        plt.tight_layout()
        st.pyplot(fig4, use_container_width=True)

    with col2:
        st.subheader("  Top Investors")
        top_investors = filtered_df.groupby("Investor_ID")["Investment_Amount"].sum().sort_values(ascending=False).head(10)
        
        fig5, ax5 = plt.subplots(figsize=(5, 5), facecolor="none")
        sns.barplot(x=top_investors.values, y=top_investors.index.astype(str), palette="mako", ax=ax5)
        ax5.set_facecolor("none")
        
        ax5.tick_params(axis='both', which='major', labelsize=10)
        ax5.set_xlabel("Investment Amount", fontsize=10)
        ax5.set_ylabel("Investor ID", fontsize=10)
        
        plt.tight_layout()
        st.pyplot(fig5, use_container_width=True)

    # =========================================================
    # RISK ANALYSIS & HEATMAP
    # =========================================================
    st.subheader("  Risk Analysis")
    fig6, ax6 = plt.subplots(figsize=(12, 4), facecolor="none")
    sns.histplot(filtered_df["Profit_Loss"], bins=30, kde=True, ax=ax6, color="#10b981")
    ax6.set_facecolor("none")
    plt.tight_layout()
    st.pyplot(fig6)

    st.subheader("  Correlation Matrix")
    numeric_df = filtered_df.select_dtypes(include=np.number)
    if not numeric_df.empty and numeric_df.shape[1] > 1:
        corr = numeric_df.corr()
        fig8, ax8 = plt.subplots(figsize=(10, 5), facecolor="none")
        sns.heatmap(corr, annot=True, cmap="Blues", ax=ax8, fmt=".2f", annot_kws={'size': 12, 'weight': 'bold'})
        plt.tight_layout()
        st.pyplot(fig8)
    else:
        st.info("Correlation heatmap available when multiple numeric columns exist.")

else:
    st.warning("No data available for the selected filters.")

# =========================================================
# DATA TABLE
# =========================================================
st.subheader("📋 Investment Portfolio Dataset")

if not filtered_df.empty:
    html_table = filtered_df.head(50).to_html(index=False, classes='styled-table')
    
    custom_html = f"""
    <style>
        body {{
            background: transparent !important;
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
        }}
        .table-container {{
            max-height: 400px;
            overflow-y: auto;
            background: rgba(240, 249, 255, 0.2) !important;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(14, 165, 233, 0.15);
            border-radius: 16px;
            padding: 8px;
        }}
        .styled-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
            color: #1e293b;
            background: transparent !important;
        }}
        .styled-table th {{
            background-color: #e0f2fe !important;
            color: #0369a1 !important;
            text-align: left;
            padding: 12px;
            font-weight: 600;
            position: sticky;
            top: 0;
            z-index: 1;
            border-bottom: 2px solid #bae6fd;
        }}
        .styled-table td {{
            padding: 10px 12px;
            background-color: #f8fafc !important;
            border-bottom: 1px solid #f1f5f9;
        }}
        .styled-table tr:nth-of-type(even) td {{
            background-color: #f0f9ff !important;
        }}
        ::-webkit-scrollbar {{ width: 5px; height: 5px; }}
        ::-webkit-scrollbar-thumb {{ background: #bae6fd; border-radius: 10px; }}
    </style>
    
    <div class="table-container">
        {html_table}
    </div>
    """
    st.components.v1.html(custom_html, height=420, scrolling=False)
else:
    st.info()

# =========================================================
# DOWNLOAD BUTTON
# =========================================================
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇ Download Filtered Data",
    data=csv,
    file_name="investment_analysis.csv",
    mime="text/csv"
)

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.markdown("""
<div style='text-align:center; padding-bottom: 40px;'>
<h3 style='color:#1e293b;'>🚀 Developed Using Python + Streamlit</h3>
<h5 style='color:#1e293b;'>Transforming Financial Data into Actionable Business Insights</h5>

<p style='color:#64748b; font-weight: bold;'>Professional FinTech Investment Analytics Dashboard</p>
</div>
""", unsafe_allow_html=True)