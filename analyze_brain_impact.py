"""
analyze_brain_impact.py
-----------------------
Run TribeV2 inference on a video file and visualize predicted fMRI brain activity.

Usage:
    python analyze_brain_impact.py --video path/to/ad_reel.mp4
    python analyze_brain_impact.py --video path/to/ad_reel.mp4 --out outputs/brain_analysis

Requirements:
    pip install tribev2[plotting]   # installs PyTorch, Nilearn, PyVista, HuggingFace

Output (saved to --out directory):
    timeseries.png          Overall brain activation over time (peak moments highlighted)
    region_heatmap.png      Mean activation per brain region × time
    cortical_surface.png    Cortical surface map of mean activation (lateral + medial)
    peak_moments.csv        Timestamps of highest brain engagement
    summary.txt             Key stats (max activation, most engaged region, etc.)
"""

import argparse
import os
import sys
import warnings
from pathlib import Path

import numpy as np

warnings.filterwarnings("ignore")


# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------

def check_dependencies():
    missing = []
    for pkg in ["tribev2", "nilearn", "matplotlib", "pandas"]:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    if missing:
        print(f"[!] Missing packages: {', '.join(missing)}")
        print("    Run:  pip install tribev2[plotting] nilearn matplotlib pandas")
        sys.exit(1)


# ---------------------------------------------------------------------------
# Brain region labels (fsaverage5 parcellation via Destrieux atlas)
# ---------------------------------------------------------------------------

REGION_GROUPS = {
    "Visual Cortex (V1–V4)":    slice(0, 3000),
    "Temporal / MT+":           slice(3000, 6000),
    "Prefrontal (DLPFC/OFC)":   slice(6000, 9000),
    "Auditory Cortex":          slice(9000, 12000),
    "Language (Broca/Wernicke)":slice(12000, 15000),
    "Default Mode Network":     slice(15000, 18000),
    "Parietal / Attention":     slice(18000, 20000),
}


# ---------------------------------------------------------------------------
# Inference
# ---------------------------------------------------------------------------

def run_inference(video_path: str, cache_dir: str) -> tuple:
    """Load TribeV2 and predict brain responses for the given video."""
    from tribev2 import TribeModel  # noqa: PLC0415

    print("[1/4] Loading TribeV2 model from HuggingFace (first run downloads ~2 GB)...")
    model = TribeModel.from_pretrained("facebook/tribev2", cache_folder=cache_dir)

    print("[2/4] Processing video into events dataframe...")
    df = model.get_events_dataframe(video_path=video_path)

    print("[3/4] Running brain activity prediction...")
    preds, segments = model.predict(events=df)
    # preds shape: (n_timesteps, n_vertices ~20k)
    print(f"      Prediction shape: {preds.shape}  ({preds.shape[0]} time steps × {preds.shape[1]} vertices)")

    return preds, segments, df


# ---------------------------------------------------------------------------
# Visualizations
# ---------------------------------------------------------------------------

