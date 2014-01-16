from auth.models import UserProfile



def current_user(req): 
    try:
        if req.user.is_superuser:
            superUP=UserProfile()
            superUP.user=req.user
            superUP.image=None
            return {'UP':superUP, 'page': str(req.get_full_path()).strip()}
        else:
            return {'UP':UserProfile.objects.get(user=req.user),
                    'page': str(req.get_full_path()).strip()}
    except:
        return {}





