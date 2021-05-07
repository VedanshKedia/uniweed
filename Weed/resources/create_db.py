from Weed.models.item import WeedProductModel
import pandas as pd

def filldb_weed():
    # df = pd.read_excel('final_soy_prod.xlsx')
    # df.to_csv('product_list.csv', index = None, header=True)
    df = pd.read_csv('Weed/product_list.csv', encoding='utf8')
    # print(df)

    for i in range(df.shape[0]):
        # ------19-10-20-----Updated DB----------------------------------------------------------
        item = WeedProductModel(name=df.Weed_Name.iloc[i], crop=df.Crop.iloc[i], product=df.Product.iloc[i], dose=df.Dosage.iloc[i], country=df.Country.iloc[i])
        # ------19-10-20-----Updated DB----------------------------------------------------------
        print("Data found: ", WeedProductModel.find_object(item))
        if (WeedProductModel.find_object(item) == False):
            print(item.name, item.crop, item.country)
            item.save_to_db()
        else:
            pass
