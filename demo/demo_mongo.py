from easy_mongo.mongo import EasyMongo


def demo_mongo():
    easy_mongo = EasyMongo('../conf/conf.yml')
    col = easy_mongo.get_collection('country')
    # get first 10 items
    # reference pymongo
    for item in col.find().limit(10):
        print(item)


if __name__ == '__main__':
    demo_mongo()
