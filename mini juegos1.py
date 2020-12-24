import tkinter as tk

ventana=tk.Tk()
ventana.title(" MINI GAMES ")
ventana.geometry('1200x720')
ventana.resizable(False,False)

import math

def calculadora():
    pisos=int(piso.get())
    metros=2.5*pisos
    vf=math.sqrt(2*9.8*metros)
    t=round(vf/9.8,2)
    km=vf/1000
    kmh=round(km/0.0002777778,2)
    resultado.config(text=" La velocidad con la que llego al piso fue de " + str(kmh) + " km/h " ) 
    tiempo.config(text= " y tardo " + str(t)+ " segundos en llegar al suelo ")                  
                    
def calculadorap():
    metros=float(prof.get())
    presion=1000*9.8*metros+101300
    presionatm=round(presion/101300,2)
    resultado1.config(text=" La presion es de "+ str(presionatm) + " atm ")
    
titulo=tk.Label(text= " CALCULADORA DE IRRELEVANCIAS ", fg="#ff0000")   
titulo.place(x=80, y=5)
opcion=tk.Label(text=" Desde que piso cayo el cuerpo? ")
opcion.place(x=100, y=40)
piso=tk.Entry()
piso.place(x=100,y=60)
piso.config(background="black",fg="#ffff00")
calculo=tk.Button(text= " Calcular ", command=calculadora, fg="#0000ff")
calculo.place(x=100,y=100)
resultado=tk.Label(text=" El resultado es ")
resultado.place(x=100, y=136)
tiempo=tk.Label(text=" ")
tiempo.place(x=100, y=155)

opcion1=tk.Label(text=" A que profundidad en metros se sumergio? ")
opcion1.place(x=100, y=180)
prof=tk.Entry()
prof.place(x=100,y=200)
prof.config(background="black",fg="#ffff00")
calculop=tk.Button(text= " Calcular ", command=calculadorap, fg="#0000ff")
calculop.place(x=100,y=240)
resultado1=tk.Label(text=" El resultado es ")
resultado1.place(x=100, y=280)

'''_________________________________________________'''

def sortear():
    import random

    l=[]

    a=random.randint(0,45)
    b=random.randint(0,45)
    c=random.randint(0,45)
    d=random.randint(0,45)
    e=random.randint(0,45)
    f=random.randint(0,45)

    l.append(a)
    l.append(b)
    l.append(c)
    l.append(d)
    l.append(e)
    l.append(f)

          
       
    while True:

        if l[0]==l[1] or l[0]==l[2] or l[0]==l[3] or l[0]==l[4] or l[0]==l[5] or l[1]==l[2] or l[1]==l[3] or l[1]==l[4] or l[1]==l[5] or l[2]==l[3] or l[2]==l[4] or l[2]==l[5] or l[3]==l[4] or l[3]==l[5] or l[4]==l[5]:
       
           l.pop()
           l.pop()
           l.pop()
           l.pop()          
           l.pop()
           l.pop()
       
           a=random.randint(0,45)
           b=random.randint(0,45)
           c=random.randint(0,45)
           d=random.randint(0,45)
           e=random.randint(0,45)
           f=random.randint(0,45)

           l.append(a)
           l.append(b)
           l.append(c)
           l.append(d)
           l.append(e)
           l.append(f) 
    
    
        else:
           break
         
       
    cont=0
    
    primer=int(n1.get())
    if primer==l[0] or primer==l[1] or primer==l[2] or primer==l[3] or primer==l[4] or primer==l[5]:
        cont=cont+1
    
    segundo=int(n12.get())
    if segundo==l[0] or segundo==l[1] or segundo==l[2] or segundo==l[3] or segundo==l[4] or segundo==l[5]:
        cont=cont+1
    
    tercero=int(n13.get())
    if tercero==l[0] or tercero==l[1] or tercero==l[2] or tercero==l[3] or tercero==l[4] or tercero==l[5]:
        cont=cont+1
    
    cuarto=int(n14.get())
    if cuarto==l[0] or cuarto==l[1] or cuarto==l[2] or cuarto==l[3] or cuarto==l[4] or cuarto==l[5]:
        cont=cont+1
    
    
    quinto=int(n15.get())
    if quinto==l[0] or quinto==l[1] or quinto==l[2] or quinto==l[3] or quinto==l[4] or quinto==l[5]:
        cont=cont+1
   
    sexto=int(n16.get())
    if sexto==l[0] or sexto==l [1] or sexto==l[2] or sexto==l[3] or sexto==l[4] or sexto==l[5]:
        cont=cont+1
    
    acertados1.config(text= " HAS ACERTADO: " + str(cont) + " NUMEROS ")
    
    s1.config(text= a, fg="#ff0000")
    s2.config(text=b, fg="#ff0000")
    s3.config(text= c, fg="#ff0000")
    s4.config(text= d, fg="#ff0000")
    s5.config(text= e, fg="#ff0000")
    s6.config(text= f, fg="#ff0000")
    sorteo.config(text= " NO VA MAS ",bg= "#ff0000")


    import mysql.connector
      

    conexion3=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="Sorteos")
     
    cursor3=conexion3.cursor()
      
    sql="insert into Sorteos( numero_jugado_1,numero_jugado_2,numero_jugado_3,numero_jugado_4,numero_jugado_5,numero_jugado_6,cant_aciertos,nro_sorteado_1,nro_sorteado_2,nro_sorteado_3,nro_sorteado_4,nro_sorteado_5,nro_sorteado_6) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
     
    datos=(l[0],l[1],l[2],l[3],l[4],l[5],cont,primer,segundo,tercero,cuarto,quinto,sexto)
      
    cursor3.execute(sql, datos)

    conexion3.commit()
      
    conexion3.close()    



