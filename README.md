Task API Endpoints
Endpoint	Method	Description	Request Body (JSON)	Success Response
/api/tasks/	GET	Get all tasks	-	200 OK (list of tasks)
/api/tasks/	POST	Create new task	{"text": "Task 1", "completed": false}	201 Created (new task)
/api/tasks/<id>/	GET	Get single task	-	200 OK (task details)
/api/tasks/<id>/	PUT	Full task update	{"text": "Updated", "completed": true}	200 OK (updated task)
/api/tasks/<id>/	PATCH	Partial update	{"completed": true}	200 OK (updated task)
/api/tasks/<id>/	DELETE	Remove task	-	204 No Content