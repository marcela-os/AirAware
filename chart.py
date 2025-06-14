import plotly.graph_objects as go

def generate_map(data):

    lati = [lat for _, _, lat, *_ in data]
    long = [long for *_, long in data]
    text_labels = []

    for station_name, id, lat, lon in data:
        label = f"{station_name} ID:{id}"
        text_labels.append(label)

    fig = go.Figure(go.Scattermap(
        lat=lati,
        lon=long,
        mode='markers',
        marker=go.scattermap.Marker(
            size=9
        ),
        text=text_labels
    ))

    fig.update_layout(
        autosize=False,
        width=1200,
        height=600,
        hovermode='closest',
        margin=dict(l=0, r=0, t=0, b=0),
        map=dict(
            bearing=0,
            center=dict(
                # lat=52.112795,
                # lon=-19.211946
                lat=52.065,
                lon=19.480
            ),
            pitch=0,
            zoom=5
        ),
    )
    return fig

if __name__ == "__main__":
    lat=['38.91427','38.91538','38.91458',
         '38.92239','38.93222','38.90842',
         '38.91931','38.93260','38.91368',
         '38.88516','38.921894','38.93206',
         '38.91275']
    lon=['-77.02827','-77.02013','-77.03155',
         '-77.04227','-77.02854','-77.02419',
         '-77.02518','-77.03304','-77.04509',
         '-76.99656','-77.042438','-77.02821',
         '-77.01239'],
    fig = generate_map(lat, lon)
    fig.show()
