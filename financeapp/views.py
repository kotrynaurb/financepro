from django.shortcuts import render, redirect, get_object_or_404, reverse

from django.db.models import Q
from django.core.paginator import Paginator

from django.views import generic
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

from .models import (Income, IncomeCategory, Expense, Company, ExpenseCategory, Bill, BillIssuer,  BillCategory,
                     AppReview, Profile)
from .forms import (ProfileUpdateForm, UserUpdateForm, IncomeCreateForm, IncomeCategoryCreateForm, ExpenseCreateForm,
                    CompanyCreateForm, ExpenseCategoryCreateForm, BillCreateForm, BillIssuerCreateForm,
                    BillCategoryCreateForm, AppReviewForm)
from .utils import get_income_plot, get_expenses_bar, get_bills_scatter


def index(request):
    """
    Gražina vartotojo apsilankymo puslapyje sesijų skaičių
    :param request:
    :return: render
    """
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {'num_visits': num_visits}

    return render(request, 'index.html', context=context)


@login_required
def income_graph_view(request):
    qs = Income.objects.filter(user=request.user)
    x = [x.date for x in qs]
    y = [y.amount for y in qs]
    chart = get_income_plot(x, y)

    total_amount = 0
    for total_amnt in Income.objects.filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount}

    return render(request, 'statistics_income.html', context=context)


@login_required
def income_graph_view_monthly(request):
    qs = Income.objects.filter(date__month=6).filter(user=request.user)
    x = [x.date for x in qs]
    y = [y.amount for y in qs]
    chart = get_income_plot(x, y)

    total_amount_monthly = 0
    for total_amnt in Income.objects.filter(date__month=6).filter(user=request.user):
        total_amount_monthly += total_amnt.amount

    context = {'chart': chart,
               'total_amount_monthly': total_amount_monthly}

    return render(request, 'statistics_income_monthly.html', context=context)


@login_required
def income_graph_view_c1(request):
    qs = Income.objects.filter(income_category__exact=1).filter(user=request.user)
    x = [x.date for x in qs]
    y = [y.amount for y in qs]
    chart = get_income_plot(x, y)

    total_amount = 0
    for total_amnt in Income.objects.filter(income_category__exact=1).filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount,
               }

    return render(request, 'statistics_income_c1.html', context=context)


@login_required
def income_graph_view_c2(request):
    qs = Income.objects.filter(income_category__exact=2).filter(user=request.user)
    x = [x.date for x in qs]
    y = [y.amount for y in qs]
    chart = get_income_plot(x, y)

    total_amount = 0
    for total_amnt in Income.objects.filter(income_category__exact=2).filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount,
               }

    return render(request, 'statistics_income_c2.html', context=context)


@login_required
def income_graph_view_c3(request):
    qs = Income.objects.filter(income_category__exact=3).filter(user=request.user)
    x = [x.date for x in qs]
    y = [y.amount for y in qs]
    chart = get_income_plot(x, y)

    total_amount = 0
    for total_amnt in Income.objects.filter(income_category__exact=3).filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount,
               }

    return render(request, 'statistics_income_c3.html', context=context)


@login_required
def income_graph_view_c4(request):
    qs = Income.objects.filter(income_category__exact=8).filter(user=request.user)
    x = [x.date for x in qs]
    y = [y.amount for y in qs]
    chart = get_income_plot(x, y)

    total_amount = 0
    for total_amnt in Income.objects.filter(income_category__exact=8).filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount,
               }

    return render(request, 'statistics_income_c4.html', context=context)


@login_required
def expenses_graph_view(request):
    qs = Expense.objects.filter(user=request.user)
    x = [x.date for x in qs]
    y = [y.amount for y in qs]
    chart = get_expenses_bar(x, y)

    total_amount = 0
    for total_amnt in Expense.objects.filter(user=request.user):
        total_amount += total_amnt.amount

    total_income = 0
    for total_amnt in Income.objects.filter(user=request.user):
        total_income += total_amnt.amount

    total_bills = 0
    for total_amnt in Bill.objects.filter(user=request.user):
        total_bills += total_amnt.amount

    total_balance = total_income - total_amount - total_bills

    context = {'chart': chart,
               'total_amount': total_amount,
               'total_balance': total_balance,
               }

    return render(request, 'statistics_expense.html', context=context)


