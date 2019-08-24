from seoul_crime.cctv_pop import CCTVModel
from seoul_crime.crime_police import CrimeModel
from seoul_crime.folium_test import FoliumTest
from seoul_crime.police_norm import PoliceNormModel
class Controller:
    def __init__(self):
        self._cctv = CCTVModel()
        self._crime = CrimeModel()
        self._usa=FoliumTest()
        self._police_norm = PoliceNormModel()
    def execute(self):
        #구별 cctv 설치와 인구 데이타 합치기
        #cctv = self._cctv
        #cctv.hook_process()
        #구별 범죄건수
        #crime = self._crime
        #crime.hook_process()
        #usa=self._usa
        #usa.hook()
        pn = self._police_norm
        pn.hook_process()

