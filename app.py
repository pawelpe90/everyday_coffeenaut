from flask import Flask
import pyvibe as pv
from reviews import reviews_bp
from media import media_bp
from map import map_bp

app = Flask(__name__)

app.register_blueprint(reviews_bp)
app.register_blueprint(media_bp)
app.register_blueprint(map_bp)


@app.route('/')
def index():
    navbar = pv.Navbar(title='Everyday Coffeenaut', logo='static/logo/logo-bw-01.png')
    navbar.add_navbarlink('Reviews', '/reviews')
    navbar.add_navbarlink('Media', '/media')

    page = pv.Page(navbar=navbar)

    with page.add_container(grid_columns=4) as container:
        with container.add_card() as card:
            card.add_header('Cafes I have visited so far...', size=3)
            card.add_text("0")

        with container.add_card() as card:
            card.add_header('Coffees I drunk today...', size=3)
            card.add_text("0")

        with container.add_card() as card:
            card.add_header('Coffees I drunk this month...', size=3)
            card.add_text("0")

    page.add_html(value='<iframe src="/iframe" width="100%" height="1200px"></iframe>')

    return page.to_html()


if __name__ == '__main__':
    app.run(debug=True)
