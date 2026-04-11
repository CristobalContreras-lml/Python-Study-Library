# ============================================================
# FUNDAMENTOS DE PYTHON - Condicionales (if / elif / else)
# ============================================================

# ── 1. IF básico ─────────────────────────────────────────────
edad = 20
if edad >= 18:
    print("Mayor de edad ✔")

# ── 2. IF / ELSE ─────────────────────────────────────────────
temperatura = 10
if temperatura >= 20:
    print("Hace calor ☀️")
else:
    print("Hace frío 🧥")

# ── 3. IF / ELIF / ELSE ──────────────────────────────────────
nota = 75
if nota >= 90:
    print("Sobresaliente 🏆")
elif nota >= 75:
    print("Notable 👍")
elif nota >= 60:
    print("Aprobado ✔")
else:
    print("Reprobado ✗")

# ── 4. OPERADORES DE COMPARACIÓN ─────────────────────────────
# ==  igual      !=  distinto     >  mayor      <  menor
# >=  mayor o igual              <=  menor o igual

# ── 5. OPERADORES LÓGICOS: and, or, not ──────────────────────
tiene_dni = True
es_mayor  = True
if tiene_dni and es_mayor:
    print("Puede votar ✔")
if not tiene_dni:
    print("Sin DNI ✗")

# ── 6. TERNARIO — if/else en una línea ───────────────────────
puntaje   = 85
resultado = "Aprobado ✔" if puntaje >= 60 else "Reprobado ✗"
print(resultado)

# ── 7. CONDICIONAL CON "in" ───────────────────────────────────
frutas = ["manzana", "banana", "mango"]
if "banana" in frutas:
    print("Tenemos banana ✔")

# ── 8. EJEMPLO FINAL — Descuento en tienda ───────────────────
precio    = 50_000
vip       = True
cupon     = False

if vip and cupon:
    descuento = 0.30
elif vip:
    descuento = 0.20
elif cupon:
    descuento = 0.10
else:
    descuento = 0.0

print(f"Precio final: ${precio * (1 - descuento):,.0f}")
