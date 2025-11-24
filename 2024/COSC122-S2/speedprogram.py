"""This program works out the speed at which a person walked given how far they
   walked in feet and how long it took them in hours.
"""

SECONDS_IN_HOUR = 3600
METRES_IN_FOOT = 0.3048
METRES_IN_KM = 1000

def main():
    """Given a distance and feet and time in hours. Calculates speed in 
    m/s and km/h"""
    
    distance_feet = float(input("Enter the distance traveled in feet: "))
    time_hours = float(input("Enter the time taken in hours: "))
    
    distance_meters = METRES_IN_FOOT * distance_feet 
    time_seconds = time_hours * SECONDS_IN_HOUR 
    
    speed_mps = distance_meters/time_seconds
    print(f"Your average speed is: {speed_mps:.4f} m/s")
    speed_kph = SECONDS_IN_HOUR * speed_mps / METRES_IN_KM
    print(f"Which is: {speed_kph:.4f} km/h")
    THI
main()