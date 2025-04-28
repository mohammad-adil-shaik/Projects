import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_echarts import st_echarts

st.set_page_config(layout="wide")



@st.cache_data
def load_data():
    return pd.read_csv("Raw_data.csv")

df = load_data()

# ----- Sidebar Menu -----
st.sidebar.image(
   "assets/a2.jpg",
    use_container_width=True
)


# st.sidebar.markdown("### 🗂️ Project: Global Trade Analytics")
selected_country = st.sidebar.selectbox("🌍 Select Country", sorted(df["country_or_area"].unique()), index=0)
year_range = st.sidebar.slider("📅 Select Year Range", int(df["year"].min()), int(df["year"].max()), (1990, 2016))
trade_type = st.sidebar.radio("🌐 Select Trade Type", df["flow"].unique().tolist())

# ----- Filter Data -----
filtered_df = df[
    (df["country_or_area"] == selected_country) &
    (df["year"].between(year_range[0], year_range[1])) &
    (df["flow"] == trade_type)
]

# ----- Main Tabs -----
st.title("📦 TradeSphere: Global Trade Analytics Dashboard")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Overview", "📦 Commodity Charts", "📈 Flow & Category", "🧪 Advanced Insights", "🚚 Crossflow"])





with tab1:
    # ---------- KPIs ----------
    st.markdown("### 💡 Key Performance Indicators")
    total_trade = filtered_df["trade_usd"].sum()
    total_weight = filtered_df["weight_kg"].sum()
    num_commodities = filtered_df["commodity"].nunique()
    avg_trade_per_commodity = total_trade / num_commodities if num_commodities else 0

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("💰 Total Trade Value (USD)", f"${total_trade:,.0f}")
    k2.metric("⚖️ Total Weight (kg)", f"{total_weight:,.0f}")
    k3.metric("📦 No. of Commodities", f"{num_commodities}")
    k4.metric("📊 Avg Trade per Commodity", f"${avg_trade_per_commodity:,.0f}")

