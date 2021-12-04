
class cinta():
    def __init__(self) -> None:
        posicion = 0
        lista = []





class maquinaDeTuring():
    def __init__(self):
        self.cinta = cinta
        self.cintaFitness = cinta
        self.cintaCruce = cinta
        self.posicion = 0
        self.estado = 0
        self.memoria = 0
        self. probCruce = 0.5
        self.probMutacion = 0.1

    def iniciarCinta(self,cinta):
        self.cinta = cinta
    
    def leerCinta(self):
        return self.cinta[self.posicion]
    
    def escribirCinta(self,valor):
        self.cinta.lista[self.cinta.posicion] = valor

    def ejecutar(self):
        while self.estado != 'F':
            self.estadosDeTransicion()
            self.mostrarCinta()
            print("Estado: ",self.estado)
            print("Posición: ",self.posicion)
            print("Memoria: ",self.memoria)
            print("\n")

    def cambiarEstado(self,stateChange):
        #stateChange =(ValorAEscribir, Direccion, Estado, valorAEscribirEnMemoria)
        if (stateChange[3] != None):
            self.memoria = stateChange[3]
        if(stateChange[0] != None):
            self.escribirCinta(stateChange[0])
        self.posicion += stateChange[1]
        self.estado = stateChange[2]

    def mostrarCinta(self):
        print({self.cinta})
    
    def cruce(self,padre1,padre2):
        """tomando dos números de la cinta (uno en self.memoria y otro en la posición de la cinta)
        y cruzando ambos, se obtiene un hijo que será el valor promedio de los dos números"""
        if random.random() < self.probCruce:
            hijo = (padre1.memoria + padre2.memoria)/2
            return hijo
        else:
            return self.memoria
        
  
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
            case 0:
                esNumero = isinstance(self.leerCinta(),float)
                match esNumero:
                    case True:
                        #si lee un número, esa posición en la cinta tiene un individuo
                        pass


                    case False:
                        #si lee una letra, esa posición en la cinta tiene un caracter especial
                        pass

            case 1:#usamos este estado y el estado 2 para hacer un bubble sort de la cinta
                esNumero = isinstance(self.leerCinta(),float)
                match esNumero:
                    case True:
                        if(self.leerCinta() > self.memoria):
                            self.cambiarEstado((None,-1,2,self.leerCinta()))
                        else:
                            self.cambiarEstado((None,1,1,self.leerCinta()))
                    case False:
                        if(self.leerCinta() == 'F'):
                            self.cambiarEstado((None,1,3,None))

            case 2:
                esNumero = isinstance(self.leerCinta(),float)
                match esNumero:
                    case True:
                        self.cambiarEstado((self.memoria,1,1,None))

            
            case 3:#el caso 3 moverá la cinta a la izquierda hasta que encuentre un símbolo
                esNumero = isinstance(self.leerCinta(),float)
                match esNumero:
                    case True:
                        self.cambiarEstado((None,-1,3,None))
                    
                    case False:
                        self.cambiarEstado((None,1,0,None))
                    
            case 'F':
                pass

            #para realizar el cruce entre individuos, se combinarán dos individuos al azar y se almacenará el resultado
            #en el lado derecho de la cinta, después del caracter F
            case 'C':
                self.cambiarEstado((self.cruce(self.cinta[0],self.cinta[1]),1,0,None))



            case _:
                print("Error: estado no reconocido")


class individuo:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = None
        self.state = 0
    


