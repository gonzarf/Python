from datetime import datetime

input_date = datetime.strptime(input("Introduzca una fecha en formato dd/mm/yyyy: "), "%d/%m/%Y")
current_date = datetime.now()
difference = (current_date-input_date).days

print(f"La diferencia en días desde hoy es: {difference}")