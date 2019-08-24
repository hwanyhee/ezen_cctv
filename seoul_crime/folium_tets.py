import pandas as pd
import folium
class FoliumTest:
    def __init__(self):
        self.context ='./data'


    def hook(self):
        self.show_map()

    def show_map(self):
        state_geo = self.context + 'us-state.json'
        state_unemployment = self.context+''
        state_date = pd.read_csv(state_unemployment)
        m = folium.Map(location=[37,-102],zoom_start=5)
        m.choropleth(



        )