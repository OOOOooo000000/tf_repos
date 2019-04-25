from tqdm import tqdm

data_size = int(1e6)

product = ''
with open('./train.txt', 'r') as f:
    for i, line in tqdm(enumerate(f)):
        product += line
        if i == data_size:
            break

with open('./small_train.txt', 'w') as f:
    f.write(product)


product = ''
with open('./test.txt', 'r') as f:
    for i, line in tqdm(enumerate(f)):
        product += line
        if i == data_size:
            break

with open('./small_test.txt', 'w') as f:
    f.write(product)


