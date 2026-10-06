
from tkinter import*
from tkinter import ttk

import requests
import time
import jdatetime
import time
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

class myclass:
    def __init__ (self):
        self.flag=0
        self.sun_id = None
        self.cloud_id = None
        self.rain_id = None
        self.wind_id=None
        self.root=Tk()
        self.root.title("weather")
        self.root.geometry("403x721+550+20")
        self.root.resizable(False,False)

        
        #canvas
        self.canvas=Canvas(self.root,width=408 ,height=725 ,highlightthickness=0)
        self.canvas.pack()

        
       #background photo by canvas
        #self.img1=PhotoImage(file="79.png")
        self.img1=PhotoImage(file="8.png")
        self.canvas.create_image(0,0,image=self.img1 ,anchor="nw")
        self.t1_id=self.canvas.create_text(95,99,text="Weather Status",fill="dark blue"
                                           ,font=("B Nazanin", 10, "bold"))
        self.canvas.tag_bind(self.t1_id ,"<Button-1>", self.weather )
        self.canvas.tag_bind(self.t1_id ,"<Enter>", self.enter )
        self.canvas.tag_bind(self.t1_id ,"<Leave>", self.leave )
        
        self.t2_id=self.canvas.create_text(335,309 ,text="Temp Chart",fill="dark blue"
                                           ,font=("B Nazanin", 9, "bold"))
        
        self.canvas.tag_bind(self.t2_id ,"<Button-1>", self.plot )
        self.canvas.tag_bind(self.t2_id ,"<Enter>", self.enter1 )
        self.canvas.tag_bind(self.t2_id ,"<Leave>", self.leave1 )
        #text
        self.canvas.create_text(110,38,text="Choose your city:" ,
                                fill="dark blue",font=("B Nazanin", 16))
        self.canvas.create_text(85,420,text="Prices:" ,
                                fill="dark blue",font=("B Nazanin", 16))
        #combobox
        self.combo1=ttk.Combobox(self.root ,width=15 , justify="left")
        self.combo1.pack()
        self.combo1.place(x=250 ,y=90)
        self.combo1["values"] = ("Tabriz", "Urmia", "Ardabil", "Isfahan", "Karaj", "Ilam",
                         "Bushehr", "Tehran", "Shahr-e Kord", "Birjand", "Mashhad",
                         "Bojnord", "Ahwaz", "Zanjan", "Semnan", "Shiraz", "Qazvin",
                         "Qom", "Gorgan", "Sanandaj", "Rasht", "Khorramabad", "Sari",
                         "Arak", "Bandar Abbas", "Hamadan", "Yasuj", "Kerman",
                         "Kermanshah", "Yazd")
        self.combo1.set("Tehran")
        
         #time
        self.time_id = self.canvas.create_text(80, 685, text="", fill="black", font=("Segoe UI", 12))
        self.date_id = self.canvas.create_text(80, 705, text="", fill="black", font=("Segoe UI", 12))
        self.update_clock()
        
        #dollar
        
        url="https://api.navasan.tech/latest/?api_key="YOUR_REAL_API_KEY"
        response = requests.get(url ,timeout=25)
        print(response.status_code)
        print(response.text)
        data = response.json()

        
        #print (data)
        dollar=data["usd_sell"]["value"]
        yoro= data["eur"]["value"]
        sekeh=data["sekkeh"]["value"]
        gold=data["18ayar"]["value"]
        ttr=data["usdt"]["value"]
        bit=data["btc"]["value"]
        self.canvas.create_text(115 ,500 ,text="  :"+dollar+" T",fill="dark blue" , font=("Segoe UI", 20))
        self.canvas.create_text(115 ,600 ,text="  :"+yoro+" T",fill="dark blue", font=("Segoe UI", 20))
        self.canvas.create_text(300 ,500 ,text="  :"+sekeh+" T",fill="dark blue" , font=("Segoe UI", 20))
        self.canvas.create_text(310 ,600 ,text="  :"+gold+" T", fill="dark blue",font=("Segoe UI",  20))
                
        self.img6=PhotoImage(file="15.png")
        self.canvas.create_image(40 ,502,image=self.img6)
        self.img7=PhotoImage(file="16.png")
        self.canvas.create_image(40 ,602,image=self.img7)
        self.img8=PhotoImage(file="13.png")
        self.canvas.create_image(225 ,502,image=self.img8)
        self.img9=PhotoImage(file="12.png")
        self.canvas.create_image(215 ,602,image=self.img9)

    def update_clock(self):
        now = datetime.now()
        self.canvas.itemconfig(self.time_id, text=now.strftime("%H : %M : %S"))
        self.canvas.itemconfig(self.date_id, text=now.strftime("%d %B %Y"))
        self.root.after(1000, self.update_clock)
       #current weather  
    def weather(self ,event):
        if (self.flag==1):
            self.canvas.delete(self.city_id)
            self.canvas.delete(self.temp_id)
            self.canvas.delete(self.s_id)
            self.canvas.delete(self.ss_id)
            self.canvas.delete(self.sky_id)
            self.canvas.delete(self.hum_id)
            self.canvas.delete(self.feels_id)
            if self.sun_id is not None:
                self.canvas.delete(self.sun_id)
                self.sun_id = None

            if self.cloud_id is not None:
                self.canvas.delete(self.cloud_id)
                self.cloud_id = None

            if self.rain_id is not None:
                self.canvas.delete(self.rain_id)
                self.rain_id = None          
            if self.wind_id is not None:
                self.canvas.delete(self.wind_id)
                self.wind_id = None
                
        api_key ="YOUR_REAL_API_KEY"
        city = self.combo1.get()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IR&appid={api_key}&units=metric"

        response = requests.get(url ,timeout=15)
        data = response.json()
        
        #print (data)
        temp=round(data["main"]["temp"])
        sky=(data["weather"][0]["description"])
        hum=(data["main"]["humidity"])
        feels=round(data["main"]["feels_like"])
        wind=(data["wind"]["speed"])
        wind_km= round(wind * 3.6, 1)
        self.city_id=self.canvas.create_text(120 ,160,text=f"  Weather condition in {city} :" ,fill="dark blue",font=("Segoe UI", 12))
        self.temp_id=self.canvas.create_text(100 ,250,text=str(temp) ,fill="dark blue",font=("Segoe UI", 65))
        self.s_id=self.canvas.create_text(150 ,220,text="°" ,fill="dark blue",font=("Segoe UI", 40))
        self.sky_id=self.canvas.create_text(100 ,320,text=str(sky) ,fill="dark blue",font=("Segoe UI", 20))
        self.hum_id=self.canvas.create_text(220 ,235,text="Humidity:" + str(hum)+"%" ,fill="dark blue",font=("Segoe UI", 10))
        self.ss_id=self.canvas.create_text(258 ,252,text="°" ,fill="dark blue",font=("Segoe UI", 10))
        self.feels_id=self.canvas.create_text(220 ,255,text="Feels like:" + str(feels) ,fill="dark blue",font=("Segoe UI", 10))
        self.wind_id=self.canvas.create_text(220 ,275,text="Wind:" + str(wind_km)+" Km/h" ,fill="dark blue",font=("Segoe UI", 10))

        if ("clear" in sky) :
            self.img3=PhotoImage(file="3.png")
            self.sun_id=self.canvas.create_image(333,220,image=self.img3)
        if ("cloud" in sky ):
            self.img4=PhotoImage(file="99.png")
            self.cloud_id=self.canvas.create_image(333,220,image=self.img4)
        if ("rain" in sky):
            self.img5=PhotoImage(file="10.png")
            self.rain_id=self.canvas.create_image(333,220,image=self.img5)
        self.flag=1
        #  7 days 
    def plot(self ,event):
        city = self.combo1.get()  # reuse your existing city_map
        
        # Open-Meteo needs lat/lon, not city name — so first do geocoding (ok)
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()
        print ("********")
        #print (geo_data)
        lat = geo_data["results"][0]["latitude"] #the whole is in the list
        lon = geo_data["results"][0]["longitude"]

        weather_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "daily": ["temperature_2m_max", "temperature_2m_min", "weather_code"],
            "timezone": "auto",
            "forecast_days": 7
        }
        
        weather_response = requests.get(weather_url, params=params)
        data = weather_response.json()
        
        chart_window=Toplevel(self.root)# NEW WWINDOW
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(data["daily"]["time"], data["daily"]["temperature_2m_max"],
                color='red',marker='o' ,label='Max Temp')
        
        ax.plot(data["daily"]["time"],data["daily"]["temperature_2m_min"],
                color='blue' ,marker='o',label='Min Temp')
        
        fig.patch.set_facecolor('#eaf4fb')  
        ax.set_facecolor('#ffffff')
        ax.set_title('Weather Chart')
        ax.set_xlabel('Day')
        ax.set_ylabel('Temp')
        ax.legend()
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.get_tk_widget().pack()
        canvas.draw()
        
        
   
  
    def enter(self,event):
        self.canvas.config(cursor="hand2") 
        self.canvas.itemconfig(self.t1_id ,fill="white")
    def leave(self, event):
        self.canvas.config(cursor="")
        self.canvas.itemconfig(self.t1_id, fill="blue")


    def enter1(self,event):
        self.canvas.config(cursor="hand2") 
        self.canvas.itemconfig(self.t2_id ,fill="white")
    def leave1(self, event):
        self.canvas.config(cursor="")
        self.canvas.itemconfig(self.t2_id, fill="blue")


def main():
    x=myclass()
    
if __name__=="__main__":main()   
        
