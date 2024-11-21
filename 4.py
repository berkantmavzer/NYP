from datetime import datetime

class Product:
    def __init__(self, name=None, price=0, quantity=1):
        self._name = name if name is not None else "Unknown"
        self._price = price if price >= 0 else 0
        self._quantity = quantity if quantity >= 1 else 1

        if len(self._name) < 3 or len(self._name) > 10:
            raise ValueError("Ürün ismi 3 ila 10 karakter arasında olmalıdır.")
        if self._price < 0:
            raise ValueError("Ücret 0'dan düşük olamaz.")
        if self._quantity < 1:
            raise ValueError("Miktar 1'den az olamaz.")

        print(f"Ürün İsmi: {self._name}, Tarih: {datetime.now()}")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if 3 <= len(value) <= 10:
            self._name = value
        else:
            raise ValueError("Ürün İsmi must be between 3 and 10 characters.")
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Ücret 0'dan düşük olamaz.")
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value >= 1:
            self._quantity = value
        else:
            raise ValueError("Miktar 1'den az olamaz.")
    
    def get_total_price(self):
        return self._price * self._quantity
    
    def __str__(self):
        return f"Ürün: {self._name}, Ücret: {self._price}, Miktar: {self._quantity}, Toplam: {self.get_total_price()}"

class ProductHelper:

    @staticmethod
    def create_item_from_text(urunler):
        urun_listesi = []
        
        try:
            with open(urunler, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        name, price, quantity = parts
                        try:
                            product = Product(name.strip(), float(price.strip()), int(quantity.strip()))
                            urun_listesi.append(product)
                        except ValueError as e:
                            print(f"Hata: {e} - Satır: {line.strip()}")
                    else:
                        print(f"Geçersiz: {line.strip()}")
        except FileNotFoundError:
            print(f"{urunler} bulunamadı.")
        
        return urun_listesi
    
    @staticmethod
    def get_ucret(products):
        ucret = 0
        for product in products:
            ucret += product.get_total_price()
        
        
        vergi_dahil_ucret = ucret * 1.20
        return vergi_dahil_ucret


if __name__ == "__main__":

    urunler = "urunler.txt"
    
    urun_listesi = ProductHelper.create_item_from_text(urunler)
    
    if urun_listesi:
        ucret = ProductHelper.get_ucret(urun_listesi)
        print(f"Toplam Ücret (Vergi Dahil): {ucret:.2f} TL")
    else:
        print("Herhangi Bir ürün bulunamadı.")