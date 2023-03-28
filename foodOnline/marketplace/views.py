from django.shortcuts import render,get_object_or_404
from menu.models import Category,FoodItem
from vendor.models import  Vendor
from django.db.models import Prefetch

# Create your views here.

def marketplace(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)
    vendor_count = vendors.count()
    context = {
        'vendors': vendors,
        'vendor_count': vendor_count,
    }
    return render(request, 'marketplace/listings.html',context)


def vendor_detail(request, vendor_slug):
    vendor = get_object_or_404(Vendor, vendor_slug=vendor_slug)

    categories = Category.objects.filter(vendor=vendor).prefetch_related(
        Prefetch(
            'fooditems',
            queryset = FoodItem.objects.filter(is_available=True)
        )
    )

    # opening_hours = OpeningHour.objects.filter(vendor=vendor).order_by('day', 'from_hour')
    
    # # Check current day's opening hours.
    # today_date = date.today()
    # today = today_date.isoweekday()
    
    # current_opening_hours = OpeningHour.objects.filter(vendor=vendor, day=today)
    # if request.user.is_authenticated:
    #     cart_items = Cart.objects.filter(user=request.user)
    # else:
    #     cart_items = None
    context = {
        'vendor': vendor,
        'categories': categories,
        # 'cart_items': cart_items,
        # 'opening_hours': opening_hours,
        # 'current_opening_hours': current_opening_hours,
    }
    return render(request, 'marketplace/vendor_detail.html',context)