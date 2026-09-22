import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Supermarket Sales & Customer Analytics",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown(
    """
    <style>
        .main-title {
            font-size: 34px;
            font-weight: 700;
            margin-bottom: 5px;
        }

        .subtitle {
            font-size: 16px;
            color: #666666;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATA LOADING AND PREPROCESSING
# ============================================================
@st.cache_data
def load_data():

    file_path = "data/supermarket_sales.csv"

    df = pd.read_csv(file_path)

    # Remove duplicate records
    df = df.drop_duplicates().copy()

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # --------------------------------------------------------
    # Convert numeric columns
    # --------------------------------------------------------
    numeric_columns = [
        "Unit price",
        "Quantity",
        "Tax 5%",
        "Total",
        "cogs",
        "gross margin percentage",
        "gross income",
        "Rating"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    # --------------------------------------------------------
    # Convert date
    # --------------------------------------------------------
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(
            df["Date"],
            errors="coerce"
        )

    # --------------------------------------------------------
    # Convert time
    # --------------------------------------------------------
    if "Time" in df.columns:
        df["Time"] = pd.to_datetime(
            df["Time"].astype(str),
            format="%H:%M",
            errors="coerce"
        )

    # --------------------------------------------------------
    # Create time-based columns
    # --------------------------------------------------------
    if "Date" in df.columns:

        df["Month Sort"] = (
            df["Date"]
            .dt.to_period("M")
            .astype(str)
        )

        df["Month"] = (
            df["Date"]
            .dt.strftime("%b %Y")
        )

        df["Day"] = df["Date"].dt.day

        df["Day Name"] = (
            df["Date"]
            .dt.day_name()
        )

    if "Time" in df.columns:
        df["Hour"] = df["Time"].dt.hour

    # --------------------------------------------------------
    # Calculate profit margin
    # --------------------------------------------------------
    if (
        "Total" in df.columns
        and "gross income" in df.columns
    ):

        df["Profit Margin"] = np.where(
            df["Total"] != 0,
            (
                df["gross income"]
                / df["Total"]
            ) * 100,
            0
        )

    # ========================================================
    # DISPLAY LABELS FOR YOUR PROJECT
    # ========================================================
    # Original branch codes:
    # A, B, C
    #
    # These are changed ONLY for dashboard presentation.
    # The underlying sales figures remain unchanged.
    # ========================================================

    branch_name_map = {
        "A": "Main Branch",
        "B": "City Center Branch",
        "C": "Express Branch"
    }

    city_name_map = {
        "Yangon": "Hyderabad",
        "Mandalay": "Vijayawada",
        "Naypyitaw": "Visakhapatnam"
    }

    if "Branch" in df.columns:

        df["Branch Name"] = (
            df["Branch"]
            .map(branch_name_map)
            .fillna(df["Branch"])
        )

    else:
        df["Branch Name"] = "Unknown Branch"

    if "City" in df.columns:

        df["City Name"] = (
            df["City"]
            .map(city_name_map)
            .fillna(df["City"])
        )

    else:
        df["City Name"] = "Unknown City"

    return df


# ============================================================
# LOAD DATA
# ============================================================
try:

    df = load_data()

except FileNotFoundError:

    st.error(
        "Dataset not found.\n\n"
        "Please make sure the file is located at:\n\n"
        "data/supermarket_sales.csv"
    )

    st.stop()

except Exception as error:

    st.error(
        "An error occurred while loading the dataset."
    )

    st.exception(error)

    st.stop()


# ============================================================
# TITLE
# ============================================================
st.markdown(
    '<div class="main-title">'
    '🛒 Supermarket Sales & Customer Analytics Dashboard'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Interactive Business Intelligence Dashboard for
        Sales, Customers, Products, Profitability and
        Business Decision-Making
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================
st.sidebar.title("🔎 Dashboard Filters")


# ============================================================
# DATE FILTER
# ============================================================
if (
    "Date" in df.columns
    and df["Date"].notna().any()
):

    minimum_date = df["Date"].min().date()
    maximum_date = df["Date"].max().date()

    date_selection = st.sidebar.date_input(
        "Date Range",
        value=(
            minimum_date,
            maximum_date
        ),
        min_value=minimum_date,
        max_value=maximum_date
    )

    if (
        isinstance(date_selection, tuple)
        and len(date_selection) == 2
    ):

        start_date = date_selection[0]
        end_date = date_selection[1]

        filtered_df = df[
            (
                df["Date"].dt.date
                >= start_date
            )
            &
            (
                df["Date"].dt.date
                <= end_date
            )
        ].copy()

    else:

        filtered_df = df.copy()

else:

    filtered_df = df.copy()


# ============================================================
# CITY FILTER
# ============================================================
locations = sorted(
    df["City Name"]
    .dropna()
    .unique()
    .tolist()
)

selected_locations = st.sidebar.multiselect(
    "City",
    locations,
    default=locations
)

if selected_locations:

    filtered_df = filtered_df[
        filtered_df["City Name"].isin(
            selected_locations
        )
    ]


# ============================================================
# SUPERMARKET BRANCH FILTER
# ============================================================
branches = sorted(
    df["Branch Name"]
    .dropna()
    .unique()
    .tolist()
)

selected_branches = st.sidebar.multiselect(
    "Supermarket Branch",
    branches,
    default=branches
)

if selected_branches:

    filtered_df = filtered_df[
        filtered_df["Branch Name"].isin(
            selected_branches
        )
    ]


# ============================================================
# PRODUCT CATEGORY FILTER
# ============================================================
categories = sorted(
    df["Product line"]
    .dropna()
    .unique()
    .tolist()
)

selected_categories = st.sidebar.multiselect(
    "Product Category",
    categories,
    default=categories
)

if selected_categories:

    filtered_df = filtered_df[
        filtered_df["Product line"].isin(
            selected_categories
        )
    ]


# ============================================================
# CUSTOMER TYPE FILTER
# ============================================================
customer_types = sorted(
    df["Customer type"]
    .dropna()
    .unique()
    .tolist()
)

selected_customer_types = st.sidebar.multiselect(
    "Customer Type",
    customer_types,
    default=customer_types
)

if selected_customer_types:

    filtered_df = filtered_df[
        filtered_df["Customer type"].isin(
            selected_customer_types
        )
    ]


# ============================================================
# GENDER FILTER
# ============================================================
genders = sorted(
    df["Gender"]
    .dropna()
    .unique()
    .tolist()
)

selected_genders = st.sidebar.multiselect(
    "Gender",
    genders,
    default=genders
)

if selected_genders:

    filtered_df = filtered_df[
        filtered_df["Gender"].isin(
            selected_genders
        )
    ]


# ============================================================
# PAYMENT FILTER
# ============================================================
payment_methods = sorted(
    df["Payment"]
    .dropna()
    .unique()
    .tolist()
)

selected_payments = st.sidebar.multiselect(
    "Payment Method",
    payment_methods,
    default=payment_methods
)

if selected_payments:

    filtered_df = filtered_df[
        filtered_df["Payment"].isin(
            selected_payments
        )
    ]


# ============================================================
# EMPTY DATA CHECK
# ============================================================
if filtered_df.empty:

    st.warning(
        "No records match the selected filters. "
        "Please change the filters."
    )

    st.stop()


# ============================================================
# KPI CALCULATIONS
# ============================================================
total_revenue = filtered_df["Total"].sum()

total_transactions = len(filtered_df)

total_quantity = filtered_df["Quantity"].sum()

total_profit = filtered_df["gross income"].sum()

average_order_value = (
    total_revenue / total_transactions
    if total_transactions > 0
    else 0
)

average_rating = (
    filtered_df["Rating"].mean()
)

overall_profit_margin = (
    (
        total_profit
        / total_revenue
    ) * 100
    if total_revenue > 0
    else 0
)


# ============================================================
# EXECUTIVE OVERVIEW
# ============================================================
st.header("📊 Executive Overview")

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

kpi1.metric(
    "Total Revenue",
    f"${total_revenue:,.2f}"
)

kpi2.metric(
    "Total Transactions",
    f"{total_transactions:,}"
)

kpi3.metric(
    "Total Profit",
    f"${total_profit:,.2f}"
)

kpi4.metric(
    "Average Order Value",
    f"${average_order_value:,.2f}"
)

kpi5.metric(
    "Quantity Sold",
    f"{total_quantity:,}"
)

kpi6, kpi7 = st.columns(2)

kpi6.metric(
    "Average Customer Rating",
    f"{average_rating:.2f}/10"
)

kpi7.metric(
    "Overall Profit Margin",
    f"{overall_profit_margin:.2f}%"
)


# ============================================================
# SALES PERFORMANCE
# ============================================================
st.header("📈 Sales Performance")


# ============================================================
# MONTHLY REVENUE
# ============================================================
monthly_sales = (
    filtered_df
    .groupby(
        "Month Sort",
        as_index=False
    )["Total"]
    .sum()
    .sort_values("Month Sort")
)

monthly_sales["Month"] = (
    pd.to_datetime(
        monthly_sales["Month Sort"]
    ).dt.strftime("%b %Y")
)

fig_monthly = px.line(
    monthly_sales,
    x="Month",
    y="Total",
    markers=True,
    title="Monthly Revenue Trend",
    labels={
        "Month": "Month",
        "Total": "Revenue"
    }
)

st.plotly_chart(
    fig_monthly,
    width="stretch"
)


# ============================================================
# CITY AND CATEGORY SALES
# ============================================================
chart1, chart2 = st.columns(2)


# ------------------------------------------------------------
# Revenue by City
# ------------------------------------------------------------
city_sales = (
    filtered_df
    .groupby(
        "City Name",
        as_index=False
    )
    .agg(
        Revenue=("Total", "sum"),
        Profit=("gross income", "sum"),
        Transactions=("Invoice ID", "count")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)

with chart1:

    fig_city = px.bar(
        city_sales,
        x="City Name",
        y="Revenue",
        text_auto=".2s",
        title="Revenue by City"
    )

    fig_city.update_layout(
        xaxis_title="City",
        yaxis_title="Revenue"
    )

    st.plotly_chart(
        fig_city,
        width="stretch"
    )


# ------------------------------------------------------------
# Revenue by Product Category
# ------------------------------------------------------------
category_sales = (
    filtered_df
    .groupby(
        "Product line",
        as_index=False
    )
    .agg(
        Revenue=("Total", "sum"),
        Quantity=("Quantity", "sum"),
        Profit=("gross income", "sum")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )

)

with chart2:

    fig_category = px.bar(
        category_sales,
        x="Product line",
        y="Revenue",
        text_auto=".2s",
        title="Revenue by Product Category"
    )

    fig_category.update_layout(
        xaxis_title="Product Category",
        yaxis_title="Revenue"
    )

    st.plotly_chart(
        fig_category,
        width="stretch"
    )


# ============================================================
# SUPERMARKET BRANCH PERFORMANCE
# ============================================================
st.header("🏪 Supermarket Branch Performance")

branch_sales = (
    filtered_df
    .groupby(
        "Branch Name",
        as_index=False
    )
    .agg(
        Revenue=("Total", "sum"),
        Profit=("gross income", "sum"),
        Transactions=("Invoice ID", "count"),
        Quantity=("Quantity", "sum")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)

branch_chart1, branch_chart2 = st.columns(2)


with branch_chart1:

    fig_branch_revenue = px.bar(
        branch_sales,
        x="Branch Name",
        y="Revenue",
        text_auto=".2s",
        title="Revenue by Supermarket Branch"
    )

    st.plotly_chart(
        fig_branch_revenue,
        width="stretch"
    )


with branch_chart2:

    fig_branch_profit = px.bar(
        branch_sales,
        x="Branch Name",
        y="Profit",
        text_auto=".2s",
        title="Profit by Supermarket Branch"
    )

    st.plotly_chart(
        fig_branch_profit,
        width="stretch"
    )


# ============================================================
# PRODUCT ANALYSIS
# ============================================================
st.header("🏆 Product Performance")


product_chart1, product_chart2 = st.columns(2)


# ------------------------------------------------------------
# Quantity by Category
# ------------------------------------------------------------
with product_chart1:

    fig_quantity = px.bar(
        category_sales.sort_values(
            "Quantity",
            ascending=False
        ),
        x="Product line",
        y="Quantity",
        text_auto=".2s",
        title="Quantity Sold by Category"
    )

    st.plotly_chart(
        fig_quantity,
        width="stretch"
    )


# ------------------------------------------------------------
# Profit by Category
# ------------------------------------------------------------
with product_chart2:

    fig_category_profit = px.bar(
        category_sales.sort_values(
            "Profit",
            ascending=False
        ),
        x="Product line",
        y="Profit",
        text_auto=".2s",
        title="Profit by Product Category"
    )

    st.plotly_chart(
        fig_category_profit,
        width="stretch"
    )


# ============================================================
# PRODUCT TABLE
# ============================================================
st.subheader("Product Category Performance Table")

category_table = category_sales.copy()

category_table.columns = [
    "Product Category",
    "Revenue",
    "Quantity Sold",
    "Profit"
]

st.dataframe(
    category_table.style.format(
        {
            "Revenue": "${:,.2f}",
            "Quantity Sold": "{:,.0f}",
            "Profit": "${:,.2f}"
        }
    ),
    width="stretch"
)


# ============================================================
# CUSTOMER ANALYSIS
# ============================================================
st.header("👥 Customer Analysis")


customer_analysis = (
    filtered_df
    .groupby(
        "Customer type",
        as_index=False
    )
    .agg(
        Revenue=("Total", "sum"),
        Transactions=("Invoice ID", "count"),
        Average_Order=("Total", "mean")
    )
)


gender_analysis = (
    filtered_df
    .groupby(
        "Gender",
        as_index=False
    )
    .agg(
        Revenue=("Total", "sum"),
        Transactions=("Invoice ID", "count"),
        Average_Order=("Total", "mean")
    )
)


customer_chart1, customer_chart2 = st.columns(2)


with customer_chart1:

    fig_customer = px.bar(
        customer_analysis,
        x="Customer type",
        y="Revenue",
        color="Customer type",
        text_auto=".2s",
        title="Revenue by Customer Type"
    )

    st.plotly_chart(
        fig_customer,
        width="stretch"
    )


with customer_chart2:

    fig_gender = px.bar(
        gender_analysis,
        x="Gender",
        y="Revenue",
        color="Gender",
        text_auto=".2s",
        title="Revenue by Gender"
    )

    st.plotly_chart(
        fig_gender,
        width="stretch"
    )


# ============================================================
# PAYMENT ANALYSIS
# ============================================================
st.header("💳 Payment Method Analysis")


payment_analysis = (
    filtered_df
    .groupby(
        "Payment",
        as_index=False
    )
    .agg(
        Transactions=("Invoice ID", "count"),
        Revenue=("Total", "sum"),
        Average_Order=("Total", "mean")
    )
)


payment_chart1, payment_chart2 = st.columns(2)


with payment_chart1:

    fig_payment_share = px.pie(
        payment_analysis,
        names="Payment",
        values="Transactions",
        title="Transaction Share by Payment Method"
    )

    st.plotly_chart(
        fig_payment_share,
        width="stretch"
    )


with payment_chart2:

    fig_payment_revenue = px.bar(
        payment_analysis,
        x="Payment",
        y="Revenue",
        color="Payment",
        text_auto=".2s",
        title="Revenue by Payment Method"
    )

    st.plotly_chart(
        fig_payment_revenue,
        width="stretch"
    )


# ============================================================
# CUSTOMER PAYMENT BEHAVIOR
# ============================================================
st.subheader("Customer Payment Behavior")


customer_payment = (
    filtered_df
    .groupby(
        [
            "Customer type",
            "Payment"
        ],
        as_index=False
    )
    .size()
    .rename(
        columns={
            "size": "Transactions"
        }
    )
)


fig_customer_payment = px.bar(
    customer_payment,
    x="Customer type",
    y="Transactions",
    color="Payment",
    barmode="group",
    title="Payment Method by Customer Type"
)

st.plotly_chart(
    fig_customer_payment,
    width="stretch"
)


# ============================================================
# CITY PERFORMANCE TABLE
# ============================================================
st.header("📍 City Performance")


city_table = (
    filtered_df
    .groupby(
        "City Name",
        as_index=False
    )
    .agg(
        Revenue=("Total", "sum"),
        Profit=("gross income", "sum"),
        Transactions=("Invoice ID", "count"),
        Quantity=("Quantity", "sum"),
        Average_Order=("Total", "mean"),
        Average_Rating=("Rating", "mean")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)


city_display = city_table.copy()

city_display.columns = [
    "City",
    "Revenue",
    "Profit",
    "Transactions",
    "Quantity Sold",
    "Average Order",
    "Average Rating"
]


st.dataframe(
    city_display.style.format(
        {
            "Revenue": "${:,.2f}",
            "Profit": "${:,.2f}",
            "Transactions": "{:,.0f}",
            "Quantity Sold": "{:,.0f}",
            "Average Order": "${:,.2f}",
            "Average Rating": "{:.2f}"
        }
    ),
    width="stretch"
)


# ============================================================
# PROFITABILITY ANALYSIS
# ============================================================
st.header("💰 Profitability Analysis")


profit_analysis = (
    filtered_df
    .groupby(
        "Product line",
        as_index=False
    )
    .agg(
        Revenue=("Total", "sum"),
        Profit=("gross income", "sum")
    )
)


profit_analysis["Profit Margin"] = np.where(
    profit_analysis["Revenue"] > 0,
    (
        profit_analysis["Profit"]
        / profit_analysis["Revenue"]
    ) * 100,
    0
)


profit_chart1, profit_chart2 = st.columns(2)


with profit_chart1:

    fig_revenue_profit = px.bar(
        profit_analysis,
        x="Product line",
        y=[
            "Revenue",
            "Profit"
        ],
        barmode="group",
        title="Revenue vs Profit by Category"
    )

    st.plotly_chart(
        fig_revenue_profit,
        width="stretch"
    )


with profit_chart2:

    fig_margin = px.bar(
        profit_analysis.sort_values(
            "Profit Margin",
            ascending=False
        ),
        x="Product line",
        y="Profit Margin",
        text_auto=".2f",
        title="Profit Margin by Category"
    )

    st.plotly_chart(
        fig_margin,
        width="stretch"
    )


# ============================================================
# TIME ANALYSIS
# ============================================================
st.header("⏰ Time-Based Sales Analysis")


if (
    "Hour" in filtered_df.columns
    and filtered_df["Hour"].notna().any()
):

    hourly_sales = (
        filtered_df
        .dropna(subset=["Hour"])
        .groupby(
            "Hour",
            as_index=False
        )
        .agg(
            Revenue=("Total", "sum"),
            Transactions=("Invoice ID", "count")
        )
        .sort_values("Hour")
    )


    time_chart1, time_chart2 = st.columns(2)


    with time_chart1:

        fig_hour_revenue = px.line(
            hourly_sales,
            x="Hour",
            y="Revenue",
            markers=True,
            title="Revenue by Hour"
        )

        st.plotly_chart(
            fig_hour_revenue,
            width="stretch"
        )


    with time_chart2:

        fig_hour_transactions = px.bar(
            hourly_sales,
            x="Hour",
            y="Transactions",
            title="Transactions by Hour"
        )

        st.plotly_chart(
            fig_hour_transactions,
            width="stretch"
        )


# ============================================================
# CUSTOMER SATISFACTION
# ============================================================
st.header("⭐ Customer Satisfaction")


rating_chart1, rating_chart2 = st.columns(2)


with rating_chart1:

    fig_rating = px.histogram(
        filtered_df,
        x="Rating",
        nbins=10,
        title="Customer Rating Distribution"
    )

    st.plotly_chart(
        fig_rating,
        width="stretch"
    )


rating_by_category = (
    filtered_df
    .groupby(
        "Product line",
        as_index=False
    )
    .agg(
        Average_Rating=("Rating", "mean")
    )
    .sort_values(
        "Average_Rating",
        ascending=False
    )
)


with rating_chart2:

    fig_rating_category = px.bar(
        rating_by_category,
        x="Product line",
        y="Average_Rating",
        text_auto=".2f",
        title="Average Rating by Product Category"
    )

    st.plotly_chart(
        fig_rating_category,
        width="stretch"
    )


# ============================================================
# KEY INSIGHTS
# ============================================================
st.header("💡 Key Insights")


top_category = (
    category_sales
    .sort_values(
        "Revenue",
        ascending=False
    )
    .iloc[0]
)


lowest_category = (
    category_sales
    .sort_values(
        "Revenue",
        ascending=True
    )
    .iloc[0]
)


top_city = (
    city_sales
    .sort_values(
        "Revenue",
        ascending=False
    )
    .iloc[0]
)


top_branch = (
    branch_sales
    .sort_values(
        "Revenue",
        ascending=False
    )
    .iloc[0]
)


top_customer = (
    customer_analysis
    .sort_values(
        "Revenue",
        ascending=False
    )
    .iloc[0]
)


top_payment = (
    payment_analysis
    .sort_values(
        "Transactions",
        ascending=False
    )
    .iloc[0]
)


insight1, insight2 = st.columns(2)


with insight1:

    st.info(
        f"""
        **Top Product Category**

        {top_category['Product line']} generated
        **${top_category['Revenue']:,.2f}**
        in revenue.
        """
    )


    st.info(
        f"""
        **Top City**

        **{top_city['City Name']}** generated
        **${top_city['Revenue']:,.2f}**
        in revenue.
        """
    )


    st.info(
        f"""
        **Top Supermarket Branch**

        **{top_branch['Branch Name']}** generated
        **${top_branch['Revenue']:,.2f}**
        in revenue.
        """
    )


with insight2:

    st.warning(
        f"""
        **Lowest Revenue Category**

        {lowest_category['Product line']} generated
        **${lowest_category['Revenue']:,.2f}**
        in revenue and may require further analysis.
        """
    )


    st.info(
        f"""
        **Highest Revenue Customer Type**

        **{top_customer['Customer type']}**
        generated
        **${top_customer['Revenue']:,.2f}**
        in revenue.
        """
    )


    st.info(
        f"""
        **Most Used Payment Method**

        **{top_payment['Payment']}**
        recorded
        **{int(top_payment['Transactions']):,}**
        transactions.
        """
    )


# ============================================================
# RECOMMENDATIONS
# ============================================================
st.header("🎯 Business Recommendations")


st.markdown(
    f"""
    ### 1. Focus on High-Performing Categories

    Continue monitoring **{top_category['Product line']}**
    because it currently contributes the highest revenue in the
    selected dataset.

    ### 2. Review Lower-Performing Categories

    Investigate **{lowest_category['Product line']}** to understand
    whether demand, pricing, product mix, or promotional activity
    is affecting its performance.

    ### 3. Study Strong City Performance

    Analyze the factors contributing to strong performance in
    **{top_city['City Name']}** and evaluate whether successful
    practices can be applied to other locations.

    ### 4. Monitor Branch Performance

    **{top_branch['Branch Name']}** currently contributes the highest
    branch revenue in the selected data. Its product mix and customer
    patterns can be studied for useful business practices.

    ### 5. Understand Customer Segments

    The **{top_customer['Customer type']}** customer segment currently
    contributes the highest revenue. Customer purchasing patterns can
    be monitored to support targeted engagement strategies.

    ### 6. Monitor Payment Preferences

    **{top_payment['Payment']}** is the most frequently used payment
    method. Maintaining a convenient payment experience can support
    customer satisfaction.

    ### 7. Focus on Profitability

    Management should evaluate revenue together with profit and
    profit margin rather than relying only on sales volume.
    """
)


# ============================================================
# DATASET SUMMARY
# ============================================================
with st.expander("📋 Dataset Summary"):

    summary1, summary2, summary3 = st.columns(3)


    summary1.metric(
        "Original Records",
        f"{len(df):,}"
    )


    summary2.metric(
        "Filtered Records",
        f"{len(filtered_df):,}"
    )


    summary3.metric(
        "Number of Columns",
        f"{len(df.columns):,}"
    )


    st.write("### Dataset Columns")

    st.write(
        df.columns.tolist()
    )


    st.write("### Data Preview")

    st.dataframe(
        filtered_df.head(20),
        width="stretch"
    )


# ============================================================
# EXPORT FILTERED DATA
# ============================================================
st.header("⬇️ Export Data")


csv_data = (
    filtered_df
    .to_csv(index=False)
    .encode("utf-8")
)


st.download_button(
    label="Download Filtered Dataset",
    data=csv_data,
    file_name="filtered_supermarket_sales.csv",
    mime="text/csv"
)


# ============================================================
# FOOTER
# ============================================================
st.divider()

st.caption(
    "Supermarket Sales & Customer Analytics Dashboard | "
    "Python • Pandas • NumPy • Plotly • Streamlit"
)