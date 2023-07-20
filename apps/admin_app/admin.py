from django.contrib import admin
from .models.staff import Position, Responsibility, Manager, Representative, Volunteer, WorkingType, Salary, Vacancy, Resume, Result, SocialMediaPost
from .models.events import EventType, Event
from .models.news import Region, NewsCategory, NewsTag, News, UserDevice, FAQTag, FAQ, Contact, Admin
admin.site.register(Position)
admin.site.register(Responsibility)
admin.site.register(Manager)
admin.site.register(Representative)
admin.site.register(Volunteer)
admin.site.register(WorkingType)
admin.site.register(Salary)
admin.site.register(Vacancy)
admin.site.register(Resume)
admin.site.register(Result)
admin.site.register(SocialMediaPost)

# ----------------------------------------------------------------

admin.site.register(EventType)
admin.site.register(Event)

# ----------------------------------------------------------------

admin.site.register(Region)
admin.site.register(NewsCategory)
admin.site.register(NewsTag)
admin.site.register(News)
admin.site.register(UserDevice)
admin.site.register(FAQTag)
admin.site.register(FAQ)
admin.site.register(Contact)
admin.site.register(Admin)



