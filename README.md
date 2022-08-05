
# QA Study Group

This is the repository where we are going to practice our coding skills.

On this repository we will not have an specific project, but a collection of exercises to practice Python and the Git and Github flow.

In order to clone this repository, click on CODE on the top, copy the HTTPS url.

On your terminal, navigate to the folder of your preference and use the following command line:

`$ git clone https://github.com/lucas-gab/qa-study-group.git`

This will clone this repository to your computer!

# Creating a new branch and navigating branches

Notice that when you clone the repository, the branch you are in is the `main` branch.

It's better to create your own branch, where you can make changes and push them to be reviewed and later be pushed to the repository, reviewed and merged into `main`.

In order to create your own branch, use the following command line on your terminal:

`$ git checkout -b BRANCH-NAME`

(`BRANCH-NAME` should be replaced by the name you would like your branch to have)

In order to navigate back to `main` you can use:

`$ git checkout main`

The same will work to navigate back to your branch. Since it has already been crated with the -b on the first command line, now we can navigate to it by only using `git checkout`

`$ git checkout BRANCH-NAME`

# Saving, adding changes to staging area and commiting changes

When you make changes to scripts you will locally save your files as the changes happen. `Cmmnd + S` will usually do the trick.

However, only saving the file is not enough. We will need to commit those changes before pushing them to the repository.

And before we start (it will sound obvious, but it is important to point out) - only commit code that works. If your code is broken or flaky and need something to fix, let's fix it first, and then commit it.

But first, we need to add our changes to the staging area. Basically, we are telling git what changes we would like to commit.

In order to add all changes, run the command line:

`$ git add .`

(The `.` on that command line refers to ALL CHANGES. You can specify the change you would like to commit, but it is very common that we would like to commit all the changes we have made so far)

Now all your changes are on the staging area, ready to be commited.

In order to commit your changes, we will need to enter a message (which will require the usage of `-m 'this is my message'` on the command line). The message is mandatory and should have a short description of what you are commiting.

`$ git commit -m 'This is my git commit message'`

Now your code is commited and ready to be pushed!

# Pushing your code to the repository

Now our code is saved, was added to the staging area and commited. Let's push it to the repository.

On your command line, use the following command line:

`$ git push origin BRANCH-NAME`

(Here, the `origin` part of the command line refers to the remote repository on GitHub. Since this repository was cloned from GitHub, the `origin` repository is already refering to this one by default. If we start a project from scratch locally on our computer, we would have to define the remote repository by using `git remote`)

Remember we have created a new branch for your code. That's where it becomes useful. Now that we have pushed the changes to the repository, they have been pushed to your new branch. 

If we had pushed the code directly into `main`, it would change our main repository directly and would not provide a chance for our peers to review our code and help us improve it or fix errors we haven't noticed.

But now your code and the main code is separated and we need to request our code to be pulled into main. So let's create a Pull Request (PR).

You should see a banner on top of the <Code> area of the repository stating that new changes were pushed into a new branch. Click on Create a Pull Request.

On the Pull Request, write a description of what you changes do. Good descriptions will help your peers on how to review your code.

Since our `main` branch is protected, you will be required to have at least 2 reviews from your peers before merging your PR.

# Updating your local main

Okay, now you have made your changes and so have your peers and you would like to have an updated `main` on your computer. All you have to do is:

`$ git pull origin main`

This will pull all the code from the main branch into your computer.

You can, of course, pull all of the changes from any other branch that were pushed to the repository into your local environment.

Same command, only changing `main` by the specific branch name

`$ git pull origin BRANCH-NAME`
