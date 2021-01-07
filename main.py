import requests
import bs4
import tkinter as tk

def get_html_data(url):
    data=requests.get(url)
    return data

def get_covid_data():
    url="https://www.worldometers.info/coronavirus/"
    html_data=get_html_data(url)
    bs=bs4.BeautifulSoup(html_data.text,'html.parser')
    info_div = bs.find("div",class_="content-inner").findAll("div",id="maincounter-wrap")
    all_data=""

    for block in info_div:
        text=block.find("h1",class_=None).get_text()

        count=block.find("span",class_=None).get_text()

        all_data=all_data+text+" "+count+"\n"

    return all_data


def get_country_data():
    name=textfield.get()
    url="https://www.worldometers.info/coronavirus/country/"+name
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = ""

    for block in info_div:
        text = block.find("h1", class_=None).get_text()

        count = block.find("span", class_=None).get_text()

        all_data = all_data + text + " " + count + "\n"

    mainlabel['text']=all_data



def reload():
    new_data=get_covid_data()
    mainlabel['text']=new_data

get_covid_data()


#gui making


root=tk.Tk()

root.geometry("900x700")
root.title("COVID TRACKER")
f=("poopins",25,"bold")

banner=tk.PhotoImage(file="covid.png")
bannerlabel=tk.Label(root,image=banner)
bannerlabel.pack()

textfield=tk.Entry(root,width=50)
textfield.pack()

mainlabel=tk.Label(root,text=get_covid_data(),font=f)
mainlabel.pack()

gbtn=tk.Button(root,text="Get Data",font=f,relief='solid',command=get_country_data)
gbtn.pack()

rbtn=tk.Button(root,text="Relaod",font=f,relief='solid',command=reload)
rbtn.pack()

root.mainloop()


