from flask import Blueprint, url_for, render_template_string
import folium

map_bp = Blueprint('map', __name__, template_folder='templates')


@map_bp.route("/iframe")
def iframe():
    """Embed a map as an iframe on a page."""
    m = folium.Map((51.763727, 19.457718), tiles="cartodb positron")

    # set the iframe width and height
    m.get_root().width = "1100px"
    m.get_root().height = "1000px"

    icon = folium.CustomIcon(
        url_for('static', filename='icons/coffee_icon.png', _external=True),
        icon_size=(25, 25),
        icon_anchor=(0, 0),
        popup_anchor=(10, -5),
    )

    folium.Marker(
        location=[51.761332, 19.458139], icon=icon, popup="The Brick"
    ).add_to(m)

    iframe = m.get_root()._repr_html_()

    return render_template_string(
        """
            {{ iframe|safe }}
        """,
        iframe=iframe,
    )