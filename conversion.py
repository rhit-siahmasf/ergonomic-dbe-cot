import base64
#
image_paths = [
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\table-images\\REBA-Table-A.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\table-images\\REBA-Table-B.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\table-images\\REBA-Table-C.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\table-images\\RULA-Table-A.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\table-images\\RULA-Table-B.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\table-images\\RULA-Table-C.png'
]
#
i = 19
for path in image_paths:
    with open(path, "rb") as image_file:
        i += 1
        encoded_string = base64.b64encode(image_file.read())
        file = open(
            'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\all-images\\image_%d' % i,
            "w")
        file.write(encoded_string.decode("utf-8"))
        file.close()

# scones = {}
# for i in range(1, 17, 1):
#     file_name = 'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\all-images\\image_%d' % i
#     with open(file_name, "r") as f:
#         encoded_string = f.read()
#         scones['image_%d' % i] = encoded_string
# print(scones)


def base64_encoder(kids):
    image_data = base64.b64encode(kids)
    if not isinstance(image_data, str):
        image_data = image_data.decode()
    return image_data
