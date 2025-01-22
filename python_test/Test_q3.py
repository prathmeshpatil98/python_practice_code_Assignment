#3 write a programme to accept distance in Km and Convert in into meters and centimets 

km = int(input("Please Enter the Kilometer : "))

metre = km * 1000
centi_meter = metre * 100

print(f"The Distance of {km} kilometer is {metre} metre and {centi_meter} Centi Meter .")