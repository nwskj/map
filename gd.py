import requests
import pandas as pd
from pyexcelerator import ExcelWriter, Sheet
# 替换为您的API密钥
api_key = 'b1ea31352a1db94138822bbdee43c259'
def get_companies(city, keywords, page_size=10):
    url = f'***{keywords}&city={city}&page_size={page_size}&page=80'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return None
def extract_info(companies):
    companies_df = pd.DataFrame(companies)
    companies_df['企业名称'] = companies_df['name']
    companies_df['地址'] = companies_df['address']
    companies_df['电话'] = companies_df['phone']
    companies_df.to_excel('companies.xlsx', index=False, engine='openpyxl')
if __name__ == '__main__':
    city = '340000'  # 替换为您想要提取的城市
    keywords = '企业名称,地址,电话'  # 替换为您想要搜索的关键词
    companies = get_companies(city, keywords)
    if companies:
        extract_info(companies)