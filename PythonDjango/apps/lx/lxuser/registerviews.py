from django.shortcuts import render
from ..models import User
from .check_password import check_password


def register(request):
    try:
        msg = 200
        post = request.POST
        nickname = post.get('nickname')
        name = post.get('name')
        password = post.get('pwd1')
        password1 = post.get('pwd2')
        msg = check_password(password, password1)
        sex = post.get('sex')
        birthday = post.get('birthday')
        age = post.get('age')
        idcard = post.get('IDCard')
        nation = post.get('nation')
        province = post.get('province')
        city = post.get('city')
        county = post.get('county')
        phone = post.get('phone')
        email = post.get('email')
        user = User(nickname=nickname, name=name, password=password, sex=sex,
                    birthday=birthday, age=age, IDCard=idcard, nation=nation, province=province,
                    city=city, county=county, phone=phone, email=email)
        user.save()
        if msg != 200:
            return render(request, 'register.html', {'msg': msg})
        else:
            return render(request, 'homepage.html', {'msg': "注册成功"})
    except:
        return render(request, 'register.html', {'msg': '注册失败'})
