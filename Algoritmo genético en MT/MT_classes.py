
class cinta():
    def __init__(self) -> None:
        self.posicion = 0
        self.lista = []
    
    def get(self) -> int:
        return self.lista[self.posicion]
    
    #desplazamiento del cabezal de la cinta a izquierda y derecha
    def SHR(self) -> None:
        self.posicion += 1
    def SHL(self) -> None:
        self.posicion -= 1

    #establecer un valor en la posicón actual de la cinta
    def set_valor(self, valor)-> float:
        self.lista[self.posicion] = valor

    def print_cinta(self):
        print(self.lista)
    
    def print_pos(self):
        print(self.posicion)
    

    

    



class maquinaDeTuring():
    def __init__(self, cantCintas):
        self.cantCintas = cantCintas
        self.cinta = []
        for i in range(cantCintas):
            self.cinta.append(cinta())
        self.estado = 0


    
    
    def escribirCinta(self,valor):
        self.cinta.lista[self.cinta.posicion] = valor

    def ejecutar(self):
        pasos = 0
        while self.estado != 'F':
            print("paso n°",pasos)
            self.mostrarMaquina()
            self.estadosDeTransicion()
            print("\n")
            pasos += 1
        print("paso n°",pasos," ------------FINAL DEL PROCESO----------------")
        self.mostrarMaquina()
        print("\n")



    def cambiarEstado(self,stateChange,newStatus):
        """cambia el estado de la máquina de turing"""
        if newStatus != None:
            self.estado = newStatus
        #stateChange =(ValorAEscribir, Direccion) un None equivale a un lambda, es decir no hace nada
        #cada stateChange es una tupla con los valores que se cambian en la máquina de turing, hay uno por cinta de la MT
        if stateChange != None:
            for i in range(len(stateChange)):
                if stateChange[i] != None:
                    if stateChange[i][0] != None:
                        self.cinta[i].set_valor(stateChange[i][0])
                    if stateChange[i][1] == 'R':
                        self.cinta[i].SHR()
                    if stateChange[i][1] == 'L':
                        self.cinta[i].SHL()


    def cargarCinta(self,indice,lista):
        self.cinta[indice].lista = lista
    
    def mostrarMaquina(self):
        print("Estado: ",self.estado)
        for i in range(len(self.cinta)):
            print("Cinta ",i,": ",self.cinta[i].lista,end=" ")
            print("Posicion: ",self.cinta[i].posicion)
            
        

    def getCinta(self,indice):
        return self.cinta[indice].lista
  
    #anatomia de estados de transición: [estado, dirección, valor, nuevo estado]
    #cinta ejemplo: 
    """ [0,20,35,10,.5,0] <-Almacena el Fitness de cada individuo
        [0,0,1,0,0,0] <-Almacena el estado de cada individuo
        [P,15,100,60,90,F]<-Almacena símbolos de la cinta y valores de los individuos

         """


    #estados de transición:[q0,0]=[0,R,q1]
    #explicación: si está en el estado q0, y lee un 0, deja el 0, se mueve a la derecha y cambia de estado a q1

    #los estados de esta máquina de turing le permitiran realizar operaciones genéticas

    def estadosDeTransicion(self):
        """el match es un switch de estados de transición, dentro de cada estado de transición hay que
        definir que pasa cuando se lee un valor"""
        match self.estado:#estado de la máquina de turing
            

            
            #la operacion de cruce entre dos cintas, se dará por la operacion AND entre la cinta[0](cinta de parentezco) y la cinta[1]
            #si el resultado de esa operación es 0, el valor [i] del hijo(cinta[3]) se tomará de la cinta[2], sinó se tomará de la cinta[1]
            case 'Cruce':
                if(self.cinta[0].get() == 0):
                    self.cambiarEstado([(None,'R'),(None,'R'),(None,'R'),(self.cinta[2].get(),'R')],'Cruce')
                
                if(self.cinta[0].get() == 1):
                    self.cambiarEstado([(None,'R'),(None,'R'),(None,'R'),(self.cinta[1].get(),'R')],'Cruce')
                
                if(self.cinta[0].get() == 'P'):
                    self.cambiarEstado([(None,'R'),(None,'R'),(None,'R'),(None)],'Cruce')
                
                if(self.cinta[0].get() == 'F'):
                    self.cambiarEstado([(None,'R'),(None,'R'),(None,'R'),(None)],'F')
                
            case 'Mutacion':#para la mutación, se tendrán dos cintas, la cinta [0] es la
                #cinta de cambio, y la cinta[1] es el individuo a mutar.
                #los valores donde se encuentra un 1 en la cinta[0], cambiara el valor correspondiente de la cinta[1]
                if(self.cinta[0].get() == 0):
                    self.cambiarEstado([(None,'R'),(None,'R')],'Mutacion')
                if(self.cinta[0].get() == 1):
                    self.cambiarEstado(None,'Alterar')
                if(self.cinta[0].get() == 'F'):
                    self.cambiarEstado(None,'F')
            
            case 'Alterar':#en este estado, se ha encontrado un 1 en la cinta de cambio,
                #se leerá el valor de la cinta[1] y se cambiará por un 0 o un 1, dependiendo de si el valor es 0 o 1
                if(self.cinta[1].get() == 0):
                    self.cambiarEstado([(None,'R'),(1,'R')],'Mutacion')
                if(self.cinta[1].get() == 1):
                    self.cambiarEstado([(None,'R'),(0,'R')],'Mutacion')

            case 'Aptitud':#para calcular la aptitud de un individuo, se leerá la cinta[0]y
                #en los lugares donde se encuentre un 1, se sumará al valor total de la cinta [3] y [4](peso y valor de la mochila)
                #los valores correspondientes.
                if(self.cinta[3].get() == 'P'):
                    self.cambiarEstado([None,None,None,(None,'R'),(None,'R')],'F')
                if(self.cinta[0].get() == 0):
                    self.cambiarEstado([(None,'R'),(None,'R'),(None,'R'),None,None],'Aptitud')
                if(self.cinta[0].get() == 1):
                    self.cambiarEstado([(None,'R'),(None,'R'),(None,'R'),(self.cinta[1].get(),'R'),(self.cinta[2].get(),'R')],'Aptitud')
                if(self.cinta[0].get() == 'F'):
                    self.cambiarEstado(None,'F')
                

                    

            case 'F':#estado final
                pass    
        
            case _:
                print("Error: estado no reconocido")











