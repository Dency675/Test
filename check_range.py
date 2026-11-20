import json
m = json.load(open("models/temperature_model.json"))
cases = json.load(open("models/temperature_model.cases.json"))
for i, name in enumerate(m["feature_names"]):
    vals = [c["features"][i] for c in cases]
    print(name, "| train:", round(m["training_min"][i], 2), "to", round(m["training_max"][i], 2),
          "| test:", round(min(vals), 2), "to", round(max(vals), 2))