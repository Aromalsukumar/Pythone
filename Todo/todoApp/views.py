from django.shortcuts import render,redirect

# Create your views here.
def index(req):
    return render(req,'index.html')
lis=[]
def add(req):
    if req.method=='POST':
        ID=req.POST['id']
        Firstname=req.POST['fname']
        Lastname=req.POST['lname']
        Fathersname=req.POST['fathersname']
        Email=req.POST['email']
        Age=req.POST['age']
        Place=req.POST['place']
        Qulifiation=req.POST['qulifi']
        lis.append({'id':ID,'fnm':Firstname,'lnm':Lastname,'fathersnm':Fathersname,'em':Email,'ag':Age,'plc':Place,'qul':Qulifiation})
        print(lis)
        return redirect(display)
    else:
        return render(req,'add.html')
def display(req):
    return render(req,'display.html',{'data':lis})
def edit(req,id):
    std={}
    pos=0
    for i in lis:
        if i['id']==id:
            std=i
            pos=lis.index(i)
    if req.method=='POST':
        Firstname=req.POST['fname']
        Lastname=req.POST['lname']
        Fathersname=req.POST['fathersname']
        Email=req.POST['email']
        Age=req.POST['age']
        Place=req.POST['place']
        Qulifiation=req.POST['qulifi']
        lis[pos]={'fnm':Firstname,'lnm':Lastname,'fathersnm':Fathersname,'em':Email,'ag':Age,'plc':Place,'qul':Qulifiation}
        return redirect(display)
    else:
        return render(req,'edit.html',{'data':std})
def delete(req,id):
    for i in lis:
        if i['id']==id:
            lis.remove(i)
            return redirect(display)
    
    
               
        