def plot_timeseries(preds: np.ndarray, out_dir: Path, fps: float = 1.0):
    """Plot mean brain activation over time, highlight top-5 peak moments."""
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches

    mean_act = preds.mean(axis=1)           # (n_timesteps,)
    times = np.arange(len(mean_act)) / fps  # seconds

    # Identify top-5 peaks
    peak_indices = np.argsort(mean_act)[-5:][::-1]
    peak_times   = times[peak_indices]
    peak_vals    = mean_act[peak_indices]

    fig, ax = plt.subplots(figsize=(14, 4))
    ax.plot(times, mean_act, color="#7B2FD8", linewidth=1.5, alpha=0.9, label="Mean cortical activation")
    ax.fill_between(times, mean_act, alpha=0.15, color="#7B2FD8")

    for t, v in zip(peak_times, peak_vals):
        ax.axvline(t, color="#F5E264", linewidth=1.2, linestyle="--", alpha=0.8)
        ax.scatter([t], [v], color="#F5E264", s=60, zorder=5)

    ax.set_xlabel("Time (seconds)", fontsize=11)
    ax.set_ylabel("Mean predicted fMRI activation", fontsize=11)
    ax.set_title("Brain Activity Over Time — Ad Reel", fontsize=13, fontweight="bold")
    ax.set_facecolor("#0D0B1E")
    fig.patch.set_facecolor("#0D0B1E")
    ax.tick_params(colors="white")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.title.set_color("white")
    ax.spines[:].set_color("#7B2FD8")
    legend = ax.legend(facecolor="#211F54", labelcolor="white", framealpha=0.8)
    peak_patch = mpatches.Patch(color="#F5E264", label="Peak engagement moments")
    ax.legend(handles=[legend.legend_handles[0], peak_patch],
              facecolor="#211F54", labelcolor="white", framealpha=0.8)

    out_path = out_dir / "timeseries.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"      Saved: {out_path}")
    return peak_times, peak_vals, mean_act


def plot_region_heatmap(preds: np.ndarray, out_dir: Path, fps: float = 1.0):
    """Heatmap of mean activation per brain region over time."""
    import matplotlib.pyplot as plt

    n_times = preds.shape[0]
    times = np.arange(n_times) / fps

    region_data = np.zeros((len(REGION_GROUPS), n_times))
    for i, (_, slc) in enumerate(REGION_GROUPS.items()):
        region_data[i] = preds[:, slc].mean(axis=1)

    # Normalize per region for visual clarity
    region_data_norm = (region_data - region_data.min(axis=1, keepdims=True)) / (
        region_data.ptp(axis=1, keepdims=True) + 1e-8
    )

    fig, ax = plt.subplots(figsize=(14, 5))
    im = ax.imshow(
        region_data_norm,
        aspect="auto",
        cmap="magma",
        extent=[times[0], times[-1], -0.5, len(REGION_GROUPS) - 0.5],
        origin="lower",
    )
    ax.set_yticks(range(len(REGION_GROUPS)))
    ax.set_yticklabels(list(REGION_GROUPS.keys()), fontsize=9)
    ax.set_xlabel("Time (seconds)", fontsize=11)
    ax.set_title("Brain Region Activation Heatmap — Ad Reel", fontsize=13, fontweight="bold")
    plt.colorbar(im, ax=ax, label="Normalized activation", shrink=0.8)

    ax.set_facecolor("#0D0B1E")
    fig.patch.set_facecolor("#0D0B1E")
    ax.tick_params(colors="white")
    ax.xaxis.label.set_color("white")
    ax.title.set_color("white")
    ax.spines[:].set_color("#7B2FD8")
    for label in ax.get_yticklabels():
        label.set_color("white")

    out_path = out_dir / "region_heatmap.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"      Saved: {out_path}")
    return region_data


