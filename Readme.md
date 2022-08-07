# LOGIN, REGISTER and PROFILE Api Created using Django Rest Framework

This repository is the submission for cybernx assignment

## API Information

### Register API (POST Method only)

<h4>
    Path
</h4>

```
127.0.0.1:8000/api/auth/register
```
<h4>
    Fields
</h4>

<table>
    <tr>
        <th>Field</th>
        <th>Type</th>
    </tr>
    <tr>
        <td>
            username
        </td>
        <td>
            string
        </td>
    </tr>
     <tr>
        <td>
            email
        </td>
        <td>
            string
        </td>
    </tr>
     <tr>
        <td>
            password
        </td>
        <td>
            string
        </td>
    </tr>
    <tr>
        <td>
            password2
        </td>
        <td>
            string
        </td>
    </tr>
     <tr>
        <td>
            first_name
        </td>
        <td>
            string
        </td>
    </tr>
     <tr>
        <td>
            last_name
        </td>
        <td>
            string
        </td>
    </tr>
     <tr>
        <td>
            mobile_number
        </td>
        <td>
            int (limit 10 to 13 characters)
        </td>
    </tr>
     <tr>
        <td>
            userPhoto
        </td>
        <td>
            Image file
        </td>
    </tr>
</table>

<h3>
    Response
</h3>

```
{
  "user": {
    "id": 7,
    "username": "test",
    "first_name": "test",
    "last_name": "tester",
    "email": "test@test.com"
  },
  "userProfile": {
    "id": 2,
    "mobile_number": "8527419623",
    "userPhoto": "/media/profile_pics/wallpaper_-_2_sLi5Dqk.png",
    "userLinked": 7
  },
  "token": "6a601f213218579c833f87f65503fe32607da80884e314f886ced237f0403393"
}
```
### Login API (POST Method only)

<h4>
    Path
</h4>

```
127.0.0.1:8000/api/auth/login
```
<h4>
    Fields
</h4>

<table>
    <tr>
        <th>Field</th>
        <th>Type</th>
    </tr>
    <tr>
        <td>
            username
        </td>
        <td>
            string
        </td>
    </tr>
     <tr>
        <td>
            password
        </td>
        <td>
            string
        </td>
    </tr>
</table>

<h3>
    Response
</h3>

```
{
  "user": {
    "id": 7,
    "username": "test",
    "first_name": "test",
    "last_name": "tester",
    "email": "test@test.com"
  },
  "token": "bc682f3fbc087d347da3e48fc90f7a85db5dc906840ede9180cd1cb6bfb91ae5"
}
```
### Profile API (GET Method only)

<h4>
    Path
</h4>

```
127.0.0.1:8000/api/auth/profiile
```
<h4>
    Addition Header
</h4>

```
"Authorization" : "Token [token you get from login or register api]"
```



<h3>
    Response
</h3>

```
{
  "user": {
    "id": 7,
    "username": "test",
    "first_name": "test",
    "last_name": "tester",
    "email": "test@test.com"
  },
  "userProfile": {
    "id": 2,
    "mobile_number": "8527419623",
    "userPhoto": "/media/profile_pics/wallpaper_-_2_sLi5Dqk.png",
    "userLinked": 7
  },
  "token": "6a601f213218579c833f87f65503fe32607da80884e314f886ced237f0403393"
}
```

## Installation

<h3>
Clone
</h3>

```bash
    git clone https://github.com/bhagwanZaki/CyberNX-assignment.git
```
<h3>Download libraries</h3>

```bash
    pip install -r requirements.txt
```

<h3> Create Database in MYSql </h3>

```sql
CREATE DATABASE cybernx;
```

<h3>Edit setting.py file located in cyberNXinternprj folder</h3>

<b>Edit line 95 and 96</b>
```
'USER':'root', # CHANGE THIS WITH YOUR USERNAME #
'PASSWORD':os.environ.get('MY_SQL_PASSWORD'), # CHANGE THIS WITH YOU PASSWORD #
```

<h3>Migrate the database</h3>

```bash
   python manage.py makemigrations
   python manage.py migrate
```

<h3>Create the superuser</h3>

```bash
    python manage.py createsuperuser
```

<h3>Run Django on localnetwork</h3>

```bash
    python manage.py runserver 0.0.0.0:8000
```