@login_required
def expenses_graph_view_monthly(request):
    qs = Expense.objects.filter(date__month=6).filter(user=request.user)
    x = [x.date for x in qs]
    y = [y.amount for y in qs]
    chart = get_expenses_bar(x, y)

    total_amount_monthly = 0
    for total_amnt in Expense.objects.filter(date__month=6).filter(user=request.user):
        total_amount_monthly += total_amnt.amount

    total_income_monthly = 0
    for total_amnt in Income.objects.filter(date__month=6).filter(user=request.user):
        total_income_monthly += total_amnt.amount

    total_bills_monthly = 0
    for total_amnt in Bill.objects.filter(date_due__month=6).filter(user=request.user):
        total_bills_monthly += total_amnt.amount

    total_balance_monthly = total_income_monthly - total_amount_monthly - total_bills_monthly

    context = {'chart': chart,
               'total_amount_monthly': total_amount_monthly,
               'total_balance_monthly': total_balance_monthly
               }

    return render(request, 'statistics_expense_monthly.html', context=context)


@login_required
def expenses_graph_view_c1(request):
    qs = Expense.objects.filter(expense_category__exact=1).filter(user=request.user)
    x = [x.date for x in qs]
    y = [y.amount for y in qs]
    chart = get_expenses_bar(x, y)

    total_amount = 0
    for total_amnt in Expense.objects.filter(expense_category__exact=1).filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount,
               }

    return render(request, 'statistics_expense_c1.html', context=context)


@login_required
def expenses_graph_view_c2(request):
    qs = Expense.objects.filter(expense_category__exact=2).filter(user=request.user)
    x = [x.date for x in qs]
    y = [y.amount for y in qs]
    chart = get_expenses_bar(x, y)

    total_amount = 0
    for total_amnt in Expense.objects.filter(expense_category__exact=2).filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount,
               }

    return render(request, 'statistics_expense_c2.html', context=context)


@login_required
def expenses_graph_view_c3(request):
    qs = Expense.objects.filter(expense_category__exact=3).filter(user=request.user)
    x = [x.date for x in qs]
    y = [y.amount for y in qs]
    chart = get_expenses_bar(x, y)

    total_amount = 0
    for total_amnt in Expense.objects.filter(expense_category__exact=3).filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount,
               }

    return render(request, 'statistics_expense_c3.html', context=context)


@login_required
def expenses_graph_view_c4(request):
    qs = Expense.objects.filter(expense_category__exact=6).filter(user=request.user)
    x = [x.date for x in qs]
    y = [y.amount for y in qs]
    chart = get_expenses_bar(x, y)

    total_amount = 0
    for total_amnt in Expense.objects.filter(expense_category__exact=6).filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount,
               }

    return render(request, 'statistics_expense_c3.html', context=context)


@login_required
def expenses_graph_view_c5(request):
    qs = Expense.objects.filter(expense_category__exact=7).filter(user=request.user)
    x = [x.date for x in qs]
    y = [y.amount for y in qs]
    chart = get_expenses_bar(x, y)

    total_amount = 0
    for total_amnt in Expense.objects.filter(expense_category__exact=7).filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount,
               }

    return render(request, 'statistics_expense_c3.html', context=context)


@login_required
def bills_scatter_view(request):
    qs = Bill.objects.filter(user=request.user)
    x = [x.date_due for x in qs]
    y = [y.amount for y in qs]
    chart = get_bills_scatter(x, y)

    total_amount = 0
    for total_amnt in Bill.objects.filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount,
               }

    return render(request, 'statistics_bill.html', context=context)


@login_required
def bills_scatter_view_monthly(request):
    qs = Bill.objects.filter(date_due__month=6).filter(user=request.user)
    x = [x.date_due for x in qs]
    y = [y.amount for y in qs]
    chart = get_bills_scatter(x, y)

    total_amount_monthly = 0
    for total_amnt in Bill.objects.filter(date_due__month=6).filter(user=request.user):
        total_amount_monthly += total_amnt.amount

    context = {'chart': chart,
               'total_amount_monthly': total_amount_monthly,
               }

    return render(request, 'statistics_bill_monthly.html', context=context)


