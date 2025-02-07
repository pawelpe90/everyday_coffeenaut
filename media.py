from flask import Blueprint
import pyvibe as pv

media_bp = Blueprint('media', __name__, template_folder='templates')


@media_bp.route('/media')
def media():
    navbar = pv.Navbar(title='Everyday Coffeenaut', logo='static/logo/logo-bw-01.png')
    navbar.add_navbarlink('Reviews', '/reviews')
    navbar.add_navbarlink('Media', '/media')

    page = pv.Page(navbar=navbar)

    page.add_link("Instagram", "https://www.instagram.com/everydaycoffeenaut/")

    return page.to_html()