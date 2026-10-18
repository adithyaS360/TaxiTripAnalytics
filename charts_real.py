# Makes report figures from the CSV files that TripAnalytics.java writes into out/
import os, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "Liberation Serif", "DejaVu Serif"], "font.size": 10})
o = "out/"
def have(f): return os.path.exists(o + f)

if have("hourly.csv"):
    h = pd.read_csv(o + "hourly.csv")
    fig, ax = plt.subplots(figsize=(6.4, 3.2)); ax.bar(h.hour, h.trips / 1000, color="#4a6fa5")
    ax.set_xlabel("Hour of day"); ax.set_ylabel("Trips (thousands)")
    a2 = ax.twinx(); a2.plot(h.hour, h.avg_speed, color="#c0392b", marker="o", ms=3); a2.set_ylabel("Avg speed (mph)", color="#c0392b")
    ax.set_xticks(range(0, 24, 2)); ax.set_title("Trip demand and average speed by hour"); fig.tight_layout(); fig.savefig(o + "fig1.png", dpi=200)
if have("kmeans_k.csv"):
    k = pd.read_csv(o + "kmeans_k.csv")
    fig, ax = plt.subplots(figsize=(6.4, 3)); ax.plot(k.k, k.silhouette, marker="o", color="#2c7a4b")
    ax.set_xlabel("Number of clusters k"); ax.set_ylabel("Silhouette score"); ax.set_title("Choosing k using silhouette score"); ax.grid(alpha=.3)
    fig.tight_layout(); fig.savefig(o + "fig2.png", dpi=200)
if have("hotspots.csv"):
    z = pd.read_csv(o + "hotspots.csv").sort_values("trips")
    fig, ax = plt.subplots(figsize=(6.4, 3.6)); ax.barh(z.Zone, z.trips / 1000, color="#e07b39")
    ax.set_xlabel("Pickups (thousands)"); ax.set_title("Top 10 pickup zones, January 2025"); fig.tight_layout(); fig.savefig(o + "fig3.png", dpi=200)
if have("segments.csv"):
    s = pd.read_csv(o + "segments.csv")
    fig, ax = plt.subplots(figsize=(6.4, 3)); lbl = [f"{d:.1f} mi" for d in s.avg_dist]
    ax.bar(lbl, s.trips / 1000, color="#7a5195"); ax.set_xlabel("Average trip distance of segment"); ax.set_ylabel("Trips (thousands)")
    ax.set_title("Trip segments found by K-Means"); fig.tight_layout(); fig.savefig(o + "fig4.png", dpi=200)
if have("pred_sample.csv"):
    p = pd.read_csv(o + "pred_sample.csv")
    fig, ax = plt.subplots(figsize=(4.6, 4.2)); ax.scatter(p.actual_fare, p.predicted_fare, s=4, alpha=.35, color="#4a6fa5")
    m = max(p.actual_fare.max(), p.predicted_fare.max()); ax.plot([0, m], [0, m], "r--", lw=1)
    ax.set_xlabel("Actual fare (USD)"); ax.set_ylabel("Predicted fare (USD)"); ax.set_title("Random Forest: actual vs predicted")
    fig.tight_layout(); fig.savefig(o + "fig5.png", dpi=200)
print("charts written to out/")