import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "none"

fig = go.Figure()
x = np.arange(10)
fig.add_trace(go.Scatter(x=x,y=x));

fig.update_layout(margin=dict(l=0, r=0, t=0),width=800,height=800)

# Save html
html = fig.to_html(
    full_html=True,
    include_plotlyjs='cdn',     # smaller file; loads Plotly from CDN
    default_width="100%",
    default_height="100%",
)

# Wrap it in a minimal full-screen HTML template

fullscreen_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<style>
  html, body {{
    height: 100vh;
    width: 100vw;
    margin: 0;     /* remove default margins */
    padding: 0;
    overflow: hidden;
    background: #fff;
  }}
  /* Container that will hold Plotly's div */
  .plot-container {{
    height: 100vh;   /* or 100% if you prefer */
    width: 100vw;
  }}
</style>
</head>
<body>
  <div class="plot-container">
    {html}
  </div>
</body>
</html>"""


with open("./Lecture1/testplot.html", "w", encoding="utf-8") as f:
    f.write(fullscreen_html)

