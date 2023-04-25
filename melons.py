import csv

melon_dict = {}

class Melon():
    
    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless
    
    def __repr__(self):
        return f"<Melon: {self.melon_id}, {self.common_name}>"
    def price_str(self):
        return f"${self.price:.2f}"



with open("melons.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        melon = Melon(row["melon_id"], row["common_name"], float(row["price"]), row["image_url"], row["color"], eval(row["seedless"]))

        melon_dict[row["melon_id"]] = melon


# print(melon_dict)
# print(melon_dict["anci"].price_str())


def find_melon(melon_id):
    if melon_id in melon_dict:
        return melon_dict[melon_id]
    else:
        return "Sorry, no melon found!"
    
# print(find_melon('anci'))

def get_melons():
    return melon_dict.items()

# print(get_melons())