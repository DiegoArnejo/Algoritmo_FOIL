import math

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

# FOIL Gain ================================================================================================

# Valores antes de aplicar la condicion
P = sum(1 for d in datos if d["en_formacion"])
N = sum(1 for d in datos if not d["en_formacion"])

# Aplicar condicion: edad <= 23"
filtrados = [d for d in datos if d["edad"] <= 23]
p = sum(1 for d in filtrados if d["en_formacion"])
n = sum(1 for d in filtrados if not d["en_formacion"])


foil_gain = p * (log2_safe(p / (p + n)) - log2_safe(P / (P + N)))

# Mostrar resultados
print("======================================================================================================")
print("\n-Condicion: edad <= 23\n")
print(f"P = (positivos antes) = {P}")
print(f"N = (negativos antes) = {N}")
print(f"p = (positivos despues) = {p}")
print(f"n = (negativos despues) = {n}")
print(f"p / (p + n) = {p / (p + n):.3f}")
print(f"P / (P + N) = {P / (P + N):.3f}")
print(f"log2(p / (p + n)) = {log2_safe(p / (p + n)):.3f}")
print(f"log2(P / (P + N)) = {log2_safe(P / (P + N)):.3f}")
print(f"\nFOIL Gain = {foil_gain:.3f}")
