# 1. 스크린샷 index 문제 해결

```python
#settings.py 에 다음 코드 추가 (정적파일 추가 경로 작성)
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

```

# 2. 업로드한 사진 보이기

``` python
#django_06_workshop/urls.py

from django.contrib import admin
from django.urls import path, include
# 아래 두개 추가
from django.conf import settings
from django.conf.urls.static import static

# + 이후 static ~~추가
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

```python
#articles/models.py

from django.db import models

# Create your models here.
#image 에 upload_to 추가
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

```django
create.html
form에 enctype 추가
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>CREATE</h1>
  <form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" accept="image/*">
  </form>
</body>
</html>
```



