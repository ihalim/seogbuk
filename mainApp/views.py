from django.shortcuts import render

# Create your views here.
def map(request):
	varlat = 37.589672;
	varlng = 127.005745;
	name = "성북 문화원";
	return render(request, 'mainApp/map.html', {'varlat': varlat,'varlng': varlng,
		'name':name})

def map2(request):
	varlat= 37.593879;
	varlng= 126.991767;
	name = "심우장";
	return render(request, 'mainApp/map.html',{'varlat': varlat, 'varlng' : varlng,
		'name':name})

def map3(request):
	varlat= 37.598924;
	varlng= 126.994380;
	name = "길상사";
	return render(request, 'mainApp/map.html',{'varlat': varlat, 'varlng' : varlng,
		'name':name})

def map4(request):
	varlat= 37.594093;
	varlng= 126.994518;
	name = "이재준가";
	return render(request, 'mainApp/map.html',{'varlat': varlat, 'varlng' : varlng,
		'name':name})

def map5(request):
	varlat= 37.595168;
	varlng= 126.994697;
	name = "수연산방";
	return render(request, 'mainApp/map.html',{'varlat': varlat, 'varlng' : varlng,
		'name':name})
