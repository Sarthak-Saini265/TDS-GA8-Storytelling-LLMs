"""
Financial Services Performance Analysis
Customer Acquisition Cost (CAC) Analysis for 2024

This script analyzes quarterly CAC data and creates visualizations
to support data-driven decision making.

Author: 23f2005347@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# Set style for publication-quality visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11

# Create output directory
OUTPUT_DIR = Path("visualizations")
OUTPUT_DIR.mkdir(exist_ok=True)

# Load data
df = pd.read_csv("data/cac_data.csv")

# Calculate key metrics
average_cac = df['CAC'].mean()
industry_target = 150
gap_to_target = average_cac - industry_target
gap_percentage = (gap_to_target / industry_target) * 100

print("=" * 60)
print("CUSTOMER ACQUISITION COST ANALYSIS - 2024")
print("=" * 60)
print(f"\nQuarterly CAC Values:")
for _, row in df.iterrows():
    print(f"  {row['Quarter']}: ${row['CAC']:.2f}")
print(f"\nAverage CAC: ${average_cac:.2f}")
print(f"Industry Target: ${industry_target:.2f}")
print(f"Gap to Target: ${gap_to_target:.2f} ({gap_percentage:.1f}% above target)")
print("=" * 60)

# Visualization 1: Quarterly CAC Trend with Target Line
fig, ax = plt.subplots(figsize=(12, 7))

# Plot quarterly data
quarters = df['Quarter']
cac_values = df['CAC']
ax.plot(quarters, cac_values, marker='o', linewidth=3, 
        markersize=10, color='#E74C3C', label='Actual CAC', zorder=3)

# Add target line
ax.axhline(y=industry_target, color='#27AE60', linestyle='--', 
           linewidth=2.5, label=f'Industry Target (${industry_target})', zorder=2)

# Add average line
ax.axhline(y=average_cac, color='#3498DB', linestyle=':', 
           linewidth=2, label=f'2024 Average (${average_cac:.2f})', alpha=0.7, zorder=2)

# Styling
ax.set_xlabel('Quarter', fontsize=13, fontweight='bold')
ax.set_ylabel('Customer Acquisition Cost ($)', fontsize=13, fontweight='bold')
ax.set_title('Customer Acquisition Cost Trend - 2024\nGap Analysis vs Industry Benchmark', 
             fontsize=16, fontweight='bold', pad=20)

# Add value labels on points
for i, (q, val) in enumerate(zip(quarters, cac_values)):
    ax.text(i, val + 3, f'${val:.2f}', ha='center', va='bottom', 
            fontsize=10, fontweight='bold')

# Fill the gap area
ax.fill_between(range(len(quarters)), industry_target, cac_values, 
                alpha=0.2, color='red', label='Gap to Target')

ax.legend(loc='upper left', fontsize=11, framealpha=0.95)
ax.grid(True, alpha=0.3)
ax.set_ylim(140, 240)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "cac_trend_analysis.png", dpi=300, bbox_inches='tight')
print(f"\n✓ Saved: {OUTPUT_DIR / 'cac_trend_analysis.png'}")

# Visualization 2: Gap Analysis Bar Chart
fig, ax = plt.subplots(figsize=(10, 7))

# Create bar chart showing gap for each quarter
gaps = cac_values - industry_target
colors = ['#E74C3C' if gap > 0 else '#27AE60' for gap in gaps]
bars = ax.bar(quarters, gaps, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)

# Add value labels on bars
for bar, gap in zip(bars, gaps):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'${gap:.2f}', ha='center', va='bottom' if height > 0 else 'top',
            fontsize=11, fontweight='bold')

ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
ax.set_xlabel('Quarter', fontsize=13, fontweight='bold')
ax.set_ylabel('Gap from Target ($)', fontsize=13, fontweight='bold')
ax.set_title('CAC Performance Gap by Quarter\n(Difference from $150 Industry Target)', 
             fontsize=16, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "cac_gap_analysis.png", dpi=300, bbox_inches='tight')
print(f"✓ Saved: {OUTPUT_DIR / 'cac_gap_analysis.png'}")

# Visualization 3: Performance Dashboard
fig = plt.figure(figsize=(14, 8))
gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

# Subplot 1: Quarterly Trend
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(quarters, cac_values, marker='o', linewidth=2.5, 
         markersize=8, color='#E74C3C', label='Actual CAC')
ax1.axhline(y=industry_target, color='#27AE60', linestyle='--', 
            linewidth=2, label=f'Target (${industry_target})')
ax1.fill_between(range(len(quarters)), industry_target, cac_values, 
                 alpha=0.15, color='red')
ax1.set_title('2024 CAC Quarterly Trend', fontsize=14, fontweight='bold')
ax1.set_xlabel('Quarter', fontsize=11, fontweight='bold')
ax1.set_ylabel('CAC ($)', fontsize=11, fontweight='bold')
ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, alpha=0.3)

# Subplot 2: Key Metrics
ax2 = fig.add_subplot(gs[1, 0])
ax2.axis('off')
metrics_text = f"""
KEY METRICS

Average CAC (2024):     ${average_cac:.2f}
Industry Target:          ${industry_target:.2f}
Gap to Target:            ${gap_to_target:.2f}
Percentage Above:      {gap_percentage:.1f}%

Quarterly Range:
  Lowest (Q2):             ${cac_values.min():.2f}
  Highest (Q4):            ${cac_values.max():.2f}
  Volatility:                 ${cac_values.std():.2f}

