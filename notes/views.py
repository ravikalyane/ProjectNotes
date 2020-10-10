from django.shortcuts import render, redirect
from .models import Note, Profile
from .forms import NotesForm, RegisterForm


def temp(request):
    profile1 = Profile.objects.get_or_create(name="priya")
    #profile = Profile.objects.all()
    return render(request, 'temp.html', {'profile1': profile1})


def index(request):
    if request.user.is_active:
        notes = Note.objects.filter(user=request.user, archive=False).order_by('-pinned')
    else:
        notes = Note.objects.all()
    return render(request, 'index.html', {'notes': notes})


def add_note(request):
    notes = Note.objects.all()
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.user = request.user
            notes.save()
            return redirect('/')
    else:
        form = NotesForm()
    return render(request, 'take_note.html', {'form': form, 'notes': notes})


def edit_note(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = NotesForm()
        else:
            note = Note.objects.get(id=id)
            form = NotesForm(instance=note)
        return render(request, 'edit_note.html', {'form': form})
    else:
        if id == 0:
            form = NotesForm(request.POST)
        else:
            note = Note.objects.get(id=id)
            form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
        return redirect('/')


def view_note(request, pk):
    notes = Note.objects.get(id=pk)
    return render(request, 'view_note.html', {'notes': notes})


def archived_note(request):
    notes = Note.objects.filter(archive=True)
    return render(request, 'archived_note.html', {'notes': notes})


def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect('/')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegisterForm
    return render(request, 'register.html', {'form': form})
