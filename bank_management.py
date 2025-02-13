######Bank Server
import mysql.connector
db=mysql.connector.connect(host='localhost', user='root',password='password',database='Bank_Management_system')
cur=db.cursor()

def bank(name,server,amount,acc_no):
    press=int(input('Press 1 for debit\nPress 2 for credit\nPress 3 to check bank bal\nPress 4 to deactivate bank acc\nPress: '))
    if press==1:
        dr=int(input('how much you want to debit: '))
        if dr>amount:
            print('Balance is exhuasted')
        elif dr<=amount:
            amount-=dr
            cur.execute('update user set amount =%s where acc_no = %s',(amount,acc_no))
            db.commit()
            print(f'Money has been debited by {dr} from your bank, balance amount {amount}')
        server[acc_no]['Amount']=amount
        back=int(input("Press 1 for back\nPress 2 for exit bank\n Press here: "))
        if back == 1:
            return bank(name,server,amount,acc_no)
        else:
            print('Thanks for the visit')
            return manager(name,server,amount,acc_no)

    elif press==2:
        cr=int(input('how much you want to Credit: '))
        amount+=cr
        cur.execute('update user set amount =%s where acc_no = %s',(amount,acc_no))
        db.commit()
        print(f'Money has been Credited by {cr} in your bank, balance amount {amount}')
        server[acc_no]['Amount']=amount
        back=int(input("Press 1 for back\nPress 2 for exit bank\nPress here: "))
        if back == 1:
            return bank(name,server,amount,acc_no)
        else:
            print('Thanks for the visit')
            manager(name,server,amount,acc_no)
    elif press==3:
        print(f'Here is your Balance {amount}')
        print(server)
        back=int(input("Press 1 for back\nPress 2 for exit bank\nPress here: "))
        if back == 1:
            return bank(name,server,amount,acc_no)
        else:
            print('Thanks for the visit')
            manager(name,server,amount,acc_no)
    elif press==4:
        config=input('Are you sure want to deactivate your acc if yes right "Yes" otherwise "No"\n').lower().strip()
        if config=='yes':
            if acc_no in server:
                cur.execute('delete from user where acc_no=%s',(acc_no,))
                db.commit()
                del server[acc_no]
                print('Your acc deactivate successfull')
                manager(name,server,amount,acc_no)
    else:
        print('Incorrect output try again')
        return bank(name,server,amount,acc_no)


def opening(name,server,amount,acc_no):
    print('Please fill the below form to open an acc')
    phone_no=int(input('Enter your phone no: '))
    amount=int(input('Deposit a min amount to open a acc: '))
    import random
    acc_no=random.randint(1000,9999)
    cur.execute('insert into user (acc_no,phone_no,amount,name) values(%s,%s,%s,%s)',(acc_no,phone_no,amount,name))
    db.commit()
    print(f'Hi {name}, your acc no is {acc_no} and balance is {amount}')
    server[acc_no]={'Name':name, 'Amount':amount}
    print('Congratulation for successfull opening\nTry some new feature')
    return bank(name,server,amount,acc_no)

# after every customer entry we going to ask the bank manager to attend more customer 
def manager(name,server,amount,acc_no):
    ask=input("Do you want to attend more customer\n").lower().strip()
    if ask=='yes':
        system(name,server,amount,acc_no)
    else:
        print(server)
    


def system(name,server,amount,acc_no):
    name = input('Enter your name:')
    print(f'Hi {name}, Welcome to Bank of chandigarh')
    customer=int(input('Press 1 if your an existing customer\nPress 2 if you are new\nPress here: '))
    if customer==1:
        acc_no = int(input("Enter your acc no of four digit\n"))
        cur.execute('select acc_no, name, amount from user where acc_no=%s',(acc_no,))
        data=cur.fetchone()  
        if data:
            acc_no,name,amount=data
            server[acc_no]={'Name':name,'Amount':amount}
            bank(name,server,amount,acc_no)
        else:
            print('You do not have an existing acc')
            opening(name,server,amount,acc_no)

    else:
        opening(name,server,amount,acc_no)

name=''
server={}
amount=0
acc_no=int()

system(name,server,amount,acc_no)

