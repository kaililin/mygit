import requests
import json
import pytest
import allure
import pymysql
headers = {'Accept': 'application/json, text/plain, */*',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Accept - Encoding': 'gzip, deflate',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
           "Content-Type": "application/json"}
urldz = "http://cqb-mgr.test.sh-weiyi.com"
connect = pymysql.connect('47.106.193.243', 'cqb_dict', 'cqb_dict', 'cqb_dict')  # 建立连接
@allure.feature('登录接口')
class Testlogin():
    @allure.story('登录')
    def login(self):

        headers = {'Host': 'cqb-mgr.test.sh-weiyi.com', 'Accept': 'application/json, text/plain, */*',
                       'Referer': 'cqb-mgr.test.sh-weiyi.com/cqb-dict-fe/app.html', 'Accept-Language': 'zh-CN,zh;q=0.9',
                       'Origin': 'http://cqb-mgr.test.sh-weiyi.com.com', 'Accept - Encoding': 'gzip, deflate',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                       "Content-Type": "application/json"}
        session=requests.session()
        data = {'userName': 'admin', 'password': '275544e07a917b07633402b8775dd25f', 'kaptcha': '22'}
        login_url = "http://cqb-mgr.test.sh-weiyi.com/cqb-dict-server/service/system/login"
        login = session.post(url=login_url, data=json.dumps(data), headers=headers)
        result=login.status_code
        assert 200 == result
        return session.cookies.get_dict()

    @allure.story('验证码')
    def test_kaptcha(self):
        headers = {'Host': 'cqb-mgr.test.sh-weiyi.com', 'Accept': 'application/json, text/plain, */*',
                       'Referer': 'cqb-mgr.test.sh-weiyi.com/cqb-dict-fe/app.html', 'Accept-Language': 'zh-CN,zh;q=0.9',
                       'Origin': 'http://cqb-mgr.test.sh-weiyi.com', 'Accept - Encoding': 'gzip, deflate',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                       "Content-Type": "application/json"}
        kaptcha_url="http://cqb-mgr.test.sh-weiyi.com/cqb-dict-server/service/system/kaptcha"
        kaptcha=requests.get(url=kaptcha_url,headers=headers)
        ka=kaptcha.status_code
        assert 200 == ka

if __name__ == '__main__':
    pytest.main()