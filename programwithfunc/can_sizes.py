import math
def compute_volume(radius, height):
    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def main():
 
    can_data = [
        {"name": "#1 Picnic", "radius": 6.83, "height": 10.16},
        {"name": "#1 Tall", "radius": 7.78, "height": 11.91},
        {"name": "#2", "radius": 8.73, "height": 11.59},
        {"name": "#2.5", "radius": 10.32, "height": 11.91},
        {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78},
        {"name": "#5", "radius": 13.02, "height": 14.29},
        {"name": "#6Z", "radius": 5.40, "height": 8.89},
        {"name": "#8Z short", "radius": 6.83, "height": 7.62},
        {"name": "#10", "radius": 15.72, "height": 17.78},
        {"name": "#211", "radius": 6.83, "height": 12.38},
        {"name": "#300", "radius": 7.62, "height": 11.27},
        {"name": "#303", "radius": 8.10, "height": 11.11}
    ]

    for can in can_data:
        radius = can["radius"]
        height = can["height"]
        
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        storage_efficiency = volume / surface_area
        
        print(f"Can: {can['name']}")
        print(f"Volume: {volume:.2f} cm³")
        print(f"Surface Area: {surface_area:.2f} cm²")
        print(f"Storage Efficiency: {storage_efficiency:.4f}")
        print("-" * 30)

if __name__ == "__main__":
    main()