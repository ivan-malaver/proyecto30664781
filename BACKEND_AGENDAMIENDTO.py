from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import requests
import datetime
from typing import List

app = FastAPI()

# Simulación de base de datos en memoria
citas = []

# Configuración del servicio GICC
GICC_URL = "https://api.gicc.com/validar"
TOKEN = "tu_token_aqui"

# Modelos de datos
class SolicitudCita(BaseModel):
    cedula: str
    placa: str
    tipo_cargue: str
    cantidad_combustible: float
    tipo_producto: str
    capacidad_vehiculo: str
    correo: str
    celular: str
    empresa: str
    fecha: str
    hora: str

class Cita(BaseModel):
    id: int
    cedula: str
    placa: str
    tipo_cargue: str
    cantidad_combustible: float
    bahia: str
    fecha: str
    hora: str
    estado: str  # "En espera" o "En curso"

# Función para validar en GICC
def validar_en_gicc(cedula: str, placa: str):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(f"{GICC_URL}?cedula={cedula}&placa={placa}", headers=headers)
    if response.status_code == 200:
        return response.json()["habilitado"]
    return False

# Endpoint para solicitar una cita
@app.post("/solicitar_cita")
def solicitar_cita(datos: SolicitudCita):
    if not validar_en_gicc(datos.cedula, datos.placa):
        raise HTTPException(status_code=400, detail="Conductor o vehículo no habilitado")
    
    nueva_cita = Cita(
        id=len(citas) + 1,
        cedula=datos.cedula,
        placa=datos.placa,
        tipo_cargue=datos.tipo_cargue,
        cantidad_combustible=datos.cantidad_combustible,
        bahia="B1",  # Lógica para asignar bahía
        fecha=datos.fecha,
        hora=datos.hora,
        estado="En espera"
    )
    citas.append(nueva_cita)
    return {"mensaje": "Cita agendada exitosamente", "cita": nueva_cita}

# Endpoint para ver citas en curso y en espera
@app.get("/citas")
def listar_citas():
    return citas
