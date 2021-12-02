class maquinaDeTuring():
    def __init__(self):
        self.cinta = []
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
        self.cinta[self.posicion] = valor

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
    #cinta ejemplo: [P,n,n,n,n,n,F]


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
    






"""
class Tape(object):
    
    blank_symbol = " "
    
    def __init__(self,
                 tape_string = ""):
        self.__tape = dict((enumerate(tape_string)))
        # last line is equivalent to the following three lines:
        #self.__tape = {}
        #for i in range(len(tape_string)):
        #    self.__tape[i] = input[i]
        
    def __str__(self):
        s = ""
        min_used_index = min(self.__tape.keys()) 
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.__tape[i]
        return s    
   
    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char 

        
class TuringMachine(object):
    
    def __init__(self, 
                 tape = "", 
                 blank_symbol = " ",
                 initial_state = "",
                 final_states = None,
                 transition_function = None):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)
        
    def get_tape(self): 
        return str(self.__tape)
    
    def step(self):
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == "R":
                self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            self.__current_state = y[0]

    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False

"""

