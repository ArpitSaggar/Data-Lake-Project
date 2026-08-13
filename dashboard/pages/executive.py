import streamlit as st

from utils import (
    metric_card,
    format_inr
)

from charts import (
    bar_chart,
    pie_chart
)


def render(
    page_df,
    device_df,
    browser_df,
    category_df,
    referral_df,
    purchase_df,
    os_df,
    total_events,
    total_revenue,
    average_price,
    purchase_events,
    conversion_rate,
):

    st.markdown(
        "<div class='section-title'>Executive Overview</div>",
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        metric_card(
            "TOTAL EVENTS",
            f"{total_events:,}",
            "📈"
        )

    with col2:

        metric_card(
            "TOTAL REVENUE",
            format_inr(total_revenue),
            "💰"
        )

    with col3:

        metric_card(
            "AVERAGE PRICE",
            format_inr(average_price),
            "🏷️"
        )

    with col4:

        metric_card(
            "CONVERSION RATE",
            f"{conversion_rate:.2f}%",
            "🎯"
        )

    st.markdown("---")

    st.markdown(
        "<div class='section-title'>Revenue Insights</div>",
        unsafe_allow_html=True
    )

    left, right = st.columns(2)

    with left:

        fig = bar_chart(
            dataframe=category_df,
            x="category",
            y="revenue",
            title="Revenue by Category"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

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

    st.markdown("---")

    st.markdown(
        "<div class='section-title'>Customer Insights</div>",
        unsafe_allow_html=True
    )

    left, right = st.columns(2)

    with left:

        fig = bar_chart(
            dataframe=browser_df,
            x="browser",
            y="revenue",
            title="Revenue by Browser"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

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

    st.markdown("---")

    st.markdown(
        "<div class='section-title'>Platform Analytics</div>",
        unsafe_allow_html=True
    )

    fig = bar_chart(
        dataframe=os_df,
        x="operating_system",
        y="revenue",
        title="Revenue by Operating System"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )