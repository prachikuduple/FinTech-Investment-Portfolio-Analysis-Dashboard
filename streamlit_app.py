# # # # import streamlit as st
# # # # import pandas as pd
# # # # import plotly.express as px
# # # # import mysql.connector

# # # # # Connect MySQL
# # # # conn = mysql.connector.connect(
# # # #     host="localhost",
# # # #     user="root",
# # # #     password="root123",
# # # #     port=3306,
# # # #     use_pure=True,
# # # #     database="investment_db"
# # # # )

# # # # # Read data
# # # # query = "SELECT * FROM investment_portfolio"
# # # # df = pd.read_sql(query, conn)

# # # # # Title
# # # # st.title("Investment Portfolio Dashboard")

# # # # # KPI
# # # # st.write("### Summary")
# # # # st.write("Total Investment:", df["Investment_Amount"].sum())
# # # # st.write("Portfolio Value:", df["Current_Value"].sum())
# # # # st.write("Total Profit/Loss:", df["Profit_Loss"].sum())

# # # # # Chart
# # # # fig = px.bar(df, x="Stock_ID", y="Profit_Loss", title="Profit/Loss by Stock")
# # # # st.plotly_chart(fig)

# # # # # Table
# # # # st.write("### Data")
# # # # st.dataframe(df)

# # # import streamlit as st
# # # import pandas as pd
# # # import numpy as np
# # # import mysql.connector
# # # import plotly.express as px
# # # import plotly.graph_objects as go
# # # import matplotlib.pyplot as plt
# # # import seaborn as sns

# # # # ---------------------------------------------------------
# # # # PAGE CONFIG
# # # # ---------------------------------------------------------

# # # st.set_page_config(
# # #     page_title="FinTech Investment Dashboard",
# # #     page_icon="📈",
# # #     layout="wide"
# # # )

# # # # ---------------------------------------------------------
# # # # CUSTOM CSS
# # # # ---------------------------------------------------------

# # # st.markdown("""
# # # <style>

# # # .main {
# # #     background-color: #0E1117;
# # # }

# # # h1, h2, h3 {
# # #     color: #00F5D4;
# # # }

# # # .stMetric {
# # #     background-color: #1F2937;
# # #     padding: 15px;
# # #     border-radius: 15px;
# # #     text-align: center;
# # #     box-shadow: 0px 0px 10px #00F5D4;
# # # }

# # # .css-1d391kg {
# # #     background-color: #111827;
# # # }

# # # </style>
# # # """, unsafe_allow_html=True)

# # # # ---------------------------------------------------------
# # # # MYSQL CONNECTION
# # # # ---------------------------------------------------------

# # # @st.cache_resource
# # # def connect_db():
# # #     conn = mysql.connector.connect(
# # #         host="localhost",
# # #         user="root",
# # #         password="root123",
# # #         database="investment_db"
# # #     )
# # #     return conn

# # # conn = connect_db()

# # # # ---------------------------------------------------------
# # # # LOAD DATA
# # # # ---------------------------------------------------------

# # # query = "SELECT * FROM investment_portfolio"

# # # cursor = conn.cursor(dictionary=True)
# # # cursor.execute(query)

# # # data = cursor.fetchall()

# # # df = pd.DataFrame(data)

# # # # ---------------------------------------------------------
# # # # DATA CLEANING
# # # # ---------------------------------------------------------

# # # df["Date_ID"] = pd.to_datetime(df["Date_ID"])

# # # # ---------------------------------------------------------
# # # # HEADER
# # # # ---------------------------------------------------------

# # # st.markdown("""
# # # <h1 style='text-align:center;'>
# # # 🚀 FinTech Investment Portfolio Dashboard
# # # </h1>
# # # """, unsafe_allow_html=True)

# # # st.markdown("---")

# # # # ---------------------------------------------------------
# # # # SIDEBAR
# # # # ---------------------------------------------------------

# # # st.sidebar.image(
# # #     "https://cdn-icons-png.flaticon.com/512/3063/3063822.png",
# # #     width=120
# # # )

# # # st.sidebar.title("📊 Dashboard Filters")

# # # sector = st.sidebar.multiselect(
# # #     "Select Sector",
# # #     options=df["Sector"].unique(),
# # #     default=df["Sector"].unique()
# # # )

# # # company = st.sidebar.multiselect(
# # #     "Select Company",
# # #     options=df["Company_Name"].unique(),
# # #     default=df["Company_Name"].unique()
# # # )

