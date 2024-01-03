
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class get_library_seats:
    def __init__(self,username,password,choose_floor,date,timestamp,seats_number):
        self.username=username #用户名
        self.password=password #密码
        self.date=date #预约日期
        self.timestamp=timestamp #预约时间段
        self.seats_number=seats_number #座位号
        self.choose_floor=choose_floor #楼层字典 i-j进行xpath匹配
    #登陆页面
    def login(self):
        username=self.username
        password=self.password
        choose_floor=self.choose_floor
        date=self.date
        timestamp=self.timestamp
        #切割时间片
        timestamp_result=timestamp.split('-')
        seats_number=self.seats_number
        password_input_xpath = '//*[@id="app"]/div[1]/div[5]/div/div[1]/form/div[2]/div/div/input'
        username_input_xpath = '//*[@id="app"]/div[1]/div[5]/div/div[1]/form/div[1]/div/div/input'
        login_button_xpath = '//*[@id="app"]/div[1]/div[5]/div/div[1]/form/div[3]/div/button'
        date_xpath='//*[@id="app"]/div[1]/div[3]/div[2]/div[3]/div[2]/div/section/div/input'
        timestamp_xpath1='//*[@id="app"]/div[1]/div[3]/div[2]/div[3]/div[2]/div/section/span/div[1]/div[1]/input'
        time_options_xpath1 = '//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span'
        timestamp_xpath2='//*[@id="app"]/div[1]/div[3]/div[2]/div[3]/div[2]/div/section/span/div[2]/div/input'
        time_options_xpath2='//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span'
        button_xpath='//*[@id="app"]/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div/div[3]/span/button[1]'
        #提供了两种登陆方式，本地没有谷歌浏览器的话就采用驱动登陆
        """
        # 设置浏览器驱动器的路径
        driver_path = "D:/谷歌驱动/chromedriver.exe"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("executable_path=" + driver_path)
    
        # 初始化 Chrome 浏览器
        driver = webdriver.Chrome(options=chrome_options)
        """

        # 输入要访问的网址
        driver = webdriver.Chrome()
        url = "https://libseat.njfu.edu.cn/#/ic/home"
        driver.get(url)

        # 显式等待，等待账号、密码输入框出现
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, username_input_xpath))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, password_input_xpath))
        )
        username_input.send_keys(username)
        # 定位密码输入框并输入值
        password_input.send_keys(password)  # 替换为实际的密码
        # 显式等待，等待登录按钮出现
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, login_button_xpath))
        )
        # 点击登录按钮
        login_button.click()
        sleep(0.3)
        #直接跳转到对应的页面
        floor_url = "https://libseat.njfu.edu.cn/#/ic/seatPredetermine/" + choose_floor
        driver.get(floor_url)
        #定位到日期
        date_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, date_xpath))
        )
        #需先清空原有日期
        date_button.clear()
        #填写用户数据
        date_button.send_keys(date)
        #定位时间戳1
        timestamp_button1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, timestamp_xpath1))
        )
        timestamp_button1.click()
        # 获取所有时间选项

        sleep(0.3)
        time_options1 = driver.find_elements(By.XPATH, time_options_xpath1)

        # 遍历时间选项，找到与 timestamp_result[0] 相匹配的选项并点击
        for option in time_options1:
            if option.text == timestamp_result[0]:
                option.click()
                break

        #定位时间戳2
        timestamp_button2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, timestamp_xpath2))
        )
        timestamp_button2.click()
        # 获取所有时间选项
        sleep(0.3)

        time_options2 = driver.find_elements(By.XPATH, time_options_xpath2)

        # 遍历时间选项，找到与 timestamp_result[0] 相匹配的选项并点击
        for option in time_options2:
            if option.text == timestamp_result[1]:
                option.click()
                break

        sleep(0.3)
        # 定位到座位，图书馆页面有的页面结构title里面还包含了需要冗余的元素
        seat_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//div[contains(@title, "{seats_number}")]'))
        )

        # 使用 JavaScript 点击座位元素
        driver.execute_script("arguments[0].click();", seat_element)
        #点击按钮进行提交座位申请
        subbmitte_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, button_xpath))
        )
        subbmitte_button.click()

        sleep(20)
        # 关闭浏览器
        driver.quit()





