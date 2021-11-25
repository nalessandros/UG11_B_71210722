def check_data_type(var1,var2):
    var2 = var2.lower()
    if (type(var1) == str and (var2) == "str"):
        print("Jawaban Anda benar")
        return True
    elif (type(var1) == int and (var2) == "int"):
        print("Jawaban Anda benar")
        return True
    elif (type(var1) == int and (var2) == "str"):
        print("Jawaban Anda salah, seharusnya adalah: int")
        return False
    else:
        print("Jawaban Anda salah, seharusnya adalah: str")
        return False

print(check_data_type("Kevin","STr"))
print(check_data_type("Kevin","str"))
print(check_data_type(12345,"str"))
print(check_data_type("9347","int"))
print(check_data_type(9876,"int"))