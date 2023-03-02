import requests

response = requests.post("http://localhost:4000/predict", json={
  "model_key": "BMW",
  "mileage":75515,
  "engine_power":135,
  "fuel": "diesel",
  "paint_color": "grey",
  "car_type": "suv",
  "private_parking_available": False,
  "has_gps": True,
  "has_air_conditioning": False,
  "automatic_car": True,
  "has_getaround_connect": True,
  "has_speed_regulator": False,
  "winter_tires": True
  })
print(response.json())