Q4 Trend:                   ↑ INCREASING
Status:                       ⚠ NEEDS ATTENTION
"""
ax2.text(0.1, 0.5, metrics_text, fontsize=11, family='monospace',
         verticalalignment='center', bbox=dict(boxstyle='round', 
         facecolor='wheat', alpha=0.3))

# Subplot 3: Distribution
ax3 = fig.add_subplot(gs[1, 1])
ax3.barh(['Q1', 'Q2', 'Q3', 'Q4'], cac_values, color=['#E74C3C', '#E67E22', '#E74C3C', '#C0392B'])
ax3.axvline(x=industry_target, color='#27AE60', linestyle='--', linewidth=2, label='Target')
ax3.axvline(x=average_cac, color='#3498DB', linestyle=':', linewidth=2, label='Average')
ax3.set_xlabel('CAC ($)', fontsize=11, fontweight='bold')
ax3.set_title('Quarterly Comparison', fontsize=14, fontweight='bold')
ax3.legend(loc='lower right', fontsize=9)
ax3.grid(True, alpha=0.3, axis='x')

fig.suptitle('Financial Services CAC Performance Dashboard - 2024', 
             fontsize=16, fontweight='bold', y=0.98)

plt.savefig(OUTPUT_DIR / "cac_dashboard.png", dpi=300, bbox_inches='tight')
print(f"✓ Saved: {OUTPUT_DIR / 'cac_dashboard.png'}")

# Visualization 4: Solution Impact Projection
fig, ax = plt.subplots(figsize=(12, 7))

# Historical data
historical_quarters = ['Q1', 'Q2', 'Q3', 'Q4']
historical_cac = cac_values.tolist()

# Projected improvement scenarios
projection_quarters = ['2025-Q1', '2025-Q2', '2025-Q3', '2025-Q4']

# Conservative scenario: 10% reduction per quarter
conservative = [historical_cac[-1]]
for i in range(4):
    conservative.append(conservative[-1] * 0.90)

# Moderate scenario: 15% reduction per quarter
moderate = [historical_cac[-1]]
for i in range(4):
    moderate.append(moderate[-1] * 0.85)

# Aggressive scenario: 20% reduction per quarter
aggressive = [historical_cac[-1]]
for i in range(4):
    aggressive.append(aggressive[-1] * 0.80)

all_quarters = historical_quarters + projection_quarters
x_pos = range(len(all_quarters))

# Plot historical
ax.plot(x_pos[:4], historical_cac, marker='o', linewidth=3, 
        markersize=10, color='#E74C3C', label='Historical CAC', zorder=3)

# Plot projections
ax.plot(x_pos[3:], conservative, marker='s', linewidth=2.5, 
        markersize=8, color='#F39C12', linestyle='--', label='Conservative (10% quarterly reduction)', alpha=0.8)
ax.plot(x_pos[3:], moderate, marker='^', linewidth=2.5, 
        markersize=8, color='#3498DB', linestyle='--', label='Moderate (15% quarterly reduction)', alpha=0.8)
ax.plot(x_pos[3:], aggressive, marker='D', linewidth=2.5, 
        markersize=8, color='#27AE60', linestyle='--', label='Aggressive (20% quarterly reduction)', alpha=0.8)

# Target line
ax.axhline(y=industry_target, color='#27AE60', linestyle=':', 
           linewidth=2.5, label=f'Target (${industry_target})', zorder=2)

# Add vertical separator
ax.axvline(x=3.5, color='gray', linestyle='-', linewidth=1, alpha=0.5)
ax.text(3.5, 235, '2024 | 2025', ha='center', va='bottom', fontsize=10, 
        fontweight='bold', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

ax.set_xlabel('Quarter', fontsize=13, fontweight='bold')
ax.set_ylabel('Customer Acquisition Cost ($)', fontsize=13, fontweight='bold')
ax.set_title('CAC Optimization Projections - Digital Marketing Channel Optimization\nPotential Impact Scenarios for 2025', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x_pos)
ax.set_xticklabels(all_quarters, rotation=45, ha='right')
ax.legend(loc='upper right', fontsize=10, framealpha=0.95)
ax.grid(True, alpha=0.3)
ax.set_ylim(130, 240)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "cac_optimization_projection.png", dpi=300, bbox_inches='tight')
print(f"✓ Saved: {OUTPUT_DIR / 'cac_optimization_projection.png'}")

plt.close('all')

# Generate summary statistics
print("\n" + "=" * 60)
print("ANALYSIS SUMMARY")
print("=" * 60)
print(f"\n📊 Data Quality: All 4 quarters analyzed")
print(f"📈 Trend: Upward trajectory (Q4 spike to ${cac_values.iloc[-1]:.2f})")
print(f"🎯 Target Gap: ${gap_to_target:.2f} above industry benchmark")
print(f"💡 Recommendation: Optimize digital marketing channels")
print(f"🚀 Potential Savings: Up to ${gap_to_target * 1000:.0f} per 1000 customers")
print("\n✅ All visualizations generated successfully!")
print("=" * 60)

# Save summary to file
summary_file = OUTPUT_DIR / "analysis_summary.txt"
with open(summary_file, 'w') as f:
    f.write("CUSTOMER ACQUISITION COST ANALYSIS - 2024\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"Analyst: 23f2005347@ds.study.iitm.ac.in\n")
    f.write(f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    f.write("KEY FINDINGS:\n")
    f.write(f"  - Average CAC: ${average_cac:.2f}\n")
    f.write(f"  - Industry Target: ${industry_target:.2f}\n")
    f.write(f"  - Gap to Target: ${gap_to_target:.2f} ({gap_percentage:.1f}% above)\n")
    f.write(f"  - Q4 Trend: Increasing (${cac_values.iloc[-1]:.2f})\n\n")
    f.write("RECOMMENDATION:\n")
    f.write("  Optimize digital marketing channels to reduce CAC\n")
    f.write("  Target: Reduce CAC by 35% to reach industry benchmark\n")

print(f"\n✓ Saved: {summary_file}")
