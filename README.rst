easy_mongo
^^^^^^^^^^
Easy to use python mongo(for kb first)

Quick Start
-----------
**Installation**: pip install easy_mongo

1.config
>>>>>>>>
Edit conf/conf.yml
::

    mongo: # mongo config
      host: 127.0.0.1
      port: 27017
      name: db_name
      password: password # blank if not require

2.demo
>>>>>>
::

    easy_mongo = EasyMongo('conf/conf.yml')
    col = easy_mongo.get_collection('country')
    # get first 10 items
    for item in col.find().limit(10):
        print(item)
