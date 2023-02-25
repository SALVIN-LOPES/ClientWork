# ClientWork

There are 4 Routes to connect
Routes = [
    "Register-User" : {{URL}}/api/register,
    "getWorks" : {{URL}}/api/works,
    "get-work-by-artist-name" : {{URL}}/api/works?artist=[artist name],
    "get-artist-by-work-type" : {{URL}}/api/work?work_type=[work_type],
]

1] Register User Inputs:
    username
    email
    password

2] The Client object will be created after successful registration of User object

3] There are 3 models Client, Work, Artist

4] There are 2 views
    registerPage,
    getWorks = [
        get all works,
        get works by artist name,
        get artist by work type,
    ]
