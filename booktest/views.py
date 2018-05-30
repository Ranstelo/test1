from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from booktest.models import BookInfo,HeroInfo
from django.template import loader,RequestContext

# Create your views here.

def index(request):
    return HttpResponse("首页")


def login(request):
    if request.session.has_key('islogin'):
        return redirect('/index')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request,'booktest/login.html',{'username':username})


def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    btn = request.POST.get('btn')
    print(btn)
    print(username,password)
    if username == 'sb' and password == '123':
        pesponse = render(request,'booktest/index.html')
        if btn == 'on':
            pesponse.set_cookie('username',username,max_age=7*24*60)
        request.session['islogin'] = True
        return pesponse


    else:
        return redirect('/login')

def login_ajax(request):
    return HttpResponse('登录成功')


def login_required(view_func):
    '''登录判断装饰器'''
    def wrapper(request, *view_args, **view_kwargs):
        # 判断用户是否登录
        if request.session.has_key('islogin'):
            # 用户已登录,调用对应的视图
            return view_func(request, *view_args, **view_kwargs)
        else:
            # 用户未登录,跳转到登录页
            return redirect('/login')
    return wrapper


@login_required # change_pwd = login_required(change_pwd)
def change_pwd(request):
    '''显示修改密码页面'''
    # # 进行用户是否登录的判断
    # if not request.session.has_key('islogin'):
    #     # 用户未登录，跳转到登录
    #     return redirect('/login')

    return render(request, 'booktest/change_pwd.html')


# /change_pwd_action
@login_required
def change_pwd_action(request):
    '''模拟修改密码处理'''
    # # 进行用户是否登录的判断
    # if not request.session.has_key('islogin'):
    #     # 用户未登录，跳转到登录
    #     return redirect('/login')

    # 1.获取新密码
    pwd = request.POST.get('pwd')
    # 获取用户名
    username = request.session.get('username')
    # 2.实际开发的时候: 修改对应数据库中的内容...
    # 3.返回一个应答
    return HttpResponse('%s修改密码为:%s'%(username,pwd))
