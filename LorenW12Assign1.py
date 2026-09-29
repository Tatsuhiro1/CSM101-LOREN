Loren_patients = {
    "ana": (80, 50, 150, 90, 140, 200, 124),
    "ben": (130, 140, 135, 90, 140, 90, 150, 200),
    "carlo": (90, 100, 95, 90, 140, 140, 120, 130),
}

Loren_status = ""

for Loren_name, Loren_readings in Loren_patients.items():
  print(f"Patient Name : {Loren_name} ")
  print("Blood Sugar Summary")

  Loren_high_count = 0
  for Loren_i in Loren_readings:
    if Loren_i > 120:
      Loren_status = "High"
      Loren_high_count += 1
    else:
      Loren_status = "Normal"

    print(f"{Loren_i} - {Loren_status}")

  sumMax = max(Loren_readings)
  sumMin = min(Loren_readings)
  sumAvg = sum(Loren_readings) / len(Loren_readings)
  sumDiff = sumMax - sumMin

  print(f"Patient {Loren_name} Overall Summary")
  print(f"High Counter {Loren_high_count} ")
  print(f"Max  {sumMax}")
  print(f"Min  {sumMin}")
  print(f"Avg  {sumAvg:.2f}")
  print(f"Diff {sumDiff}\n")