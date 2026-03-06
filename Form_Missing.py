results = []

name = _items[0]["json"]["Nombre"]
email = _items[0]["json"]["Email"]
message = _items[0]["json"]["Mensaje"]

clean_name = " ".join(name.split())
clean_email = email.strip().lower()
text = message.lower()

score = 0

if "urgente" in text or "lo antes posible" in text:
  score += 50

if "asesoria" in text or "curso" in text:
  score += 30

if len(text) > 120:
  score +=20

if score >= 70:
  level = "caliente"
elif score >= 40:
  level = "medio"
else:
  level = "frio"

results.append({
    "json": {
      "name": clean_name,
      "email": clean_email,
      "message": message,
      "score": score,
      "level": level
    }
})

return results