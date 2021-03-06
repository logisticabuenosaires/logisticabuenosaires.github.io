# coding: utf8

db.define_table("Avenida_principal",
          Field("Av_principaid","id"),
          Field("cod_Av_principaid","integer"),           
          Field("nombre_de_Av_principal","string"),
          Field("numero_de_Av_principal","integer"),
          Field("entre_calles_A"),
          Field("entre_calles_B"),            
          )              
 #################  #############################
db.define_table("entre_calles",
          Field("entre_calles_id","id"),
          Field("cod_entre_calle","integer"), 
          Field("nombre_entre_calle","string"),           
          )                          
##############################################
db.define_table("provincia",
          Field("provincia_id","id"),
          Field("cod_provincia","integer"),           
          Field("pais"),
          Field("nombre_de_provincia","string"),)               
#############################  
    ###########################################################################
db.define_table('Paises',
   Field("Pais_id","id"),
   Field("cod_pais","integer"),
   Field("Pais"),
   Field("capital"),)
           
db.define_table("Armado_de_rutas",
          Field("id_Armado_de_rutas","id"),
          Field("cod_Armado_de_rutas","integer"),           
          Field("arm_pais",db.Paises,requires=IS_IN_DB(db,db.Paises.id, "%(Pais)s"),
              comment=A("Cargar mas paises",_href=URL(r=request,f="cargar_ps",c="Generar_guia_de_carga"))),
          Field("provincia",db.provincia,requires=IS_IN_DB(db,db.provincia.id, "%(nombre_de_provincia)s"),
              comment=A("Cargar mas provincias",_href=URL(r=request,f="cargar_prv",c="Generar_guia_de_carga"))),
          Field("Av_principal",db.Avenida_principal,requires=IS_IN_DB(db, db.Avenida_principal.id, "%(nombre_de_Av_principal)s"),
              comment=A("Cargar mas Avenidas",_href=URL(r=request,f="cargar_av",c="Generar_guia_de_carga"))),
          Field("nombre_de_entre_calle_A",db.entre_calles,requires=IS_IN_DB(db, db.entre_calles.id, "%(nombre_entre_calle)s"),
              comment=A("Cargar mas calles",_href=URL(r=request,f="cargar_cal",c="Generar_guia_de_carga"))),
          Field("nombre_de_entre_calle_B",db.entre_calles,requires=IS_IN_DB(db, db.entre_calles.id, "%(nombre_entre_calle)s")),
          )
