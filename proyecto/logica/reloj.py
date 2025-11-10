
import datetime

class SimulationClock:

    def __init__(self, hora_inicio=6, minuto_inicio=0, segundo_inicio=0):
        #inicializa el reloj en una hora específico. Por defecto, la simulación empieza a las 06:00)
        self._fecha_base = datetime.date(2025, 1, 1)
        
   
        self.tiempo_actual = datetime.datetime.combine(
            self._fecha_base, 
            datetime.time(hora_inicio, minuto_inicio, segundo_inicio)
        )
        
        print(f" Reloj de simulación iniciado a las {self.get_hora_str()}")

    def avanzar_tiempo(self, segundos=0, minutos=0, horas=0):
        delta = datetime.timedelta(hours=horas, minutes=minutos, seconds=segundos)
        self.tiempo_actual += delta

    def get_hora_str(self, formato="%H:%M:%S"):
      #devuele hora actual de la simulación
        return self.tiempo_actual.strftime(formato)

    def get_tiempo_actual(self):
      
        #devuelve el objeto 'datetime' completo para comparaciones.
        return self.tiempo_actual

    def es_hora_especifica(self, hora, minuto, segundo=0):
     
        #comprueba si la hora actual es exactamente una hora específica.
       
        return self.tiempo_actual.time() == datetime.time(hora, minuto, segundo)
