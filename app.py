"""
OmicsVault — Multi-Omics Biomarker Discovery Platform for Cancer
Main application entry point.

Run: streamlit run app.py
"""

import streamlit as st
import sys
import os

# ── Path setup ─────────────────────────────────────────────────────────────────
APP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, APP_DIR)

# ── Page config (must be first Streamlit call) ─────────────────────────────────
st.set_page_config(
    page_title="OmicsVault — Multi-Omics Biomarker Discovery",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "mailto:support@omicsvault.io",
        "About": "OmicsVault v1.0 — Precision Oncology Research Platform",
    },
)

# ── Database init ──────────────────────────────────────────────────────────────
from database.db_setup import init_database
init_database()

# ── Auth ───────────────────────────────────────────────────────────────────────
from modules.auth import is_authenticated, render_login_page, logout, get_current_user

# ── Module imports ─────────────────────────────────────────────────────────────
from modules.dashboard import render_dashboard
from modules.data_upload import render_data_upload
from modules.data_integration import render_data_integration
from modules.statistics import render_statistics
from modules.visualization import render_visualization
from modules.machine_learning import render_machine_learning
from modules.biomarker_discovery import render_biomarker_discovery
from modules.clinical_insights import render_clinical_insights
from modules.results_explorer import render_results_explorer
from modules.settings import render_settings

# ══════════════════════════════════════════════════════════════════════════════
# GLOBAL CSS
# ══════════════════════════════════════════════════════════════════════════════
GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=DM+Serif+Display:ital@0;1&display=swap');

/* ── Root variables ── */
:root {
    --primary:    #0A2463;
    --secondary:  #1B9AAA;
    --cancer:     #E84855;
    --normal:     #3BB273;
    --accent:     #8B2FC9;
    --warning:    #F4A261;
    --bg:         #0D1B2A;
    --card:       #112240;
    --border:     rgba(27, 154, 170, 0.18);
    --text:       #CCD6F6;
    --muted:      #64748b;
    --font-main:  'Space Grotesk', sans-serif;
    --font-mono:  'JetBrains Mono', monospace;
    --font-serif: 'DM Serif Display', serif;
}

/* ── App base ── */
.stApp {
    background: var(--bg) !important;
    font-family: var(--font-main) !important;
    color: var(--text) !important;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #091524 0%, #0D1B2A 100%) !important;
    border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] .stMarkdown,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: var(--text) !important;
}

/* ── Sidebar radio nav ── */
[data-testid="stSidebar"] .stRadio > div {
    gap: 0.2rem !important;
}

[data-testid="stSidebar"] .stRadio label {
    display: flex !important;
    align-items: center !important;
    padding: 0.55rem 0.8rem !important;
    border-radius: 8px !important;
    cursor: pointer !important;
    color: #94a3b8 !important;
    transition: all 0.15s ease !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    border: 1px solid transparent !important;
}

[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(27, 154, 170, 0.1) !important;
    color: var(--text) !important;
    border-color: rgba(27, 154, 170, 0.2) !important;
}

/* ── Main content ── */
.main .block-container {
    padding: 1.5rem 2rem 3rem !important;
    max-width: 1400px !important;
}

/* ── Typography ── */
h1, h2, h3 {
    font-family: var(--font-main) !important;
    color: var(--text) !important;
    letter-spacing: -0.02em !important;
}

h1 { font-size: 1.8rem !important; font-weight: 700 !important; }
h2 { font-size: 1.4rem !important; font-weight: 700 !important; }
h3 { font-size: 1.15rem !important; font-weight: 600 !important; }

.stMarkdown p, .stMarkdown li { color: var(--text) !important; }

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #1B9AAA, #0A2463) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: var(--font-main) !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    padding: 0.5rem 1.2rem !important;
    transition: all 0.2s ease !important;
    letter-spacing: 0.01em !important;
}

.stButton > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 20px rgba(27, 154, 170, 0.35) !important;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #E84855, #8B2FC9) !important;
}

/* ── Inputs ── */
.stTextInput input, .stSelectbox select,
.stNumberInput input, .stTextArea textarea {
    background: rgba(17, 34, 64, 0.8) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 8px !important;
    font-family: var(--font-main) !important;
}

