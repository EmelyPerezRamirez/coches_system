from models import coches_model, cochesBD

class CochesController:

    def insertar_controller(self):
        coche1 = coches_model.cochesModel(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())                    
        coche1 = cochesBD.cochesBD(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1

    def eliminar_controller(self):
        id=self.id.get()
        res=self.confirmacion_eliminar("eliminar")
        if res:
            respuesta = cochesBD.cochesBD.eliminar(id)
            self.respuesta_sql(respuesta)

        else: 
            respuesta = False
            self.respuesta_sql(respuesta)

    def modificar_controller(self):
        id=self.id.get()                     
        coche1 = cochesBD.cochesBD(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta = coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1
        # self.modificar_view()

    def consultar_controller(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in cochesBD.cochesBD.consultar():
            self.tree.insert("", "end", values=row)

    def buscar_controller(self,tipo_accion):
        id=self.id.get()
        coche1 = cochesBD.cochesBD.buscar(id)
        if len(coche1)>0:
            self.encontrado(coche1, tipo_accion)