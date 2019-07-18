from django.shortcuts import render
from ..models import User


def register(request):
    try:
        post = request.POST
        nickname = post.get('nickname')
        print(nickname)
        name = post.get('name')
        print(name)
        password = post.get('pwd1')
        print(password)
        password1 = post.get('pwd2')
        sex = post.get('sex')
        print(sex)
        birthday = post.get('birthday')
        print(birthday)
        age = post.get('age')
        print(age)
        idcard = post.get('IDCard')
        print(idcard)
        nation = post.get('nation')
        print(nation)
        province = post.get('province')
        print(province)
        city = post.get('city')
        print(city)
        county = post.get('county')
        print(county)
        phone = post.get('phone')
        print(phone)
        email = post.get('email')
        print(email)
        user = User(nickname=nickname, name=name, password=password, sex=sex,
                    birthday=birthday, age=age, IDCard=idcard, nation=nation, province=province,
                    city=city, county=county, phone=phone, email=email)
        user.save(force_insert=True)
        return render(request, 'register.html', {'msg': '注册成功'})
    except:
        return render(request, 'homepage.html', {'msg': 'None'})