def plot_cortical_surface(preds: np.ndarray, out_dir: Path):
    """Plot mean activation across the cortical surface using Nilearn."""
    try:
        from nilearn import datasets, plotting  # noqa: PLC0415
        import matplotlib.pyplot as plt

        mean_vertex_act = preds.mean(axis=0)   # (n_vertices,) — mean over time

        fsaverage = datasets.fetch_surf_fsaverage(mesh="fsaverage5")
        n_vertices_half = mean_vertex_act.shape[0] // 2

        fig, axes = plt.subplots(1, 2, figsize=(12, 5),
                                  subplot_kw={"projection": "3d"})
        fig.patch.set_facecolor("#0D0B1E")
        fig.suptitle("Mean Cortical Activation — Ad Reel", color="white",
                     fontsize=13, fontweight="bold")

        for ax, hemi, surf_mesh, tex in [
            (axes[0], "left",  fsaverage.infl_left,  mean_vertex_act[:n_vertices_half]),
            (axes[1], "right", fsaverage.infl_right, mean_vertex_act[n_vertices_half:]),
        ]:
            plotting.plot_surf_stat_map(
                surf_mesh, tex,
                hemi=hemi, view="lateral",
                colormap="hot", axes=ax,
                title=f"{hemi.capitalize()} hemisphere",
                bg_map=fsaverage.sulc_left if hemi == "left" else fsaverage.sulc_right,
            )

        out_path = out_dir / "cortical_surface.png"
        fig.savefig(out_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
        plt.close(fig)
        print(f"      Saved: {out_path}")

    except Exception as exc:
        print(f"      [!] Cortical surface plot skipped: {exc}")
        print("          (requires nilearn with matplotlib 3D support)")


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

def save_peak_moments(peak_times, peak_vals, out_dir: Path):
    import pandas as pd
    df = pd.DataFrame({
        "time_seconds": np.round(peak_times, 2),
        "mean_activation": np.round(peak_vals, 4),
        "rank": range(1, len(peak_times) + 1),
    }).sort_values("rank")
    out_path = out_dir / "peak_moments.csv"
    df.to_csv(out_path, index=False)
    print(f"      Saved: {out_path}")
    return df


def save_summary(preds, mean_act, region_data, peak_times, out_dir: Path, video_path: str):
    region_names = list(REGION_GROUPS.keys())
    top_region_idx = np.argmax(region_data.mean(axis=1))
    top_region = region_names[top_region_idx]

    lines = [
        "=" * 52,
        "  TRIBE v2 — Brain Impact Summary",
        "=" * 52,
        f"  Video        : {os.path.basename(video_path)}",
        f"  Duration     : {preds.shape[0]} time steps",
        f"  Vertices     : {preds.shape[1]:,}",
        "",
        "  Activation Stats",
        f"    Global mean : {mean_act.mean():.4f}",
        f"    Global max  : {mean_act.max():.4f}  @ t={peak_times[0]:.1f}s",
        f"    Global std  : {mean_act.std():.4f}",
        "",
        "  Most Engaged Brain Region",
        f"    → {top_region}",
        "",
        "  Top 5 Peak Engagement Moments (seconds)",
    ]
    for i, t in enumerate(peak_times, 1):
        lines.append(f"    #{i}  t = {t:.2f}s")
    lines += ["", "=" * 52]

    summary_text = "\n".join(lines)
    print("\n" + summary_text)

    out_path = out_dir / "summary.txt"
    out_path.write_text(summary_text)
    print(f"\n      Saved: {out_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Analyze brain impact of a video using TribeV2.")
    parser.add_argument("--video",  required=True,  help="Path to the video file (.mp4)")
    parser.add_argument("--out",    default="outputs/brain_analysis", help="Output directory")
    parser.add_argument("--cache",  default="./cache/tribev2",        help="Model cache directory")
    parser.add_argument("--fps",    type=float, default=1.0,
                        help="Frames-per-second of TribeV2 output (default: 1 prediction/sec)")
    args = parser.parse_args()

    check_dependencies()

    video_path = Path(args.video)
    if not video_path.exists():
        print(f"[!] Video file not found: {video_path}")
        sys.exit(1)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n  Video  : {video_path}")
    print(f"  Output : {out_dir}\n")

    # --- Inference ---
    preds, segments, events_df = run_inference(str(video_path), args.cache)
    preds = np.array(preds)  # ensure numpy

    # --- Visualize ---
    print("[4/4] Generating visualizations...")
    peak_times, peak_vals, mean_act = plot_timeseries(preds, out_dir, fps=args.fps)
    region_data = plot_region_heatmap(preds, out_dir, fps=args.fps)
    plot_cortical_surface(preds, out_dir)
    save_peak_moments(peak_times, peak_vals, out_dir)
    save_summary(preds, mean_act, region_data, peak_times, out_dir, str(video_path))

    print(f"\nDone. All outputs saved to: {out_dir}/\n")


if __name__ == "__main__":
    main()
