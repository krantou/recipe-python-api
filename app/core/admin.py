from django.contrib import admin # noqa

'''
Django admin customization.
We need to enable django admin for our user.
'''


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUseradmin
from django.utils.translation import gettext_lazy as _

from core import models

class UserAdmin(BaseUseradmin):
    '''Define the admin pages for users'''

    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permission'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password',
                'name',
                'is_active',
                'is_staff',
                'is_superuser'
            )
        }),
    )


# We need to register our user model.
# we need to specify user admin so as to have the
# customization we added above
admin.site.register(models.User, UserAdmin)