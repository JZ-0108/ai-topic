from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	names="第七組"
	return render(request,"index.html",locals())


def Watering(request):
	return render(request, "Watering.html", locals())

def humidity(request):
	return render(request, "humidity.html", locals())

def temperature(request):
	return render(request, "temperature.html", locals())

def rain(request):
	return render(request, "rain.html", locals())
'''
	def news(request):
		posts = Post.objects.all()
		return render(request,"news.html",locals())

	@login_required(login_url="/admin/login/")
	def show(request,id):
		try:
			post = Post.objects.get(id=id)
		except:
			return redirect("/news/")
		return render(request,"show.html",locals())

	@login_required(login_url="/admin/login/")
	def rank(request):
		if request.method == 'POST':
			id = request.POST["id"]
			if id.strip() =="999":
				return redirect("/rank")
			try:
				country = Country.objects.get(id=id)
			except:
				return redirect("/rank/")
			cities = City.objects.filter(country=country)
		else:
			cities = City.objects.all().order_by('population')
		countries = Country.objects.all()
		return render(request, 'rank.html', locals())

	@login_required(login_url="/admin/login/")
	def chart(request):
		if request.method == 'POST':
			id = request.POST["id"]
			if id.strip()=="999":
				return redirect("/chart/")
			try:
				country = Country.objects.get(id=id)
			except:
				return redirect("/chart/")
			cities = City.objects.filter(country=country)
		else:
			cities = City.objects.all()
		countries = Country.objects.all()
		names = [city.name for city in cities]
		population = [city.population for city in cities]
		return render(request, "chart.html", locals())

	def mylogout(request):
		logout(request)
		return redirect("/")

	def delete(request,id):
		try:
			post = Post.objects.get(id=id)
			post.delete()
		except:
			return redirect("/news/")
		return redirect("/news/")

	def addnote(request):
		if request.method == "POST":
			title = request.POST["title"]
			if len(title) > 10:
				note = Note(title=title)
				note.save()
		return redirect("/note/")

	def note(request):
		notes = Note.objects.all()
		return render(request,"note.html",locals())
'''