def kalkulator_bmi():
    try:
        berat = float(input("isi berat badan anda disini(kg): "))
        tinggi = float(input("isi tinggi badan anda disini(cm): "))    
       
        tinggi_meter = tinggi / 100
        bmi = berat / (tinggi_meter ** 2)
        
        print(f"nilai BMI anda adalah {bmi:.2f}!")
        
        if bmi < 18.5: 
                  print("kategori: kurus")
        elif 18.5 <= bmi < 25:
                  print("kategori: sedang")
        elif 18.5 <= bmi < 30:
                  print("kategori: gendut")
        else: 
                  print("kamu obesitas empal gentong")
    except ValueError: 
          print("angka tidak valid")
          
kalkulator_bmi()
