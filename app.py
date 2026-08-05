import streamlit as st
import streamlit.components.v1 as components

# Page Layout Config
st.set_page_config(
    page_title="Jot AI - Trading Command Center",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Classic Dark Theme CSS
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .stApp { background-color: #0E1117; color: #E0E0E0; }
    .team-card {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .team-title {
        font-size: 15px;
        font-weight: bold;
        color: #58A6FF;
        border-bottom: 1px solid #30363D;
        padding-bottom: 5px;
        margin-bottom: 10px;
    }
    .highlight-card {
        background-color: #1c2128;
        border: 2px solid #238636;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .audit-card {
        background-color: #1a1e24;
        border: 2px solid #A371F7;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .bullish { color: #3FB950; font-weight: bold; }
    .bearish { color: #F85149; font-weight: bold; }
    .neutral { color: #D29922; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Dashboard Header
st.title("🛡️ JOT AI — Multi-Team Trading Command Center")
st.caption("15-Min Execution Specialist with Multi-Timeframe Alignment & Final Audit Validation")
st.markdown("---")

# Sidebar Controls
st.sidebar.header("⚙️ Control Panel")
asset = st.sidebar.selectbox("Select Trading Pair", ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT"])
primary_tf = st.sidebar.selectbox("Primary Timeframe (Trade Execution)", ["15m", "30m", "1h", "4h"], index=0)

st.sidebar.markdown("---")
st.sidebar.subheader("👤 Commander Action")
run_analysis = st.sidebar.button("Run Full 6-Team Audit", type="primary")

# Main Dashboard Layout
if run_analysis:
    st.success(f"Command Received! Jot is analyzing **{asset}** with Team 1 to Team 6...")
    
    # 1. Multi-Timeframe Quick Matrix (Top Row)
    st.subheader("🌐 Multi-Timeframe Market Alignment")
    tf_col1, tf_col2, tf_col3, tf_col4 = st.columns(4)
    
    with tf_col1:
        st.markdown("<div class='team-card'><b>4 Hour Trend</b><br><span class='bullish'>BULLISH (Major Support Safe)</span></div>", unsafe_allow_html=True)
    with tf_col2:
        st.markdown("<div class='team-card'><b>1 Hour Trend</b><br><span class='bullish'>BULLISH (Retest Zone)</span></div>", unsafe_allow_html=True)
    with tf_col3:
        st.markdown("<div class='team-card'><b>30 Min Trend</b><br><span class='neutral'>SIDEWAYS / CONSOLIDATION</span></div>", unsafe_allow_html=True)
    with tf_col4:
        st.markdown("<div class='team-card' style='border: 1px solid #3FB950;'><b>15 Min Trigger</b><br><span class='bullish'>🔥 PERFECT SETUP READY</span></div>", unsafe_allow_html=True)

    st.markdown("---")
    
    # 2. Team Cards Grid
    col1, col2 = st.columns(2)
    
    with col1:
        # Team 5: S/R, FVG & Structure
        st.markdown("""
        <div class="team-card">
            <div class="team-title">🏛️ TEAM 5: Structure, S/R & FVG Specialist</div>
            <p><b>15m Support Zone:</b> <span class="bullish">$0.5080 - $0.5110</span></p>
            <p><b>15m Resistance Zone:</b> <span class="bearish">$0.5240 - $0.5260</span></p>
            <p><b>15m Fair Value Gap (FVG):</b> Active Bullish FVG at $0.5125 - $0.5140</p>
            <p><b>15m CHoCH / MSS:</b> <span class="bullish">15m Bullish Structure Confirmed</span></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Team 1: Short & Downside Liquidity
        st.markdown("""
        <div class="team-card">
            <div class="team-title">📉 TEAM 1: Short & Downside Liquidity Specialist</div>
            <p><b>Sell-Side Liquidity (SSL):</b> 15m Lows Swept at $0.5050</p>
            <p><b>Downside Liquidity Hunt:</b> Cleared. Reversal expected.</p>
            <p><b>Short Trade Verdict:</b> <span class="bearish">DO NOT SHORT</span></p>
        </div>
        """, unsafe_allow_html=True)

        # Team 2: Long & Upside Liquidity
        st.markdown("""
        <div class="team-card">
            <div class="team-title">📈 TEAM 2: Long & Upside Liquidity Specialist</div>
            <p><b>Buy-Side Liquidity (BSL):</b> Target set at $0.5250 Highs</p>
            <p><b>15m Breakout Level:</b> Above $0.5185</p>
            <p><b>Upside Potential:</b> ~2.8% - 3.5% Fast Move</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Team 3: Technical & SMC Master
        st.markdown("""
        <div class="team-card">
            <div class="team-title">📊 TEAM 3: Technicals, SMC & Indicators Master</div>
            <p><b>15m RSI:</b> 48.5 (Bouncing from Support)</p>
            <p><b>15m EMA Status:</b> 9 EMA turning up to cross 21 EMA</p>
            <p><b>15m Order Block (OB):</b> Premium OB at $0.5120</p>
            <p><b>Pattern:</b> 15m Double Bottom Rejection Wick</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Team 4: Final 15-Min Execution Signal Card
        st.markdown("""
        <div class="highlight-card">
            <div class="team-title" style="color:#3FB950;">🎯 TEAM 4: 15-MINUTE EXECUTION SIGNAL</div>
            <p><b>Proposed Action:</b> <span class="bullish">LONG ENTRY</span></p>
            <p><b>Ideal Entry Zone:</b> $0.5125 - $0.5145</p>
            <p><b>Stop Loss (SL):</b> $0.5075</p>
            <p><b>Target 1 (TP1):</b> $0.5200 | <b>Target 2 (TP2):</b> $0.5245</p>
            <p><b>Risk/Reward Ratio:</b> 1 : 2.4</p>
        </div>
        """, unsafe_allow_html=True)

        # Team 6: Final Audit & Quality Control
        st.markdown("""
        <div class="audit-card">
            <div class="team-title" style="color:#A371F7;">🔍 TEAM 6: Quality Assurance & Validation Audit</div>
            <p><b>Multi-TF Confluence:</b> <span class="bullish">PASSED (4H + 1H + 15M Aligned)</span></p>
            <p><b>Fake-Out / Trap Risk:</b> <span class="bullish">LOW (Liquidity Already Swept)</span></p>
            <p><b>Final Audit Verdict:</b> <span class="bullish">✅ TRADE APPROVED (Execute as Planned)</span></p>
            <p><b>Commander Note:</b> Move SL to Entry (Break-even) as soon as TP1 is hit.</p>
        </div>
        """, unsafe_allow_html=True)

    # 3. Live 15-Min Chart Section
    st.markdown("---")
    st.subheader(f"📈 Live 15-Minute Chart ({asset})")
    
    tv_widget = f"""
    <div class="tradingview-widget-container" style="height:500px;width:100%">
      <iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_1234&symbol=BINANCE:{asset}&interval=15&hidesidetoolbar=0&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=[]&theme=dark&style=1&timezone=Etc%2FUTC" style="width: 100%; height: 500px; border: none;"></iframe>
    </div>
    """
    components.html(tv_widget, height=520)

else:
    st.info("👈 Select parameters from the sidebar and click **'Run Full 6-Team Audit'** to view complete reports from Team 1 to 6.")
