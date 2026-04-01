import zoneinfo
from fastapi import FastAPI
from datetime import datetime


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello life"}


country_timezones = {
    "NI": "America/Managua",              # Nicaragua
    "CO": "America/Bogota",           # Colombia (misma hora UTC-5)
    "MX": "America/Mexico_City",          # México
    "AR": "America/Argentina/Buenos_Aires", # Argentina
    "PE": "America/Lima",                 # Perú
    "US": "America/New_York",             # Estados Unidos
    "ES": "Europe/Madrid",                # España
    "JP": "Asia/Tokyo",                   # Japón
    "AU": "Australia/Sydney",             # Australia
    "BR": "America/Sao_Paulo"             # Brasil
}

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    now = datetime.now(tz)
    return {
        "mensaje": "Hola Santiago",
        "hora": datetime.now(tz),
        "pais": iso,
        "activo": True,
        "zona_horaria": timezone_str
    }


format_hours = {
    "24": "%H:%M:%S",           # 24 horas: 14:30:25
    "12": "%I:%M:%S %p",        # 12 horas: 02:30:25 PM
    "24SIMPLE": "%H:%M",       # 24 horas sin segundos: 14:30
    "12SIMPLE": "%I:%M %p",    # 12 horas sin segundos: 02:30 PM
    "MILITAR": "%H%M%S",       # Formato militar: 143025
}

@app.get ("/hour/{format}")
async def hour(format: str):
    format = format.upper()

    format_str = format_hours.get(format)

    now = datetime.now()

    hora_formateada = now.strftime(format_str)

    return {
        "formato": format,
        "hora_formateada": hora_formateada
    }