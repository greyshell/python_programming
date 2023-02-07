import secretstorage

conn = secretstorage.dbus_init()
collection = secretstorage.get_default_collection(conn)
for item in collection.get_all_items():
    print(item.get_label())
    print(item.get_attributes())
