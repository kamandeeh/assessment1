print("""
SIM 2
1. Safaricom+
2. M-PESA
""")
choice1 = int(input("Enter your choice [1-2]: "))
def safaricom():
    print("""
    SIM 2
1. M-Banking services
2. My Account
""")
    
def m_pesa():
    print("""
    SIM 2
1. Send Money
2. Withdraw Cash
3. Buy Airtime
4. Lipa na M-PESA
""")
if choice1 == 1:
    safaricom()
elif choice1 == 2:
    m_pesa()
# fisrt choice option when the M-PESA menu / option is clicked
mpesa_choice = int(input("Enter your choice [1-4]: "))
# send money function
def send_money():
    print("""
    Send Money
    """)
    return int(input("Enter Phone no: ")) and int(input("Enter Amount: ")) and int(input("Enter Pin: ")) and print("Money Sent!")
# withdraw cash function
def with_draw_cash():
    print("""
    Withdraw Cash
    """)
    return int(input("Enter Amount: ")) and int(input("Enter Pin: ")) and int(input("confirm Pin: ")) and print("Withdraw  was Successful!")
# buy airtime function
def buy_airtime():
    print("""
    Buy Airtime
1. My Number
2. Other Number
    """)
# Lipa Na Mpesa function
def lipa_na_mpesa():
    print("""
    Lipa Na M-Pesa
1. Paybill
2. Buy Goods and Services
3. Pochi La Biashara
    """)
# conditional statements to determine the output depending on the user's choice
if mpesa_choice == 1:
    send_money()
elif mpesa_choice == 2:
    with_draw_cash()
elif mpesa_choice == 3:
    buy_airtime()
    buy_airtime_choice = int(input("Enter your choice [1-2]: ")) 
elif mpesa_choice == 4:     
    lipa_na_mpesa() 
    lipa_na_mpesa_choice = int(input("Enter your choice [1-3]: ")) 
# my number function if the user is buying airtime for their own number.
def my_number():
    print("""
    My Number
    """)
    return int(input("Enter Amount: ")) and int(input("Enter Pin: ")) and print("Airtime Bought!")
# other number function if the user is buying airtime for another number.
def other_number():
    print("""
    Other Number
    """)
    return int(input("Enter Phone no: ")) and int(input("Enter Amount: ")) and int(input("Enter Pin: ")) and print("Airtime Bought!")
# conditional statement to decide which function is called depending on the user's choice.
if mpesa_choice == 3:
    if buy_airtime_choice == 1:
        my_number()
    elif buy_airtime_choice == 2:
        other_number()
def pay_bill():
    print("""
    Paybill
1. Search Contact From Sim 
2. Enter Business Number
    """)
def buy_goods_and_services():
    print("""
    Buy Good and Services
    """)    
    return int(input("Enter Till: ")) and str(input("Enter Account Number: ")) and int(input("Enter Amount: ")) and int(input("Enter Pin: ")) and print("Payment Successful!")
def pochi_la_biashara():
    print("""
    Pochi la biashara
    """)        
    return int(input("Enter Phone Number: ")) and int(input("Enter Amount: ")) and int(input("Enter Pin: ")) and print("Money Sent!")
# Conditional statement to decide which function is called depending on the user's choice.
if mpesa_choice == 4:
    if lipa_na_mpesa_choice == 1:
        pay_bill()
        pay_bill_choice = int(input("Enter your choice [1-2]: "))
    elif lipa_na_mpesa_choice == 2:
        buy_goods_and_services()
    elif lipa_na_mpesa_choice == 3:
        pochi_la_biashara()
def search_from_sim():
    print("""
    Search Contact From Sim
    """)
    return str(input("Enter Contact Name: ")) and int(input("Enter Account Number: ")) and int(input("Enter Amount: ")) and int(input("Enter Pin: ")) and print("Payment Successful!")
def enter_business_number():
    print("""
    Enter Business Number
    """)
    return int(input("Enter Business Number: ")) and int(input("Enter Account Number: ")) and int(input("Enter Amount: ")) and int(input("Enter Pin: ")) and print("Payment Successful!")
# Conditional statement to decide which function is called depending on the user's choice.
if mpesa_choice == 4 and lipa_na_mpesa_choice == 1:
    if pay_bill_choice == 1:
        search_from_sim()
    elif pay_bill_choice == 2:
        enter_business_number()