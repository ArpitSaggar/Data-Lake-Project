import streamlit as st
from babel.numbers import format_currency


# ----------------------------------------------------
# INDIAN CURRENCY FORMAT
# ----------------------------------------------------

def format_inr(value):
    """
    Formats numbers using the Indian numbering system.
    Example:
    707761445 -> ₹70,77,61,445.00
    """
    return format_currency(
        value,
        "INR",
        locale="en_IN"
    )


# ----------------------------------------------------
# LARGE KPI CARD
# ----------------------------------------------------

def metric_card(title, value, icon="📊"):

    html = f"""<div class="metric-card">
<div style="font-size:34px; text-align:center; margin-bottom:10px;">
{icon}
</div>
<div class="metric-title">
{title}
</div>
<div class="metric-value">
{value}
</div>
</div>"""

    st.markdown(
        html.strip(),
        unsafe_allow_html=True
    )


# ----------------------------------------------------
# SMALL METRIC CARD
# ----------------------------------------------------

def small_metric(title, value):

    html = f"""<div style="
background:#18212F;
padding:14px;
border-radius:12px;
text-align:center;
border:1px solid rgba(255,255,255,.08);
">
<div style="
font-size:13px;
color:#94A3B8;
margin-bottom:8px;
">
{title}
</div>
<div style="
font-size:22px;
font-weight:700;
color:white;
">
{value}
</div>
</div>"""

    st.markdown(
        html.strip(),
        unsafe_allow_html=True
    )