from django import forms

from .models import (Profile, User, Income, IncomeCategory, Expense, Company, ExpenseCategory, Bill, BillCategory,
                     BillIssuer, AppReview)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture',)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class DateInput(forms.DateInput):
    input_type = 'date'


class IncomeCreateForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('amount', 'date', 'note', 'income_category', 'user')

        widgets = {
            'date': DateInput(),
            'user': forms.HiddenInput()
        }


class IncomeCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = IncomeCategory
        fields = ('category',)


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('amount', 'date', 'company', 'expense_category', 'note', 'pic', 'user')

        widgets = {
            'user': forms.HiddenInput(),
            'date': DateInput()
        }


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'address', 'phone', 'email')


class ExpenseCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ('category',)


class BillCreateForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ('amount', 'date_due', 'date_paid', 'bill_category', 'bill_issuer', 'status', 'note', 'pic', 'user')

        widgets = {
            'user': forms.HiddenInput(),
            'date_due': DateInput(),
            'date_paid': DateInput()
        }


class BillIssuerCreateForm(forms.ModelForm):
    class Meta:
        model = BillIssuer
        fields = ('name', 'address', 'phone', 'email')


class BillCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = BillCategory
        fields = ('category',)


class AppReviewForm(forms.ModelForm):
    class Meta:
        model = AppReview
        fields = ('content', 'reviewer')
        widgets = {
            'reviewer': forms.HiddenInput()
        }
