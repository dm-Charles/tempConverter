def celsiusConverter():
     try:
         fahrenheitTemp = int(temperatureEntry.get())
         celsiusTemp = (fahrenheitTemp - 32) * (5/9)
         answerLabel["text"] = f"{celsiusTemp}\N{DEGREE CELSIUS}"
     except:
         answerLabel["text"] = f"Integers only"
