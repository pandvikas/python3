import requests

# giao tiếp tab 1 và 2
driver.switch_to_window(driver.window_handles[0])

# requests dử liệu web
x = requests.get('https://api.ipify.org')

IP = x.text
ip = 0
while ip < 100:
    if IP == "":
        print('đang check IP', end=('/ r'))
        ip = ip + 1
        time.sleep(1)
    else:
        print(' địa chỉ ip là : ', IP)
        ip = 100

# nhập user pass và click
userID = '100071151885191'
passwd = 'nihAJ439FUc'
# user
driver.find_element_by_xpath('/html/body/div[1]/div[2]/di').send_keys(userID)
# pass
driver.find_element_by_name('pass').send_keys(passwd)
time.sleep(1)
driver.find_element_by_name('login').click()

# lấy title của web
print(driver.title)

# string
string.lower()  # viết thường tất cả
string.strip()  # bỏ khoảng trắng đầu và cuối string
string.upper()  # viết hoa tất cả
string[:10]  # lấy từ 0 - 10 ký tự của chuỗi

# sử dụng javascript
js = ''
driver.execute_script(js)

# tổ hợp phím copy paste
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[4]').send_keys(Keys.COMMAND, 'a')
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[4]').send_keys(Keys.COMMAND, 'c')
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[4]').send_keys(Keys.COMMAND, 'v')

# xem text của thẻ
so_sanh_2b = driver.find_element_by_xpath('/html/body/di]/div/div').text
so_sanh_2b = driver.find_element_by_xpath(
    '/html/body/di]/div/div').get_attribute('innerHTML')
