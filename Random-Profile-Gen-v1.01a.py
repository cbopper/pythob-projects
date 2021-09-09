from tkinter import *
import random as r

def randomAge():
    rand = r.randint(18,95)
    rand1 = int
    if rand >= 70:
        rand1 = r.randint(18,95)
    else:
        rand1 = rand
    return rand1


def randomJob():
    jobs = ['Archeologist', 'Blacksmith', 'Gamekeeper',  'Solicitor', 'Travel Agent', 'Baggage Handler', 'Sales Associate', 'Human Resorces', 'Engineering Manager', 
        'Editor', 'Butcher', 'Librarian', 'Software Consultant', 'Bank Clerk', 'Researcher', 'Marine Biologist', 'Manicurist', 'Funeral Director', 'Taxi Driver', 
        'Delivery Driver', 'Bus Driver', 'Farmer', 'Fitness Instructor', 'Interior Designer', 'Civil Engineer', 'Locksmith']
    total_jobs = len(jobs) - 1
    r_job = jobs[r.randint(0,total_jobs)]
    return r_job

def randomName():
    first_names = ['Sandra', 'Claire', 'Tim', 'George', 'Rowena', ' Delia', 'Kathleen', 'Porfirio', 'Dianna', 'Dorthy', 'Brianna', 'Estela', 'Joy', 'Paulette',
     'Bridgett', 'Allen', 'Elvira', 'Terrel', 'Benjamin', 'Debbie', 'Lorenzo', 'Kelly', 'Moses', 'Harvey', 'Raphael', 'Karl', 'Cheyenne', 'Miranda', 'Essie', 'Adeline']

    last_names = ['Diaz', 'Luna', 'Wells', 'Lowery', 'Cobb', 'Osborne', 'Moore', 'Gillespie', 'Nicholson', 'Petty', 'Kirby', 'Rush', 'Allison', 'Robles', 'Scott',
     'Jones', 'Johns', 'Berger', 'Parsons', 'Sutton', 'Baldwin', 'Cox', 'Peterson', 'Wyatt', 'Buckley', ' Clements', 'Fraizer', 'Bradford', 'Cummings', 'Warner']

    
    r_firstname = first_names[r.randint(0,29)]
    r_lastname = last_names[r.randint(0,29)]
    r_name = r_firstname+" "+r_lastname
    return r_name
     
def newPerson2():
    screen1.destroy()
    newPerson()

def savePerson():
    print("Save Person")

def newPerson():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("300x300")

    name = randomName()
    age = randomAge()
    job = randomJob()

    Label(screen1,text="").pack()
    Label(screen1,text="You are currently on").pack()
    Label(screen1, text=name+"\'s page",font=("calibri", 13)).pack()
    Label(screen1,text="").pack()
    Label(screen1,text="They are " +str(age)+" years old.",font=("calibri", 13)).pack()
    Label(screen1,text="").pack()
    Label(screen1,text="They work as a ").pack()
    Label(screen1, text=job,font=("calibri", 13)).pack()
    Label(screen1,text="").pack()
    Button(screen1, text="Save", command=savePerson).pack()
    Label(screen1,text="").pack()
    Button(screen1, text="New Person", command=newPerson2).pack()






    


def main():
    global screen
    screen = Tk()
    screen.title("Main")
    screen.geometry("300x300")

    Label(screen,text="Welcome to dating profile generator!", width="300",height="3",font=("calibri",13)).pack()

    Button(screen, text="New Person", command=newPerson).pack()

    screen.mainloop()

main()
