from Disease.models.item import DiseaseProductModel
import pandas as pd

def filldb_disease():
    df = pd.read_csv('Disease/disease_product.csv')
    # print(df)

    for i in range(df.shape[0]):
        # ------19-10-20-----Updated DB----------------------------------------------------------
        item = DiseaseProductModel(name=df.Disease_Name.iloc[i], crop=df.Crop.iloc[i], product=df.Product.iloc[i], dose=df.Dosage.iloc[i], country=df.Country.iloc[i])
        # ------19-10-20-----Updated DB----------------------------------------------------------
        if (DiseaseProductModel.find_object(item) == False):
            # print(item.name, item.crop, item.country)
            item.save_to_db()
        else:
            pass