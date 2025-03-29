import json

# Load config file
with open("config.json", "r") as f:
    config = json.load(f)

def adjust_wind_speed(new_speed):
    config["wind_speed"] = new_speed
    save_config()

def adjust_humidity(new_humidity):
    config["humidity"] = new_humidity
    save_config()

def save_config():
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    adjust_wind_speed(3)
    adjust_humidity(0.5)