# # # # ---------------------------------------------------------
# # # # FILTER DATA
# # # # ---------------------------------------------------------

# # # filtered_df = df[
# # #     (df["Sector"].isin(sector)) &
# # #     (df["Company_Name"].isin(company))
# # # ]

# # # # ---------------------------------------------------------
# # # # KPI SECTION
# # # # ---------------------------------------------------------

# # # total_investment = filtered_df["Investment_Amount"].sum()
# # # portfolio_value = filtered_df["Current_Value"].sum()
# # # profit_loss = filtered_df["Profit_Loss"].sum()
# # # total_companies = filtered_df["Company_Name"].nunique()

# # # col1, col2, col3, col4 = st.columns(4)

# # # col1.metric(
# # #     "💰 Total Investment",
# # #     f"₹ {total_investment:,.0f}"
# # # )

# # # col2.metric(
# # #     "📈 Portfolio Value",
# # #     f"₹ {portfolio_value:,.0f}"
# # # )

# # # col3.metric(
# # #     "📊 Profit / Loss",
# # #     f"₹ {profit_loss:,.0f}"
# # # )

# # # col4.metric(
# # #     "🏢 Companies",
# # #     total_companies
# # # )

# # # st.markdown("---")

# # # # ---------------------------------------------------------
# # # # CHART 1 - PIE CHART
# # # # ---------------------------------------------------------

# # # sector_data = filtered_df.groupby("Sector")[
# # #     "Investment_Amount"
# # # ].sum().reset_index()

# # # fig1 = px.pie(
# # #     sector_data,
# # #     names="Sector",
# # #     values="Investment_Amount",
# # #     hole=0.5,
# # #     color_discrete_sequence=px.colors.sequential.Tealgrn
# # # )

# # # fig1.update_layout(
# # #     title="💼 Sector Wise Investment",
# # #     template="plotly_dark"
# # # )

# # # # ---------------------------------------------------------
# # # # CHART 2 - TOP STOCKS BAR CHART
# # # # ---------------------------------------------------------

# # # top_stocks = filtered_df.groupby("Company_Name")[
# # #     "Profit_Loss"
# # # ].sum().reset_index()

# # # top_stocks = top_stocks.sort_values(
# # #     by="Profit_Loss",
# # #     ascending=False
# # # )

# # # fig2 = px.bar(
# # #     top_stocks,
# # #     x="Company_Name",
# # #     y="Profit_Loss",
# # #     color="Profit_Loss",
# # #     template="plotly_dark",
# # #     title="🏆 Top Performing Stocks"
# # # )

# # # # ---------------------------------------------------------
# # # # CHART 3 - TREEMAP
# # # # ---------------------------------------------------------

# # # fig3 = px.treemap(
# # #     filtered_df,
# # #     path=["Sector", "Company_Name"],
# # #     values="Current_Value",
# # #     color="Profit_Loss",
# # #     color_continuous_scale="RdYlGn",
# # #     title="🌳 Portfolio Distribution"
# # # )

# # # fig3.update_layout(template="plotly_dark")

# # # # ---------------------------------------------------------
# # # # CHART 4 - LINE CHART
# # # # ---------------------------------------------------------

# # # date_data = filtered_df.groupby("Buy_Date")[
# # #     "Current_Value"
# # # ].sum().reset_index()

# # # fig4 = px.line(
# # #     date_data,
# # #     x="Buy_Date",
# # #     y="Current_Value",
# # #     markers=True,
# # #     template="plotly_dark",
# # #     title="📅 Portfolio Growth Over Time"
# # # )

# # # # ---------------------------------------------------------
# # # # CHART 5 - SEABORN HEATMAP
# # # # ---------------------------------------------------------

# # # st.subheader("🔥 Correlation Heatmap")

# # # numeric_df = filtered_df.select_dtypes(include=np.number)

# # # corr = numeric_df.corr()

# # # fig5, ax = plt.subplots(figsize=(10, 6))

# # # sns.heatmap(
# # #     corr,
# # #     annot=True,
# # #     cmap="coolwarm",
# # #     linewidths=1,
# # #     ax=ax
# # # )

# # # st.pyplot(fig5)

# # # # ---------------------------------------------------------
# # # # CHART 6 - SEABORN HISTOGRAM
# # # # ---------------------------------------------------------

# # # st.subheader("📉 Profit Distribution")

# # # fig6, ax = plt.subplots(figsize=(10, 5))

# # # sns.histplot(
# # #     filtered_df["Profit_Loss"],
# # #     kde=True,
# # #     color="cyan",
# # #     bins=20,
# # #     ax=ax
# # # )