"""
Tape (cinta)
Cabezal (apuntador,simbolo a sobreescribir,izquierda-derecha-izquierda)
Registro de estados
Tabla de transiciones
La maquina de turing tiene las caracteristicas de un Automata finito
Q = Es un conjunto de estados
    Σ = Alfabeto conjunto de caracteres (codigo utf-8 ="\u03A3")
    Γ = Simbolos de la cinta
    s = Estado inicial sϵQ
    δ= Reglas nde transicion (Codigo utf-8 = "\u03B4")
    QxΣ->Q Reglas de transicion
    bϵΓ = es un simbolo denominado blanco, que se puede repetir infinitamente en toda la cinta
    F⊆Q Estado finales o de aceptacion

    Q = {s,q1}
    Σ = {a}
    Γ = {a,b}
    s = Estado inicial q0ϵQ
    δ= Reglas de transicion
    Reglas de transicion
    Q x Σ -> Q
    ((q0,a)->q1*)
    (estado, valor) -> nuevo estado, nuevo valor, dirección)
    (s,a)->q1,b,right
    (q1,b)->--Valido--
    "si estamos en el estado s leyendo la posición q1, donde hay
    escrito el símbolo 'a', entonces este símbolo debe ser reemplazado
    por el símbolo 'b', y pasar a leer la celda siguiente, a la derecha".
    F⊆Q = {q1}

    Estructura gafica es un grafo dirigido que se conecta en los vertices
    con:
        (lee el cabezal/
        símbolo que escribirá el cabezal,
        movimiento del cabezal.)
        (s,a)->q1,b,right
        ('a',b,right)

"""
