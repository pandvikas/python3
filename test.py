from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
import requests
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

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
# nhập user pass và click
userID = '100070863217471'
passwd = '5xPsmhRYIn'
# user
driver.find_element_by_xpath('/html/body/div[1]/div[2]/di').send_keys(userID)
# pass
driver.find_element_by_name('pass').send_keys(passwd)
time.sleep(1)
driver.find_element_by_name('login').click()

print(driver.title)


js = '''function settime(pasa) {
  if (pasa < 1000) {
    setTimeout(() => {
      pasa = pasa + 1;
      if (
        document.querySelector("input#code_in_cliff.inputtext._8n1_._9c54")
          .value === ""
      ) {
        document.querySelector("title#pageTitle").innerText = "bắt đầu";
        window.open("https://temp-mail.org/vi/", "_blank");
        settime(1000);
      } else {
        console.log("đang đợi vào");
        settime(pasa);
      }
    }, 1000);
  }
}
settime(1);'''
driver.execute_script(js)

i = 0

while i < 1000:
    if driver.title == "Facebook":
        i = 1000
        print('load thành công')
        time.sleep(1)
    else:
        i = i + 1
        time.sleep(1)
        print('đang load trang')

gss = driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/div[1]/div/div/div[1]/div[2]/form/div[2]/div/a').text
so_sanh_chuoi = str(
    'Cập nhật thông tin liên hệ').lower().strip()

print(str(gss.lower().strip())[:10])
print(so_sanh_chuoi[:10])

e = 0
while e < 1000:
    if so_sanh_chuoi[:10] == str(gss.lower().strip())[:10]:
        print('đăng nhập thành công')
        e = 1000
    else:
        print('thất bại chờ tiếp tục %s giây' % (e+1))
        e = e + 1
        time.sleep(1)
time.sleep(2)
driver.switch_to_window(driver.window_handles[0])
driver.get('https://m.facebook.com/changeemail/')
time.sleep(3)
driver.switch_to_window(driver.window_handles[1])
time.sleep(2)
js_2 = '''function settime(pasa) {
  if (pasa < 1000) {
    setTimeout(() => {
      pasa = pasa + 1;
      if (
        document.querySelector("input#mail.emailbox-input.opentip").value ===
          "" ||
        document.querySelector("input#mail.emailbox-input.opentip").value ===
          "Đang tải" ||
        document.querySelector("input#mail.emailbox-input.opentip").value ===
          "Đang tải." ||
        document.querySelector("input#mail.emailbox-input.opentip").value ===
          "Đang tải.." ||
        document.querySelector("input#mail.emailbox-input.opentip").value ===
          "Đang tải..."
      ) {
        console.log("chưa loat xong mail");
        settime(pasa);
      } else {
        console.log("lấy thành công mail");
        document.querySelector("h2").innerText = "copydone";
        document.querySelector(
            "p").innerHTML = document.querySelector("#mail").value
        settime(1000);
      }
    }, 1000);
  }
}
settime(1);'''
driver.execute_script(js_2)
q = 0
email = ''
while q < 1000:
    if driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/h2').text.strip() == str('copydone'):
        time.sleep(3)
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/button[1]').click()
        print('copymail thành công')
        email = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[2]/div[2]/p').text
        driver.switch_to_window(driver.window_handles[0])
        q = 1000
    else:
        print('đang copy')
        time.sleep(1)
        q = q + 1
time.sleep(2)
print(email)
time.sleep(4)
so_sanh_1a = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/form/div[1]/div/div').text.lower()
so_sanh_1a = str('Email mới').lower()
so_sanh_2a = str('thêm địa chỉ em')
so_sanh_2b = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[2]/div/div[2]/div/div').text.lower().strip()[0:15]
print(so_sanh_2b)
print(so_sanh_2a)
w = 0
while w < 1000:
    if so_sanh_2a == so_sanh_2b or so_sanh_1a == so_sanh_1a:
        print('chuyển tab thành công')
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/form/div[1]/div/input').send_keys(email)
        time.sleep(3)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/form/div[2]/div[1]/button').click()
        w = 1000
    else:
        print('đang chuyển tab')
        w = w + 1
        time.sleep(1)
time.sleep(3)
driver.switch_to_window(driver.window_handles[1])
time.sleep(2)
driver.execute_script('''function settime(pasa) {
  if (pasa < 1000) {
    setTimeout(() => {
      pasa = pasa + 1;
      if (
        document.querySelector(
          "#tm-body > main > div.container > div > div.col-sm-12.col-md-12.col-lg-12.col-xl-8 > div.tm-content > div > div.inboxWarpMain > div > div.inbox-dataList > ul > li:nth-child(2) > div:nth-child(1) > a > span.inboxSenderEmail.inboxSenderEllipsis"
        )
      ) {
        if (
          document.querySelector(
            "#tm-body > main > div.container > div > div.col-sm-12.col-md-12.col-lg-12.col-xl-8 > div.tm-content > div > div.inboxWarpMain > div > div.inbox-dataList > ul > li:nth-child(2) > div:nth-child(1) > a > span.inboxSenderEmail.inboxSenderEllipsis"
          ).innerText === "registration@facebookmail.com"
        ) {
          document.querySelector("#mail").value = document
            .querySelector(
              "#tm-body > main > div.container > div > div.col-sm-12.col-md-12.col-lg-12.col-xl-8 > div.tm-content > div > div.inboxWarpMain > div > div.inbox-dataList > ul > li:nth-child(2) > div.col-box.hidden-xs-sm > span > a"
            )
            .innerText.slice(0, 5);
          document.querySelector("p").innerText = document
            .querySelector(
              "#tm-body > main > div.container > div > div.col-sm-12.col-md-12.col-lg-12.col-xl-8 > div.tm-content > div > div.inboxWarpMain > div > div.inbox-dataList > ul > li:nth-child(2) > div.col-box.hidden-xs-sm > span > a"
            )
            .innerText.slice(21, 29);
          console.log("lấy thành công mail");
          settime(1000);
        }
      } else {
        console.log("đang đợi mail");
        settime(pasa);
      }
    }, 1000);
  }
}
settime(1);''')
time.sleep(5)

mail_2 = ''
abcd = 0
while abcd < 1000:
    if driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/p').text.lower().strip() == "facebook":
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/button[1]').click()
        print('lấy mã xác nhận thành công')
        abcd = 1000
    elif abcd == 50:
        print('gửi lại mail', abcd)
    else:
        print('đang chờ mã xác nhận', abcd)
        time.sleep(1)
        abcd = abcd + 1

driver.switch_to_window(driver.window_handles[0])
time.sleep(3)
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[4]').send_keys(Keys.COMMAND, 'v')
time.sleep(3)
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div/form/a').click()
input()
driver.quit()
