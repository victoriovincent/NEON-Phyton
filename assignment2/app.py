def celciusKelvin(suhu,skala):
    "Fungsi untuk konversi suhu dari skala celsius ke kelvin dan sebaliknya"
    if skala=="c":
        return suhu+273.15
    elif skala=="k":
        return suhu-273.15
    else:
        return; 

def toFahrenheit(suhu,skala):
    "Fungsi untuk konversi suhu dari celsius atau kelvin ke farenheit"
    if skala=="c":
        return (suhu*9)/5+32
    elif skala=="k":
        return (celciusKelvin(suhu,skala)*9)/5+32
    else:
        return;
    
def fToKelvinCelcius(suhu,skalaOutput):
    "Fungsi untuk konversi dari farenheit ke celsius atau kelvin"
    if skalaOutput=="c":
        return (suhu-32)*5/9,"k"
    elif skalaOutput=="k":
        return  (suhu-32)*5/9+273.15,"k"
    else:
        return;      