with tab2:
    st.markdown("### 📈 Trade Value per Year by Commodity")
    if not filtered_df.empty:
        scatter = alt.Chart(filtered_df).mark_circle(size=70).encode(
            x="year:O",
            y="trade_usd:Q",
            color="commodity:N",
            tooltip=["commodity", "trade_usd", "year"]
        ).interactive().properties(height=400)
        st.altair_chart(scatter, use_container_width=True)
    else:
        st.info("No data available for selected filters.")

    st.markdown("### 🏆 Top Commodities by Trade Value")
    if not filtered_df.empty:
        top_commodities = (
            filtered_df.groupby("commodity")["trade_usd"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )
        bar = alt.Chart(top_commodities).mark_bar().encode(
            x="trade_usd:Q",
            y=alt.Y("commodity:N", sort='-x'),
            color=alt.value("#f77f00"),
            tooltip=["commodity", "trade_usd"]
        ).properties(height=400)
        st.altair_chart(bar, use_container_width=True)
    else:
        st.info("No data available to display top commodities.")


with tab3:
    st.markdown("### 📈 Trade Flow Trends")

    pivot_data = filtered_df[
        filtered_df["flow"].isin(["Import", "Re-Import", "Export", "Re-Export"])
    ].pivot_table(index='year', columns='flow', values='trade_usd', aggfunc='sum').fillna(0).reset_index()

    years = pivot_data["year"].astype(str).tolist()
    color_map = {
        "Import": "#FF5733", "Re-Import": "#FFC300",
        "Export": "#007BFF", "Re-Export": "#28B463"
    }

    series = []
    for flow in ["Import", "Re-Import", "Export", "Re-Export"]:
        if flow in pivot_data.columns and pivot_data[flow].sum() > 0:
            series.append({
                "name": flow,
                "type": "line",
                "stack": "Total",
                "data": pivot_data[flow].tolist(),
                "lineStyle": {"color": color_map[flow]}
            })

    if series:
        line_chart_options = {
            "title": {
                "text": f"📈 Trade Flow Trends for {selected_country}",
                "left": "center",
                "top": "5%"
            },
            "tooltip": {"trigger": "axis"},
            "legend": {
                "data": [s["name"] for s in series],
                "top": "12%",
                "left": "center"
            },
            "grid": {
                "left": "3%",
                "right": "4%",
                "bottom": "10%",
                "top": "18%",
                "containLabel": True
            },
            "toolbox": {"feature": {"saveAsImage": {}}},
            "xAxis": {
                "type": "category",
                "boundaryGap": False,
                "data": years
            },
            "yAxis": {"type": "value"},
            "series": series,
        }
        st_echarts(options=line_chart_options, height="400px")
    else:
        st.info("No data available for the selected trade flow.")

    st.markdown("### 🥧 Trade Value by Category")

    # ✅ No need to refilter, just use filtered_df directly
    pie_filter = filtered_df

    if "category" not in pie_filter.columns or pie_filter["category"].isnull().all():
        pie_data = [{"value": 1, "name": "No Category Data"}]
    else:
        category_data = pie_filter.groupby("category")["trade_usd"].sum().reset_index()
        category_data = category_data[category_data["trade_usd"] > 0]

        if not category_data.empty:
            pie_data = [
                {"value": row["trade_usd"], "name": row["category"]}
                for _, row in category_data.iterrows()
            ]
        else:
            pie_data = [{"value": 1, "name": "No Trade Value"}]

    pie_chart_options = {
        "title": {
            "text": f"Trade Value by Category ({selected_country})",
            "subtext": f"{year_range[0]} to {year_range[1]}",
            "left": "center",
        },
        "tooltip": {"trigger": "item"},
        "legend": {"show": False},
        "series": [{
            "name": "Category",
            "type": "pie",
            "radius": ["40%", "70%"],
            "minAngle": 2,
            "avoidLabelOverlap": False,
            "label": {
                "show": True,
                "formatter": "{b}"
            },
            "labelLine": {"show": True},
            "data": pie_data,
            "emphasis": {
                "itemStyle": {
                    "shadowBlur": 10,
                    "shadowOffsetX": 0,
                    "shadowColor": "rgba(0, 0, 0, 0.5)"
                }
            }
        }]
    }

    st_echarts(options=pie_chart_options, height="600px")

    st.markdown("### 🌳 Trade Value by Category")

    if not filtered_df.empty:
        treemap_data = filtered_df.groupby('category')['trade_usd'].sum().reset_index()
        treemap_data = treemap_data.sort_values('trade_usd', ascending=False)

        treemap_option = {
            "series": [{
                "type": "treemap",
                "data": [{"name": row["category"], "value": row["trade_usd"]} for _, row in treemap_data.iterrows()]
            }]
        }

        st_echarts(options=treemap_option, height="600px")
    else:
        st.info("No data available to show treemap.")






with tab4:
    st.markdown("### 🔥 Trade Value by Country and Category")
    heatmap_data = filtered_df.groupby(["country_or_area", "category"])["trade_usd"].sum().reset_index()
    heatmap_pivot = heatmap_data.pivot(index="category", columns="country_or_area", values="trade_usd").fillna(0)
    fig_hm, ax_hm = plt.subplots(figsize=(14, 8))
    sns.heatmap(heatmap_pivot, cmap="YlGnBu", ax=ax_hm)
    st.pyplot(fig_hm)

    st.markdown("### 📐 Top 20 Commodities by Trade Value")
    pareto_data = filtered_df.groupby("commodity")["trade_usd"].sum().sort_values(ascending=False).reset_index()
    pareto_data["cumulative_percent"] = pareto_data["trade_usd"].cumsum() / pareto_data["trade_usd"].sum() * 100
    fig_pareto, ax1 = plt.subplots(figsize=(12, 5))
    sns.barplot(x="commodity", y="trade_usd", data=pareto_data.head(20), ax=ax1, color="skyblue")
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)
    ax2 = ax1.twinx()
    sns.lineplot(x="commodity", y="cumulative_percent", data=pareto_data.head(20), ax=ax2, color="red", marker="o")
    ax1.set_ylabel("Trade USD")
    ax2.set_ylabel("Cumulative %")
    st.pyplot(fig_pareto)

    st.markdown("### 🫧 Trade Value vs Weight (Bubble Size = Quantity)")
    bubble_data = filtered_df.dropna(subset=["trade_usd", "weight_kg", "quantity"]).sample(n=min(500, len(filtered_df)), random_state=1)
    fig_bubble, ax_bubble = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=bubble_data,
        x="weight_kg", y="trade_usd", size="quantity",
        hue="flow", alpha=0.6, sizes=(20, 400), ax=ax_bubble
    )
    ax_bubble.set_xscale("log")
    ax_bubble.set_yscale("log")
    ax_bubble.set_xlabel("Weight (kg) [log]")
    ax_bubble.set_ylabel("Trade Value (USD) [log]")
    st.pyplot(fig_bubble)


with tab5:
    st.markdown(f"### 🚚 Import vs Export Strength for {selected_country}")

    # Corrected filtering for selected country
    import_export = df[
        (df["country_or_area"] == selected_country) &
        (df["year"].between(year_range[0], year_range[1]))
    ].groupby(["commodity", "flow"])["trade_usd"].sum().unstack(fill_value=0).reset_index()

    import_export["Import"] = -import_export.get("Import", 0)
    import_export["Re-Import"] = -import_export.get("Re-Import", 0)
    import_export["Export"] = import_export.get("Export", 0)
    import_export["Re-Export"] = import_export.get("Re-Export", 0)

    import_export["Total_Import"] = import_export["Import"] + import_export["Re-Import"]
    import_export["Total_Export"] = import_export["Export"] + import_export["Re-Export"]

    import_export["Volume"] = import_export["Total_Export"].abs() + import_export["Total_Import"].abs()
    top_items = import_export.sort_values("Volume", ascending=False).head(20)

    fig_strength, ax_strength = plt.subplots(figsize=(14, 8))
    ax_strength.barh(top_items["commodity"], top_items["Total_Import"], color='red', label="Import")
    ax_strength.barh(top_items["commodity"], top_items["Total_Export"], color='green', label="Export")

    ax_strength.set_xlabel("Trade Value (USD)")
    ax_strength.set_title(f"Top Commodities for {selected_country}: Import vs Export Strength")
    ax_strength.legend()
    st.pyplot(fig_strength)


