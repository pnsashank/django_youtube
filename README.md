# django_youtube

'youtube_api' application of this project hosts the url to fetch results from the Youtube Data v3 API and presents in json formatted output that includes pagination.

The database used here is sqlite3. The data that is fetched from the API is passed into the database named 'Latest_results' which contains the four fields: video_title, description, date_published, channel_title.

The youtube v3 api is fetched asynchronously through the use of tasks.py which uses 'background_task' library from django to achieve this. 'background_task' runs only when written in a separate program called tasks.py. Hence the use of tasks.py. Inorder to populate the database in background asynchronously run 'python3 manage.py process_task' under the outer django_api directoy.

django_api-->'python3 manage.py process_task'(in a new command prompt), can exit the by pressing 'Ctrl+C', which kills the process.

The other reason to use this is that django is a sychronous web-framework, mainly used for synchronous web applications. The use of Celery was considered, but due to the complexities arising from the use of message brokers(rabbitmq,redis etc) to communicate with Celery workers, not necessary for this simple application, hence the use of background_task library of django.

In order to run the 'youtube_api' application to view the paginated responses, in order of the response that are published at the latest, run 'python3 manage.py runserver' under the outer django_api directory.

django_api-->'python3 manage.py runserver',  can exit the by pressing 'Ctrl+C', which kills the process.

Serializers are used in the rest framework to convert the data from the database( which in this case is 'Latest_results'), to JSON formatted output.

The Pagination of the output json formatted data can be viewed in the 'settings.py' of the inner django_api directory under REST_FRAMEWORK, with page_size equal to '3'. Can be set to a desired number, which indicates the number of responses in each page.