.stTextInput input:focus, .stSelectbox:focus-within select {
    border-color: var(--secondary) !important;
    box-shadow: 0 0 0 2px rgba(27, 154, 170, 0.2) !important;
}

/* ── Selectbox ── */
.stSelectbox > div > div {
    background: rgba(17, 34, 64, 0.8) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 8px !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(17, 34, 64, 0.6) !important;
    border-radius: 10px !important;
    padding: 4px !important;
    gap: 2px !important;
    border: 1px solid var(--border) !important;
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--muted) !important;
    border-radius: 8px !important;
    font-family: var(--font-main) !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
    padding: 0.5rem 1rem !important;
    transition: all 0.15s ease !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--secondary)22, var(--accent)22) !important;
    color: var(--text) !important;
    border: 1px solid var(--secondary)44 !important;
}

/* ── Metrics ── */
[data-testid="metric-container"] {
    background: linear-gradient(135deg, rgba(17,34,64,0.9), rgba(10,36,99,0.5)) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    padding: 0.8rem 1rem !important;
}

[data-testid="metric-container"] label {
    color: var(--muted) !important;
    font-size: 0.78rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}

[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: var(--text) !important;
    font-size: 1.6rem !important;
    font-weight: 700 !important;
}

/* ── DataFrames ── */
[data-testid="stDataFrame"] {
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    overflow: hidden !important;
}

.dvn-scroller {
    background: rgba(17, 34, 64, 0.7) !important;
}

/* ── Expanders ── */
.streamlit-expanderHeader {
    background: rgba(17, 34, 64, 0.6) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: var(--font-main) !important;
}

.streamlit-expanderContent {
    background: rgba(13, 27, 42, 0.6) !important;
    border: 1px solid var(--border) !important;
    border-top: none !important;
    border-radius: 0 0 8px 8px !important;
}

/* ── Alerts ── */
.stSuccess, .stInfo, .stWarning, .stError {
    border-radius: 8px !important;
    font-family: var(--font-main) !important;
}

.stSuccess { border-left: 4px solid var(--normal) !important; }
.stInfo { border-left: 4px solid var(--secondary) !important; }
.stWarning { border-left: 4px solid var(--warning) !important; }
.stError { border-left: 4px solid var(--cancer) !important; }

/* ── Checkboxes ── */
.stCheckbox label { color: var(--text) !important; }

/* ── Sliders ── */
.stSlider [data-baseweb="slider"] div {
    background: var(--secondary) !important;
}

/* ── File uploader ── */
[data-testid="stFileUploadDropzone"] {
    background: rgba(17, 34, 64, 0.5) !important;
    border: 2px dashed var(--secondary) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
}

/* ── Plotly chart backgrounds ── */
.js-plotly-plot {
    border-radius: 10px !important;
    overflow: hidden !important;
}

/* ── Divider ── */
hr {
    border-color: var(--border) !important;
    margin: 1rem 0 !important;
}

/* ── Caption ── */
.stCaption, caption {
    color: var(--muted) !important;
    font-size: 0.82rem !important;
}

/* ── Download button ── */
[data-testid="stDownloadButton"] button {
    background: rgba(27, 154, 170, 0.15) !important;
    border: 1px solid rgba(27, 154, 170, 0.4) !important;
    color: var(--secondary) !important;
    border-radius: 8px !important;
}

/* ── Multiselect ── */
.stMultiSelect [data-baseweb="tag"] {
    background: rgba(27, 154, 170, 0.2) !important;
    border: 1px solid rgba(27, 154, 170, 0.4) !important;
    color: var(--text) !important;
    border-radius: 6px !important;
}

