import math

def cone_surface_area():
    
    r = float(input("What is the radius of the cone (in feet)? "))
    l = float(input("What is the slant height of the cone (in feet)? "))
    
    SA = math.pi * r**2 + math.pi * r * l
    
    SA_rounded = round(SA, 1)
    
    print(f"The surface area of the cone is: {SA_rounded} square feet")

cone_surface_area()


