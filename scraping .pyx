# distutils: language=c++
# distutils: extra_compile_args = ["-O3"]
# cython: language_level=3, boundscheck=False, wraparound=False
# cython: cdivision=True


from libcpp.vector cimport vector #ここでcppのvectorを呼び出している。
ctypedef long long LL
ctypedef vector[LL] vec



import requests
from bs4 import BeautifulSoup
import os

############################################################################

cpdef scrape():

        url='https://tenki.jp/forecast/3/16/4410/13204/1hour.html#forecast-point-1h-today'#tenki.jp

        page=requests.get(url)

        if page.status_code==200:
             print('http request successful')

        page.encoding=page.apparent_encoding#Requestで日本語を扱えるようにする．

        soup=BeautifulSoup(page.text,'lxml')#html構文解析

        today_table=soup.find(id='forecast-point-1h-today')#tableのweather取得 
        weather=today_table.find('tr',class_='weather')

        data=weather.find_all('p')#dataに今日のデータ格納

        # forecasts={"ko":None,"yowa":None,"ame":None,"tuyo":None,"gou":None}
        forecasts={}
        check=[0,0,0,0,0]
        for i in range(len(data)):
                if check[0]==0 and data[i].contents[0]=="小雨":
                        forecasts["ko"]=i+1
                        check[0]=1
                elif check[1]==0 and data[i].contents[0]=="弱雨":
                        forecasts["yowa"]=i+1
                        check[1]=1
                elif check[2]==0 and data[i].contents[0]=="雨":
                        forecasts["ame"]=i+1
                        check[2]=1
                elif check[3]==0 and data[i].contents[0]=="強雨":
                        forecasts["tuyo"]=i+1
                        check[3]=1
                elif check[4]==0 and data[i].contents[0]=="豪雨":
                        forecasts["gou"]=i+1
                        check[4]=1
        

        if check[0]==0:
                forecasts["ko"]=None
                check[0]=1
        if check[1]==0:
                forecasts["yowa"]=None
                check[1]=1
        if check[2]==0:
                forecasts["ame"]=None
                check[2]=1
        if check[3]==0:
                forecasts["tuyo"]=None
                check[3]=1
        if check[4]==0:
                forecasts["gou"]=None
                check[4]=1

        return forecasts









