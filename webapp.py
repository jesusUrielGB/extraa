import web
# @
from web import form
from data import Clientes
from data import Peliculas
render=web.template.render('templates')

urls = (
    '/(.*)', 'index'
)
db = web.database(dbn='mysql', db='frrxzga3znzs04h5', user='vd5qggehmcq2cg2w', pw='aivtsmmu4s2eoxo9', host="o61qijqeuqnj9chh.cbetxkdyhwsb.us-east-1.rds.amazonaws.com")
Clientes = Clientes()  
Clientes.read()
peliculas=Peliculas()
peliculas.read()
myform = form.Form( 
    form.Dropdown('Cliente', Clientes.getClientes()), 
    form.Dropdown('Pelicula',peliculas.getPeliculas()), 
    form.Dropdown('Formato', ["Blueray","DVD"]),
    form.Dropdown('Tiempo', ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"])
    
    ) 
class index:
    def GET(self,results):
        form = myform()
        registros=db.select('detalle')
        return render.index(form,registros)
        
    def POST(self,results): 
        form = myform() 
        if not form.validates(): 
            return render.index(form)
        else:
            precio=0
            if form.d.Formato=="Blueray":
                precio=20
            elif form.d.Formato=="DVD":
                precio=10
            total=int(form.d.Tiempo)*precio
            db.insert('detalle',cliente=form.d.Cliente, pelicula=form.d.Pelicula, formato=form.d.Formato, tiempo=form.d.Tiempo,total=total)
            
            registros=db.select('detalle')
            return render.index(form,registros)


if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()
