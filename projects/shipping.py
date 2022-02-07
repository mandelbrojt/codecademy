package_weight = float(input("What is the weight in pounds of your package?: "))

# Ground Shipping
if package_weight <= 2.0:
    price_per_pound = 1.50
    flat_charge = 20.0
    cost = package_weight * price_per_pound + flat_charge
    print("The standard ground shipping cost of your package is: " + str(cost))
elif package_weight > 2.0 and package_weight <= 6.0:
    price_per_pound = 3.0
    flat_charge = 20.0
    cost = package_weight * price_per_pound + flat_charge
    print("The standard ground shipping cost of your package is: " + str(cost))
elif package_weight > 6.0 and package_weight <= 10.0:
    price_per_pound = 4.0
    flat_charge = 20.0
    cost = package_weight * price_per_pound + flat_charge
    print("The standard ground shipping cost of your package is: " + str(cost))
else:
    price_per_pound = 4.75
    flat_charge = 20.0
    cost = package_weight * price_per_pound + flat_charge
    print("The standard ground shipping cost of your package is: " + str(cost))

premium_ground_shipping = 125.0
print("The premium ground shipping cost is: " + str(premium_ground_shipping))

# Drone Shipping
if package_weight <= 2.0:
    price_per_pound = 4.50
    flat_charge = 0.0
    cost = package_weight * price_per_pound + flat_charge
    print("The standard drone shipping cost of your package is: " + str(round(cost,2)))
elif package_weight > 2.0 and package_weight <= 6.0:
    price_per_pound = 9.0
    flat_charge = 0.0
    cost = package_weight * price_per_pound + flat_charge
    print("The standard drone shipping cost of your package is: " + str(round(cost,2)))
elif package_weight > 6.0 and package_weight <= 10.0:
    price_per_pound = 12.0
    flat_charge = 0.0
    cost = package_weight * price_per_pound + flat_charge
    print("The standard drone shipping cost of your package is: " + str(round(cost,2)))
else:
    price_per_pound = 14.25
    flat_charge = 0.0
    cost = package_weight * price_per_pound + flat_charge
    print("The standard drone shipping cost of your package is: " + str(round(cost,2)))