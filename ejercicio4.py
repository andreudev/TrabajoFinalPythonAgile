contactos = {
    "Pedro": {
        "telefono": ["8962368", 987654321],
        "email": ["correo@ejemplo.com", "correo12@ejemplo.com"],
        "direccion": {"Calle": "3A", "Barrio": "El Bosque", "Ciudad": "Bogotá"},
    },
    "Juan": {
        "telefono": ["33333333", 987654321],
        "email": ["correo@ejemplo.com", "correo12@ejemplo.com"],
        "direccion": {"Calle": "4A", "Barrio": "El Popular", "Ciudad": "Bogotá"},
    },
    "Maria": {
        "telefono": ["32131231", 987654321],
        "email": ["correo@ejemplo.com", "correo12@ejemplo.com"],
        "direccion": {"Calle": "5B", "Barrio": "Aguaclara", "Ciudad": "Tunja"},
    },
}

contactos["Tatiana"] = {
    "telefono": ["1234567", 987654321],
    "email": ["correo@ejemplo.com", "correo12@ejemplo.com", "correo12@ejemplo.com"],
    "direccion": {"Calle": "6C", "Barrio": "El ocho", "Ciudad": "Cali"},
}

contactos["Andres"]["Fecha de nacimiento"] = [20, "Enero", 1995]

pop = contactos.pop("Juan")

# fechanacimiento = contactos["Andres"]["Fecha de nacimiento"][2]

# print(fechanacimiento)

# print(contactos["calendario"])

# for contacto, info in contactos.items():
#     print(f"\nDatos de {contacto}:")
#     print("Telefono:")
#     for telefono in info["telefono"]:
#         print(telefono)
#     print("Email:")
#     for email in info["email"]:
#         print(email)
#     print("Direccion:")
#     for clave, valor in info["direccion"].items():
#         print(f"{clave}: {valor}")
