from datetime import datetime
from airflow.decorators import dag, task

# In Airflow 3, standard operators like BashOperator are maintained in the standard provider package
try:
    from airflow.providers.standard.operators.bash import BashOperator
except ImportError:
    # Fallback if standard provider is not explicitly installed or for slightly older versions
    from airflow.operators.bash import BashOperator

@dag(
    dag_id="call_website_dag",
    schedule=None,
    start_date=datetime(2026, 3, 18),
    tags=["example:Operator", "BashOperator"],
)
def call_bashOperator_workflow():
    """
    Airflow 3.0 DAG to print a message and run a bash command calling a particular website.
    """

    @task.python
    def print_intro():
        # Prints the required message
        print("Hi lets open Anti Gravity Web Site")

    # Runs a bash command to call a website using curl
    # this directly call the functions that why in set dependency we dont have to use ()
    run_bash_website_call = BashOperator(
        task_id="call_website_using_bash",
        bash_command="curl -s -I https://antigravity.google/"
    )

    @task.bash
    def run_after_run_bash_website_call_function():
        """Also another way to call bash command using task decorator"""
        return "echo Hello , Zub3r Ahm3d"


    # Set dependency: print_intro runs before the bash command
    print_intro() >> run_bash_website_call >> run_after_run_bash_website_call_function()

# Instantiate the DAG
call_bashOperator_workflow()
