import math
import customtkinter

#calculate time in months to pay of debt
def calc():
    #output calculations
    app = customtkinter.CTk()
    app.geometry("500x350")
    app.title("Calculations")

    frame2 = customtkinter.CTkFrame(master=app)
    frame2.pack(pady=20, padx=60, fill="both", expand=True)

    bold_font = customtkinter.CTkFont(family="Helvetica", size=12, weight="bold")
    bold_font2 = customtkinter.CTkFont(family="Helvetica", size=15, weight="bold")

    paymentPerMonth = int(mPEntry.get())
    debt = int(debtEntry.get())
    temp = paymentPerMonth
    mIAddOne = changeToYearly()

    headT = (f"At a debt of ${debt} with an annual interest of {round(yearlyInterest * 100, 3)}%")
    head = customtkinter.CTkLabel(master=frame2, text=headT, font=bold_font2)
    head.pack(pady=12, padx=10)
    for i in range(round(paymentPerMonth*0.1), round(paymentPerMonth*2.4), round(paymentPerMonth*0.1)):
        paymentPerMonth = int(i)
        base = (-paymentPerMonth/((monthlyInterest*debt)-paymentPerMonth))
        if base <= 1:
            failT = (f"With ${paymentPerMonth} per month you would never pay off the debt!")
            fail = customtkinter.CTkLabel(master=frame2, text=failT, font=("Helvetica", 12))
            fail.pack(pady=2, padx=10)

        else:
            numberOfMonths = math.log(base, mIAddOne)
            numberOfYears = numberOfMonths // 12
            leftOverMonths = numberOfMonths % 12
            totalPaid = numberOfMonths * paymentPerMonth
            if totalPaid > 1000:
                totalPaid = round(totalPaid, -2)
            profit = totalPaid - debt
            if profit > 1000:
                profit = round(profit, -2)
            timeT = (f"With ${paymentPerMonth} per month it would take {round(numberOfYears)} years and {round(leftOverMonths + 0.5)} months! (That's ${paymentPerMonth * 12} per year) In total you paid ${round(totalPaid, 2)} and the bank made a profit of ${round(profit, 2)}!")
            if i == temp:
                time = customtkinter.CTkLabel(master=frame2, text=timeT, font=bold_font)
                time.pack(pady=6, padx=10)
            else:
                time = customtkinter.CTkLabel(master=frame2, text=timeT, font=("Helvetica", 12))
                time.pack(pady=6, padx=10)
    app.mainloop()


#differentiatie between what the user has input
def changeToYearly():
    global monthlyInterest
    global yearlyInterest
    someInterest = float(sIEntry.get())
    if yearlyInputTrue.get() == 1:
        yearlyInterest = someInterest
        monthlyInterest = ((yearlyInterest+1) ** (1/12)) - 1
    else:
        monthlyInterest = someInterest
        yearlyInterest = (1+monthlyInterest)**12 - 1
    mIAddOne = monthlyInterest + 1
    return mIAddOne


#GUI 
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Debt Calculator")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

debtEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Debt: ", font=("Helvetica", 12))
debtEntry.pack(pady=12, padx=10)

mPEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Montly Payment: ", font=("Helvetica", 12))
mPEntry.pack(pady=12, padx=10)

helpLabel = customtkinter.CTkLabel(master=frame, text="Note: When entering percentage have it between 0-1 e.g 8.69% ---> 0.0869", font=("Helvetica", 10))
helpLabel.pack(pady=12, padx=10)

sIEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Montly Interest Rate: ", font=("Helvetica", 12))
sIEntry.pack(pady=12, padx=10)

yearlyInputTrue = customtkinter.IntVar()
checkbox = customtkinter.CTkCheckBox(master=frame, text="Tick if you are inputting yearly interest instead", variable=yearlyInputTrue, command=changeToYearly, font=("Helvetica", 10))
checkbox.pack(pady=20)

button = customtkinter.CTkButton(master=frame, text="CALCULATE", command=calc)
button.pack(pady=12, padx=10)

root.mainloop()