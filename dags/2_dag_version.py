from airflow.sdk import dag , task

@dag(
    dag_id = "dag_version"
)

def dag_version():

    @task.python
    def first_task():
        print("This is the first dag")

    @task.python
    def second_task():
        print("This is the second dag")

    @task.python
    def third_task():
        print("This is the third dag")

    @task.python
    def final_task():
        print("This if Final Tas to be executed")    
    

    # defining dag dependencies 
    first = first_task()
    second = second_task()
    third = third_task()
    final = final_task()


    first >> second >> third >> final


# Instanciating the dag
dag_version()