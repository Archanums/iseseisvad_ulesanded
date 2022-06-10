from tkinter import *


def save_info():
    firstname_info = firstname.get() #võtab eesnime
    lastname_info = lastname.get() #Võtab perekonna nime
    age_info = age.get()  #võtab vanuse
    age_info = str(age_info)   #vanuse info
    print(firstname_info, lastname_info, age_info)   #prindib nime ja vanuse

    file = open("user.txt", "w")  #avab usertxt faili
    file.write(firstname_info) #kirjutab faili eesnime
    file.write(lastname_info) #kirjutab faili perekonnanime
    file.write(age_info) #kirjutab faili vanus
    file.close()  #fail kinni
    print(" User ", firstname_info, " has been registered successfully")  #prindib et eesnime info on registreeritud edukalt

    firstname_entry.delete(0, END)  #kustutab sisestatud eesnime
    lastname_entry.delete(0, END) #kustutab sisestatud perekonnanime
    age_entry.delete(0, END) #kustutab sisestatud vanuse


screen = Tk()
screen.geometry("500x500")  #ekraani suuruseks paneb 500
screen.title("Python Form")  #paneb ekraanile nime
heading = Label(text="Python Form", bg="grey", fg="black", width="500", height="3") #kirja värv
heading.pack() #pakime ekraanile

firstname_text = Label(text="Firstname * ", ) #eesnimi ekraanile
lastname_text = Label(text="Lastname * ", ) #perekonna nime kysimine ekraanile
age_text = Label(text="Age * ", ) # avanuse kusimine ekraanile
firstname_text.place(x=15, y=70) # eesnime kysimise asukoht
lastname_text.place(x=15, y=140) # perekonnanime kysimise asukoht
age_text.place(x=15, y=210) #vanuse kysimise asukoht

firstname = StringVar() #eesnime string
lastname = StringVar() #perekonnanime string
age = IntVar() #vanuse int

firstname_entry = Entry(textvariable=firstname, width="30") #eesnime sisestamine
lastname_entry = Entry(textvariable=lastname, width="30") #perekonnanime sisestamine
age_entry = Entry(textvariable=age, width="30") #vanuse sisestamine

firstname_entry.place(x=15, y=100) # eesnime sisestus koht
lastname_entry.place(x=15, y=180) # perekonnanime sisestus koht
age_entry.place(x=15, y=240) #vanuse sisestus koht

register = Button(screen, text="Register", width="30", height="2", command=save_info, bg="grey") # registreerimis nupu suurs
register.place(x=15, y=290) #registreerimis nupu koht

screen.mainloop() # paneb loopi