# # # plt.xlabel("Profit / Loss")

# # # st.pyplot(fig6)

# # # # ---------------------------------------------------------
# # # # CHART 7 - SCATTER PLOT
# # # # ---------------------------------------------------------

# # # fig7 = px.scatter(
# # #     filtered_df,
# # #     x="Investment_Amount",
# # #     y="Current_Value",
# # #     color="Sector",
# # #     size="Quantity",
# # #     hover_name="Company_Name",
# # #     template="plotly_dark",
# # #     title="📊 Investment vs Current Value"
# # # )

# # # # ---------------------------------------------------------
# # # # DASHBOARD LAYOUT
# # # # ---------------------------------------------------------

# # # left, right = st.columns(2)

# # # left.plotly_chart(fig1, use_container_width=True)
# # # right.plotly_chart(fig2, use_container_width=True)

# # # left2, right2 = st.columns(2)

# # # left2.plotly_chart(fig3, use_container_width=True)
# # # right2.plotly_chart(fig4, use_container_width=True)

# # # st.plotly_chart(fig7, use_container_width=True)

# # # # ---------------------------------------------------------
# # # # TOP 10 INVESTORS
# # # # ---------------------------------------------------------

# # # st.subheader("🏅 Top 10 Investors")

# # # top_investors = filtered_df.groupby("Investor_Name")[
# # #     "Current_Value"
# # # ].sum().reset_index()

# # # top_investors = top_investors.sort_values(
# # #     by="Current_Value",
# # #     ascending=False
# # # ).head(10)

# # # fig8 = px.bar(
# # #     top_investors,
# # #     x="Investor_Name",
# # #     y="Current_Value",
# # #     color="Current_Value",
# # #     template="plotly_dark",
# # #     title="👑 Top Investors"
# # # )

# # # st.plotly_chart(fig8, use_container_width=True)

# # # # ---------------------------------------------------------
# # # # DATA TABLE
# # # # ---------------------------------------------------------

# # # st.subheader("📋 Investment Portfolio Data")

# # # st.dataframe(
# # #     filtered_df,
# # #     use_container_width=True
# # # )

# # # # ---------------------------------------------------------
# # # # DOWNLOAD BUTTON
# # # # ---------------------------------------------------------

# # # csv = filtered_df.to_csv(index=False).encode("utf-8")

# # # st.download_button(
# # #     label="⬇ Download Portfolio Data",
# # #     data=csv,
# # #     file_name="investment_portfolio.csv",
# # #     mime="text/csv"
# # # )

# # # # ---------------------------------------------------------
# # # # FOOTER
# # # # ---------------------------------------------------------

# # # st.markdown("---")

# # # st.markdown("""
# # # <center>
# # # <h4>🚀 Developed using Streamlit + MySQL + Seaborn + Plotly</h4>
# # # </center>
# # # """, unsafe_allow_html=True)

# # # ==========================================
# # # STREAMLIT INVESTMENT DASHBOARD FILTERS
# # # ==========================================

# # import streamlit as st
# # import pandas as pd

# # # ==========================================
# # # PAGE CONFIG
# # # ==========================================

# # st.set_page_config(
# #     page_title="Investment Portfolio Dashboard",
# #     layout="wide"
# # )

# # st.title("📈 Investment Portfolio Dashboard")

# # # ==========================================
# # # LOAD DATA
# # # ==========================================

# # df = pd.read_csv("C:\Python_programED\cleaned_fact_investment.csv")

# # # ==========================================
# # # CLEAN COLUMN NAMES
# # # ==========================================

# # df.columns = df.columns.str.strip()

# # # ==========================================
# # # SHOW COLUMNS
# # # ==========================================

# # st.write("Available Columns")
# # st.write(df.columns.tolist())

# # # ==========================================
# # # SIDEBAR FILTERS
# # # ==========================================

# # st.sidebar.header("🔍 Filters")

# # # ==========================================
# # # TRANSACTION ID FILTER
# # # ==========================================

# # if "Transaction_ID" in df.columns:

# #     transaction = st.sidebar.multiselect(
# #         "Select Transaction ID",
# #         options=df["Transaction_ID"].unique()
# #     )

# #     if transaction:
# #         df = df[df["Transaction_ID"].isin(transaction)]

# # # ==========================================
# # # INVESTOR ID FILTER
# # # ==========================================

# # if "Investot_ID" in df.columns:

# #     investor = st.sidebar.multiselect(
# #         "Select Investor ID",
# #         options=df["Investot_ID"].unique()
# #     )

# #     if investor:
# #         df = df[df["Investot_ID"].isin(investor)]

# # # ==========================================
# # # STOCK ID FILTER
# # # ==========================================

# # if "Stock_ID" in df.columns:

# #     stock = st.sidebar.multiselect(
# #         "Select Stock ID",
# #         options=df["Stock_ID"].unique()
# #     )

# #     if stock:
# #         df = df[df["Stock_ID"].isin(stock)]

# # # ==========================================
# # # DATE FILTER
# # # ==========================================

# # if "Date_ID" in df.columns:

# #     df["Date_ID"] = pd.to_datetime(df["Date_ID"])

# #     min_date = df["Date_ID"].min()
# #     max_date = df["Date_ID"].max()

# #     date_range = st.sidebar.date_input(
# #         "Select Date Range",
# #         [min_date, max_date]
# #     )

# #     if len(date_range) == 2:

# #         start_date = pd.to_datetime(date_range[0])
# #         end_date = pd.to_datetime(date_range[1])

# #         df = df[
# #             (df["Date_ID"] >= start_date) &
# #             (df["Date_ID"] <= end_date)
# #         ]

# # # ==========================================
# # # BUY PRICE FILTER
# # # ==========================================

# # if "Buy_Price" in df.columns:

# #     min_buy = float(df["Buy_Price"].min())
# #     max_buy = float(df["Buy_Price"].max())

# #     buy_range = st.sidebar.slider(
# #         "Buy Price Range",
# #         min_buy,
# #         max_buy,
# #         (min_buy, max_buy)
# #     )

# #     df = df[
# #         (df["Buy_Price"] >= buy_range[0]) &
# #         (df["Buy_Price"] <= buy_range[1])
# #     ]

# # # ==========================================
# # # CURRENT PRICE FILTER
# # # ==========================================

# # if "Current_Price" in df.columns:

# #     min_current = float(df["Current_Price"].min())
# #     max_current = float(df["Current_Price"].max())

# #     current_range = st.sidebar.slider(
# #         "Current Price Range",
# #         min_current,
# #         max_current,
# #         (min_current, max_current)
# #     )

# #     df = df[
# #         (df["Current_Price"] >= current_range[0]) &
# #         (df["Current_Price"] <= current_range[1])
# #     ]

# # # ==========================================
# # # QUANTITY FILTER
# # # ==========================================

# # if "Quantity" in df.columns:

# #     #min_qty = int(df["Quantity"].min())
# #     #max_qty = int(df["Quantity"].max())
# #     df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

# # df["Quantity"] = df["Quantity"].fillna(0)

# # min_qty = int(df["Quantity"].min())
# # max_qty =

# #     qty_range = st.sidebar.slider(
# #         "Quantity Range",
# #         min_qty,
# #         max_qty,
# #         (min_qty, max_qty)
# #     )

# #     df = df[
# #         (df["Quantity"] >= qty_range[0]) &
# #         (df["Quantity"] <= qty_range[1])
# #     ]

# # # ==========================================
# # # INVESTMENT AMOUNT FILTER
# # # ==========================================

# # if "Investment_Amount" in df.columns:

# #     min_amt = int(df["Investment_Amount"].min())
# #     max_amt = int(df["Investment_Amount"].max())

# #     amt_range = st.sidebar.slider(
# #         "Investment Amount Range",
# #         min_amt,
# #         max_amt,
# #         (min_amt, max_amt)
# #     )

# #     df = df[
# #         (df["Investment_Amount"] >= amt_range[0]) &
# #         (df["Investment_Amount"] <= amt_range[1])
# #     ]

# # # ==========================================
# # # KPI CARDS
# # # ==========================================

# # st.subheader("📊 Dashboard Summary")

# # col1, col2, col3, col4 = st.columns(4)

# # with col1:
# #     st.metric(
# #         "Total Investment",
# #         f"₹ {df['Investment_Amount'].sum():,.0f}"
# #     )

# # with col2:
# #     st.metric(
# #         "Total Quantity",
# #         f"{df['Quantity'].sum():,.0f}"
# #     )

# # with col3:
# #     st.metric(
# #         "Average Buy Price",
# #         f"₹ {df['Buy_Price'].mean():,.2f}"
# #     )

# # with col4:
# #     st.metric(
# #         "Average Current Price",
# #         f"₹ {df['Current_Price'].mean():,.2f}"
# #     )

