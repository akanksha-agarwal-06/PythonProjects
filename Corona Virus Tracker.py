from tkinter import *
import json
import requests

root = Tk()

root.title("Corona Virus Tracker")
root.configure(background = "light grey")
root.geometry("1000x700")


api_request = requests.get('https://api.thevirustracker.com/free-api?global=stats')

api = json.loads(api_request.content)

api_country_request = requests.get('https://api.thevirustracker.com/free-api?countryTotals=ALL')

api_country = json.loads(api_country_request.content)



# variables for collecting global counts
total_confirmed = api['results'][0]['total_cases']
new_confirmed = api['results'][0]['total_new_cases_today']
total_deaths = api['results'][0]['total_deaths']
new_deaths = api['results'][0]['total_new_deaths_today']
total_recovered = api['results'][0]['total_recovered']
active_cases = api['results'][0]['total_active_cases']



# Code for populating countries in the dropdown
dicton = api_country['countryitems'][0]
country = []   # list with countirs for populating the dropdown
country_code = {}  # dictionary for populating country along with its key code


for key in dicton:

    if isinstance(api_country['countryitems'][0][key], dict):
        country.append(api_country['countryitems'][0][key]['title'])

        title = api_country['countryitems'][0][key]['title']
        country_code[title] = key


# Selection command to display the country selected on a label
selected = StringVar()
selected.set("Select")


def selection(selected):

    # Updates the country_label to display the name of the country selected from the dropdown menu
    country_label.config(text=selected)


    # Extract the key from the country_code dictionary for fetching other values
    code = country_code[selected]

    infcount_country = api_country['countryitems'][0][code]['total_cases']
    dthcount_country = api_country['countryitems'][0][code]['total_deaths']
    reccount_country = api_country['countryitems'][0][code]['total_recovered']
    actcount_country = api_country['countryitems'][0][code]['total_active_cases']
    newcases_count_country = api_country['countryitems'][0][code]['total_new_cases_today']
    newdth_count_country = api_country['countryitems'][0][code]['total_new_deaths_today']


    # Updating the labels in the Country-wise section
    infcount_country_lbl.config(text=infcount_country)
    dthcount_country_lbl.config(text=dthcount_country)
    reccount_country_lbl.config(text=reccount_country)
    actcount_country_lbl.config(text=actcount_country)
    newcases_count_country_lbl.config(text=newcases_count_country)
    newdth_count_country_lbl.config(text=newdth_count_country)


# Labels for Global Section
global_label = Label(root, text='Global', background='blue', foreground='white', width=85, font=('helvetica',20, 'bold' ))
infected_label = Label(root, text='Infected ', background='light grey', foreground='black', width=15,  font=('helvetica',15,'bold'))
totalcon_label = Label(root, text= str(total_confirmed), background='light grey', foreground='dark orange', width=15, font=('helvetica',25,'bold'))

deaths_label = Label(root, text='Deaths ', background='light grey', foreground='black', width=15, font=('helvetica',15,'bold'))
totaldth_label = Label(root, text=str(total_deaths), background='light grey', foreground='red', width=15, font=('helvetica',25,'bold'))

recovered_label = Label(root, text='Recovered ', background='light grey', foreground='black', width=15, font=('helvetica',15,'bold'))
totalrec_label = Label(root, text=str(total_recovered), background='light grey', foreground='green', width=15, font=('helvetica',25,'bold'))

newcases_label = Label(root, text='New Cases Today ', background='light grey', foreground='black', width=15,  font=('helvetica',15,'bold'))
newcon_label = Label(root, text= str(new_confirmed), background='light grey', foreground='dark orange', width=15, font=('helvetica',25,'bold'))
newdeaths_label = Label(root, text='New Deaths Today ', background='light grey', foreground='black', width=15,  font=('helvetica',15,'bold'))
newdth_label = Label(root, text=str(new_deaths), background='light grey', foreground='red', width=15, font=('helvetica',25,'bold'))
active_cases_label = Label(root, text='Active Cases ', background='light grey', foreground='black', width=15, font=('helvetica',15,'bold'))
country_count_label = Label(root, text= str(active_cases), background='light grey', foreground='purple', width=15, font=('helvetica',25,'bold'))

