from models.item import WeedProductModel
import pandas as pd

def filldb():
    df = pd.read_csv('product_list.csv')
    # print(df)

    for i in range(df.shape[0]):
        # ------19-10-20-----Updated DB----------------------------------------------------------
        item = WeedProductModel(name=df.Weed_Name.iloc[i], crop=df.Crop.iloc[i], product=df.Product.iloc[i], dose=df.Dosage.iloc[i], country=df.Country.iloc[i])
        # ------19-10-20-----Updated DB----------------------------------------------------------
        if (WeedProductModel.find_object(item) == False):
            print(item.name, item.crop, item.country)
            item.save_to_db()
        else:
            pass