# # # ==========================================
# # # SHOW FILTERED DATA
# # # ==========================================

# # st.subheader("📁 Filtered Investment Data")

# # st.dataframe(df, use_container_width=True)

# # # ==========================================
# # # TOTAL RECORDS
# # # ==========================================

# # st.success(f"Total Records: {len(df)}")

# # =========================================================
# # PROFESSIONAL STREAMLIT INVESTMENT PORTFOLIO DASHBOARD
# # =========================================================

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # =========================================================
# # PAGE CONFIG
# # =========================================================

# st.set_page_config(
#     page_title="Investment Portfolio Dashboard",
#     layout="wide"
# )

# # =========================================================
# # TITLE
# # =========================================================

# st.title("📈 Investment Portfolio Dashboard")
# st.markdown("---")

# # =========================================================
# # FILE UPLOAD
# # =========================================================

# uploaded_file = st.file_uploader(
#     "Upload Investment CSV File",
#     type=["csv"]
# )

# # =========================================================
# # STOP IF FILE NOT UPLOADED
# # =========================================================

# if uploaded_file is None:
#     st.warning("Please upload CSV file")
#     st.stop()

# # =========================================================
# # READ CSV
# # =========================================================

# df = pd.read_csv(uploaded_file)

# # =========================================================
# # CLEAN COLUMN NAMES
# # =========================================================

# df.columns = df.columns.str.strip()

# # =========================================================
# # SHOW COLUMN NAMES
# # =========================================================

# st.subheader("📌 Dataset Columns")

# st.write(df.columns.tolist())

# # =========================================================
# # DATA CLEANING
# # =========================================================

# # Numeric Columns
# numeric_cols = [
#     "Buy_Price",
#     "Current_Price",
#     "Quantity",
#     "Investment_Amount"
# ]

# for col in numeric_cols:

#     if col in df.columns:

#         df[col] = pd.to_numeric(
#             df[col],
#             errors="coerce"
#         )

#         df[col] = df[col].fillna(0)

# # Date Column
# if "Date_ID" in df.columns:

#     df["Date_ID"] = pd.to_datetime(
#         df["Date_ID"],
#         errors="coerce"
#     )

# # =========================================================
# # SIDEBAR
# # =========================================================

# st.sidebar.header("🔍 Filter Data")

# # =========================================================
# # TRANSACTION FILTER
# # =========================================================

# if "Transaction_ID" in df.columns:

#     transaction_filter = st.sidebar.multiselect(
#         "Select Transaction ID",
#         options=df["Transaction_ID"].dropna().unique()
#     )

#     if transaction_filter:

#         df = df[
#             df["Transaction_ID"].isin(transaction_filter)
#         ]

# # =========================================================
# # INVESTOR FILTER
# # =========================================================

# if "Investot_ID" in df.columns:

#     investor_filter = st.sidebar.multiselect(
#         "Select Investor ID",
#         options=df["Investot_ID"].dropna().unique()
#     )

#     if investor_filter:

#         df = df[
#             df["Investot_ID"].isin(investor_filter)
#         ]

# # =========================================================
# # STOCK FILTER
# # =========================================================

# if "Stock_ID" in df.columns:

#     stock_filter = st.sidebar.multiselect(
#         "Select Stock ID",
#         options=df["Stock_ID"].dropna().unique()
#     )

#     if stock_filter:

#         df = df[
#             df["Stock_ID"].isin(stock_filter)
#         ]

# # =========================================================
# # DATE FILTER
# # =========================================================

# if "Date_ID" in df.columns:

#     min_date = df["Date_ID"].min()
#     max_date = df["Date_ID"].max()

#     date_filter = st.sidebar.date_input(
#         "Select Date Range",
#         [min_date, max_date]
#     )

#     if len(date_filter) == 2:

#         start_date = pd.to_datetime(date_filter[0])
#         end_date = pd.to_datetime(date_filter[1])

#         df = df[
#             (df["Date_ID"] >= start_date) &
#             (df["Date_ID"] <= end_date)
#         ]

# # =========================================================
# # QUANTITY SLIDER
# # =========================================================

# if "Quantity" in df.columns:

#     min_qty = int(df["Quantity"].min())
#     max_qty = int(df["Quantity"].max())

#     quantity_range = st.sidebar.slider(
#         "Select Quantity Range",
#         min_qty,
#         max_qty,
#         (min_qty, max_qty)
#     )

#     df = df[
#         (df["Quantity"] >= quantity_range[0]) &
#         (df["Quantity"] <= quantity_range[1])
#     ]

