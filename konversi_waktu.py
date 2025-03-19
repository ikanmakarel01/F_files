def konversi_waktu(jam,menit,format_24):
    if format_24 == True:
        return f"0{jam}:{menit}" if jam < 10 else f"{jam}:{menit}"
    elif format_24 == False:
        if jam == 0:
            jam = 12
            return f"{jam}:{menit} AM"
        elif jam == 12:
            return f"{jam}:{menit} PM"
        elif jam > 12:
            jam = jam - 12
            return f"{jam}:0{menit} PM" if jam < 10 else f"{jam}:{menit} PM"
        elif jam < 12:
            return f"{jam}:0{menit} AM" if jam < 10 else f"{jam}:{menit} AM"
        
print(konversi_waktu(0,30,False))
print(konversi_waktu(13,30,False))
print(konversi_waktu(12,30,True))
print(konversi_waktu(9,5,True))