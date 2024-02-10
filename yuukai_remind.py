import os
import requests
import random

# LINEのトークンとAPIのURL
token ='ruL56iOY316G7pXovrGonWU3vjw4MeUC3aGmVolOTz7' 
api_URL='https://notify-api.line.me/api/notify'

# 通知内容
send_contents = '\nみんな～!夕会の時間だよ～!'\
                '\nzoomリンクはこちら!'\
                '\nhttps://us05web.zoom.us/j/81784068934?pwd=sD1gtwSqwkGUEMSbU8ZP73lBpqNmWa.1' #通知内容

# 画像の相対パス
image_dir = './png'
image_files = [f for f in os.listdir(image_dir) if f.endswith('.png')]
image_path = os.path.join(image_dir, random.choice(image_files))

token_dic ={'Authorization': 'Bearer' + ' ' + token}
send_dic = {'message': send_contents}

# 画像ファイルを開いて送信
with open(image_path, 'rb') as image_file:
    files = {'imageFile': image_file}
    response = requests.post(api_URL, headers=token_dic, data=send_dic, files=files)

# 応答内容を確認
print(response.text)