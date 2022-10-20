from django.shortcuts import render, redirect
from .models import MessageRoom, DirectMessage
from django.contrib.auth.decorators import login_required
from .forms import DirectMessageForm

# Create your views here.


@login_required
def index(request):
    # send = request.user.touser_set.all()
    # receiver = request.user.fromuser_set.all()
    # context = {"messagerooms": send.union(receiver, all=True).order_by("-updated_at")}
    return render(request, "chat/index.html")


def send(request, pk):
    form = DirectMessageForm(request.POST or None)
    if form.is_valid():
        print(-1)
        print(MessageRoom.objects.filter(touser_id=request.user.id, fromuser_id=pk))
        if MessageRoom.objects.filter(touser_id=request.user.id, fromuser_id=pk):
            room = MessageRoom.objects.get(touser_id=request.user.id, fromuser_id=pk)
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
            if MessageRoom.objects.filter(touser_id=pk, fromuser_id=request.user.id):
                room = MessageRoom.objects.get(touser_id=pk, fromuser_id=request.user.id)
                temp = form.save(commit=False)
                temp.room_number_id = room.id
                temp.who_id = pk
                temp.save()
                room.last_user = request.user.username
                room.last_message = temp.content
                room.count += 1
                room.save()
            else:
                temp = form.save(commit=False)
                room = MessageRoom.objects.create(
                    touser_id=request.user.id,
                    fromuser_id=pk,
                    count=1,
                    last_user=request.user,
                    last_message=temp.content,
                )
                temp.room_number_id = room.id
                temp.who_id = pk
                temp.save()
                return redirect("chat:index")
    return render(request, "chat/send.html", {"form": form})
