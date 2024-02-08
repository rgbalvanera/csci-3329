#define the function header
def convert(dollar):
    #find the conversion unit knowing that 1 peso = 0.058 usd
    conversion_unit = 1/0.058
    #convert currencies
    pesos = dollar * conversion_unit
    #return pesos
    return pesos

#input us dollars
usd = float(input("US Dollar: $"))
#output pesos
print("Mexico Peso: ${:.2f}".format(convert(usd))) 