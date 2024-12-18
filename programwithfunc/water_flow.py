import math

def water_column_height(tower_height, tank_height):

        h = tower_height + ((3 * tank_height) / 4)
        return h


def pressure_gain_from_water_height(height):

    density_of_water = 998.2  
    gravity = 9.80665        

    pressure = (density_of_water * gravity * height) / 1000  

    return pressure

height = 10 
pressure = pressure_gain_from_water_height(height)
print(f"Pressure from a water height of {height} meters is {pressure:.2f} kPa")

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    
    density_of_water = 998.2  

    pressure_loss = -(friction_factor * pipe_length * density_of_water * fluid_velocity**2) / (2000 * pipe_diameter)

    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings): 
     
     density_of_water = 998.2
     
     p = (-0.04 * density_of_water * quantity_fittings * fluid_velocity ** 2) / 2000

     return p

def reynolds_number(hydraulic_diameter, fluid_velocity):
     
     density_of_water = 998.2

     viscosity = 0.0010016

     reynolds = (density_of_water * fluid_velocity * hydraulic_diameter) / viscosity
     return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    # Constants
    water_density = 998.2  
    
    # Calculate the constant k
    k = (0.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) - 1)
    
    # Calculate pressure loss P in kilopascals
    P = ((-1 * k) * water_density * fluid_velocity ** 2) / 2000
    
    return P