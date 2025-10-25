"""
Marimo notebook for Leiden DC clustering animation
WITH EMBEDDED GIF (self-contained version)
"""
import marimo

__generated_with = "0.9.14"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import plotly.express as px
    return mo, pd, px


@app.cell
def __(mo):
    mo.md(
        """
        # Leiden Clustering - DC
        """
    )
    return






@app.cell
def __(mo, pd):
    import json
    import requests
    from io import StringIO

    # Enable HTTP requests in WASM/Pyodide
    try:
        import pyodide_http
        pyodide_http.patch_all()
    except ImportError:
        pass

    # Load results from GitHub - use requests then parse
    results_url = 'https://massafn.github.io/leidendc/leiden_gamma_sweep_results.csv'
    csv_response = requests.get(results_url)
    results_df = pd.read_csv(StringIO(csv_response.text))

    # Load cluster legend info with actual cluster IDs
    legend_url = 'https://massafn.github.io/leidendc/cluster_legend_info.json'
    try:
        response = requests.get(legend_url)
        cluster_legend = json.loads(response.text)
    except:
        cluster_legend = {}

    # Maximally distinct color palette (same as used in map generation)
    color_palette = [
        '#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf',
        '#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d', '#666666',
        '#8dd3c7', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd',
        '#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3',
        '#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#a65628', '#f781bf', '#999999',
        '#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5',
        '#d9d9d9', '#bc80bd', '#ccebc5', '#ffed6f', '#1f78b4', '#33a02c', '#e31a1c', '#ff7f00',
        '#6a3d9a', '#b15928', '#a6cee3', '#b2df8a', '#fb9a99'
    ]

    # Create slider for gamma
    gamma_slider = mo.ui.slider(
        start=0.25,
        stop=6.0,
        step=0.25,
        value=1.0,
        label="γ"
    )

    # Simple run button to advance to next gamma
    run_button = mo.ui.run_button(label="▶ Next")

    mo.hstack([gamma_slider, run_button])
    return cluster_legend, color_palette, gamma_slider, legend_url, results_df, results_url, run_button


@app.cell
def __(gamma_slider, run_button):
    # When button is clicked, advance to next gamma
    if run_button.value:
        current = gamma_slider.value
        next_gamma = round(current + 0.25, 2)
        if next_gamma > 6.0:
            next_gamma = 0.25
        current_gamma = next_gamma
    else:
        current_gamma = gamma_slider.value

    return current_gamma,


@app.cell
def __(mo, current_gamma):
    # Display interactive map based on current gamma (either from animation or slider)
    selected_gamma_map = current_gamma

    # Construct URL for the PNG map corresponding to selected gamma
    map_url = f'https://massafn.github.io/leidendc/leiden_map_gamma_{selected_gamma_map:.2f}.png'

    mo.md(f"""
    **γ = {selected_gamma_map:.2f}**
    """)
    return map_url, selected_gamma_map


@app.cell
def __(mo, map_url):
    # Display the map image
    mo.md(f'<img src="{map_url}" style="max-width: 100%; height: auto;" />')
    return


@app.cell
def __(mo, cluster_legend, selected_gamma_map):
    # Display legend with actual cluster IDs from the data
    gamma_key = f'{selected_gamma_map:.2f}'

    # Get cluster info for this gamma
    if gamma_key in cluster_legend:
        clusters = cluster_legend[gamma_key]

        # Build HTML legend with color swatches
        legend_html = '<div style="margin: 20px 0;"><h3>Cluster Colors</h3>'
        legend_html += '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); gap: 10px;">'

        for cluster in clusters:
            cluster_id = cluster['cluster_id']
            color = cluster['color']
            legend_html += f'<div style="display: flex; align-items: center; gap: 5px;">'
            legend_html += f'<span style="display: inline-block; width: 30px; height: 20px; background-color: {color}; border: 1px solid black;"></span>'
            legend_html += f'<span style="font-size: 12px;">C{cluster_id}</span>'
            legend_html += '</div>'

        legend_html += '</div></div>'
    else:
        legend_html = '<div style="margin: 20px 0;"><p><em>Loading legend...</em></p></div>'

    mo.md(legend_html)
    return gamma_key, legend_html




@app.cell
def __(current_gamma, results_df):
    # Get selected gamma value (from animation or slider)
    selected_gamma = current_gamma

    # Get results for selected gamma
    result_row = results_df[results_df['gamma'] == selected_gamma].iloc[0]

    return result_row, selected_gamma


@app.cell
def __(mo, px, results_df):
    mo.md("## Trends Across All Resolution Parameters")

    # Create interactive plot
    fig1 = px.line(
        results_df,
        x='gamma',
        y='n_communities',
        markers=True,
        title='Clusters vs Gamma',
        labels={'gamma': 'Gamma', 'n_communities': 'Number of Clusters'}
    )
    fig1.update_traces(line_color='#2166ac', line_width=3, marker_size=10)

    fig2 = px.line(
        results_df,
        x='gamma',
        y='modularity',
        markers=True,
        title='Modularity vs. Gamma',
        labels={'gamma': 'Gamma', 'modularity': 'Modularity'}
    )
    fig2.update_traces(line_color='#b2182b', line_width=3, marker_size=10)

    mo.vstack([
        mo.ui.plotly(fig1),
        mo.ui.plotly(fig2)
    ])
    return fig1, fig2






if __name__ == "__main__":
    app.run()
