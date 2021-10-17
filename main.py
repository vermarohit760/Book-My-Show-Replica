class user:
    seat_list=[]
    user_dict={}
    def __init__(self,key_dict,row_number,col_number,name,gender,age,ticket_price,phone_number):
        self.name=name
        self.gender=gender
        self.age=age
        self.ticket_price=ticket_price
        self.phone_number=phone_number
        user.seat_list.append((row_number,col_number))
        user.user_dict[key_dict]={}
        user.user_dict[key_dict]['name']=name
        user.user_dict[key_dict]['gender']=gender
        user.user_dict[key_dict]['age']=age
        user.user_dict[key_dict]['ticket price']=ticket_price
        user.user_dict[key_dict]['phone number']=phone_number
        

def options():
    while True:
        try:
            print('1. show the seats')
            print('2. buy a ticket')
            print('3. statistics')
            print('4. show booked ticked user info')
            print('0. exit')
            print('--> Please select one option from 1,2,3,4,0 ')
            n=int(input())
            if n==1:
                show_the_seats(row,col)
            elif n==2:
                buy_a_ticket()
            elif n==3:
                statistics()
            elif n==4:
                booked_ticket_user_info()
            elif n==0:
                print('Thank you for using BOOK MY SHOW,We hope you will enjoy the show...... Please visit again!!')
                break
            assert n>=0 and n<=4
        except:
            print('Something went wrong!!!! Please enter the valid option from 1,2,3,4,0')
    
def show_the_seats(row,col):
    print('---------------------------------------------------------------------')
    w=len(str(row))
    for i in range(1,col+1):
        if i==1:
            print(str(i).rjust(2*w+3,' '),end='')
        else:
            print(str(i).rjust(w+2,' '),end='')
    print()
    for j in range(1,row+1):
        print(str(j).rjust(w,' '),end=' ')
        for k in range(1,col+1):
            if (j,k) in user.seat_list:
                print('B'.rjust(w+2,' '),end='')
            else:
                print('S'.rjust(w+2,' '),end='')
        print()
    print('--------------------------------------------------------------------')

def ticket_price(user_row):
    price=0
    if row*col>60:
        if row%2==0:
            middle_of_row=row//2
            if user_row<=middle_of_row:
                price=10
            else:
                price=8
        else:
            middle_of_row=(row-1)//2
            if user_row<=middle_of_row:
                price=10
            else:
                price=8
    else:
        price=10
    return price

def total_income():
    total=0
    if row*col>60:
        if row%2==0:
            middle_of_row=row//2
            for c in range(1,row+1):
                if c<=middle_of_row:
                    total=total+(col*10)
                else:
                    total=total+(col*8)
        else:
            middle_of_row=(row-1)//2
            for c in range(1,row+1):
                if c<=middle_of_row:
                    total=total+(col*10)
                else:
                    total=total+(col*8)
    else:
        total=row*col*10
    return total
            
def buy_a_ticket():
    global current_income
    print('------------------------------------------------------------------------')
    while True:
        print('---->Enter the row to be book (from 1 to ',row,')')
        while True:
            try:
                a=int(input())
                assert a>=1 and a<=row
                break
            except:
                print('Something went wrong!!! Enter the valid row from 1 to ',row)
        print('---->Enter the column to be book (from 1 to ',col,')')
        while True:
            try:
                b=int(input())
                assert b>=1 and b<=col
                break
            except:
                print('Something went wrong!!! Enter the valid row from 1 to ',col)
        if (a,b) in user.seat_list:
            print('This seat is already booked ')
        else:
            break
    current_price=ticket_price(a)
    print('---->Price of the ticket is :-',current_price,'$')
    while True:
        print("---->If you want to book ticket select 1. Yes otherwise select 2. for No")
        print('1. Yes')
        print('2. No')
        try:
            user_input=int(input())
            if user_input==1:
                print("---->Enter the name:")
                name=input()
                print('---->Enter the gender:')
                while True:
                    print('* M')
                    print('* F')
                    print('* T')
                    gender=input()
                    gender_list=['m','M','f','F','t','T']
                    if gender in gender_list:
                        break
                    else:
                        print('--> Please enter the valid gender :')
                print('---->Enter the age:')
                while True:
                    try:
                        age=int(input())
                        break
                    except:
                        print('-->Something went wrong!!! Please enter the valid age:')
                print('---->Enter the phone number:')
                while True:
                    try:
                        phone_number=int(input())
                        break
                    except:
                        print('-->Something went wrong!!! Please enter the valid phone number:')
                print()
                print('*****Hurray!!! Your ticket Booked Successfully*****')
                combo_of_row_col=str(a)+str(b)
                user_object=user(combo_of_row_col,a,b,name,gender,age,current_price,phone_number)
                current_income=current_income+current_price
                print('------------------------------------------------------------------------')
                break
            elif user_input==2:
                break
            else:
                print('->something went wrong!!! Enter the valid option from 1 or 2')
                    
        except:
            print('->something went wrong!!!  Enter the valid number')
        
def statistics():
    print('------------------------------------------------------------------------')
    print("1. Number of purchased ticket   :  ",len(user.seat_list))
    print('2. Percentage of tickets booked :  ',((len(user.seat_list)*100)/(row*col)),'%')
    print('3. Current income               :  ',current_income,'$')
    print('4. Total income                 :  ',total_income(),'$')
    print('------------------------------------------------------------------------')
    
def booked_ticket_user_info():
    print('------------------------------------------------------------------------')
    print('---->Enter the row to get user info (from 1 to ',row,')')
    while True:
        try:
            p=int(input())
            assert p>=1 and p<=row
            break
        except:
            print('Something went wrong!!! Enter the valid row from 1 to ',row)
    print('---->Enter the column to get user info (from 1 to ',col,')')
    while True:
        try:
            q=int(input())
            assert q>=1 and q<=col
            break
        except:
            print('Something went wrong!!! Enter the valid row from 1 to ',col)
    if (p,q) in user.seat_list:
        h=str(p)+str(q)
        print("Name         : ",user.user_dict[h]['name'])
        print('Gender       : ',user.user_dict[h]['gender'])
        print('Age          : ',user.user_dict[h]['age'])
        print('Ticket Price : ',user.user_dict[h]['ticket price'],'$')
        print('Phone Number : ',user.user_dict[h]['phone number'])
    else:
        print('=> This seat is vacant')
    print('-----------------------------------------------------------------------')   
current_income=0
print('---->Enter the number of row in Cinemahall :- ')
while True:
    try:
        row=int(input())
        break
    except:
        print('-->Something went wrong!! Please enter the valid row in cinemahall. The value must be integer type :')
print("---->Enter the number of column in Cinemahall :- ")
while True:
    try:
        col=int(input())
        break
    except:
        print('-->Something went wrong!! Please enter the valid column in cinemahall. The value must be integer type :')
while True:
        options()
        break