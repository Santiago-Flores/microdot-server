# Aplicacion del servidor
from boot import initialize_connection
from microdot import Microdot, send_file

initialize_connection()
application = Microdot()

@application.route('/')
async def home(request):
    return send_file('index.html')

@application.route('/<folder>/<filename>')
async def serve_file(request, folder, filename):
    return send_file(f"/{folder}/{filename}")

application.run(port=80)

