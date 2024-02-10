import requests #ライブラリのインポート

token ='OYHZoLDpfG8ljYqIHdl4RBpbRC451DTKGWc8osRh7XT' #LINEのトークン
api_URl='https://notify-api.line.me/api/notify' #apiのURL

send_contents = '\n退勤打刻も忘れずにしましょう。' #通知内容

token_dic ={'Authorization': 'Bearer' + ' ' + token}
send_dic = {'message': send_contents}

#LINE通知を送る
requests.post(api_URl, headers=token_dic, data=send_dic)