# # =========================================================
# # INVESTMENT AMOUNT SLIDER
# # =========================================================

# if "Investment_Amount" in df.columns:

#     min_amt = int(df["Investment_Amount"].min())
#     max_amt = int(df["Investment_Amount"].max())

#     investment_range = st.sidebar.slider(
#         "Select Investment Amount",
#         min_amt,
#         max_amt,
#         (min_amt, max_amt)
#     )

#     df = df[
#         (df["Investment_Amount"] >= investment_range[0]) &
#         (df["Investment_Amount"] <= investment_range[1])
#     ]

# # =========================================================
# # CALCULATE PROFIT / LOSS
# # =========================================================

# if (
#     "Current_Price" in df.columns and
#     "Buy_Price" in df.columns and
#     "Quantity" in df.columns
# ):

#     df["Profit_Loss"] = (
#         (df["Current_Price"] - df["Buy_Price"])
#         * df["Quantity"]
#     )

# # =========================================================
# # KPI SECTION
# # =========================================================

# st.subheader("📊 Dashboard KPIs")

# col1, col2, col3, col4 = st.columns(4)

# # Total Investment
# with col1:

#     total_investment = df["Investment_Amount"].sum()

#     st.metric(
#         "💰 Total Investment",
#         f"₹ {total_investment:,.0f}"
#     )

# # Total Quantity
# with col2:

#     total_quantity = df["Quantity"].sum()

#     st.metric(
#         "📦 Total Quantity",
#         f"{total_quantity:,.0f}"
#     )

# # Average Buy Price
# with col3:

#     avg_buy = df["Buy_Price"].mean()

#     st.metric(
#         "📉 Avg Buy Price",
#         f"₹ {avg_buy:,.2f}"
#     )

# # Total Profit/Loss
# with col4:

#     total_profit = df["Profit_Loss"].sum()

#     st.metric(
#         "📈 Total Profit/Loss",
#         f"₹ {total_profit:,.0f}"
#     )

# st.markdown("---")

# # =========================================================
# # SHOW DATAFRAME
# # =========================================================

# st.subheader("📁 Filtered Investment Data")

# st.dataframe(
#     df,
#     use_container_width=True
# )

# # =========================================================
# # CHARTS SECTION
# # =========================================================

# st.subheader("📊 Investment Charts")

# # =========================================================
# # TOP STOCK INVESTMENT
# # =========================================================

# if (
#     "Stock_ID" in df.columns and
#     "Investment_Amount" in df.columns
# ):

#     top_stock = (
#         df.groupby("Stock_ID")["Investment_Amount"]
#         .sum()
#         .sort_values(ascending=False)
#         .head(10)
#     )

#     fig1, ax1 = plt.subplots(figsize=(10, 5))

#     sns.barplot(
#         x=top_stock.index,
#         y=top_stock.values,
#         ax=ax1
#     )

#     plt.title("Top 10 Stocks by Investment Amount")
#     plt.xlabel("Stock ID")
#     plt.ylabel("Investment Amount")
#     plt.xticks(rotation=45)

#     st.pyplot(fig1)

# # =========================================================
# # PROFIT / LOSS CHART
# # =========================================================

# if (
#     "Stock_ID" in df.columns and
#     "Profit_Loss" in df.columns
# ):

#     profit_chart = (
#         df.groupby("Stock_ID")["Profit_Loss"]
#         .sum()
#         .sort_values(ascending=False)
#         .head(10)
#     )

#     fig2, ax2 = plt.subplots(figsize=(10, 5))

#     sns.lineplot(
#         x=profit_chart.index,
#         y=profit_chart.values,
#         marker="o",
#         ax=ax2
#     )

#     plt.title("Profit / Loss by Stock")
#     plt.xlabel("Stock ID")
#     plt.ylabel("Profit / Loss")

#     st.pyplot(fig2)

# # =========================================================
# # QUANTITY DISTRIBUTION
# # =========================================================

# if "Quantity" in df.columns:

#     fig3, ax3 = plt.subplots(figsize=(10, 5))

#     sns.histplot(
#         df["Quantity"],
#         kde=True,
#         ax=ax3
#     )

#     plt.title("Quantity Distribution")

#     st.pyplot(fig3)

# # =========================================================
# # BUY PRICE VS CURRENT PRICE
# # =========================================================

# if (
#     "Buy_Price" in df.columns and
#     "Current_Price" in df.columns
# ):

#     fig4, ax4 = plt.subplots(figsize=(10, 5))

