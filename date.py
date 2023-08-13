def number_to_date(number):
    if 1>number or number>365:
        print("number should be between 1 and 365")
    
    month_lentgh=[31,31,31,31,31,31,30,30,30,30,30,29]
    month_name=["farvrdin", "ordibehasht", "khordad", "tir"," mordad", "shahrivar",
        "mehr", "aban","azar", "dey", "bahman", "esfand"]
    month=0
    while(number>month_lentgh[month]):
        number-=month_lentgh[month]
        month+=1
    return f"{number} e {month_name[month]}"
input_number=int(input("enter a number:"))
print(number_to_date(input_number))