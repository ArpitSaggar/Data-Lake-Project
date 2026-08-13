import streamlit as st

from styles import load_css
from utils import metric_card, small_metric, format_inr
from data_loader import (
    load_page,
    load_device,
    load_browser,
    load_category,
    load_referral,
    load_purchase,
    load_os
)

from charts import (
    bar_chart,
    pie_chart
)
# ----------------------------------------------------
# STREAMLIT APP
# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------

st.set_page_config(
    page_title="Enterprise Clickstream Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# LOAD CSS
# ----------------------------------------------------

load_css()

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------

st.markdown(
"""
<div class="header-box">

<div class="header-title">

Enterprise Clickstream Analytics

</div>

<div class="header-subtitle">

Apache Spark • Apache Kafka • DuckDB • Plotly • Streamlit

<br><br>

Designed & Developed by
<b>Arpit Saggar</b>

</div>

</div>
""",
unsafe_allow_html=True
)

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "",
    [
        "Executive Overview",
        "Customer Behaviour",
        "Revenue Analytics",
        "Product Intelligence",
        "System Overview",
        "About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption("Enterprise Clickstream Analytics")

st.sidebar.caption("Version 1.0")


page_df = load_page()

device_df = load_device()

browser_df = load_browser()

category_df = load_category()

referral_df = load_referral()

purchase_df = load_purchase()

os_df = load_os()
# ----------------------------------------------------
# FILTERS
# ----------------------------------------------------

st.sidebar.markdown("---")

st.sidebar.subheader("Filters")

selected_device = st.sidebar.multiselect(
    "Device",
    sorted(device_df["device"].unique()),
    default=sorted(device_df["device"].unique())
)

selected_browser = st.sidebar.multiselect(
    "Browser",
    sorted(browser_df["browser"].unique()),
    default=sorted(browser_df["browser"].unique())
)

selected_os = st.sidebar.multiselect(
    "Operating System",
    sorted(os_df["operating_system"].unique()),
    default=sorted(os_df["operating_system"].unique())
)

selected_referral = st.sidebar.multiselect(
    "Referral Source",
    sorted(referral_df["referral_source"].unique()),
    default=sorted(referral_df["referral_source"].unique())
)
# ----------------------------------------------------
# APPLY FILTERS
# ----------------------------------------------------

device_df = device_df[
    device_df["device"].isin(selected_device)
]

browser_df = browser_df[
    browser_df["browser"].isin(selected_browser)
]

os_df = os_df[
    os_df["operating_system"].isin(selected_os)
]

referral_df = referral_df[
    referral_df["referral_source"].isin(selected_referral)
]

# ----------------------------------------------------
# KPI CALCULATIONS
# ----------------------------------------------------

total_events = int(page_df["total_visits"].sum())

total_revenue = float(category_df["revenue"].sum())

average_price = float(category_df["avg_price"].mean())

purchase_events = int(
    purchase_df.loc[
        purchase_df["is_purchase"] == True,
        "events"
    ].sum()
)

conversion_rate = (
    purchase_events
    /
    total_events
) * 100

# ----------------------------------------------------
# EXECUTIVE OVERVIEW
# ----------------------------------------------------

if page == "Executive Overview":

    st.markdown(
        "<div class='section-title'>Executive Overview</div>",
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        metric_card(
            "TOTAL EVENTS",
            f"{total_events:,}"
        )

    with col2:

        metric_card(
            "TOTAL REVENUE",
            format_inr(total_revenue)
        )

    with col3:

        metric_card(
            "AVERAGE PRICE",
            format_inr(average_price)
        )

    with col4:

        metric_card(
            "CONVERSION RATE",
            f"{conversion_rate:.2f}%"
        )

    st.write("")

    st.markdown("---")

    st.subheader("Business Summary")

    left, right = st.columns(2)

    with left:

        st.metric(
            "Categories",
            len(category_df)
        )

        st.metric(
            "Browsers",
            len(browser_df)
        )

        st.metric(
            "Referral Sources",
            len(referral_df)
        )

    with right:

        st.metric(
            "Devices",
            len(device_df)
        )

        st.metric(
            "Purchase Events",
            f"{purchase_events:,}"
        )

        st.metric(
            "Operating Systems",
            len(os_df)
        )

    st.markdown("---")
    # ----------------------------------------------------
    # REVENUE INSIGHTS
    # ----------------------------------------------------

    st.markdown(
        "<div class='section-title'>Revenue Insights</div>",
        unsafe_allow_html=True
    )

    chart1, chart2 = st.columns(2)

    with chart1:

        fig = bar_chart(
            dataframe=category_df.sort_values(
                "revenue",
                ascending=False
            ),
            x="category",
            y="revenue",
            title="Revenue by Category"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with chart2:

        fig = pie_chart(
            dataframe=device_df,
            names="device",
            values="revenue",
            title="Revenue by Device"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ----------------------------------------------------
    # CUSTOMER INSIGHTS
    # ----------------------------------------------------

    st.markdown("---")

    st.markdown(
        "<div class='section-title'>Customer Insights</div>",
        unsafe_allow_html=True
    )

    chart3, chart4 = st.columns(2)

    with chart3:

        fig = bar_chart(
            dataframe=browser_df.sort_values(
                "revenue",
                ascending=False
            ),
            x="browser",
            y="revenue",
            title="Revenue by Browser"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with chart4:

        fig = pie_chart(
            dataframe=referral_df,
            names="referral_source",
            values="revenue",
            title="Revenue by Referral Source"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ----------------------------------------------------
    # OPERATING SYSTEM ANALYTICS
    # ----------------------------------------------------

    st.markdown("---")

    st.markdown(
        "<div class='section-title'>Platform Analytics</div>",
        unsafe_allow_html=True
    )

    fig = bar_chart(
        dataframe=os_df.sort_values(
            "revenue",
            ascending=False
        ),
        x="operating_system",
        y="revenue",
        title="Revenue by Operating System"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

elif page == "Customer Behaviour":

    st.markdown(
        "<div class='section-title'>Customer Behaviour</div>",
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Browser Distribution")

        fig = pie_chart(
            dataframe=browser_df,
            names="browser",
            values="revenue",
            title="Revenue Share by Browser"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.subheader("Operating System Distribution")

        fig = pie_chart(
            dataframe=os_df,
            names="operating_system",
            values="revenue",
            title="Revenue Share by Operating System"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    st.subheader("Traffic Sources")

    fig = bar_chart(
        dataframe=referral_df.sort_values(
            "revenue",
            ascending=False
        ),
        x="referral_source",
        y="revenue",
        title="Revenue by Referral Source"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

elif page == "Revenue Analytics":

    st.markdown(
        "<div class='section-title'>Revenue Analytics</div>",
        unsafe_allow_html=True
    )

    st.metric(
        "Total Revenue",
        f"₹{total_revenue:,.0f}"
    )

    st.metric(
        "Average Product Price",
        f"₹{average_price:.2f}"
    )

    st.markdown("---")

    st.subheader("Category Revenue")

    fig = bar_chart(
        dataframe=category_df.sort_values(
            "revenue",
            ascending=False
        ),
        x="category",
        y="revenue",
        title="Revenue by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Category Analytics")

    st.dataframe(
        category_df.sort_values(
            "revenue",
            ascending=False
        ),
        use_container_width=True
    )

# ----------------------------------------------------
# PRODUCT INTELLIGENCE
# ----------------------------------------------------

elif page == "Product Intelligence":

    st.markdown(
        "<div class='section-title'>Product Intelligence</div>",
        unsafe_allow_html=True
    )

    highest_revenue = category_df.loc[
        category_df["revenue"].idxmax()
    ]

    most_orders = category_df.loc[
        category_df["orders"].idxmax()
    ]

    highest_price = category_df.loc[
        category_df["avg_price"].idxmax()
    ]

    c1, c2, c3 = st.columns(3)

    with c1:

        metric_card(
            "TOP CATEGORY",
            highest_revenue["category"]
        )

        st.metric(
            "Revenue",
            f"₹{highest_revenue['revenue']:,.0f}"
        )

    with c2:

        metric_card(
            "MOST ORDERS",
            most_orders["category"]
        )

        st.metric(
            "Orders",
            f"{int(most_orders['orders'])}"
        )

    with c3:

        metric_card(
            "HIGHEST PRICE",
            highest_price["category"]
        )

        st.metric(
            "Average Price",
            f"₹{highest_price['avg_price']:.2f}"
        )

    st.markdown("---")

    fig = bar_chart(
        dataframe=category_df.sort_values(
            "orders",
            ascending=False
        ),
        x="category",
        y="orders",
        title="Orders by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Complete Category Analytics")

    st.dataframe(
        category_df.sort_values(
            "revenue",
            ascending=False
        ),
        use_container_width=True,
        hide_index=True
    )

# ----------------------------------------------------
# SYSTEM OVERVIEW
# ----------------------------------------------------

elif page == "System Overview":

    st.markdown(
        "<div class='section-title'>System Architecture</div>",
        unsafe_allow_html=True
    )

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "EVENTS PROCESSED",
            f"{total_events:,}"
        )

    with c2:
        metric_card(
            "TOTAL REVENUE",
            f"₹{total_revenue:,.0f}"
        )

    with c3:
        metric_card(
            "PRODUCT CATEGORIES",
            str(len(category_df))
        )

    with c4:
        metric_card(
            "DEVICES",
            str(len(device_df))
        )

    st.markdown("---")

    st.subheader("Data Pipeline Architecture")

    st.code("""
                 CSV Dataset
                      │
                      ▼
              Apache Kafka Producer
                      │
                      ▼
              Apache Kafka Consumer
                      │
                      ▼
               Bronze Layer (Parquet)
                      │
                      ▼
              Apache Spark Cleaning
                      │
                      ▼
               Silver Layer (Parquet)
                      │
                      ▼
            Apache Spark Aggregations
                      │
                      ▼
                Gold Layer (Parquet)
                      │
                      ▼
                   DuckDB Engine
                      │
                      ▼
             Streamlit BI Dashboard
""")

    st.markdown("---")

    st.subheader("Technology Stack")

    col1, col2 = st.columns(2)

    with col1:

        st.success("✅ Apache Kafka")

        st.success("✅ Apache Spark")

        st.success("✅ DuckDB")

        st.success("✅ Streamlit")

    with col2:

        st.success("✅ Plotly")

        st.success("✅ Python")

        st.success("✅ Parquet")

        st.success("✅ Pandas")

    st.markdown("---")

    st.subheader("Project Statistics")

    stats = {
        "Bronze Records": total_events,
        "Purchase Events": purchase_events,
        "Categories": len(category_df),
        "Browsers": len(browser_df),
        "Devices": len(device_df),
        "Operating Systems": len(os_df)
    }

    st.json(stats)

    st.markdown("---")

    st.info(
        "This dashboard demonstrates a complete Medallion (Bronze → Silver → Gold) Data Engineering architecture built using Apache Kafka, Apache Spark, DuckDB and Streamlit."
    )

# ----------------------------------------------------
# ABOUT
# ----------------------------------------------------

else:

    st.markdown(
        "<div class='section-title'>About</div>",
        unsafe_allow_html=True
    )

    st.markdown("""
### Enterprise Clickstream Analytics

This project demonstrates a complete modern Data Engineering pipeline built using:

- Apache Kafka
- Apache Spark
- DuckDB
- Streamlit
- Plotly
- Python

---

### Features

- End-to-End Data Pipeline
- Bronze → Silver → Gold Architecture
- Interactive Dashboard
- Dynamic Filters
- Business KPIs
- Revenue Analytics
- Customer Behaviour Analytics

---

### Designed & Developed by

## Arpit Saggar
""")

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.markdown("---")

st.caption(
    "Enterprise Clickstream Analytics | Apache Kafka • Apache Spark • DuckDB • Streamlit | © 2026 Arpit Saggar"
)
