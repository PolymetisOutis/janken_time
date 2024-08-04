from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from base import forms
from base.models import Champion, CustomUser, Category

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import DeleteView
from django.http import HttpResponseRedirect

@login_required
def self_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    if request.method == 'POST':
      edit_form = forms.UserEditForm(
      request.POST or None, 
      request.FILES or None, 
      instance = request.user
      )
      if edit_form.is_valid():
        messages.success(request, 'You have been updated')
        edit_form.save()


    champ_list = []
    for i in user.champions.all():
        champ_list.append(i)
    matches = user.matches
    wins = user.wins
    wins_rate = user.wins_rate
    print(matches)
    context = {
      'champions': champ_list,
      'matches': matches,
      'wins': wins,
      'wins_rate': wins_rate,
      }
    return render(request, 'account/self_profile.html', context)


@login_required # 以下追記箇所
def edit_page(request):
  edit_form = forms.UserEditForm(
    request.POST or None, 
    request.FILES or None, 
    instance = request.user
    )
  if edit_form.is_valid():
    messages.success(request, 'You have been updated')
    edit_form.save()
  return render(request, 'account/edit_page.html', context={
      'edit_form': edit_form,
  })
  # return redirect('base:self_profile')



class AccountDeleteView(LoginRequiredMixin, DeleteView):
  model = CustomUser  # あなたのユーザーモデル
  success_url = reverse_lazy('index')  # 退会後のリダイレクト先
  template_name = 'account/account_confirm_delete.html'

  def get_object(self, queryset=None):
      return self.request.user

  def delete(self, request, *args, **kwargs):
      user = self.get_object()
      logout(request)
      messages.success(request, '退会処理が完了しました。')
      user.delete()
      return HttpResponseRedirect(self.success_url)