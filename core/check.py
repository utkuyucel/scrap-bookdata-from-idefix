import requests as req
from bs4 import BeautifulSoup as bs

class Checker:
	
	def __init__(self, dict_):
		self.dict = dict_
		self.get_url = input("Aradığınız kitabın adını giriniz: ")
		self.run()

	def _check(self):
		try:
			checkStock = self.results.h3.text # stokta yok 
			return 0

		except:	
			self.price = self.soup.find(id = "salePrice").text
			return self.price

	def run(self):
		if self.get_url in self.dict:
			
			URL = self.dict[self.get_url]
			page = req.get(URL)
			self.soup = bs(page.content, "html.parser")
			self.results = self.soup.find(class_ = "col-lg-9 col-md-8 col-sm-8 mobileBasketSubm")

			if self._check() != 0:
				print(f"\n{self.get_url.upper()}, Stoklarda VAR.")
				print("Fiyat:", self.price, "\n")

			else:
				print(f"{self.get_url.upper()}, Stokta yok.")
			
		else:
			print(f"Girilen sözlükte {self.get_url} adında bir kitap bulunmamaktadır.")

if __name__ == "__main__":
	sample_dict = {"deneme":"deneme1"}

	checker = Checker(sample_dict)
	


