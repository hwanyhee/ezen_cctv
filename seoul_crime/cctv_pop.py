import pandas as pd
import numpy as np
from seoul_crime.data_reader import DataReader

#인구당 최적화된 CCTV수
class CCTVModel:
    def __init__(self):
        self.dr = DataReader()

    def hook_process(self):
        print('----------------1.cctv 파일로 DF 생성---------------')
        self.get_cctv()

    def get_cctv(self):
        self.dr.context='./data/'
        self.dr.fname='cctv_in_seoul.csv'
        cctv = self.dr.csv_to_dframe()
        print(cctv.columns)#Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object')
        self.dr.fname='population_in_seoul.xls'
        pop = self.dr.xls_to_dframe(2,'B,D,G,J,N')
        print(pop.columns)#Index(['자치구', '계', '계.1', '계.2', '65세이상고령자'], dtype='object')
