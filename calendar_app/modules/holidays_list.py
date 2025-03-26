HOLIDAYS = {
    "2026-01-01": "New Year",
    "2026-08-15": "Independence Day",
    "2026-12-25": "Christmas"
}

def get_holidays():
    return HOLIDAYS

if __name__ == "__main__":
 for date, name in  get_holidays().items():
                print(f"{date}: {name}")