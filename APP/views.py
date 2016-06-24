#coding: utf-8
from json import loads
from urllib import urlopen
from APP.models import IPdb
from django.shortcuts import render
from collections import OrderedDict

def index(request):
	# myip用来获取本地IP
	return render(request, 'index.html', {'data' : SearchIP('myip')})
	
def handle(request):
	# IP为用户输入的ip
	return render(request, 'other.html', {'data' : SearchIP(request.GET['ip'])})
	
def get_ips(request):
	#获取数据库中的历史记录
	ips = IPdb.objects.all().order_by('-date')[:10]
	return render(request, 'ips.html', {'ips' : ips})

def SearchIP(ip):
	# 调用淘宝IP库,检验IP合法性,查询IP地理位置
	keys = ['ip', 'country', 'area', 'region', 'city']
	url = 'http://ip.taobao.com/service/getIpInfo.php?ip='+ip
	data = urlopen(url).read()
	jsondata = loads(data)
	if jsondata[u'code'] == 0:
		data = jsondata[u'data']
		info = [data[key.decode()].encode('utf-8') for key in keys]
		if ip != 'myip':
			# 将查询到的信息保存进数据库
			IPdb.objects.create(ip=info[0], addr=(info[1]+info[2]+info[3]+info[4]))
		return info
	else:
		return ['IP is invalid']
