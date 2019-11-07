from aiohttp import web
import aiohttp_jinja2
import jinja2
from pathlib import Path

here = Path(__file__).resolve().parent


@aiohttp_jinja2.template('index.html')
def index_handler(request):
    return {'world': 'word'}


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(here)))
app.router.add_get('/', index_handler)

web.run_app(app, host='0.0.0.0', port=80)