# Dropdown, button and labels for list of countries
country_label = Label(root, text='Country', background='blue', foreground='white', width=85, font=('helvetica', 20, 'bold'))
dropdown_label = Label(root, text = 'Select a country', background='light grey', foreground='black', font=('helvetica',15,'bold'))
country_dropdown = OptionMenu(root, selected, *country, command=selection)
country_dropdown.config(bg = "grey")
country_dropdown['menu'].config(bg='black')

infected_country_lbl = Label(root, text='Infected ', background='light grey', foreground='black', width=15,  font=('helvetica',15,'bold'))
infcount_country_lbl = Label(root, text=' ', background='light grey', foreground='dark orange', width=15, font=('helvetica',25,'bold'))

deaths_country_lbl = Label(root, text='Deaths ', background='light grey', foreground='black', width=15, font=('helvetica',15,'bold'))
dthcount_country_lbl = Label(root, text=' ', background='light grey', foreground='red', width=15, font=('helvetica',25,'bold'))

recovered_country_lbl = Label(root, text='Recovered ', background='light grey', foreground='black', width=15, font=('helvetica',15,'bold'))
reccount_country_lbl = Label(root, text=' ', background='light grey', foreground='green', width=15, font=('helvetica',25,'bold'))

active_country_lbl = Label(root, text='Active ', background='light grey', foreground='black', width=15, font=('helvetica',15,'bold'))
actcount_country_lbl = Label(root, text=' ', background='light grey', foreground='purple', width=15, font=('helvetica',25,'bold'))

newcases_country_lbl = Label(root, text='New Cases Today ', background='light grey', foreground='black', width=15,  font=('helvetica',15,'bold'))
newcases_count_country_lbl = Label(root, text= ' ', background='light grey', foreground='dark orange', width=15, font=('helvetica',25,'bold'))

newdeaths_country_lbl = Label(root, text='New Deaths Today ', background='light grey', foreground='black', width=15,  font=('helvetica',15,'bold'))
newdth_count_country_lbl = Label(root, text=' ', background='light grey', foreground='red', width=15, font=('helvetica',25,'bold'))



# Grid positions for Global section
global_label.grid(row=0, column=0, columnspan=3, pady=30, ipady=8)
infected_label.grid(row=1, column=0, padx=40)
totalcon_label.grid(row=2, column=0, padx=40, pady=(0,20))
deaths_label.grid(row=1, column=1, padx=40)
totaldth_label.grid(row=2, column=1, padx=40, pady=(0,20))
recovered_label.grid(row=1, column=2, padx=40)
totalrec_label.grid(row=2, column=2, padx=40)
newcases_label.grid(row=3, column=0, padx=40, pady=(20,0))
newdeaths_label.grid(row=3, column=1, padx=40, pady=(20,0))
newcon_label.grid(row=4, column=0, padx=40)
newdth_label.grid(row=4, column=1, padx=40)
active_cases_label.grid(row=3, column=2, padx=40, pady=(20,0))
country_count_label.grid(row=4, column=2, padx=40)
country_label.grid(row=5, column=0, columnspan=3, pady=30, ipady=8)


# Grid positions for Country-wise section
dropdown_label.grid(row=6, column=0)
country_dropdown.grid(row=7, column=0)

infected_country_lbl.grid(row=6, column=1, padx=40)
infcount_country_lbl.grid(row=7, column=1, padx=40, pady=(0,20))
deaths_country_lbl.grid(row=6, column=2, padx=40)
dthcount_country_lbl.grid(row=7, column=2, padx=40, pady=(0,20))
recovered_country_lbl.grid(row=8, column=1, padx=40)
reccount_country_lbl.grid(row=9, column=1, padx=40, pady=(0,20))
active_country_lbl.grid(row=8, column=2, padx=40)
actcount_country_lbl.grid(row=9, column=2, padx=40, pady=(0,20))

newcases_country_lbl.grid(row=10, column=1, padx=40)
newcases_count_country_lbl.grid(row=11, column=1, padx=40)
newdeaths_country_lbl.grid(row=10, column=2, padx=40)
newdth_count_country_lbl.grid(row=11, column=2, padx=40)





root = mainloop()