#     sns.scatterplot(
#         x=df["Buy_Price"],
#         y=df["Current_Price"],
#         ax=ax4
#     )

#     plt.title("Buy Price vs Current Price")
#     plt.xlabel("Buy Price")
#     plt.ylabel("Current Price")

#     st.pyplot(fig4)

# # =========================================================
# # TOTAL RECORDS
# # =========================================================

# st.success(f"✅ Total Records After Filtering: {len(df)}")

# # =========================================================
# # DOWNLOAD FILTERED DATA
# # =========================================================

# csv = df.to_csv(index=False).encode("utf-8")

# st.download_button(
#     label="📥 Download Filtered CSV",
#     data=csv,
#     file_name="filtered_investment_data.csv",
#     mime="text/csv"
# )

# =========================================================
# PROFESSIONAL STREAMLIT INVESTMENT DASHBOARD
# ONE-TIME RUN COMPLETE ERROR-FREE CODE
# =========================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Investment Portfolio Dashboard",
    layout="wide"
)

# =========================================================
# TITLE
# =========================================================

st.title("📈 Investment Portfolio Dashboard")
st.markdown("---")

# =========================================================
# FILE UPLOADER
# =========================================================

uploaded_file = st.file_uploader(
    "Upload Investment CSV File",
    type=["csv"]
)

# =========================================================
# STOP IF NO FILE
# =========================================================

if uploaded_file is None:
    st.warning("Please Upload CSV File")
    st.stop()

# =========================================================
# READ CSV FILE
# =========================================================

df = pd.read_csv(uploaded_file)

# =========================================================
# CLEAN COLUMN NAMES
# =========================================================

df.columns = df.columns.str.strip()

# =========================================================
# FILL ALL NULL VALUES
# =========================================================

df = df.fillna(0)

# =========================================================
# CONVERT NUMERIC COLUMNS
# =========================================================

numeric_cols = [
    "Buy_Price",
    "Current_Price",
    "Quantity",
    "Investment_Amount"
]

for col in numeric_cols:

    if col in df.columns:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

        df[col] = df[col].fillna(0)

# =========================================================
# DATE COLUMN CONVERSION
# =========================================================

if "Date_ID" in df.columns:

    df["Date_ID"] = pd.to_datetime(
        df["Date_ID"],
        errors="coerce"
    )

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("🔍 Filters")

# =========================================================
# TRANSACTION FILTER
# =========================================================

if "Transaction_ID" in df.columns:

    transaction_filter = st.sidebar.multiselect(
        "Transaction ID",
        options=df["Transaction_ID"].unique()
    )

    if transaction_filter:

        df = df[
            df["Transaction_ID"].isin(transaction_filter)
        ]

# =========================================================
# INVESTOR FILTER
# =========================================================

if "Investot_ID" in df.columns:

    investor_filter = st.sidebar.multiselect(
        "Investor ID",
        options=df["Investot_ID"].unique()
    )

    if investor_filter:

        df = df[
            df["Investot_ID"].isin(investor_filter)
        ]

# =========================================================
# STOCK FILTER
# =========================================================

if "Stock_ID" in df.columns:

    stock_filter = st.sidebar.multiselect(
        "Stock ID",
        options=df["Stock_ID"].unique()
    )

    if stock_filter:

        df = df[
            df["Stock_ID"].isin(stock_filter)
        ]

# =========================================================
# DATE FILTER
# =========================================================

if "Date_ID" in df.columns:

    min_date = df["Date_ID"].min()
    max_date = df["Date_ID"].max()

    if pd.notnull(min_date) and pd.notnull(max_date):

        date_filter = st.sidebar.date_input(
            "Select Date Range",
            [min_date, max_date]
        )

        if len(date_filter) == 2:

            start_date = pd.to_datetime(date_filter[0])
            end_date = pd.to_datetime(date_filter[1])

            df = df[
                (df["Date_ID"] >= start_date) &
                (df["Date_ID"] <= end_date)
            ]

# =========================================================
# QUANTITY SLIDER
# =========================================================

if "Quantity" in df.columns:

    min_qty = int(df["Quantity"].min())
    max_qty = int(df["Quantity"].max())

    quantity_range = st.sidebar.slider(
        "Quantity Range",
        min_qty,
        max_qty,
        (min_qty, max_qty)
    )

    df = df[
        (df["Quantity"] >= quantity_range[0]) &
        (df["Quantity"] <= quantity_range[1])
    ]

# =========================================================
# INVESTMENT AMOUNT SLIDER
# =========================================================

