import yaml
import numpy as np

class WindObject(object):

    #def __init__(self, input_calculation_object, windfarm, windturbine):
    #    self.calculation_object = input_calculation_object
    #    self.windfarm = windfarm
    #    self.windturbine = windturbine

    def __init__(self):
        self.filepath = None
        self.turbineX = None
        self.turbineY = None
        self.wind_direction = None
        self.model = None
        self.rotorDiameter = None
        self.hubHeight = None
        self.axialIndunction = None
        self.generatorEfficiency = None
        self.windSpeeds = None
        self.windDirections = None
        self.windFrequencies = None
        self.Ct = None
        self.Cp = None
        self.cp_curve_cp = None
        self.cp_curve_wind_speed = None
        self.cut_in_speed = None
        self.model = None
        self.boundary_center = None
        self.boundary_radius = None
        self.air_density = None
        self.rated_power = None
        self.turbulence_intensity = None
        
               
    #def yaml_loader(self, filepath):
    #    with open(filepath, "r") as file_descriptor:
    #        data = yaml.load(file_descriptor)
    #    return data

    def yaml_loader(self, filepath, first_filename):
        self.filepath = filepath
        with open(filepath + first_filename, "r") as file_descriptor:
            data = yaml.safe_load(file_descriptor)
        return data

    def yaml_dump(filepath, data):
        with open(filepath, "w") as file_descriptor:
            yaml.safe_dump(data, file_descriptor)

    def return_wind_object(self, wind_object):
        wind_plant_filename = wind_object.get('definitions').get('wind_plant').get('properties').get('layout').get('items')[1].get('$ref')
        wind_turbine_data = self.yaml_loader(self.filepath, wind_plant_filename)
        plant_energy_properties = wind_object.get('definitions').get('plant_energy').get('properties') 
        wind_resource_filename = plant_energy_properties.get('wind_resource_selection').get('properties').get('items')[0].get('$ref')
        wind_resource_data = self.yaml_loader(self.filepath, wind_resource_filename)
        self.wind_resource(wind_resource_data)
                
        return wind_object

    def wind_turbine(self, wind_turbine_data):
        wind_turbine_lookup_properties = wind_turbine_data.get('definitions').get('wind_turbine_lookup').get('properties')
        wind_turbine = wind_turbine_data.get('definitions').get('wind_turbine')
        def_hub = wind_turbine_data.get('definitions').get('hub')
        self.hubHeight = def_hub.get('properties').get('height').get('default')
        rotor_radius = wind_turbine_data.get('definitions').get('rotor').get('radius')
        self.rotorDiameter = rotor_radius * 2
        wind_speed = wind_turbine_lookup_properties.get('wind_speed').get('maximum')        
        self.rated_power = wind_turbine_lookup_properties.get('power').get('maximum')
        self.cut_in_speed = wind_turbine_data.get('definitions').get('operating_mode').get('properties').get('cut_in_wind_speed').get('default')
        #self.axialIndunction = 
        #self.generatorEfficiency =
        self.Cp = wind_turbine_lookup_properties.get('c_p')
        #self.Ct = 
        #self.generatorEfficiency =

    def wind_resource(self, wind_resource_data):
        wind_resource_properties = wind_resource_data.get('definitions').get('wind_inflow').get('properties')
        self.windDirections = wind_resource_properties.get('direction').get('bins')
        self.windSpeeds = wind_resource_properties.get('speed').get('default')
        self.windFrequencies = wind_resource_properties.get('probability').get('defaults')
        self.turbulence_intensity = wind_resource_properties.get('ti').get('default')
        #self.air_density = 

    def wind_farm(self, wind_farm_data):
        position_items = wind_farm_data.get('definitions').get('position').get('items')
        self.turbineX = position_items.get('xc')
        self.turbineY = position_items.get('yc')
        #self.boundary_center =
        #self.boundary_radius =

        