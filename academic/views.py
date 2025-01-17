from django.shortcuts import render, redirect
from .models import AcademicSession
from .forms import AcademicSessionForm
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DeleteView, DetailView
from django.urls import reverse_lazy

# Create your views here.
def session_list_create_update(request, pk=None):
    if pk:
        academic_session = get_object_or_404(AcademicSession, pk=pk)
    else:
        academic_session = None

    if request.method == 'POST':
        if academic_session:
            form = AcademicSessionForm(request.POST, instance=academic_session)
        else:
            form = AcademicSessionForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('session-list-create-update')

    else:
        if academic_session:
            form = AcademicSessionForm(instance=academic_session)
        else:
            form = AcademicSessionForm()

    academic_sessions = AcademicSession.objects.all()
    return render(request, 'academic/session_list_create_update.html', {'form': form, 'academic_sessions': academic_sessions, 'edit_academic_session': academic_session})

class SessionDeleteView(DeleteView):
    model = AcademicSession
    template_name = "academic/session_delete.html"
    success_url = reverse_lazy('session-list-create-update')

class SessionDetailView(DetailView):
    model = AcademicSession
    template_name = "academic/session_detail.html"
    context_object_name = 'academic_session'
#=======================================================================================S
