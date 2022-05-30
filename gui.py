#Variabler
#En lista som loggar transaktioner
#Namnet på filen som transaktionerna lagras i
transactions = []                   
filename = "transaktioner.txt"     


#Beräknar saldo på ditt konto
def saldo():
    saldo = 0 
    for t in transactions:
        saldo += t
    return saldo


#Skriver ned alla transaktioner
def print_transactions():   
    line = 0
    summa = 0
    output = ("\n<=>   Transaktioner   <=>"
              "\n{:>3} {:>12} {:>12}"
              "\n≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖").format("Nr", "Händelse", "Saldo")
    for t in transactions:
        line += 1
        summa += t
        output += ("\n{:>2}. {:>9} kr {:>9} kr".format(line, t, summa))
    
    return output

def validate_int(output, error_mess):
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error_mess)
    return value

#Den kollar så att filen är tillgänglig 
#Finns den ingen så skapas det en ny
def check_file_exists():
    try:
        with open(filename, "x"):
            print("Filen har skapats")

        with open(filename, "a") as f:
            f.write("{}\n".format(500))
    except:
        return

#Den läser upp filens innerhåll
def read_file():
    check_file_exists()

    with open(filename) as f:
        for rad in f:
            if len(rad) > 0:
                add_transaction(int(rad))
            
#Lagrar transaktioner till en lista
def add_transaction(transaction, toFile = False):
    transactions.append(transaction)
    if toFile:
        write_transaction_to_file(transaction)

#Skriver transaktionen till filen
def write_transaction_to_file(transaction):
    with open(filename, "a") as f:
        f.write("{}\n".format(transaction))

read_file()
#Programloop
while True:     
#Bank menyn som visas
    meny = (f"\n≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖\n"
            "\n           ▶ Bank of SWED ◀"
            "\n\n≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖"
            "\n<=> 1. Redovisa Saldo             <=>"
            "\n<=> 2. Insättning                 <=>"
            "\n<=> 3. Uttag                      <=>"
            "\n<=> 0. Avsluta/Stoppa programmet  <=>"
            "\n\n≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖"
            "\n<=> Gör ditt val:                 <=>\n\n"
            "").format(saldo())


    välj = validate_int(meny, "Felaktig Inmatning!")
#Avslutar/Stoppar programmet
    if välj == 0:              
        break
#Visar Transaktioner
    elif välj == 1:             
        print(print_transactions())
#Sätter in pengar
    elif välj == 2:             
        print("<=>   Insättning   <=>")
        insättning = int(input("<=>  Ange Belopp:  <=>"))
        if insättning > 0:
            add_transaction(insättning, True)
        else:
            print(" Insättningen måste vara större än 0! ")
#Gör ditt Uttag
    elif välj == 3:             
        print("<=>     Uttag     <=>")
        uttag = int(input("<=>  Ange Belopp:  <=>"))
        if uttag <= saldo() and uttag >= 0:
            add_transaction(-uttag, True)
        elif uttag < 0:
            print(" Uttaget måste vara större än 0! ")
        else:
            print(" Beloppet får inte vara större än saldo! ")


    else:
        print("<=>  Felaktigt val!  <=>")

print("\nTack för ditt besök, välkommen åter!")
