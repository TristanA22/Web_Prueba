from django.db import models

class Pais(models.Model):
    idPais = models.IntegerField(primary_key=True, verbose_name="Id de categoria")
    nombrePais = models.CharField(max_length=50, verbose_name="Nombre de la categoria")

    def __str__(self):
        return self.nombrePais

class Registrou(models.Model):
    n_identificacion = models.CharField(max_length=20, primary_key=True, verbose_name=" Numero de Identificacion ")
    nombre_completo = models.CharField(max_length=100, verbose_name="  Nombre Completo")
    telefono = models.IntegerField(verbose_name=" Telefono ")
    direccion = models.CharField( max_length=100, verbose_name= " Direccion ")
    email = models.EmailField( max_length= 150, verbose_name=" Email")
    password = models.CharField( max_length=25, verbose_name= " Password " )
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.n_identificacion