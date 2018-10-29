from get_url import GET_URL
from get_data import GET_DATA
import os

os.chdir(os.path.dirname(__file__))

if __name__ =='__main__':
    if os.path.exists('./output.csv'):
        data = pd.read_csv('./output.csv')
    else:
        url = 'https://en.wikipedia.org/wiki/World_Happiness_Report'
        response = GET_URL().response(url)
        data = GET_DATA(response).read_data()
