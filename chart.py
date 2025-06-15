import plotly.graph_objects as go

def generate_map(data, aq_index):

    value_colors = {
        0: '#00a05d',
        1: '#ffd60a',
        2: '#fb8500',
        3: '#d93e00',
        4: '#d00000',
        -1: '#4582EC'
    }

    value_labels = {
        0: 'Bardzo dobry',
        1: 'Dobry',
        2: 'Umiarkowany',
        3: 'Dostateczny',
        4: 'Zły',
        -1: 'Brak indeksu'
    }

    value_sizes = {
        -1: 10,
         0: 12,
         1: 14,
         2: 16,
         3: 18,
         4: 20
    }


    index_dict = {station_id: numeric_level for station_id, numeric_level, _ in aq_index}


    lats, lons, texts, colors, sizes = [], [], [], [], []

    for station_name, station_id, lat, lon in data:
        value = index_dict.get(station_id, -1)  # jeśli brak danych, -1
        color = value_colors.get(value, '#b0b0b0')
        label_text = value_labels.get(value, 'Brak indeksu')
        size = value_sizes.get(value, 6)

        lats.append(lat)
        lons.append(lon)
        colors.append(color)
        sizes.append(size)
        texts.append(f"<b>{station_name}</b><br>ID: {station_id}<br>Poziom: {label_text}")

    fig = go.Figure()

    fig.add_trace(go.Scattermapbox(
        lat=lats,
        lon=lons,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=sizes,
            color=colors,
            opacity=0.85,
            symbol='circle'
        ),
        text=texts,
        hoverinfo='text',
        showlegend=False
    ))

    # Warstwa ukryta do legendy (kolor + opis)
    for value, label in sorted(value_labels.items()):
        fig.add_trace(go.Scattermapbox(
            lat=[None],
            lon=[None],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=10,
                color=value_colors[value],
                opacity=0.85,
                symbol='circle'
            ),
            name=label
        ))

    # Layout mapy
    fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            center=dict(lat=52.065, lon=19.480),
            zoom=5.3
        ),
        autosize=False,
        width=1200,
        height=610,
        margin=dict(l=0, r=0, t=0, b=0),
        # margin=dict(l=20, r=20, t=40, b=20),
        # paper_bgcolor="white",
        # plot_bgcolor="white",
        legend=dict(
            title=dict(text="Poziom jakości powietrza"),
            font=dict(size=12),
            orientation="v",
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="lightgray",
            borderwidth=1,
            x=0.01,
            y=0.99
        )
    )

    return fig



