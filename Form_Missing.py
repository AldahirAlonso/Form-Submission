results = []

name = _items[0]["json"]["Nombre"]
email = _items[0]["json"]["Email"]
message = _items[0]["json"]["Mensaje"]

results.append({
    "json": {
      "name": name,
      "email": email,
      "message": message
    }
})

return results