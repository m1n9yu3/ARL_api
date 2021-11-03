# arl api 编写

该项目编写的目的, 因为当时使用的是 1h1g的小型主机，特别特别的卡，导致无法正常的删除任务，于是就有了这个项目

快速使用 arl api , 进行信息导出

基于[ARL](https://github.com/TophantTechnology/ARL)  开发







# 自动化任务设想

1. 根据 title 删除指定的 任务， 比如说 "云防护-站点不存在"
2. 删除相同的 target 
3. 相同任务名，子域名导出


# 使用方法

config.ini 文件 填充相应的配置


删除相同 target 的任务
```shell
python3 main.py --del_same
```


删除指定标题的资产任务
```shell
python3 main.py --del_title  xxx
```
比如 云防护-站点不存在





# 接口收集

登录接口
http://地址/api/user/login

任务查询
```http request
GET /api/task/?page=1&size=1000 HTTP/1.1
Host: xxxxxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
token: 45b5e144b84b04ebf1ced64d79589741
Connection: close
```
任务停止
```http request
GET /api/task/stop/6063de21081e5e00123a623d HTTP/1.1
Host: xxxxxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
token: 45b5e144b84b04ebf1ced64d79589741
Connection: close
```

任务批量停止
```http request
POST /api/task/batch_stop/ HTTP/1.1
Host: xxxxxxxx
Content-Length: 283
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
token: 45b5e144b84b04ebf1ced64d79589741
Content-Type: application/json; charset=UTF-8
Connection: close

{"task_id":["6063de21081e5e00123a623d","6063de21081e5e00123a623c","6063de21081e5e00123a623b","6063de21081e5e00123a623a","6063de21081e5e00123a6239","6063de21081e5e00123a6238","6063de21081e5e00123a6237","6063de21081e5e00123a6236","6063de21081e5e00123a6235","6063de21081e5e00123a6234"]}
```
任务批量删除
```http request
POST /api/task/delete/ HTTP/1.1
Host: xxxxxxxx
Content-Length: 304
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
token: 45b5e144b84b04ebf1ced64d79589741
Content-Type: application/json; charset=UTF-8
Connection: close

{"del_task_data":true,"task_id":["6063de21081e5e00123a623d","6063de21081e5e00123a623c","6063de21081e5e00123a623b","6063de21081e5e00123a623a","6063de21081e5e00123a6239","6063de21081e5e00123a6238","6063de21081e5e00123a6237","6063de21081e5e00123a6236","6063de21081e5e00123a6235","6063de21081e5e00123a6234"]}
```

任务添加
```http request
POST /api/task/ HTTP/1.1
Host: xxxxxxxx
Content-Length: 365
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
token: 45b5e144b84b04ebf1ced64d79589741
Content-Type: application/json; charset=UTF-8
Connection: close

{"name":"test","target":"http://baidu.com","domain_brute_type":"big","port_scan_type":"top100","domain_brute":true,"alt_dns":true,"riskiq_search":true,"arl_search":true,"port_scan":true,"service_detection":true,"os_detection":true,"fofa_search":true,"ssl_cert":true,"site_identify":true,"search_engines":true,"site_spider":true,"site_capture":true,"file_leak":true}
```


资产搜索
```http request
GET /api/site/?page=1&size=10&tabIndex=0&ts=1618221346906 HTTP/1.1
Host: xxxxxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
token: 45b5e144b84b04ebf1ced64d79589741
Content-Length: 21
Connection: close
```

资产标题搜索
```http request
GET /api/site/?page=1&size=100&tabIndex=0&ts=1618224528539&title=%E7%AB%99%E7%82%B9%E4%B8%8D%E5%AD%98%E5%9C%A8 HTTP/1.1
Host: xxxxxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
token: 45b5e144b84b04ebf1ced64d79589741
Connection: close


```


资产删除
```http request
POST /api/task/delete/ HTTP/1.1
Host: xxxxxxx
Content-Length: 61
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
token: 45b5e144b84b04ebf1ced64d79589741
Content-Type: application/json; charset=UTF-8
Connection: close

{"task_id":["6063ddfc081e5e00113f3561"],"del_task_data":true}
```
