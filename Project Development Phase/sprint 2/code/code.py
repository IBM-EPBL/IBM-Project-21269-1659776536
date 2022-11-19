
#importing Random function to generate the value
import random as rand


for i in range(3):
    print("Test case:",i+1)
    print("Water Quality Monitoring and Control System")
    temperature = int(rand.randint(-40,100))
    pH = int(rand.randint(0,14))
    DO = int(rand.randint(0,100))
    TDS = int(rand.randint(0,3700))
    Manganese = int(rand.randint(0,10))
    Copper = int(rand.randint(0,20))
    ammonia_Nitrate = int(rand.randint(0,100))
    Hardness = int(rand.randint(0,100))
    Zinc =  int(rand.randint(0,100))
    Conductivity =  f"{float(rand.uniform(0.001,2000)):.2f}"
    Chloride = int(rand.randint(0,200))
    Sulphate = int(rand.randint(0,100))
   
    print(
        "Temperature:", temperature,
        "\npH:", pH,
        "\nDO:", DO,
        "\nTDS:", TDS,
        "\nManganese:", Manganese,
        "\nCopper:", Copper,
        "\nAmmonia & Nitrate:",ammonia_Nitrate,
        "\nHardness:",Hardness,
        "\nZinc:", Zinc,
        "\nConductivity:", Conductivity,
       "\nChloride:", Chloride,
        "\nSulphate:", Sulphate, "\n"
    )

