> Revisado 09/02/2024

#### ANALISIS:

Menu
1.CRUD campers
	1.Crear camper (Id, nombre, Apellidos, direccion, acudiente, telefonos(fijo y celular), estado)
	2.Buscar camper
		1.Listar campers
			1.Listar por estado
			2.Listar por identificador de ruta
		2.Buscar por id
	3.Actualizar camper(Preguntara por el id y vuelve a pedir los datos, al final mostrara el cambio)
	4.Eliminar camper(Preguntar id, preguntar si esta seguro, mostrar el camper eliminado)
2.CRUD trainers
	1.Crear trainer(Id, nombre, horario disponibles)
	2.Buscar trainer
		1.Listar todos los trainers (Mostrar todo el array de trainers)
		2.Buscar por ID (Preguntar id y filtrar)
	3.Actualizar trainer (Preguntar id, volver a pedir los datos y mostrar el cambio)
	4.Eliminar trainer(Preguntar id, reguntar si esta seguro, mostrar el camper eliminado)
3.Gestor de matriculas
	1. CRUD rutas
		1.Crear Ruta(Nombre, se le asigan automaticamente el comun core, se pregunta solo por BD Y Backend)
		2.Buscar Ruta
			1.Listar todas las rutas(Lista todo el array de rutas)
			2.Buscar ruta por nombre(Busca la ruta por nombre)
		3.Actualizar Ruta(Lista la ruta y devuelve la plantilla vacia para modificar, mostrar cambio)
		4.Eliminar Ruta(Preguntar nombre, mostrar, preguntas si sesta seguro, mostrar el registro eliminado)
	2.Gestion rutas
		1.CRUD grupos (Identificador, Salon, Trainer, Horario, Inicio, Finalizacion)
			1.Crear grupos 
					(1. Asignar salon 
					Asignar ruta  ---------> Esto tendra un id para identificar el salon con la ruta, el horario, el trainer demas para luego asignar facilmente los 
					Asignar trainer           campers
					Asignar horario
					Fecha inicio
					Fecha finalizacion)
			2.Buscar grupos
				1.Listar todos los grupos
				2.Buscar por identificador
				3.Buscar por identificador y mostrar campers registrados
			3.Editar grupo
				(Preguntar por identificador(Plantilla vacia, mostrar cambios))
			4.Eliminar grupo
				(Preguntar por identificador, preguntar si esta seguro, mostrar el eliminado)
		2.Asignar campers a los nodos
			1.Asignar camper (Preguntar por identificador, mostrar los datos, preguntar por id del camper,luego preguntar si desea asignar otro camper, sino cerrar, pendiente de que no pase de 33 cupos, contador)
			2.Cambiar a camper de grupo(Mostrar el registro, llenar plantilla, cambiar)
	3.Registro de prueba inicial
		(Preguntar por el id del estudiante, mostrar primero los estudiantes que no han presentado
		prueba inicial)
	4.Registro de notas
		(Preguntar por el identificador del salon
		Listar todos los estudiantes, Preguntar por el id del estudiante
		Preguntar por la nota a registrar
		Registrar nota, Listar al estudiante y confirmar)
4.Mostrar
	1.Listar campers inscritos
		(Mostrar estado "Inscrito"
	2.Listar campers que aprobaron el examen inicial, (Prueba inicial), "Aprobado"
	3.Listar trainers
	4.Listar estudiantes (con estadoaux "Bajo rendimiento")
	5.Listar campers y entrenadores (campers "Ruta", trainer "Ruta", o crear apartado en el array de nodos con estudiantes donde se guardaran todos los estudiantes(Mejor opcion)
	6.Listar campers perdieron y aprobados cada uno de los modulos a tener en cuenta la ruta y el entrenador(Mirar como hacer xd)

##### DATOS Y APUNTES A TENER EN CUENTA PARA LA REALIZACION DEL PROYECTO

Pre inscrito pasar primeras pruebas 

Estado: Pre inscrito, inscrito, aprobado, en riesgo, filtrado Inscrito despues de el quizis de fundamentos 

Artemis, Apolo, Sputnik (33) por cada Sala Apartado que seleccione la sala, segun el horario y se lo asigne al trainer (6-9) (10-12) (2-5) (6-9) 

Comun Core todos los temas que se ven sin importar al ruta, fundamentos programacion, programacion web, programacion formal, bases de datos todas para todos, Backend depende de la ruta, asignar modulo a las areas Inscrito a aprobado, asignacion de rutas  

Depende del horario del trainer se les asigna la ruta 

Para poder asignar el camper primero se asigna el trainer dentro del area y no colisionar en su sala de entrenamiento Info del trainer la misma que el camper 

El salon segun el horario se empieza a descontar, el punto 8 es la asigancion de datos  

Prueba teorica 30% y demas

##### LINK DEL PRIMER ESQUEMA DEL PROYECTO, ANTES DE LA REFACTORIZACION E INICIO DESDE 0, PARA REESTRUCTURACION DE LAS FUNCIONES Y EL MENU

A continuacion podra encontrar el link del esquema/primer intento, del proyecto, debido a complicaciones se decidio empezar desde 0 en un archivo nuevo, basandose en este:

https://github.com/JuanRivasfr/Pprimerfiltro