@login_required
def bills_scatter_view_c1(request):
    qs = Bill.objects.filter(bill_category__exact=1).filter(user=request.user)
    x = [x.date_due for x in qs]
    y = [y.amount for y in qs]
    chart = get_bills_scatter(x, y)

    total_amount = 0
    for total_amnt in Bill.objects.filter(bill_category__exact=1).filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount,
               }

    return render(request, 'statistics_bill_c1.html', context=context)


@login_required
def bills_scatter_view_c2(request):
    qs = Bill.objects.filter(bill_category__exact=2).filter(user=request.user)
    x = [x.date_due for x in qs]
    y = [y.amount for y in qs]
    chart = get_bills_scatter(x, y)

    total_amount = 0
    for total_amnt in Bill.objects.filter(bill_category__exact=2).filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount,
               }

    return render(request, 'statistics_bill_c2.html', context=context)


@login_required
def bills_scatter_view_c3(request):
    qs = Bill.objects.filter(bill_category__exact=3).filter(user=request.user)
    x = [x.date_due for x in qs]
    y = [y.amount for y in qs]
    chart = get_bills_scatter(x, y)

    total_amount = 0
    for total_amnt in Bill.objects.filter(bill_category__exact=3).filter(user=request.user):
        total_amount += total_amnt.amount

    context = {'chart': chart,
               'total_amount': total_amount,
               }

    return render(request, 'statistics_bill_c3.html', context=context)


@login_required
def get_income(request):
    income = Income.objects.filter(user=request.user).order_by('date')
    paginator = Paginator(income, 6)
    page_number = request.GET.get('page')
    paged_income = paginator.get_page(page_number)

    context = {
        'income': paged_income
    }
    return render(request, 'all_income.html', context=context)


@login_required
def get_single_income(request, income_id):
    single_income = get_object_or_404(Income, pk=income_id, user=request.user)
    return render(request, 'income.html', {'income_obj': single_income})


class ExpenseListView(LoginRequiredMixin, generic.ListView):
    model = Expense
    context_object_name = 'expense_list'
    template_name = 'expenses.html'
    paginate_by = 6

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)


class ExpenseDetailView(LoginRequiredMixin, generic.DetailView):
    model = Expense
    context_object_name = 'expense'
    template_name = 'expense.html'

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)


class BillListView(LoginRequiredMixin, generic.ListView):
    model = Bill
    context_object_name = 'bill_list'
    template_name = 'bills.html'
    paginate_by = 6

    def get_queryset(self):
        return Bill.objects.filter(user=self.request.user)


class BillDetailView(LoginRequiredMixin, generic.DetailView):
    model = Bill
    context_object_name = 'bill'
    template_name = 'bill.html'

    def get_queryset(self):
        return Bill.objects.filter(user=self.request.user)


def search(request):
    query_text = request.GET['search_text']
    search_results_income = Income.objects.filter(Q(amount__icontains=query_text) |
                                                  Q(date__icontains=query_text) |
                                                  Q(income_category__category__icontains=query_text))

    search_results_expense = Expense.objects.filter(Q(amount__icontains=query_text) |
                                                    Q(date__icontains=query_text) |
                                                    Q(expense_category__category__icontains=query_text))

    search_results_bill = Bill.objects.filter(Q(amount__icontains=query_text) |
                                              Q(date_paid__icontains=query_text) |
                                              Q(date_due__icontains=query_text) |
                                              Q(bill_category__category__icontains=query_text))

    context = {'income_list': search_results_income,
               'expense_list': search_results_expense,
               'bill_list': search_results_bill,
               'query_text': query_text}

    return render(request, 'search.html', context=context)


