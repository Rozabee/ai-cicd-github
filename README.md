<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Your First GitHub Actions AI workflow

**Project Link:** [View Project](http://nextwork.ai/projects/ai-cicd-github)

**Author:** Bea Baldonado  
**Email:** baldonado.beanicole1013@gmail.com

---

![Image](http://nextwork.ai/passionate_violet_adorable_toutouwai/uploads/ai-cicd-github_d2f6s4y1)

---

## Introducing Today's Project!

In this project, I'm going to build... test scripts using Python and its virtual enviroment. CI/CD is... means continouos integration and continous deployment/development. GitHub Actions helps me... to run the python tests. 



### Key tools and concepts

The key tools I used include Cursor, Github, Pytest, Python, Github Action Workflow, and Artifacts. 

Key concepts I learnt include 
>>Setting up the python virtual environment. 
>>Differences of Forking and cloning
>>CI/CD pipeline workflow using Github Actions. 
>>Automated tests using pytest. 
>>How the artifacts is important when other developers wants to run the test. 

### Challenges and wins

This project took me approximately 3days. 

The most challenging part was understanding the workflow of CI/CD and how to execute it tests. 

But with the help of step by step tutorial of nextwork.ai, it didnt feel like i was totally lost. 
I actually prefer to learn with this set up and that theres a ask feature whenever i have questions. 



### Why I did this project

I did this project to learn how to set up a Python virtual enviroment and how to automate tests. I learned alot with the CI/CD pipeline concept which i have been planning to learn. I didnt know that testing is a big part of the workflow. 

Another skill I want to learn is designing and creating a test environment automation to a simple application. Maybe for my next project, I'll make a simple calculator app and integrate a CI/CD pipeline test automation using Github Action! 

This project have helped me to learn more about python and its framework, pytest! This still helped me because it is aligned in the Software Automation QA Tester role path that i wanted to take.


---

## Setting Up the Python Environment

In this step, I'm setting up Python virtual env by installing its dependencies. This is important because we will use it for the testing scripts and to isolate the project dependencies from the other projects in the computer 

![Image](http://nextwork.ai/passionate_violet_adorable_toutouwai/uploads/ai-cicd-github_m5v9b3x7)

### Activating the virtual environment

I activated my venv by putting this in the terminal 
>> venv/Scripts/activate

The (venv) prompt means that the virtual enviroment is active.
You should see (venv) in the terminal. It indicates that it is active.

![Image](http://nextwork.ai/passionate_violet_adorable_toutouwai/uploads/ai-cicd-github_p2w8n4r6)

### Exploring the project structure

I found key files including the 
app.py >> contains functionalities like add(), is_even(), and reverse_string()
tests/ >> directoryy for the test files
requirement.txt >> lists all the project dependencies
pyproject.toml >> python project configuration
.github >> where the project will be located and where CI workflow will live.

The .github folder is for to commit the changes to Github account. 

---

## Writing and Testing a Python Function

In a Test-driven development, they write automated test codes before they actualy code what they will be testing. 

👉 Note: It follows a three-step loop: Red-Green-Refractor cycle.

In this step, I'm writing Python function with type hints. 
I will be using the popular Python test framework (PYTEST). This framework makes it easy to write simple yet powerful, tests. 
This runs a automated checks and helps developers make the work more reliable and efficient. 

Tests are important because we have to make sure that everything works before we give our prodcuts to the end users. 

A little analogy for it is, imagine you are going to fed a baby, warm milk. The mom would try to taste the milk and check if its too hot before giving it to the baby. Just like in developing the software products, we have to think our usesrs as a baby. 
Some users are non-technical people and that we have to make our software user-friendly so they use them with ease. 

![Image](http://nextwork.ai/passionate_violet_adorable_toutouwai/uploads/ai-cicd-github_q8j4m1h6)

### Creating the multiply function

For this example, I wrote a multiply function that get 2 int parameters and return an integer. 

Type hints help because it predicts the code function without you writing it. Its helpful when you get to reuse its function rather than manually writing it again.

Note: Remember to always validate the code. 

![Image](http://nextwork.ai/passionate_violet_adorable_toutouwai/uploads/ai-cicd-github_a6s2v5t8)

### Running and verifying tests

In runing the tests, make sure you are in a virtual env (venv). 
I made a mistake on running "pytest -v" when i wasnt in venv. 

To activate, just type this again on your terminal. 
>> venv\Scripts\activate

From there, I verified my tests by running "pytest -v" 
The output showed that the defined functions inside the test_app have PASSED. 
 

---

## Building a CI Pipeline with GitHub Actions

In this step, I'm creating Github Actions workflow file that runs of every push. 

To test this, i intentionally break the test and watch if the pipeline catches it. 

After that, we'll fix the test to verify the pipeline passes. 

CI helps because it automatically run the tests for you on every single push and catches bugs or broken codes immediately rather than slippring through to production. 


![Image](http://nextwork.ai/passionate_violet_adorable_toutouwai/uploads/ai-cicd-github_g1k5n9r3)

### Configuring the workflow

I configured the workflow to CI using Github Actions workflow.

The steps include having a on, to trigger workflow everytime theres a single push. Then to runs-on to the available platform of github which is Linux. Then put the steps and run the scripts automatically by Github. 

### Testing the pipeline

CI caught the bug when i added the ci.yml file under the github\workflows file and then i commited and uploaded the changes to my github repository. 

👉 to run the workflow, do this  command on the terminal. 
>> git add . 
>> git commit -m "Run test"
>> git push origin main 

After that, i go to my repository and checked my actions where my github actions workflow will be located. 

I intentionally made an error code to see if the workflow catches it. On the github, it show if the run test is passed or failed. 

The error will show on the github results and I fixed it by locating the error on the source code then compiling it again and do the command to commit the changes again. 

This shows CI helps because it automatically run the tests for you and get you a visualization directly on the github where the issue is located. CI is helpful in the development process so that testers and/or developers can catch the bugs quickly and already have a test result then immediately fix it. 

---

## Packaging Code with CI Artifacts

I'm adding a build step  to my CI pipeline so that my pytests file turns into installable package that a team or other people can download and use. 

Uploading my CI pipeline/workflow package as an artifact that can be downloadable packaged code from github.

![Image](http://nextwork.ai/passionate_violet_adorable_toutouwai/uploads/ai-cicd-github_n3m7k1w9)

### Adding build and upload steps

I added a build step that will turn my pytest file into a installable package.

Artifacts are useful because the developers in the team can install this package and install my python code on their own machine. 

![Image](http://nextwork.ai/passionate_violet_adorable_toutouwai/uploads/ai-cicd-github_s6p9c4v1)

### Downloading the packaged artifact

I downloaded my package from the github actions workflow after it successfully run. 

The CI artifacts will only run when added this code on ci.yml.

>>    - name: Build package
        run: python -m build

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: python-package
          path: dist/

When the tests are passed, this artifact is ready to be installed and can be automated for the next step which is deployment. The CD, continous deployment. This automates the deployment of a validated code after the successful tests and it will be ready to the end-user or for the production. . 

This means my CI pipeline now can be shared among other developers. This helps for us developers and tester when deploying. They will install this package and test it on their own computer, eliminating its, "it works on my computer." narrative when testing. 




---

---
