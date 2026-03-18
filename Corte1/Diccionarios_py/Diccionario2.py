# ---------- ACCEDER A VALORES USANDO LA CLAVE ----------
# Un diccionario guarda información en pares clave : valor.
# Para acceder a un valor, se usa: diccionario[clave]

building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

print(building_heights["Burj Khalifa"])   # Devuelve el valor asociado a la clave
print(building_heights["Ping An"])
print()


# ---------- DICCIONARIO CON LISTAS COMO VALORES ----------
# Los valores de un diccionario pueden ser cualquier tipo de dato,
# incluso listas.

zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

print(zodiac_elements["earth"])   # Devuelve una lista completa
print(zodiac_elements["fire"])
print()


# ---------- VERIFICAR SI UNA CLAVE EXISTE ----------
# Acceder a una clave inexistente causa un error (KeyError).
# Para evitarlo, se usa el operador "in".

key_to_check = "Landmark 81"

if key_to_check in building_heights:
    print(building_heights[key_to_check])
else:
    print("Key not found")
print()


# ---------- AGREGAR UNA NUEVA CLAVE ----------
# Si la clave no existe, se crea automáticamente.

zodiac_elements["energy"] = "Not a Zodiac element"

if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])
print()


# ---------- ACCESO SEGURO CON get() ----------
# get() permite acceder a una clave sin causar error.
# Si la clave no existe, devuelve None (o un valor por defecto).

print(building_heights.get("Shanghai Tower"))  # Clave existente
print(building_heights.get("My House"))        # Clave inexistente → None
print()


# ---------- get() CON VALOR POR DEFECTO ----------
# Si la clave no existe, se usa el valor indicado.

user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

tc_id = user_ids.get("teraCoder", 1000)        # Devuelve el valor real
stack_id = user_ids.get("superStackSmash", 100000)  # Usa el valor por defecto

print(tc_id)
print(stack_id)
print()


# ---------- ELIMINAR ELEMENTOS CON pop() ----------
# pop() elimina una clave y devuelve su valor.
# Si no existe, devuelve el valor por defecto.

raffle = {
    223842: "Teddy Bear",
    872921: "Concert Tickets",
    320291: "Gift Basket",
    412123: "Necklace",
    298787: "Pasta Maker"
}

print(raffle.pop(320291, "No Prize"))  # Elimina y devuelve el premio
print(raffle)
print()


# ---------- EJEMPLO PRÁCTICO CON pop() ----------
# pop() es útil para consumir elementos y actualizar valores.

available_items = {
    "health potion": 10,
    "cake of the cure": 5,
    "green elixir": 20,
    "strength sandwich": 25,
    "stamina grains": 15,
    "power stew": 30
}

health_points = 20

# Se suman puntos y se eliminan los ítems usados
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)   # Ítems restantes
print(health_points)     # Puntos finales
print()


# ---------- OBTENER TODAS LAS CLAVES ----------
# list(diccionario) o diccionario.keys() devuelve las claves.

test_scores = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martin": [78, 80, 78],
    "Dina": [64, 60, 75]
}

print(list(test_scores))   # Convierte las claves en lista

for student in test_scores.keys():
    print(student)
print()


# ---------- OBTENER TODOS LOS VALORES ----------
# values() permite recorrer únicamente los valores.

for score_list in test_scores.values():
    print(score_list)
print()


# ---------- OPERAR CON LOS VALORES ----------
# Ejemplo: sumar todos los valores del diccionario.

num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

total_exercises = 0
for exercises in num_exercises.values():
    total_exercises += exercises

print(total_exercises)
print()


# ---------- OBTENER CLAVE Y VALOR CON items() ----------
# items() devuelve pares (clave, valor), ideal para recorrer todo.

biggest_brands = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8
}

for company, value in biggest_brands.items():
    print(company, "has a value of", value, "billion dollars")
print()


pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9
}

for occupation, percentage in pct_women_in_occupation.items():
    print("Women make up", percentage, "percent of", occupation + "s")
