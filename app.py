import streamlit as st

st.set_page_config(
    page_title="Master Streamlit Hub",
    layout="centered"
)

st.title("📂 Master Streamlit Project Hub")
st.write("Welcome! Click any project below to open it in a new tab.")

# Add your Streamlit project URL entries here:
projects = [
    {
        "name": "TSV/CSV Converter Outbound",
        "desc": "TSV/CSV Converter Outbound",
        "url": "https://csvmakeroutbound-a6m526ig59dshbntyv9hyr.streamlit.app/"
    },
    {
        "name": "Inbound TSV to CSV Converter",
        "desc": "Inbound TSV to CSV Converter",
        "url": "https://inboundcsvmaker-h5qh2arri4ajr5ulnsmjap.streamlit.app/"
    },
    {
        "name": "📦 Leon's Warehouse Pick List Merger",
        "desc": "📦 Leon's Warehouse Pick List Merger",
        "url": "https://bs04papersum-serkfdc9lkvmvg64phhcp7.streamlit.app/"
    },
    {
        "name": "Inventory Volume Calculator",
        "desc": "Inventory Volume Calculator",
        "url": "https://usluggagevolumes-2dzmdwn4uv6avzhmy5yacr.streamlit.app/"
    },
    {
        "name": "📦 Leon's Warehouse Pick List Merger",
        "desc": "📦 Leon's Warehouse Pick List Merger",
        "url": "https://sumpaperlist-cxjb4cd8qecpikhqvn9wbg.streamlit.app/"
    },
]

for p in projects:
    st.markdown(f"### {p['name']}")
    st.write(p["desc"])
    st.markdown(f"[▶ Open App]({p['url']})")
    st.markdown("---")
