from tkinter import*
from tkinter import messagebox


#create a function for clean the data

def clearall():

    dayField.delete(0,END)
    monthField.delete(0,END)
    yearField.delete(0,END)
    givendayField.delete(0,END)
    givenmonthField.delete(0,END)
    givenyearField.delete(0,END)
    rsltyearsField.delete(0,END)
    rsltmonthField.delete(0,END)
    rsltdaysField.delete(0,END)

# create a function for checking the error


def CheckError():
    if(dayField.get()=="" or monthField.get()=='' or yearField.get()=="" or givendayField.get()=="" or
    givenmonthField.get()=="" or givenyearField.get()==""):

      messagebox.showerror("Input Error")
      clearall()
      return -1
    # calculating the age
def calculateAge():

    value=CheckError()
    if value==-1:
        return

    else:
        birth_day=int(dayField.get())
        birth_month=int(monthField.get())
        birth_year=int(yearField.get())

        given_day=int(givendayField.get())
        given_month=int(givenmonthField.get())
        given_year=int(givenyearField.get())

        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if(birth_day>given_day):
            given_month=given_month-1
            given_day=given_day+month[birth_month-1]

            #if birth month exceeds given month, then
            #  donot count this year and add 12 to the
            # month so that we can subtract and find out
            # the difference

        if(birth_month>given_month):
            given_year = given_year - 1
            given_month = given_month + 12


        calculate_day=given_day-birth_day
        calculate_month=given_month-birth_month
        calculate_year=given_year-birth_year

        rsltdaysField.insert(10, str(calculate_day))
        rsltmonthField.insert(10, str(calculate_month))
        rsltyearsField.insert(10, str(calculate_year))


#drive code
if __name__ == '__main__':

    root=Tk()
    root.title("Age calculator")
    root.configure(bg="seagreen")
    root.geometry('524x260')
    root.resizable(True,True)

# create a date of birth
    dob=Label(root,text="Date Of Birth",bg="blue")
    day=Label(root,text="Day",bg='seagreen')
    month=Label(root,text='Month',bg='seagreen')
    year=Label(root,text='Year',bg='seagreen')

# create a given date
    givendate=Label(root,text="Given Date",bg='blue')
    givenday=Label(root,text='Given Day',bg='seagreen')
    givenmonth=Label(root,text='Given Month',bg='seagreen')
    givenyear=Label(root,text='Given Year',bg='seagreen')

# create a result label
    rsltyears=Label(root,text='Years',bg='seagreen')
    rsltmonth=Label(root,text='Months',bg='seagreen')
    rsltdays=Label(root,text='Days',bg='seagreen')

#create a resultant label

    rsltage=Button(root,text='Resultant Ages',bg='red',command=calculateAge)
    rsltclearall=Button(root,text='Clearall',bg='red',command=clearall)

    # Create a text entry box for filling or typing the information.
    dayField=Entry(root)
    monthField=Entry(root)
    yearField=Entry(root)

    givendayField=Entry(root)
    givenmonthField=Entry(root)
    givenyearField=Entry(root)

    rsltdaysField=Entry(root)
    rsltmonthField=Entry(root)
    rsltyearsField=Entry(root)


# grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    dob.grid(row=0,column=1)

    day.grid(row=1,column=0)
    dayField.grid(row=1, column=1)
    month.grid(row=2,column=0)
    monthField.grid(row=2, column=1)
    year.grid(row=3,column=0)
    yearField.grid(row=3,column=1)

    givendate.grid(row=0,column=4)
    givenday.grid(row=1,column=3)
    givendayField.grid(row=1,column=4)

    givenmonth.grid(row=2,column=3)
    givenmonthField.grid(row=2, column=4)
    givenyear.grid(row=3,column=3)
    givenyearField.grid(row=3, column=4)


    rsltage.grid(row=4,column=2)
    rsltyears.grid(row=5,column=2)
    rsltyearsField.grid(row=6, column=2)

    rsltmonth.grid(row=7,column=2)
    rsltmonthField.grid(row=8, column=2)

    rsltdays.grid(row=9,column=2)
    rsltdaysField.grid(row=10, column=2)
    rsltclearall.grid(row=12,column=2)

    root.mainloop()
    