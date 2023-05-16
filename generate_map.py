# Import the required library
import folium
from points import points

# Define the start and end points
start_point = [52.4054, 16.9313]  # Poznan
end_point = [52.7294, 15.2408]  # Gorzow Wielkopolski


# Function to draw the map
def draw_map(points):
    # Create the map
    map = folium.Map(location=[points[0]["latitude"], points[0]["longitude"]], zoom_start=12)

    # Draw the route
    # Start point marker
    folium.Marker([points[0]["latitude"], points[0]["longitude"]], popup='<i>Start</i>', color='green', fill_color='green').add_to(map)
    # End point marker
    folium.Marker([points[-1]["latitude"], points[-1]["longitude"]], popup='<i>End</i>', color='red', fill_color='red').add_to(map)
    # Route
    folium.PolyLine(locations=[[p["latitude"], p["longitude"]] for p in points], color="blue", weight=2.5, opacity=1).add_to(map)

    # Save it to a file. You can give unique name to the file everytime this function is called
    map.save('static/maps/map.html')


# Call the function
draw_map(points)