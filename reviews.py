from flask import Blueprint
import pyvibe as pv

reviews_bp = Blueprint('reviews', __name__, template_folder='templates')


@reviews_bp.route('/reviews')
def reviews():
    navbar = pv.Navbar(title='Everyday Coffeenaut', logo='static/logo/logo-bw-01.png')
    navbar.add_navbarlink('Reviews', '/reviews')
    navbar.add_navbarlink('Media', '/media')

    page = pv.Page(navbar=navbar)

    with page.add_container(grid_columns=3) as container:
        with container.add_card() as card:
            card.add_header("The Brick (Łódź, Poland)")
            card.add_text("Very good cafe.")
            card.add_link("Instagram", "https://www.instagram.com/thebrickcoffeefactory/")

        with container.add_card() as card:
            card.add_header("The Brick (Łódź, Poland)")
            card.add_text("Very good cafe.")
            card.add_link("Instagram", "https://www.instagram.com/thebrickcoffeefactory/")

    return page.to_html()