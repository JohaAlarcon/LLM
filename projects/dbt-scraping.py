import requests
from lxml import html


headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

dbt_url = "https://courses.getdbt.com"

login_url = f'{dbt_url}/users/sign_in'
session = requests.session()
login_form_res = session.get(login_url, headers=headers)

parser = html.fromstring(login_form_res.text)
token_especial = parser.xpath('//input[@name="authenticity_token"]/@value')[0]
print(token_especial)


login_data = {
    "login": "johana.alarcon.tech@gmail.com",
    "password": "",
    "commit": "login",
    "authenticity_token": token_especial
}

session.post(login_url, data=login_data, headers=headers)

data_url = f'{dbt_url}/courses/fundamentals'
respuesta = session.get(data_url, headers=headers)

parser = html.fromstring(respuesta.text)
course_list = parser.xpath('//div[contains(@class,"list-group")]/a/@href')
for course in course_list:
    course_url =f'{dbt_url}{course}'
    print(course_url)

