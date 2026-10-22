def calculate_receiving_points(receiving_yards, touchdowns, receptions):
    return (receiving_yards / 10) + (touchdowns * 6) + receptions

def calculate_rushing_points(rushing_yards, touchdowns):
    return (rushing_yards / 10) + (touchdowns * 6) 