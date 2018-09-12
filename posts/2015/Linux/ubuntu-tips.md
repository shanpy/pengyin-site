.. title: Ubuntu Tips
.. date: 2015-08-01
.. category: Linux
.. tags: Linux, Ubuntu
.. slug: ubuntu-tips
.. authors: Pengyin Shan
.. description: This posts will be continously updated, including useful tips I learned when using Ubuntu 14/15.

###JAVA_HOME Errors

When you final setting up `JAVA_HOME`, you are supposed to set its path in two different places:

1. `~/.bashrc`: You will see something like `export JAVA_HOME="/usr/lib/jvm/java-8-oracle"`. Note *there are double quote sign in path, and there is no space between JAVA_HOME and path.*

2. `/etc/environment` (Read Only): You will see something like `JAVA_HOME="/usr/lib/jvm/java-8-oracle". Note: *there is double quote for path, and there is no space between JAVA_HOME and path*.` This is a read-only file and you need to be admin if you want to modify it.

If your `JAVA_HOME` is not correctly set up, you may get following error in you Ubuntu:

####Cannot Update/Remove Software

You can find a official forum <a href="https://bugs.launchpad.net/ubuntu/+source/texinfo/+bug/993407">here</a>.

One of my application, `xpad`, cannot be removed because of this. When I run `sudo apt-get remove xpad`, a error message *install-info can fail to install due to syntax errors in /etc/environment* appears.

I check my `/etc/environment` file. It turns out I had extra spaces in my JAVA_HOME, which cause the problem.

Also, if your `software updater` in Ubuntu failed to download necessary packages, you may have a wrong setup of `JAVA_HOME`.

####Reminder in Terminal

When you open terminal, you may get some error message such as `bash: export: ``/usr/lib/jvm/java-8-oracle': not a valid identifier`. In this case, you need to check your ~/.bashrc file to make sure your JAVA_HOME format is correct.

>If you forget extact format of JAVA_HOME, you can open ~/.bashrc file using gedit, then following the format of other variables. You can varify by checking the color highlight of your JAVA_HOME line should be the same as all lines above.