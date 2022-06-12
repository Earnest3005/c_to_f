#讓使用者輸入攝氏溫度，然後印出華氏溫度

celsius = input('請輸入攝氏溫度： ')
celsius = float(celsius)
fahrenheit = 9 * celsius / 5 + 32
print('華氏溫度為：', fahrenheit, '度')
