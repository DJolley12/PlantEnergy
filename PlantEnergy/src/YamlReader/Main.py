from WindObject import WindObject

if __name__ == "__main__":
    filepath = "D:\source\WindFarmCode\YamlReader\YamlReader\YamlReader\\"
    ex16 = "iea37-ex16.yaml"
    ex16_fullpath = filepath + ex16
    windrose = "iea37-windrose.yaml"
    wind_object = WindObject()
    data = wind_object.yaml_loader(filepath, ex16)
    wind_object.return_wind_object(data)

    print(wind_object.turbineX)