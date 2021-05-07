from flask_restful import Resource, reqparse
from flask import request
from Disease.models.item import DiseaseProductModel
from Disease.predict_disease import predict
import base64
import re
import datetime
from Disease.alert import message
class Ping(Resource):
    def get(self):
        return "working"

class Item_Disease(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('price',
    #                     type=float,
    #                     required=True,
    #                     help="This field cannot be left blank!"
    #                     )
    # parser.add_argument('store_id',
    #                     type=int,
    #                     required=True,
    #                     help="Every item needs a store_id."
    #                     )
    parser.add_argument('image',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    # parser.add_argument('crop',
    #                     type=str,
    #                     required=True,
    #                     help="Every item needs a store_id."
    #                     )


    def post(self):

        # Add code to predict weed name

        # if not WeedProductModel.find_by_name(crop):
        #     return {'message': "Crop with name '{}' doesnot exists.".format(name)}, 400

        # if ItemModel.find_by_name(weed_name):
        #     return {'message': "An item with name '{}' already exists.".format(name)}, 400

        # data = Item.parser.parse_args()

        data = request.get_json()
        # print("\n\n---------------image data---------------------\n\n")
        # print(data)

        # Code to decode image

        
        imgdata = re.search('base64,(.*)', data['image']).group(1)
        imgdata = base64.b64decode(imgdata)
        filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
        filepath = 'Disease/temp_images/'+filename
        # print(type(imgdata))
        # print("img_data=\n", imgdata)

        x = datetime.datetime.now()
        print('\n\nPrediction called at:', x)

        with open(filepath, 'wb') as f:
            f.write(imgdata)

        # Code to save image
        crops = ['rice']
        country = ['indonesia', 'vietnam']
        if data['crop'].lower() in crops and data['country'].lower() in country:
            result = predict(filename, data['language'].lower(), data['crop'].lower())
        else:
            message_result = message(3, data['language'].lower())
            return {'message': message_result}
                # return {'message': "Sorry, we don't predict weed for this crop."}
        #except:
        #    print("error in code 19-10-2020")
        #    message_result = message(1, data['language'].lower())
        #      return {'message': message_result}
            # return {'message': "Please enter a crop name"}

        # ------19-10-20------------------------------------------------------

        # ------20-09-20------------Get Prediction------------------------------------------

        # result = predict(filename)

        # ------20-09-20------------------------------------------------------


        
        print("\nresult keys:\n ", result.keys())

        if('message' in result.keys()):
            return result
        else:
            disease_name = result['result']

            products = []
            # products = list(map(lambda x: {'prod': x.product, 'dose': x.dose} if x.product else [], WeedProductModel.find_product(weed_name,data['crop'].title(), data['country'].title())))
            
            x = DiseaseProductModel.find_product(disease_name,data['crop'].title(), data['country'].title())

            for prod in x:
                if prod.product:
                    products.append({'prod': prod.product, 'dose': prod.dose})

            if (products):
                # test = products
                # print(test)

                # ----20-09-20----Returing results--------------------------------------------------------
                # return {'weedname': weed_name,'items': list(map(lambda x: x.json(), WeedProductModel.find_by_name(weed_name)))}
                # ----20-09-20------------------------------------------------

                # ----19-10-20----Returing results--------------------------------------------------------
                return {'botanicalName': disease_name,'productName': products }
                # ----19-10-20------------------------------------------------

                # return {'botanicalName': weed_name, 'productName': list(map(lambda x: {x.product, x.dose}.json(), WeedProductModel.query.filter(name=weed_name)))}
            else:
                if disease_name == 'False Smut':
                    message_result = message(4, data['language'].lower())
                    print(message_result)
                else:
                    message_result = message(3, data['language'].lower())
                return {'botanicalName': disease_name, 'message': message_result}
# ----Change (Commented the code below)----
#        weed_name = predict(filename)
#
#        if (WeedProductModel.find_by_name(weed_name)):
#            # return {'weedname': weed_name,'items': list(map(lambda x: x.json(), WeedProductModel.find_by_name(weed_name)))}
#            return {'botanicalName': weed_name,'productName': list(map(lambda x: {'prod': x.product, 'dose': x.dose}, WeedProductModel.find_by_name(weed_name)))}
#            # return {'botanicalName': weed_name, 'productName': list(map(lambda x: {x.product, x.dose}.json(), WeedProductModel.query.filter(name=weed_name)))}
#        else:
#            return {'message': 'No product found for this crop'}

        # try:
        #     if (ItemModel.query.filter(name=weed_name)):
        #         return {'items': list(map(lambda x: x.json(), ItemModel.query.filter(name=weed_name)))}
        #     else:
        #         return {'message': 'No product found for this crop'}
        # except:
        #     return {'message': 'Error Occured'}
