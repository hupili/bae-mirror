# 用 BAE (百度应用引擎) 镜像站点 (Python)

就当是个BAE的Python环境的"hello world"吧。

## 用法

   * 注册什么的不多说了。
   * 进入应用管理界面，创建一个版本（只能通过web创建，之后可以Git管理）。
   可以创建20个版本，示例用“1”。
   web管理界面的“版本”，实质是Git repo下的一个子目录比如`1/`。
   可以通过三级域名访问，如`1.yourapp.duapp.com`, `2.yourapp.duapp.com`。
   * 通过Git克隆BAE的repo。下面已经有`1/`了。
   * 将该工程下的内容复制到`1/`中。
   commit并push代码，可以去应用域名看到一个
   [默认的镜像(点击查看示例)](http://1.snsapi.duapp.com/)。
   * 创建一个`config.py`，在里面添加一行设置要镜像的站点：
   `BASE_URL = 'http://snsapi.sinaapp.com'`.
   [样例](http://2.snsapi.duapp.com/).

## 改进

   * 对非200返回值的处理。如301和302等比较重要。
   * 可以将网页抓取结果存库以提高速度。
   * 动态页面：session维护，cookie处理等。
   * ...

还有不少可以改进的地方，不过对一个"hello world"来说太多了。
目前对于镜像静态页面的站点工作良好。
近期无改进计划，欢迎PR。

## License

[![copyleft](http://unlicense.org/pd-icon.png)](http://unlicense.org)
