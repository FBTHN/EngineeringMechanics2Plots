import numpy as np
import plotly.graph_objects as go

fig = go.Figure()
x = np.arange(10)
fig.add_trace(go.Scatter(x=x,y=x));

# Save interactive HTML file (self‑contained)
fig.write_html("testplot.html")
