def sisip():
    kal = input("Masukkan kalimat awal: ")
    sip = input("Masukkan kata untuk disisipkan: ")
    ind = int(input("Masukkan index: "))
    haha = list(kal.strip(" "))
    kalimat = ""

    for i in range (len(haha)):
        if i == ind - 1:
            kalimat = kalimat + sip
            kalimat = kalimat + kal[i]
        else:
            kalimat = kalimat + kal[i]
    print(kalimat)
sisip()