#(0°C × 9/5) + 32 = 32°F

def cel2far(celtemp):
  far=(celtemp*9/5)+32
  return far

celtemp=int(input("Enter the temp in celcius: "))
fartemp=int(cel2far(celtemp))
print(f"The converted temp is {fartemp}F")