/* ── Progress bar ── */
.stProgress > div > div {
    background: linear-gradient(90deg, var(--secondary), var(--accent)) !important;
    border-radius: 4px !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb {
    background: var(--secondary);
    border-radius: 4px;
    opacity: 0.6;
}
</style>
"""


# ══════════════════════════════════════════════════════════════════════════════
# NAVIGATION CONFIG
# ══════════════════════════════════════════════════════════════════════════════
NAV_ITEMS = [
    ("🏠", "Dashboard",              "dashboard"),
    ("📁", "Data Upload",            "upload"),
    ("🔗", "Data Integration",       "integration"),
    ("📈", "Statistical Analysis",   "statistics"),
    ("📊", "Visualization",          "visualization"),
    ("🤖", "Machine Learning",       "ml"),
    ("🎯", "Biomarker Discovery",    "biomarkers"),
    ("🏥", "Clinical Insights",      "clinical"),
    ("🔍", "Results Explorer",       "results"),
    ("⚙️",  "Settings",              "settings"),
]

PAGE_RENDERERS = {
    "dashboard":   render_dashboard,
    "upload":      render_data_upload,
    "integration": render_data_integration,
    "statistics":  render_statistics,
    "visualization": render_visualization,
    "ml":          render_machine_learning,
    "biomarkers":  render_biomarker_discovery,
    "clinical":    render_clinical_insights,
    "results":     render_results_explorer,
    "settings":    render_settings,
}


# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
def render_sidebar() -> str:
    """Render sidebar navigation and return selected page key."""
    user = get_current_user()
    from modules.auth import ROLE_PERMISSIONS
    allowed = ROLE_PERMISSIONS.get(user["role"], [])

    with st.sidebar:
        # ── Brand ──────────────────────────────────────────────────────────────
        st.markdown("""
        <div style='padding: 1.2rem 0.5rem 1rem; border-bottom: 1px solid rgba(27,154,170,0.2); margin-bottom: 0.8rem'>
            <div style='display:flex; align-items:center; gap:0.7rem'>
                <span style='font-size:2rem'>🧬</span>
                <div>
                    <div style='font-family:"Space Grotesk",sans-serif; font-weight:700;
                                font-size:1.15rem; color:#CCD6F6; letter-spacing:-0.01em'>
                        OmicsVault
                    </div>
                    <div style='font-size:0.72rem; color:#64748b; margin-top:1px'>
                        Biomarker Discovery Platform
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Dataset status pill ────────────────────────────────────────────────
        datasets = st.session_state.get("uploaded_datasets", {})
        n_datasets = len(datasets)
        integrated = "integrated_data" in st.session_state

        st.markdown(f"""
        <div style='display:flex; gap:6px; margin-bottom:0.8rem; flex-wrap:wrap'>
            <span style='background:rgba(27,154,170,0.15); border:1px solid rgba(27,154,170,0.3);
                         border-radius:20px; padding:3px 10px; color:#1B9AAA;
                         font-size:0.72rem; font-weight:600'>
                📂 {n_datasets} layer{"s" if n_datasets != 1 else ""}
            </span>
            {"<span style='background:rgba(59,178,115,0.15); border:1px solid rgba(59,178,115,0.3); border-radius:20px; padding:3px 10px; color:#3BB273; font-size:0.72rem; font-weight:600'>✅ Integrated</span>" if integrated else ""}
        </div>
        """, unsafe_allow_html=True)

        # ── Navigation ─────────────────────────────────────────────────────────
        st.markdown("<div style='font-size:0.7rem; color:#64748b; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.4rem; padding-left:0.3rem'>Navigation</div>", unsafe_allow_html=True)

        nav_labels = [
            f"{icon}  {label}"
            for icon, label, key in NAV_ITEMS
            if key in allowed
        ]
        nav_keys = [key for _, _, key in NAV_ITEMS if key in allowed]

        if "current_page" not in st.session_state:
            st.session_state["current_page"] = "dashboard"

        current_idx = nav_keys.index(st.session_state["current_page"]) if st.session_state["current_page"] in nav_keys else 0

        selected_label = st.radio(
            "nav",
            nav_labels,
            index=current_idx,
            label_visibility="collapsed",
        )

        # Map label back to key
        selected_key = nav_keys[nav_labels.index(selected_label)] if selected_label in nav_labels else "dashboard"
        st.session_state["current_page"] = selected_key

        # ── User info + logout ──────────────────────────────────────────────────
        st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
        st.markdown("<hr style='border-color:rgba(27,154,170,0.15); margin:0.5rem 0'>",
                    unsafe_allow_html=True)

        role_badge_colors = {
            "admin": "#E84855",
            "researcher": "#1B9AAA",
            "guest": "#64748b"
        }
        role_color = role_badge_colors.get(user["role"], "#64748b")

        col_usr, col_btn = st.columns([2, 1])
        with col_usr:
            st.markdown(f"""
            <div style='padding:0.4rem 0.2rem'>
                <div style='color:#CCD6F6; font-size:0.88rem; font-weight:600'>{user["username"]}</div>
                <span style='background:{role_color}22; border:1px solid {role_color}55;
                             border-radius:4px; padding:1px 6px; color:{role_color};
                             font-size:0.7rem; font-weight:700; text-transform:uppercase'>
                    {user["role"]}
                </span>
            </div>
            """, unsafe_allow_html=True)
        with col_btn:
            if st.button("↩", help="Sign out", key="sidebar_logout"):
                logout()

        # ── Quick actions ──────────────────────────────────────────────────────
        if not datasets:
            st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
            if st.button("⚡ Quick Demo", use_container_width=True,
                          key="sidebar_demo", help="Load all demo datasets"):
                from utils.sample_data import get_all_demo_datasets
                with st.spinner("Loading demo data..."):
                    demo_data = get_all_demo_datasets()
                    st.session_state["uploaded_datasets"] = demo_data
                st.success("✅ Demo data loaded!")
                st.session_state["current_page"] = "dashboard"
                st.rerun()

    return selected_key


# ══════════════════════════════════════════════════════════════════════════════
# BREADCRUMB & PAGE HEADER
# ══════════════════════════════════════════════════════════════════════════════
def render_topbar(page_key: str):
    """Render top status bar."""
    page_name = next((label for _, label, key in NAV_ITEMS if key == page_key), "Dashboard")
    datasets = st.session_state.get("uploaded_datasets", {})

    # Compact status row
    status_parts = []
    for name, df in list(datasets.items())[:4]:
        import pandas as pd
        if isinstance(df, pd.DataFrame):
            status_parts.append(
                f"<span style='background:rgba(27,154,170,0.1); border:1px solid rgba(27,154,170,0.2); "
                f"border-radius:4px; padding:1px 7px; font-size:0.72rem; color:#1B9AAA'>{name}</span>"
            )
    if len(datasets) > 4:
        status_parts.append(
            f"<span style='color:#64748b; font-size:0.72rem'>+{len(datasets)-4} more</span>"
        )

    status_html = " ".join(status_parts) if status_parts else (
        "<span style='color:#64748b; font-size:0.72rem'>No datasets loaded</span>"
    )

    ml_status = ""
    if st.session_state.get("model_metrics"):
        acc = st.session_state["model_metrics"].get("accuracy", 0)
        ml_status = (
            f"<span style='background:rgba(59,178,115,0.1); border:1px solid rgba(59,178,115,0.2); "
            f"border-radius:4px; padding:1px 7px; font-size:0.72rem; color:#3BB273'>🤖 Model: {acc:.1%}</span>"
        )

    st.markdown(f"""
    <div style='
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.5rem 0;
        margin-bottom: 0.5rem;
        border-bottom: 1px solid rgba(27,154,170,0.12);
        font-family: "Space Grotesk", sans-serif;
    '>
        <div style='display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap'>
            <span style='color:#64748b; font-size:0.72rem'>Datasets:</span>
            {status_html}
        </div>
        <div style='display:flex; gap:0.5rem; align-items:center'>
            {ml_status}
            <span style='color:#64748b; font-size:0.72rem'>OmicsVault v1.0</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN APP
# ══════════════════════════════════════════════════════════════════════════════
def main():
    # Inject global CSS
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    # Auth gate
    if not is_authenticated():
        render_login_page()
        return

    # Sidebar navigation
    page_key = render_sidebar()

    # Top status bar
    render_topbar(page_key)

    # Render selected page
    renderer = PAGE_RENDERERS.get(page_key, render_dashboard)

    # Permission check
    from modules.auth import check_permission
    if not check_permission(page_key):
        st.error("🚫 You don't have permission to access this page.")
        user = get_current_user()
        st.info(f"Your role: **{user['role']}**. Contact an admin to upgrade your access.")
        return

    try:
        renderer()
    except Exception as e:
        st.error(f"❌ Page error: {str(e)}")
        st.exception(e)
        st.info("Try refreshing the page or clearing session data in Settings.")


if __name__ == "__main__":
    main()
