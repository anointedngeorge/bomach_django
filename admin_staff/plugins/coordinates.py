from math import radians, sin, cos, sqrt, atan2
# from geopy.distance import geodesic



def calculate_distance(receiver_lat, receiver_lon, sender_lat, sender_lon):
    # Convert coordinates to radians
    lat1 = radians(receiver_lat)
    lon1 = radians(receiver_lon)
    lat2 = radians(sender_lat)
    lon2 = radians(sender_lon)

    # Radius of the Earth in kilometers
    earth_radius = 6371

    # Calculate the differences between the coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = earth_radius * c

    return float(f"{distance:.2f}")

# # Coordinates
# lat1 = 6.4445504
# lon1 = 7.497941
# lat2 = 6.431668999999999
# lon2 = 7.520178499999999

# # Calculate the distance
# distance = calculate_distance(lat1, lon1, lat2, lon2)

# # Print the result
# print(f"The distance between the coordinates is approximately {distance} kilometers.")




