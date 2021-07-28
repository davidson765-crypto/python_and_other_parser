import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin


def main():
	session = requests.Session()

	url = 'https://www.google.com/'

	r = session.get(url).content

	#r = requests.get(url)

	#with open('sec.html','w',encoding='utf-8') as file:

	soup = bs(r,'html.parser')

	script_file = []

	for script in soup.find_all('script'):

		if script.attrs.get('src'):

			script_url = urljoin(url,script.attrs.get('src'))

			script_file.append(script_url)
		else:
			script_file.append(script)
	print(script_file)


	css_file = []

	for css in soup.find_all('link'):

		if css.attrs.get('href'):

			css_url = urljoin(url,css.attrs.get('href'))
			css_file.append(css_url)
	print(css_file)




	with open('sec.html','w',encoding='utf-8') as file:

		ahref = soup.select('a[href]')

		for i in ahref:
			if "vk" in i.text or "Vk" in i.text or "VK" in i.text:

				file.write(str(str(i)))




if __name__=='__main__':
	main()
