from django.core.management.base import BaseComand

class Command(BaseComand):
    def handle(self,*args, **options):
        conecction = mail.get_conection()
        conecction.open()
        import import ipdb; ipdb.set_trace()
        mail0 = mail.EmailMessage(
            'Asunto 0'
            'Cuerpo del mail 0 '
            'tec.bertola@gmail.com'
            'papihades@gmail.com'
            conecction = conecction
        )
        mail0.send()
        mail1.mail.EmailMessage(
            'Asunto 1'
            'Cuerpo del mail 1 '
            'tec.bertola@gmail.com'
            'eldwarf1@gmail.com'
            conecction = conecction
        )
        mail2.mail.EmailMessage(
            'Asunto 2'
            'Cuerpo del mail 2 '
            'tec.bertola@gmail.com'
            'pdalmasso@gmail.com'
            conecction = conecction
        )
    """docstring for Command.BaseComandef
    def handle(self,*args, **options):
        print "Hola Mundo "
        print args
        print options
         __init__(self, arg):
        super(Command,BaseComand._
        def handle(self,*args, **options):
            print "Hola Mundo "
        print args
        print options
        _init__()
        self.arg = arg