def reconfig():
    s1.config(text= " ??? ",foreground= "green")
    s2.config(text= " ??? ",foreground= "green")
    s3.config(text= " ??? ",foreground= "green")
    s4.config(text= " ??? ",foreground= "green")
    s5.config(text= " ??? ",foreground= "green")
    s6.config(text= " ??? ",foreground= "green")
    acertados1.config(text="  ")
    
    sorteo.config(text=" SORTEAR ",background= "green")

comojugar=tk.Label(text=" TIENES LO QUE SE NECESITA PARA SER MILLONARIO ??? ", fg="#ff0000")
comojugar.place(x=50,y=320)
comojugar1=tk.Label(text= " SELECCIONA 6 NUMEROS DEL 0 AL 45 Y AVERIGUALO!! ", fg="#ff0000")
comojugar1.place(x=50,y=340)
n1=tk.Entry(ventana,background="black",fg="#03f943", width=8)
n1.place(x=10,y=370)
#n1.config(font=50)
n12=tk.Entry(ventana,background="black",fg="#03f943", width=8)
n12.place(x=80,y=370)
n13=tk.Entry(ventana,background="black",fg="#03f943", width=8)
n13.place(x=150,y=370)
n14=tk.Entry(ventana,background="black",fg="#03f943", width=8)
n14.place(x=220,y=370)
n15=tk.Entry(ventana,background="black",fg="#03f943", width=8)
n15.place(x=290,y=370)
n16=tk.Entry(ventana,background="black",fg="#03f943", width=8)
n16.place(x=360,y=370)
acertados1=tk.Label(text= "  ")
acertados1.place(x=10,y=400)
sorteo=tk.Button(ventana,text=" SORTEAR " ,background="green", width=20, height=5,command=sortear)
sorteo.place(x=124,y=450)
reiniciar=tk.Button(ventana,text=" REINICIAR ",command=reconfig, fg="#0000ff")
reiniciar.place(x=170,y=630)


s1=tk.Label(text=" ??? ",foreground= "green")
s1.place(x=55, y=580)
s1.config(font=60)
s2=tk.Label(text=" ??? ",foreground= "green")
s2.place(x=105, y=580)
s2.config(font=60)
s3=tk.Label(text=" ??? ",foreground= "green")
s3.place(x=155, y=580)
s3.config(font=60)
s4=tk.Label(text=" ??? ",foreground= "green")
s4.place(x=205, y=580)
s4.config(font=60)
s5=tk.Label(text=" ??? ",foreground= "green")
s5.place(x=255, y=580)
s5.config(font=60)
s6=tk.Label(text=" ??? ",foreground= "green")
s6.place(x=305, y=580)
s6.config(font=60)

'''divisor_hor=tk.Label(text="___________________________________________________________________________")
divisor_hor.place(x=20,y=300)'''

'''________________________________________________________________________'''




def verificarp():
    cont=0
    c1=int(respuesta1.get())
    if c1 == pregunta_azar[1]:
        label1.config(text= "CORRECTO", fg="#008000")
        cont=cont+1
    else:
        label1.config(text= "INCORRECTO",fg="#ff0000")
    

    
    c2=int(respuesta2.get())
    if c2 == pregunta_azar2[1]:
        label2.config(text= "CORRECTO",fg="#008000")
        cont=cont+1
    else:
        label2.config(text= "INCORRECTO", fg="#ff0000")
    

    c3=int(respuesta3.get())
    if c3 == pregunta_azar3[1]:
        label3.config(text= "CORRECTO",fg="#008000")
        cont=cont+1
    else:
        label3.config(text= "INCORRECTO", fg="#ff0000")


    c4=int(respuesta4.get())
    if c4 == pregunta_azar4[1]:
        label4.config(text= "CORRECTO",fg="#008000")
        cont=cont+1
    else:
        label4.config(text= "INCORRECTO", fg="#ff0000")


    c5=int(respuesta5.get())
    if c5 == pregunta_azar5[1]:
        label5.config(text= "CORRECTO",fg="#008000")
        cont=cont+1
    else:
        label5.config(text= "INCORRECTO",fg="#ff0000")

    label_punt.config(text= " ACERTASTE " + str(cont)+ " RESPUESTAS ",fg="#0000ff")

    
