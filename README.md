# Leiden Clustering - DC Metro Area

Interactive visualization of Leiden community detection algorithm on DC metro residential mobility network.

## Live Demo

👉 **[View Interactive Notebook](https://YOUR-USERNAME.github.io/leiden-dc-interactive/)**

## About

This interactive notebook explores how communities emerge at different resolution parameters (γ) in the DC metro area residential mobility network using the Leiden algorithm.

### Features

- 🎬 **Animated GIF** showing community evolution across γ values (0.25 to 3.0)
- 🎚️ **Interactive Slider** to explore different resolution parameters
- 📊 **Interactive Plots** powered by Plotly
- 📈 **Real-time Statistics** that update as you adjust parameters
- 📋 **Summary Table** with all results

### Dataset

- **Network:** DC Metro Area Residential Mobility (2020-2021)
- **Nodes:** 1,536 census tracts (contiguous: 1,496)
- **Edges:** 1,063,054 origin-destination pairs
- **Total moves:** 9,824,939
- **Area:** Washington DC + Maryland + Virginia + West Virginia

### Method

- **Algorithm:** Leiden Community Detection
- **Quality Function:** RBConfigurationVertexPartition (modularity with resolution)
- **Resolution Parameter (γ):** 0.25 to 3.0
- Higher γ → more clusters (finer resolution)

### Key Findings

- Peak modularity at γ ≈ 1.0-1.25
- Clusters range from 3 (γ=0.25) to 24 (γ=3.0) in contiguous map
- Communities progressively split as resolution increases

## Technology

This notebook uses:
- **[marimo](https://marimo.io)** - Reactive Python notebooks
- **WebAssembly** - Runs Python entirely in the browser
- **Plotly** - Interactive visualizations
- **Pandas** - Data manipulation
- **Leiden Algorithm** - Community detection

## How It Works

The notebook runs entirely in your browser using WebAssembly (WASM). No Python server needed! The first load may take a few seconds as it initializes Python in the browser.

## Browser Compatibility

Works best in:
- Chrome (recommended)
- Firefox
- Edge
- Safari (latest version)

---

🤖 Generated with marimo and Claude Code
