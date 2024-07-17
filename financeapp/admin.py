from django.contrib import admin
from .models import IncomeCategory, ExpenseCategory, Income, Expense, BillIssuer, BillCategory, Bill, Profile, Company, AppReview


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'income_category', 'user')
    list_filter = ('date', 'amount', 'income_category__category')
    search_fields = ('date', 'amount', 'income_category__category')
    list_editable = ('amount', 'income_category', 'user')


class IncomeInLine(admin.TabularInline):
    model = Income
    extra = 0


class IncomeCategoryAdmin(admin.ModelAdmin):
    inlines = (IncomeInLine, )


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'display_categories', 'company', 'user')
    list_filter = ('date', 'amount', 'expense_category__category')
    search_fields = ('date', 'amount', 'expense_category__category')
    list_editable = ('amount', 'user')


class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'date_due', 'date_paid', 'bill_issuer', 'status', 'user')
    list_filter = ('amount', 'date_due', 'date_paid', 'bill_issuer')
    search_fields = ('amount', 'date_due', 'date_paid')
    list_editable = ('amount', 'date_due', 'date_paid', 'bill_issuer', 'status', 'user')

    fieldsets = (
        ('Bill issuer', {'fields': ['bill_issuer', 'bill_category']}),
        ('Bill info', {'fields': ['id', 'amount', 'date_due', 'date_paid', 'status', 'note', 'pic', 'user']})
    )


class BillInLine(admin.TabularInline):
    model = Bill
    extra = 0


class BillIssuerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')
    search_fields = ('name', 'address', 'phone', 'email')
    list_editable = ('address', 'phone', 'email')
    inlines = (BillInLine,)


class ExpsenseInLine(admin.TabularInline):
    model = Expense
    extra = 0


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')
    search_fields = ('name', 'address', 'phone', 'email')
    list_editable = ('address', 'phone', 'email')
    inlines = (ExpsenseInLine, )


admin.site.register(IncomeCategory, IncomeCategoryAdmin)
admin.site.register(ExpenseCategory)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(BillIssuer, BillIssuerAdmin)
admin.site.register(BillCategory)
admin.site.register(Bill, BillAdmin)
admin.site.register(Profile)
admin.site.register(AppReview)