import random
import mysql.connector
conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="Quiz")
cursor1=conexion1.cursor()
cursor1.execute("select pregunta, correcta from preguntas ")
todas_preguntas=cursor1.fetchall()
pregunta_azar=(random.choice(todas_preguntas))
pregunta_usuario=pregunta_azar[0]
#respuesta=int(input(pregunta_usuario))

opcion=tk.Label(text=" CUANTO SABES DE CULTURA GENERAL? ", fg="#ff0000")
opcion.place(x=712, y=5)

pregunta1=tk.Label(text= " P1: " + pregunta_usuario)
pregunta1.place(x=720,y=40)
respuesta1=tk.Entry()
respuesta1.place(x=720,y=60)
label1=tk.Label(text=" ")
label1.place(x=850,y=60)
    
cursor2=conexion1.cursor()
cursor2.execute("select pregunta, correcta from preguntas ")
todas_preguntas2=cursor2.fetchall()
pregunta_azar2=(random.choice(todas_preguntas))
pregunta_usuario2=pregunta_azar2[0]


pregunta2=tk.Label(text= " P2: " + pregunta_usuario2)
pregunta2.place(x=720,y=90)
respuesta2=tk.Entry()
respuesta2.place(x=720,y=110)
label2=tk.Label(text=" ")
label2.place(x=850,y=110)


cursor3=conexion1.cursor()
cursor3.execute("select pregunta, correcta from preguntas ")
todas_preguntas3=cursor3.fetchall()
pregunta_azar3=(random.choice(todas_preguntas))
pregunta_usuario3=pregunta_azar3[0]


pregunta3=tk.Label(text= " P3: " + pregunta_usuario3)
pregunta3.place(x=720,y=140)
respuesta3=tk.Entry()
respuesta3.place(x=720,y=160)
label3=tk.Label(text=" ")
label3.place(x=850,y=160)

cursor4=conexion1.cursor()
cursor4.execute("select pregunta, correcta from preguntas ")
todas_preguntas4=cursor4.fetchall()
pregunta_azar4=(random.choice(todas_preguntas))
pregunta_usuario4=pregunta_azar4[0]


pregunta4=tk.Label(text= " P4: " + pregunta_usuario4)
pregunta4.place(x=720,y=190)
respuesta4=tk.Entry()
respuesta4.place(x=720,y=210)
label4=tk.Label(text=" ")
label4.place(x=850,y=210)

cursor5=conexion1.cursor()
cursor5.execute("select pregunta, correcta from preguntas ")
todas_preguntas5=cursor5.fetchall()
pregunta_azar5=(random.choice(todas_preguntas))
pregunta_usuario5=pregunta_azar5[0]


pregunta5=tk.Label(text= " P5: " + pregunta_usuario5)
pregunta5.place(x=720,y=240)
respuesta5=tk.Entry()
respuesta5.place(x=720,y=260)
label5=tk.Label(text=" ")
label5.place(x=850,y=260)

label_punt=tk.Label(text=" ", fg="#0000ff")
label_punt.place(x=850,y=305)
verificar=tk.Button(ventana,text=" VERIFICAR ",fg="#0000ff", command=verificarp)
verificar.place(x=720,y=300)

'''volver=tk.Button(ventana, text=" VOLVER A JUGAR " ,foreground="green", command=volver)
volver.place(x= 1010, y=300)'''

"""boton_puntaje=tk.Button(text=" VER PUNTAJE ",fg="#0000ff" ,command=ver_puntaje)
boton_puntaje.place(x=10,y=440)
cantidad=tk.Label(text=" TU PUNTAJE ES: ", fg="#0000ff")
cantidad.place(x=10,y=470)"""

conexion1.close()

'''___________________________________________________________'''


def base_datos():
      
      usuario=pregunta.get()
      usuario1=int(respuesta.get())
      
      import mysql.connector
      

      conexion2=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="Quiz")
     
      cursor2=conexion2.cursor()
      
      sql="insert into preguntas( pregunta,correcta) values (%s,%s)"
     
      datos=( usuario , usuario1 )
      
      cursor2.execute(sql, datos)

      conexion2.commit()
      
      conexion2.close()    
      
      pregunta.delete(0, tk.END)
      respuesta.delete(0, tk.END)

comentario=tk.Label(text=" APORTA TU GRANITO DE ARENA CARGANDO PREGUNTAS AL JUEGO!!! ",fg="#ff0000")
comentario.place(x=712, y=370)
comentario1=tk.Label(text=" RECUERDA QUE LA RESPUESTA DEBE SER UN VALOR NUMERICO ENTERO ", fg="#ff0000")
comentario1.place(x=712, y= 390)
pedido=tk.Label(text=" Escriba aqui su pregunta ")
pedido.place(x=720, y=450)
pregunta=tk.Entry()
pregunta.place(x=720,y=490)


pedido1=tk.Label(text=" Escriba aqui su respuesta")
pedido1.place(x=720, y=530)
respuesta=tk.Entry()
respuesta.place(x=720,y=570)
botonresp=tk.Button(text= " Enviar a base de datos ",command=base_datos, fg="#0000ff")#command=resp_base) #falta command
botonresp.place(x=720,y=610)


ventana.mainloop()