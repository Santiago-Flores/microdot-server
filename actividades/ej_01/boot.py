# Configuracion inicial
def initialize_connection():
    import network
    wifi = network.WLAN(network.STA_IF)
    if not wifi.isconnected():
        print('Estableciendo conexión con el servidor...')
        wifi.active(True)
        wifi.connect('Cooperadora Alumnos', '')
        while not wifi.isconnected():
            pass
    print('Configuración de red:', wifi.ifconfig())

initialize_connection()
