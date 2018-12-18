from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Business, User, Review
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserForm
from django.urls import reverse_lazy
from .filters import UserFilter
from django_filters.views import FilterView


class AboutPageView(generic.TemplateView):
	template_name = 'yelp/about.html'

class HomePageView(generic.TemplateView):
	template_name = 'yelp/home.html'

class BusinessListView(generic.ListView):
	model = Business
	context_object_name = 'businesses'
	template_name = 'yelp/business.html'
	paginate_by = 100

	def get_queryset(self):
		return Business.objects.all()\
                                .select_related('city', 'state', 'noise_level', 'attire')\
                                .order_by('business_name')

class BusinessDetailListView(generic.DetailView):
	model = Business
	context_object_name = 'business'
	template_name = 'yelp/business_detail.html'

@method_decorator(login_required, name='dispatch')
class UserListView(generic.ListView):
	model = User
	context_object_name = 'users'
	template_name = 'yelp/user.html'
	paginate_by = 100

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return User.objects.all()\
                                .order_by('user_name')

@method_decorator(login_required, name='dispatch')
class UserDetailListView(generic.DetailView):
	model = User
	context_object_name = 'user_'
	template_name = 'yelp/user_detail.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

@method_decorator(login_required, name='dispatch')
class ReviewListView(generic.ListView):
	model = Review
	context_object_name = 'reviews'
	template_name = 'yelp/review.html'
	paginate_by = 50

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Review.objects.all()\
                                .select_related('user', 'business')\
                                .order_by('business')

@method_decorator(login_required, name='dispatch')
class ReviewDetailListView(generic.DetailView):
	model = Review
	context_object_name = 'review'
	template_name = 'yelp/review_detail.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


## Form Views

@method_decorator(login_required, name='dispatch')
class UserCreateView(generic.View):
	model = User
	form_class = UserForm
	success_message = "User created successfully"
	template_name = 'yelp/user_new.html'
	# fields = '__all__' <-- superseded by form_class
	# success_url = reverse_lazy('heritagesites/site_list')

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def post(self, request):
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			for business in form.cleaned_data['business']:
				Review.objects.create(user=user, business=business)
			# return redirect(user) # shortcut to object's get_absolute_url()
			return HttpResponseRedirect(user.get_absolute_url())
		return render(request, 'yelp/user_new.html', {'form': form})

	def get(self, request):
		form = UserForm()
		return render(request, 'yelp/user_new.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(generic.UpdateView):
	model = User
	form_class = UserForm
	# fields = '__all__' <-- superseded by form_class
	context_object_name = 'user'
	# pk_url_kwarg = 'site_pk'
	success_message = "User updated successfully"
	template_name = 'yelp/user_update.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		user = form.save(commit=False)
		# site.updated_by = self.request.user
		# site.date_updated = timezone.now()
		user.save()

		# Current country_area_id values linked to site
		old_ids = Review.objects\
			.values_list('business_id', flat=True)\
			.filter(user_id=user.user_id)

		# New countries list
		businesses = form.cleaned_data['business']
		# review = form.cleaned_data['review_text']		#New and check
		# New ids
		new_ids = []

		# Insert new unmatched country entries
		for business in businesses:
			new_id = business.business_id
			new_ids.append(new_id)
			if new_id in old_ids:
				continue
			else:
				Review.objects.create(user=user, business=business)

		# Delete old unmatched country entries
		for old_id in old_ids:
			if old_id in new_ids:
				continue
			else:
				Review.objects \
					.filter(user_id=user.user_id, business_id=old_id) \
					.delete()

		return HttpResponseRedirect(user.get_absolute_url())
		# return redirect('heritagesites/site_detail', pk=site.pk)

class UserDeleteView(generic.DeleteView):
	model = User
	success_message = "User deleted successfully"
	success_url = reverse_lazy('user')
	context_object_name = 'user'
	template_name = 'yelp/user_delete.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()

		# Delete HeritageSiteJurisdiction entries
		Review.objects \
			.filter(user_id=self.object.user_id) \
			.delete()

		self.object.delete()

		return HttpResponseRedirect(self.get_success_url())

class UserFilterView(FilterView):
	filterset_class = UserFilter
	template_name = 'yelp/site_filter.html'