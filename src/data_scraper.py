
import requests
from bs4 import BeautifulSoup

class Scraper:
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

    def __init__(self, search_key):
        self.search_key = search_key
        self.url = f'https://audioshopnepal.com/?s={self.search_key}&post_type=product'
        self.extracted_data = None

    def fetch_page(self):
        return requests.get(self.url, Scraper.header)
    
    def parse_page(self):
        response = self.fetch_page()
        return BeautifulSoup(response.text, 'html.parser')
    
    # @staticmethod
    # def ask_for_search_item():
    #     print("\n=== 🎯 Data Scraping Interface ===")
    #     print("\nYou've chosen to scrape data. Let's get started!")

    #     search_term = input("\n🔍 Enter the item you want to search for: ").lower().strip()

    #     return Scraper(search_term)


    def scrape(self):
        print(f'Scraping the data. Please wait!!!\n')
        page_soup = self.parse_page()

        instrument_elems = page_soup.find_all("div", class_ = 'wd-product')

        if len(instrument_elems) < 1:
            print(f'\nSorry we found no results for the search key "{self.search_key}"!!\n')
            return
        
        # extracted_instruments = []
        for element in instrument_elems:
            availability = element.find("p", class_ = 'wd-product-stock').text.strip()
            if availability.startswith('Out'):
                continue

            name = element.find("h3", class_ = 'wd-entities-title').text.strip()
            category = element.find("div", class_ = 'wd-product-cats').text.strip()
            rating = element.find("div", class_ = 'star-rating').text.strip()
            discount = 'Not Given'
            detail_url = "Not Given"
            image_url = "Not Given" 
            original_price = current_price ="Not Mentioned"
            brand = "Not Mentioned"
            # description = "Not Given"

            if element.find('span', class_ = 'product-label'):
                discount = element.find('span', class_ = 'product-label').text.strip()

            #for extracting url that takes to the product description page
            if element.find('a', class_ = 'product-image-link', href=True):
                detail_url = element.find('a', class_ = 'product-image-link', href=True)['href']

            #for extracting image url
            if element.find('img', class_ = 'attachment-large', src=True):
                image_url = element.find('img', class_ = 'attachment-large', src=True)['src']


            #for extracting price
            prices = element.find_all('span', class_ = 'screen-reader-text')
            if element.find("bdi"):
                original_price = current_price = element.find("bdi").text.strip()

            elif not prices:
                original_price = current_price = element.find('bdi').text.strip()
                
            elif 0 < len(prices) < 2: 
                original_price = current_price = element.find_all('span', class_ = 'screen-reader-text')[0].text.strip()

            else:
                original_price = prices[0].text.strip().replace("Original price was: ", "")
                current_price = prices[1].text.strip().replace("Current price is: ", "")
            
            #for brand
            brand_elem = element.find('div', class_ = 'fade-in-block')
            if brand_elem.find('p'):
                brand = brand_elem.find('p').text.strip()
            
            #FIXME: please check this
            #for extracting instrument description and features
            # desc_elem = element.find('div', class_ = ['summary', 'entry-summary', 'wd-scroll', 'text-left'])
            # desc_elem = element.find('div', class_ = 'woocommerce-product-details__short-description')
            # description = desc_elem.text
            # breakpoint()

            instrument_data = {
                "Name" : name, 
                "Category" : category,
                "Brand" : brand,
                "Rating" : rating, 
                "Availability" : availability,
                "Original Price" : original_price,
                "Discount" : discount,
                "Current Price" : current_price, 
                "Detail URL" : detail_url, 
                "Image URL" : image_url}

            self.extracted_data.append(instrument_data)

            # print([f'{key} : {value}' for instrument in extracted_instruments for key, value in instrument.items() ])

        print(f'\n🔸 Displaying the extracted data for your search key "{self.search_key}":\n')

        for instrument in self.extracted_data:
                for key, value in instrument.items():
                    print(f'{key} : {value}')
                print()

        return self.extracted_data

    def display_extracted_data(self):
        for instrument in self.extracted_data:
            for key, value in instrument.items():
                print(f'{key} : {value}')
            print()


