from django.shortcuts import render
from django.contrib import messages
import requests
import datetime
# import folium


def home(request):
   
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'Ahmedabad'     



    url = f'//weather_API_WITH_API_ID//'
    PARAMS = {'units':'metric'}

#     url2=f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=94ac81109dc71e5526ab76e7b9b1e537'
#     data2 = requests.get(url2).json()
#     figure = folium.Figure()
#     lat=data2[0]['lat']
#     lon=data2[0]['lon']
#     m=folium.Map(location=[lat,lon],zoom_start=10)
#     folium.Marker(location=[lat,lon]).add_to(m)
#     m.add_to(figure)
#     figure.render()
#     context={'map':figure}
    

# enter your cityimageapi key
    API_KEY =  ''

# enter your search engine id
    SEARCH_ENGINE_ID = ''
     
    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"


    data = requests.get(city_url).json()
    count = 1
    search_items = data.get('items')
    image_url = search_items[1]['link']
    

    try:
          
          data = requests.get(url,params=PARAMS).json()
          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          hum = data['main']['humidity']
          day = datetime.date.today()

          # lat=data2[0]['lat']
          # lon=data2[0]['lon']
          # m=folium.Map(location=[lat,lon],zoom_start=10)
          # folium.Marker(location=[lat,lon]).add_to(m)
          # m.add_to(figure)
          # figure.render()
          # context={'map':figure}

          # context = {'map': m._repr_html_()}

          return render(request,'index.html',{'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False ,'image_url':image_url,'humidity':hum})
    
    except KeyError:
          exception_occurred = True
          messages.error(request,'Entered data is not available to API')   
          day = datetime.date.today()

          return render(request,'index.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'Ahmedabad' , 'exception_occurred':exception_occurred,'humidity':49})
               
    
# def map(request):
#      if 'city' in request.POST:
#          city = request.POST['city']
#      else:
#          city = 'Ahmedabad'     
#      url2=f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=94ac81109dc71e5526ab76e7b9b1e537'
#      data2 = requests.get(url2).json()
#      lat=data2[0]['lat']
#      lon=data2[0]['lon']
#      m=folium.Map(location=[lat,lon],zoom_start=10)
#      context = {'map': m._repr_html_()}
#      return render(request,'map.html',context)