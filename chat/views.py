from django.shortcuts import render, redirect
from .models import MessageRoom, DirectMessage
from django.contrib.auth.decorators import login_required
from .forms import DirectMessageForm

# Create your views here.


@login_required
def index(request):
    send = MessageRoom.objects.filter(to_user=request.user)
    receiver = MessageRoom.objects.filter(from_user=request.user)
    context = {"messagerooms": send.union(receiver, all=False).order_by("-updated_at")}
    return render(request, "chat/index.html", context)


def detail(request, user_id):
    message = DirectMessage.objects.filter()
    form = DirectMessageForm()
    pass


def send(request, pk):
    form = DirectMessageForm(request.POST or None)
    if form.is_valid():
        if MessageRoom.objects.filter(to_user_id=request.user.id, from_user_id=pk).exists():
            room = MessageRoom.objects.get(to_user_id=request.user.id, from_user_id=pk)
            temp = form.save(commit=False)
            temp.room_number_id = room.id
            temp.who_id = pk
            temp.save()
            room.last_user = request.user.username
            room.last_message = temp.content
            room.count += 1
            room.save()
            return redirect("chat:index")
        else:
            if MessageRoom.objects.filter(to_user_id=pk, from_user_id=request.user.id).exists():
                room = MessageRoom.objects.get(to_user_id=pk, from_user_id=request.user.id)
                temp = form.save(commit=False)
                temp.room_number_id = room.id
                temp.who_id = pk
                temp.save()
                room.last_user = request.user.username
                room.last_message = temp.content
                room.count += 1
                room.save()
                return redirect("chat:index")
            else:
                temp = form.save(commit=False)
                room = MessageRoom.objects.create(
                    to_user_id=request.user.id,
                    from_user_id=pk,
                    count=1,
                    last_user=request.user,
                    last_message=temp.content,
                )
                temp.room_number_id = room.id
                temp.who_id = pk
                temp.save()
                return redirect("chat:index")
    return render(request, "chat/send.html", {"form": form})
