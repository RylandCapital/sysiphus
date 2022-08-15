from systems_rbos.build import build


rbos_data = build()
counts = rbos_data['target_label'].value_counts()
print(((counts/counts.sum())*100).round(2))

#client = pymongo.MongoClient("mongodb+srv://rylandcapital:<password>@cluster0.cl0ndyw.mongodb.net/?retryWrites=true&w=majority")
#db = client.test






