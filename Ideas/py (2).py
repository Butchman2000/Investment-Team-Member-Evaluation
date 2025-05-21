"""
===============================
  MORNING REBOUND STRATEGY — IDEA CANVAS
===============================

We’re modeling high-beta stocks on a dip & rip setup.
Focus: 9:30–10:15AM ET. Target: Large wick reversals + volume confirmation.
We will not catch knives. We wait for the reversal setup + market context alignment.
"""

# (goto drawing_1.png)

# === CONFIG ===
config = {
    'entry_window': ('09:30', '10:15'),
    'min_wick_length': 0.5,  # In $ or %
    'min_volume_spike': 1.5, # Relative to rolling avg
    'vol_filter': True,      # We ignore if VIX > 20 or vol of vol is rising
    'max_spy_correlation': 0.85,
}

# === STRATEGY NOTES ===
"""
Looking for:
- Gap-down open (overnight fear, bad print, or soft premarket)
- First 3 candles weak, but forming long bottom wick
- 9:35–9:45 shows a candle with:
    - Wick > $0.5
    - Volume > 1.5x avg
    - Buyer reversal strength on tape

Ideal candle confirmation: 9:47–9:52

Entry: Call options (3–5 DTE) OR shares, depending on liquidity

Exit ideas:
- VWAP tag
- Previous close reclaim
- 2R+ based on wick base
"""

# === MACRO CONTEXT ===
"""
- If CPI drop just printed => bullish bias
- If VIX < 18 and skew flattening => higher odds of continuation
- If SPY is consolidating (not crashing), safer to enter
- Look for divergences: TSLA wicking up while SPY is still soft
"""

# === TODO ===
"""
- Simulate this on TSLA, NVDA, META
- Backtest wick + vol spike pattern
- Model implied volatility shifts on the option chain (delta skew?)
- Mark false reversals — why did they fail?
"""


"""
MODEL: Morning Dip & Rip
Logic: Looks for early morning sell-off, strength signal, and catches retrace.
"""

# === Global Parameters (to be moved to utils.py or config later)
MAX_LOOKBACK = 30  # minutes after open
ENTRY_WINDOW_START = "09:45"
ENTRY_WINDOW_END = "10:15"
MIN_WICK_RATIO = 2.0
MIN_VOLUME_SPIKE = 1.5  # compared to avg volume
OPTION_DTE_RANGE = (3, 10)  # days to expiration
EXIT_TIME = "12:00"
# Add more as needed...

# === Step 1: Detect morning dip pattern
def detect_morning_dip(candles):
    """
    Detects morning dip using wick size, candle shape, and volume.
    Returns True if entry signal is met.
    """
    pass  # Placeholder for later candlestick analysis

# === Step 2: Confirm strength with order flow / volume
def confirm_strength(order_flow, volume_profile):
    """
    Confirms bounce likelihood by checking volume surge or order flow.
    """
    pass

# === Step 3: Execute trade logic (simulation or paper)
def place_trade():
    """
    Logic for entering call options, or simulated long position.
    """
    pass

# === Step 4: Exit logic
def exit_trade():
    """
    Exits based on time, price targets, or weakness.
    """
    pass

# === Step 5: Logging
def log_trade(entry, exit, reason):
    """
    Logs the trade for auditability.
    """
    pass

# === Entry Point
def run_model(data):
    """
    Orchestrates the full logic.
    """
    if detect_morning_dip(data['candles']) and confirm_strength(data['order_flow'], data['volume']):
        place_trade()
    else:
        print("No signal today.")

# Placeholder for future ML optimization hooks
# TODO: Refactor all global parameters into a config file
# TODO: Add brute-force grid search or AI optimizer (later phase)
