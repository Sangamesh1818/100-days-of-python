km_driven_after_service = int(input("Enter the kilometers driven after service: "))
months_since_service = int(input("Enter the number of months since last service: "))

if (km_driven_after_service >= 10000 or months_since_service > 6):
    print(f"Your vehicle is due for service. Please schedule a service appointment.")
elif (km_driven_after_service >= 8000 or months_since_service >=5):
    print(f"Your vehicle is not due for service yet. Please check again later.")
else:
    print(f"Your vehicle is not due for service yet. Please check again later.")