import requests  # Importamos la librería requests para hacer solicitudes HTTP

def get_pokemon_info(nombre):
    # Función que recibe el nombre de un Pokémon y devuelve información sobre él
    
    nombre = nombre.lower().strip()  # Convertimos el nombre a minúsculas y eliminamos espacios extras
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"  # Construimos la URL para consultar la API
    
    response = requests.get(url)  # Hacemos la solicitud GET a la API
    
    if response.status_code == 200:  # Si la respuesta fue exitosa
        data = response.json()  # Convertimos la respuesta JSON a un diccionario de Python
        
        # Extraemos y transformamos los datos necesarios
        nombre = data['name'].capitalize()  # Nombre capitalizado
        id_pokemon = data['id']  # ID del Pokémon
        # Obtenemos todos los tipos del Pokémon, capitalizamos y unimos con coma y espacio
        tipo = ', '.join([t['type']['name'].capitalize() for t in data['types']])
        altura = data['height'] / 10  # Altura en metros (la API da decímetros)
        peso = data['weight'] / 10    # Peso en kilogramos (la API da hectogramos)
        sprite = data['sprites']['front_default']  # URL de la imagen frontal del Pokémon
        
        # Devolvemos un diccionario con la información que queremos mostrar
        return {
            "nombre": nombre,
            "id": id_pokemon,
            "tipo": tipo,
            "altura": altura,
            "peso": peso,
            "imagen": sprite
        }
    elif response.status_code == 404:  # Si la API no encuentra el Pokémon
        return None  # Retornamos None para indicar que no se encontró
    else:
        # Si hubo otro tipo de error, lanzamos una excepción con el código de error
        raise Exception(f"Error {response.status_code} al conectar con la API.")

if __name__ == "__main__":
    print("🔎 Bienvenido al buscador de Pokémon (escribe 'salir' para terminar)\n")

    while True:
        nombre_pokemon = input("👉 Ingresa el nombre del Pokémon: ")  # Pedimos nombre al usuario

        if nombre_pokemon.lower().strip() == "salir":  # Si escribe salir, terminamos el programa
            print("👋 ¡Hasta la próxima!")
            break

        info = get_pokemon_info(nombre_pokemon)  # Consultamos la API con el nombre dado

        if info:
            # Si recibimos información, la mostramos formateada
            print(f"\n📋 Información de {info['nombre']}")
            print(f"🆔 ID: {info['id']}")
            print(f"🧬 Tipo: {info['tipo']}")
            print(f"📏 Altura: {info['altura']} m")
            print(f"⚖️ Peso: {info['peso']} kg")
            print(f"🖼️ Imagen: {info['imagen']}\n")
        else:
            # Si no se encontró el Pokémon, mostramos mensaje de error
            print("❌ Pokémon no encontrado. Verifica el nombre.\n")