@csrf_protect
def register_user(request):
    if request.method == 'GET':
        return render(request, 'registration/registration.html')
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.warning(request, "Passwords don't match")

        if User.objects.filter(username=username).exists():
            messages.warning(request, f'Username {username} is taken')

        if not email:
            messages.warning(request, 'Email is not entered')

        if User.objects.filter(email=email).exists():
            messages.warning(request, f'Email {email} already in use')

        if messages.get_messages(request):
            return redirect('register-url')

        User.objects.create_user(username=username, email=email, password=password)
        messages.info(request, f'User {username} created successfully!')
        return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.info(request, "Profile updated")
        else:
            messages.warning(request, "Profile not updated")
        return redirect('profile-url')

    p_form = ProfileUpdateForm(instance=request.user.profile)
    u_form = UserUpdateForm(instance=request.user)

    context = {
        'p_form': p_form,
        'u_form': u_form
    }

    return render(request, 'profile.html', context=context)


class IncomeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Income
    form_class = IncomeCreateForm
    template_name = 'income_create_form.html'
    success_url = '/finance/allincome'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseCreateView(LoginRequiredMixin, generic.CreateView):
    model = Expense
    form_class = ExpenseCreateForm
    template_name = 'expense_create_form.html'
    success_url = '/finance/expenses'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BillCreateView(LoginRequiredMixin, generic.CreateView):
    model = Bill
    form_class = BillCreateForm
    template_name = 'bill_create_form.html'

    def get_success_url(self):
        return reverse('bill-all')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Income
    template_name = 'income_delete.html'
    success_url = '/finance/allincome'

    def test_func(self):
        income_object = self.get_object()
        return income_object.user == self.request.user


class ExpenseDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Expense
    template_name = 'expense_delete.html'
    success_url = '/finance/expenses'

    def test_func(self):
        income_object = self.get_object()
        return income_object.user == self.request.user


class BillDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Bill
    template_name = 'bill_delete.html'
    success_url = '/finance/bills'

    def test_func(self):
        bill_object = self.get_object()
        return bill_object.user == self.request.user


class IncomeUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Income
    form_class = IncomeCreateForm
    template_name = 'income_create_form.html'
    success_url = '/finance/allincome'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        income_object = self.get_object()
        return income_object.user == self.request.user


class ExpenseUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Expense
    form_class = ExpenseCreateForm
    template_name = 'expense_create_form.html'
    success_url = '/finance/expenses'

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        income_object = self.get_object()
        return income_object.user == self.request.user


class BillUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Bill
    form_class = BillCreateForm
    template_name = 'bill_create_form.html'
    success_url = '/finance/bills'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        bill_object = self.get_object()
        return bill_object.user == self.request.user


class AppReviewListView(generic.edit.FormMixin, generic.ListView):
    model = AppReview
    context_object_name = 'appreview'
    template_name = 'reviews.html'
    form_class = AppReviewForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.reviewer = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('reviews')


class AppReviewListView2(generic.edit.FormMixin, generic.ListView):
    model = AppReview
    context_object_name = 'appreview2'
    template_name = 'reviews_logged_out.html'
    form_class = AppReviewForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.reviewer = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('reviews')


class IncomeCategoryModeratorCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = IncomeCategory
    form_class = IncomeCategoryCreateForm
    template_name = 'moderator_income_category_create_form.html'

    def get_success_url(self):
        return reverse('income-new',)

    def test_func(self):
        return self.request.user.groups.filter(name='moderators').exists()


class ExpenseCategoryModeratorCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = ExpenseCategory
    form_class = ExpenseCategoryCreateForm
    template_name = 'moderator_expense_category_create_form.html'

    def get_success_url(self):
        return reverse('expense-new',)

    def test_func(self):
        return self.request.user.groups.filter(name='moderators').exists()


class CompanyModeratorCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Company
    form_class = CompanyCreateForm
    template_name = 'moderator_company_create_form.html'

    def get_success_url(self):
        return reverse('expense-new', )

    def test_func(self):
        return self.request.user.groups.filter(name='moderators').exists()


class BillCategoryModeratorCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = BillCategory
    form_class = BillCategoryCreateForm
    template_name = 'moderator_bill_category_create_form.html'

    def get_success_url(self):
        return reverse('bill-new', )

    def test_func(self):
        return self.request.user.groups.filter(name='moderators').exists()


class BillIssuerModeratorCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = BillIssuer
    form_class = BillIssuerCreateForm
    template_name = 'moderator_bill_issuer_create_form.html'

    def get_success_url(self):
        return reverse('bill-new', )

    def test_func(self):
        return self.request.user.groups.filter(name='moderators').exists()
