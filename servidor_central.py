import Pyro5.api
import os

@Pyro5.api.expose
class Estacionamiento(object):
    def __init__(self):
        self.cajones = {"cajon1": 0, "cajon2": 0, "cajon3": 0}

    def actualizar_estado(self, c1, c2, c3):
        self.cajones["cajon1"] = c1
        self.cajones["cajon2"] = c2
        self.cajones["cajon3"] = c3
        # El flush=True obliga a Python a mostrar el print en Railway al instante
        print(f"📞 [RMI] ¡Flask me mandó datos nuevos! -> {self.cajones}", flush=True)
        return "Estado actualizado en el Servidor Central RMI"
    def consultar_estado(self):
        return self.cajones

# Usamos el puerto que nos dé Railway, o el 9090 por defecto
puerto = int(os.environ.get("PORT", 9090))
daemon = Pyro5.api.Daemon(host="::", port=puerto)

# Registramos el objeto con un nombre fácil de recordar
uri = daemon.register(Estacionamiento, "estacionamiento.central")

print("="*50, flush=True)
print("🏢 SERVIDOR CENTRAL RMI INICIADO EN LA NUBE 🏢", flush=True)
print(f"Escuchando llamadas en el puerto: {puerto}", flush=True)
print("="*50, flush=True)

daemon.requestLoop()
