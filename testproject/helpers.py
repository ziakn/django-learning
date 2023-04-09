# helpers.py

class HelperClass:
    @staticmethod
    def greet(name):
        return f"Hello, {name}!"

    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def genrate_image_path(obj):
        date = obj.created_at
        path ='media/files/images/'+str(date.year)+'/'+str(date.month)+'/'+str(date.day)+'/'+str(date.strftime("%f"))+'-'+str(obj.salt)+'/'+str(date.year)+str(date.month)+str(date.day)+'_'+str(date.strftime("%f"))+'-'+str(obj.salt)+'/'+str(date.year)+str(date.month)+str(date.day)+'_'+str(date.strftime("%f"))+'-'+str(obj.salt)+'.'+obj.extension
        return path