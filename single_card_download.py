import os
import time
import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from http.client import IncompleteRead

class SingleCardDownloader:
	HD_PATH = "cards_hd/"
	NORMAL_PATH = "cards/"
	def __init__(self, seriers_name, card_idx_in_seriers):
		self.seriers_name = seriers_name
		self.card_idx_in_seriers = card_idx_in_seriers
		self.image_name = "%s_%s.png"%(seriers_name, card_idx_in_seriers)
		self.url_requested = False
	
	def get_card_page(self):
		self.url_requested = True
		url = "https://limitlesstcg.com/cards/%s/%s"%(self.seriers_name, self.card_idx_in_seriers)
		user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
		req = Request(url)
		# req.add_header("Cookie", "cookiename=cookievalue")
		req.add_header("user-agent", user_agent)
		card_page_data = urlopen(req).read()
		return BeautifulSoup(card_page_data)

	@staticmethod
	def get_img_node(card_page_soup):
		card_img_node = card_page_soup.find("img", class_="card shadow resp-w")
		return card_img_node
	
	def _get_img_impl(self, get_hd_img=False):
		path = self.HD_PATH if get_hd_img else self.NORMAL_PATH
		path_to_img= path + self.image_name
		print("geting img to %s"%path_to_img)
		if os.path.exists(path_to_img):
			print("already done")
			return path_to_img
		card_page = self.get_card_page()
		card_img_node = self.get_img_node(card_page)
		url_key = "data-src" if get_hd_img else "src"
		img_url = card_img_node[url_key]
		print("from: %s"%img_url)
		time.sleep(0.2)
		card_img_data = requests.get(img_url).content
		with open(path_to_img, "wb") as f:
			f.write(card_img_data)
		print("done")
		return path_to_img

	def get_img_hd(self):
		return self._get_img_impl(get_hd_img=True)

	def get_img(self):
		return self._get_img_impl(get_hd_img=False)
