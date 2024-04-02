from django.http import HttpResponse
from django.shortcuts import render, redirect

from Billing_App.models import Login, Item, Bill


def main_page(request):
    return render(request,'Homepage.html')


def login(request):
    if request.method =="POST":
        username = request.POST['usernm']
        password = request.POST['psswd']
        res = Login.objects.filter(username=username,password=password)
        if res.exists():
            data = res[0]
            if data.usertype == 'Admin':
                return HttpResponse("<script>alert('Successfully LoggedIn');window.location='/admin_page'</script>")

        else:
            return HttpResponse("<script>alert('Invalid User');window.location='/'</script>")

def admin_page(request):
    return render(request,'item_list.html')

def add_items(request):
    name =request.POST['name']
    price = request.POST['price']
    des = request.POST['details']

    obj = Item()
    obj.name =name
    obj.price =price
    obj.description =des
    obj.save()
    return HttpResponse("<script>alert('Items Added Successfully');window.location='/admin_page'</script>")


def View_items(request):
    items = Item.objects.all()
    return render(request,'View_Items.html',{'items':items})

def update_items(request,edid):
    items = Item.objects.get(id=edid)
    return render(request,'Edit_items.html',{'items':items,'edid':edid})

def update_items_post(request,edid):
    nm = request.POST['name']
    pr = request.POST['price']
    des = request.POST['details']

    Item.objects.filter(id=edid).update(name=nm,price=pr,description =des)
    return HttpResponse("<script>alert('Items Edited Successfully');window.location='/View_items'</script>")


def delete_added_items(request,dltid):
    Item.objects.get(id=dltid).delete()
    return HttpResponse("<script>alert('Items Deleted Successfully');window.location='/View_items'</script>")


def create_bill(request):
    if request.POST == 'POST':
        item_ids =request.POST.getlist('items')
        items = Item.objects.filter(id__in=item_ids)
        total_cost = sum(items.price for items in items)
        bill = Bill.objects.create(total_cost = total_cost)
        bill.items.set(items)
        return redirect('bill_detail',pk=bill.pk)
    else:
        items=Item.objects.all()
        return render(request,'create_bill.html',{'items':items})
def bill_detils(request,pk):
    bill = Bill.objects.get(pk=pk)
    return  render(request,'bill details.html',{'bill':bill})





