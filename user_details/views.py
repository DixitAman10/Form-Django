from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import UserProfileForm
from .models import UserDetails


class CreateProfileView(View):

    template_name = 'user_details/create_profile.html'

    def get_context_data(self, *args, **kwargs):

        ctx = {}
        ctx['user_profile_form'] = UserProfileForm()
        return ctx

    def get(self, *args, **kwargs):

        ctx = self.get_context_data(*args, **kwargs)
        return render(self.request, self.template_name, ctx)

    def get_success_url(self, user_id):
        print('*****')
        
        return reverse_lazy('user_details:user_profile',
                            kwargs={'user_id': user_id})

    def post(self, *args, **kwargs):

        user_profile_form = UserProfileForm(self.request.POST)

        if user_profile_form.is_valid():
            print('form_valid')
            return self.form_valid(user_profile_form)

        else:
            print('form_invalid')
            return self.form_invalid(user_profile_form)

    def form_valid(self, user_profile_form):

        user_profile_form.save()
        email = user_profile_form.cleaned_data['email']
        user_id = UserDetails.objects.get(email=email).pk

        return HttpResponseRedirect(self.get_success_url(user_id))

    def form_invalid(self, user_profile_form):

        ctx = {'user_profile_form': user_profile_form}
        return render(self.request, self.template_name, ctx)


class UserProfileView(View):

    template_name = 'user_details/user_profile.html'

    def get_context_data(self, *args, **kwargs):

        ctx = {}
        ctx['user_profile'] = UserDetails.objects.get(pk=kwargs['user_id'])
        return ctx

    def get(self, *args, **kwargs):

        ctx = self.get_context_data(*args, **kwargs)
        return render(self.request, self.template_name, ctx)

