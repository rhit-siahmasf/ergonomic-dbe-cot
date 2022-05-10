import base64

image_paths = [
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\reba-images\\A1.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\reba-images\\A2.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\reba-images\\A2-2.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\reba-images\\A3.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\reba-images\\A3-2.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\reba-images\\B1.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\reba-images\\B1-2.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\reba-images\\B2.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\reba-images\\B3.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\rula-images\\A1.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\rula-images\\A1-2.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\rula-images\\A2.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\rula-images\\A3.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\rula-images\\B1.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\rula-images\\B2.png',
    'C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\rula-images\\B2-2.png',
]
i = 0
for path in image_paths:
    with open(path, "rb") as image_file:
        i += 1
        encoded_string = base64.b64encode(image_file.read())
        file = open('C:\\Users\\siahmasf\\Documents\\Quarters\\Spring 2022\\Ergonomics Project (CSSE371)\\ergonomic-dbe-cot\\all-images\\image_%d'%i, "w")
        file.write(encoded_string.decode("utf-8"))
        file.close()
