import pandas as pd
import numpy as np
import json
import googlemaps


class DataReader:
    def __init__(self):
        self._context = None
        self._fname = None

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname):
        self._fname = fname

    def new_file(self) -> str:
        return self._context + self._fname

    def csv_to_dframe(self) -> object:
        file = self.new_file()
        return pd.read_csv(file, encoding='UTF-8', thousands=',')

    def xls_to_dframe(self, header, usecols) -> object:
        file = self.new_file()
        return pd.read_excel(file, encoding='UTF-8', header=header, usecols=usecols)

    def json_to_dframe(self, header, usecols) -> object:
        file = self.new_file()
        return json.load(open(file, encoding='UTF-8'))

    @staticmethod
    def create_gmaps():
        #구글 손솔에서 제한사항 설정시
        #애프리케이션 제한사항은 없음을
        #api제한사항은 Geocoding/Geolocation/Maps Javascript API선택
        return googlemaps.Client(key='')  # 구글지도 API키 넣기