if "Investment_Amount" in df.columns:

    min_amt = int(df["Investment_Amount"].min())
    max_amt = int(df["Investment_Amount"].max())

    amount_range = st.sidebar.slider(
        "Investment Amount Range",
        min_amt,
        max_amt,
        (min_amt, max_amt)
    )

    df = df[
        (df["Investment_Amount"] >= amount_range[0]) &
        (df["Investment_Amount"] <= amount_range[1])
    ]

# =========================================================
# PROFIT / LOSS CALCULATION
# =========================================================

if (
    "Buy_Price" in df.columns and
    "Current_Price" in df.columns and
    "Quantity" in df.columns
):

    df["Profit_Loss"] = (
        (df["Current_Price"] - df["Buy_Price"])
        * df["Quantity"]
    )

# =========================================================
# KPI SECTION
# =========================================================

st.subheader("📊 Dashboard KPIs")

col1, col2, col3, col4 = st.columns(4)

# Total Investment
with col1:

    total_investment = df["Investment_Amount"].sum()

    st.metric(
        "💰 Total Investment",
        f"₹ {total_investment:,.0f}"
    )

# Total Quantity
with col2:

    total_quantity = df["Quantity"].sum()

    st.metric(
        "📦 Total Quantity",
        f"{total_quantity:,.0f}"
    )

# Average Buy Price
with col3:

    avg_buy = df["Buy_Price"].mean()

    st.metric(
        "📉 Avg Buy Price",
        f"₹ {avg_buy:,.2f}"
    )

# Profit/Loss
with col4:

    total_profit = df["Profit_Loss"].sum()

    st.metric(
        "📈 Profit / Loss",
        f"₹ {total_profit:,.0f}"
    )

st.markdown("---")

# =========================================================
# DATAFRAME
# =========================================================

st.subheader("📁 Investment Data")

st.dataframe(
    df,
    use_container_width=True
)

# =========================================================
# TOP STOCK INVESTMENT BAR CHART
# =========================================================

if (
    "Stock_ID" in df.columns and
    "Investment_Amount" in df.columns
):

    st.subheader("📊 Top Stock Investment")

    top_stock = (
        df.groupby("Stock_ID")["Investment_Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig1, ax1 = plt.subplots(figsize=(10, 5))

    sns.barplot(
        x=top_stock.index,
        y=top_stock.values,
        ax=ax1
    )

    plt.title("Top 10 Stocks by Investment")
    plt.xlabel("Stock ID")
    plt.ylabel("Investment Amount")
    plt.xticks(rotation=45)

    st.pyplot(fig1)

# =========================================================
# PROFIT / LOSS LINE CHART
# =========================================================

if (
    "Stock_ID" in df.columns and
    "Profit_Loss" in df.columns
):

    st.subheader("📈 Profit / Loss Analysis")

    profit_chart = (
        df.groupby("Stock_ID")["Profit_Loss"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig2, ax2 = plt.subplots(figsize=(10, 5))

    sns.lineplot(
        x=profit_chart.index,
        y=profit_chart.values,
        marker="o",
        ax=ax2
    )

    plt.title("Profit / Loss by Stock")
    plt.xlabel("Stock ID")
    plt.ylabel("Profit / Loss")

    st.pyplot(fig2)

# =========================================================
# QUANTITY HISTOGRAM
# =========================================================

if "Quantity" in df.columns:

    st.subheader("📦 Quantity Distribution")

    fig3, ax3 = plt.subplots(figsize=(10, 5))

    sns.histplot(
        df["Quantity"],
        kde=True,
        ax=ax3
    )

    plt.title("Quantity Distribution")

    st.pyplot(fig3)

# =========================================================
# BUY PRICE VS CURRENT PRICE
# =========================================================

if (
    "Buy_Price" in df.columns and
    "Current_Price" in df.columns
):

    st.subheader("💹 Buy Price vs Current Price")

    fig4, ax4 = plt.subplots(figsize=(10, 5))

    sns.scatterplot(
        x=df["Buy_Price"],
        y=df["Current_Price"],
        ax=ax4
    )

    plt.xlabel("Buy Price")
    plt.ylabel("Current Price")
    plt.title("Buy Price vs Current Price")

    st.pyplot(fig4)

# =========================================================
# TOTAL RECORDS
# =========================================================

st.success(f"✅ Total Records: {len(df)}")

# =========================================================
# DOWNLOAD BUTTON
# =========================================================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_investment_data.csv",
    mime="text/csv"
)