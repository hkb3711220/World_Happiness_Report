from get_url import GET_URL
import os
import pandas as pd
from pandas import DataFrame

os.chdir(os.path.dirname(__file__))

class GET_DATA(object):

    def __init__(self, res_text):
        self.columns = []
        self.dataset = []
        self.res_text = res_text

    def read_data(self):

        if os.path.exists('./output.csv'):
            df = pd.read_csv('./output.csv')
        else:
            df = self.make_dataframe(export=True)

        return df

    def make_dataframe(self, export=False):

        columns, dataset = self.extract()
        df = DataFrame() #空のデータファームを作成する。

        for col_name, data in zip(columns, dataset):
            df[col_name] = data

        if export:
            try:
                df.to_csv('output.csv', index=False)
            except:
                print('File not created')

        return df

    def extract(self):
        tables = self.res_text.find_all('table', attrs={'class':'wikitable'})
        #WE JUST NEED FIRST TABLE
        table = tables[0]
        for tr in table.tr:
            try:
                self.columns.append(tr.text.replace('\n', ''))
            except:
                pass

        for i in range(len(self.columns)):
            self.dataset.append([])

        tbody = table.tbody
        trs = tbody.find_all('tr')
        for tr in trs:
            for i, td in enumerate(tr.find_all('td')):
                self.dataset[i].append(td.text.replace('\n', ''))

        return self.columns, self.dataset
