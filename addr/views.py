from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Friend
from  .forms import FriendForm, MemoForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def friend_list(request):
    friends = Friend.objects.filter(approved_friend=1)
    return render(request, 'addr/friend_list.html',{'friends': friends})


def friend_detail(request, pk):
    friend = get_object_or_404(Friend, pk=pk)
    return render(request, 'addr/friend_detail.html', {'friend': friend})

@login_required
def friend_new(request):
    if request.method == "POST":
        form = FriendForm(request.POST)
        if form.is_valid():
            friend = form.save(commit=False)
            friend.author = User.objects.get(id=1)
            friend.save()
            return redirect('addr:friend_detail', pk=friend.pk)
    else:
        form = FriendForm()
    return render(request, 'addr/friend_edit.html', {'form': form})


@login_required
def friend_edit(request, pk):
    friend = get_object_or_404(Friend, pk=pk)
    if request.method == "POST":
        form = FriendForm(request.POST, instance=friend)
        if form.is_valid():
            friend = form.save(commit=False)
            friend.author = User.objects.get(id=1)
            friend.save()
            return redirect('addr:friend_detail', pk=friend.pk)
    else:
        form = FriendForm(instance=friend)
    return render(request, 'addr/friend_edit.html', {'form': form})

@login_required
def friend_draft_list(request):
    friends = Friend.objects.filter(approved_friend=0)
    return render(request, 'addr/friend_draft_list.html', {'friends': friends})

@login_required
def friend_approve(request, pk):
    friend = get_object_or_404(Friend, pk=pk)
    friend.approve()
    return redirect('addr:friend_detail', pk=friend.pk)

@login_required
def friend_remove(request, pk):
    friend = get_object_or_404(Friend, pk=pk)
    friend.delete()
    return redirect('addr:friend_list')


def add_memo_to_friend(request, pk):
    friend = get_object_or_404(Friend, pk=pk)
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.friend = friend
            memo.save()
            return redirect('friend_detail', pk=friend.pk)
    else:
        form = MemoForm()
    return render(request, 'addr/add_memo_to_friend.html',{'form':form})