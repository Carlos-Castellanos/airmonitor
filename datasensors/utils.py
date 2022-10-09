# import csv, uuid
# import dataset


# def csv2dataset(filename_input, filename_output):
#     with open(filename_input, 'r') as file_input:
#         input_data = csv.DictReader(file_input)
#         db = dataset.connect('sqlite:///' + filename_output)
#         table = db['contactos']
#         for contact in input_data:
#             contact['uuid'] = uuid.uuid4().hex
#             table.insert(contact)


# if __name__ == '__main__':
#     csv2dataset('data.csv', 'datasensor.sqlite')