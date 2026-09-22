import math

def inducir_regla(positivos, negativos):
    atributos = ["edad", "departamento", "nivel_educativo"]
    regla = {}

    for atributo in atributos:
        valores_pos = set(p[atributo] for p in positivos)
        valores_neg = set(p[atributo] for p in negativos)
 
        if atributo == "edad":
            valores_validos = [v for v in valores_pos if v not in valores_neg]
        else:
             valores_validos = list(valores_pos - valores_neg)

        if valores_validos:
            regla[atributo] = valores_validos

    return regla

# Clasificador
def atributos_exclusivos(datos):
    pos = [d for d in datos if d["en_formacion"]]
    neg = [d for d in datos if not d["en_formacion"]]

    edad = {d["edad"] for d in pos} - {d["edad"] for d in neg}
    departamento = {d["departamento"] for d in pos} - {d["departamento"] for d in neg}
    nivel_educativo = {d["nivel_educativo"] for d in pos} - {d["nivel_educativo"] for d in neg}

    return edad, departamento, nivel_educativo

# Calculo FOIL Gain
def log2_safe(x):
    return math.log2(x) if x > 0 else float('-inf')


# Set de datos
datos = [
 {"edad": 22, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
 {"edad": 24, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": True},
 {"edad": 21, "departamento": "RRHH", "nivel_educativo": "terciario", "en_formacion": True},
 {"edad": 35, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": False},
 {"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría", "en_formacion": False},
 {"edad": 29, "departamento": "RRHH", "nivel_educativo": "universitario", "en_formacion": False},
 {"edad": 23, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
 {"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False}
 ]

# Separar ejemplos positivos y negativos
positivos = [p for p in datos if p["en_formacion"]]
negativos = [p for p in datos if not p["en_formacion"]]

# Ejecutar el algoritmo
regla_inducida = inducir_regla(positivos, negativos)

# Mostrar la regla
print("\nRegla inducida para identificar a personas en formacion:")
for atributo, valores in regla_inducida.items():
    print(f"- {atributo} debe ser: {valores}")

# Llamada a funcion identificadora
atributos_unicos = atributos_exclusivos(datos)
atributos_unicos = [list(conjunto) for conjunto in atributos_unicos]

# Mostrar atributos que aparecen en positivos pero no en negativos
print("- Aquellos atributos que aparecen en los positivos pero no en los negativos son:", atributos_unicos)
print(" ")

# FOIL Gain ================================================================================================

# Valores antes de aplicar la condicion
P = sum(1 for d in datos if d["en_formacion"])
N = sum(1 for d in datos if not d["en_formacion"])

# Aplicar condicion: nivel_educativo == "terciario"
filtrados = [d for d in datos if d["nivel_educativo"] == "terciario"]
p = sum(1 for d in filtrados if d["en_formacion"])
n = sum(1 for d in filtrados if not d["en_formacion"])


foil_gain = p * (log2_safe(p / (p + n)) - log2_safe(P / (P + N)))

# Mostrar resultados
print("======================================================================================================")
print("\n-Condicion: nivel_educativo == 'terciario'\n")
print(f"P = (positivos antes) = {P}")
print(f"N = (negativos antes) = {N}")
print(f"p = (positivos despues) = {p}")
print(f"n = (negativos despues) = {n}")
print(f"p / (p + n) = {p / (p + n):.3f}")
print(f"P / (P + N) = {P / (P + N):.3f}")
print(f"log2(p / (p + n)) = {log2_safe(p / (p + n)):.3f}")
print(f"log2(P / (P + N)) = {log2_safe(P / (P + N)):.3f}")
print(f"\nFOIL Gain = {foil_gain:.3f}")
