SELECT estudiante.name, materia.name 
from estudiante join materia on estudiante.id = materia.estudiante_id 
where estudiante.name = 'juan';


SELECT estudiante.name 
from estudiante
where id in 
    (SELECT estudiante_id 
        from materia
        where materia.name = 'programacion'
    );