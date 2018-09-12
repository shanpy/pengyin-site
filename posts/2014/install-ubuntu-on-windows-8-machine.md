.. title: Install Ubuntu 14 on External Drive from Windows8 Machine with Node.js, Hexo and Jekyll
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Linux
.. tags: Linux, Operating System
.. slug: install-ubuntu-on-windows-8-machine
.. authors: Pengyin Shan
.. description: This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on late 2014. This post descibed my express of installing Ubuntu 14 on a Window 8 machine, then configuring Node.js, Hexo, Jekyll and Java development environment on it.

Yesterday, I was thinking of changing my window 8.1 laptop to a dual boot Liunx PC. After checking out my laptop configuration, I felt it may not be a good idea because since my laptop only has 100GB storage in total. After giving windows 8.1 at least 60G, new system can not get enough space. So I decided to install linux system on a 300G external drive, and let laptop boot from this hard drive when I start it.

I followed this article <a href="http://www.everydaylinuxuser.com/2014/05/install-ubuntu-1404-alongside-windows.html">Install Ubuntu 14.04 alongside Windows 8.1 in 10 easy steps</a>, posted by *Gary Newell*, and had no big trouble in process. However, I want to write this post to record some tips during installation process and configuration for Node.js, Hexo and Jekyll after installation.

#Installation Process

##Step 1

First you need to backup your windows 8.1. Windows requires you using at least *16GB* usb for backup. You just need to type "recovery" in start window and Windows will find "Recovery Drive" program for you.

> Please note during recovery process, the focus on your screen is set to the "cancel" button by default. So if you accidently hid Enter, the recovery process will be cancelled. I learned this becuase my cat step over Enter button twice during this process :-(

You have a choice to free recovery partition after back-up finishing.

You may also want to back-up your personal file to a save place

##Step 2

Create Linux Boot USB. Normally a 4GB usb is fine. I use <a href="http://www.linuxliveusb.com/">LinuxLive USB Creator</a>, which is free and very powerful.

##Step 3

Shrink windows parition if you want to install Linux locally.

>Please note you may not be able to shrink C drive a lot using Disk Management on Windows 8.1 when Window is active.

I searched on Google and downloaded <a href="http://www.partitionwizard.com/">Partition Wizard</a> to shrink C drive. There is a free "Home Edition" and a demo "Professional Edition". Home edition can not merge partitions.

You may want to format your Linux drive to *NTFS* format. But when I installed Ubuntu 14 I was give a chance to re-format it to `Ext4` format, so I don't think it is necessary.

##Step 4

You need to turn off your `fast-boot` and `secure boot`.

To turn off your fast boot, go to `control panel` -> `power options` -> `Choose what the power button does`. In the new window, expand `Shutdown Settings` then uncheck `Turn on fast startup (recommanded)`.

To turn off secure boot, you need to first hold `shift` button, then restart while holding `shift`. You will be lead to a blue screen with a button called `Troubleshoot`. Click this button and choose `Advanced Options`, then select `UEFI Firmeware Settings`. Click `resart` button on this page, and your pc will restart and go to BIOS setting.

BIOS may looks differently for different PC. In my dell XPS 12, you can move to Boot menu in BIOS setting, then you can disable secure boot. In the next few step you will setup boot priority from here also. Make sure you click `F10` to save setting and restart your pc.

##Step 5

Insert your Linux live USB to your pc. If you want to install Linux on a external drive, insert your external drive also. Start your pc. Re-start pc with `shift` key to enter the blue setup scrren in step 4. This time click "Use a device" button, and select the name of your Linux live USB

##Step 6

Now your pc should run the Linux system from Live USB. Installation process is different between different systems.

If you want to install Ubuntu on *external drive or select internal drive*, make sure you choose **something else** in installation manager.

>Special for Ubuntu 14: the installation manager will give you a change to choose the drive you want to install to. Usually the internal drive is `sda` and external drive is `sdb`. The empty drive that you want to install should under one of these two type. *You should format this drive to ext4 format and assign* `/` *as the mount*. If you don't choose `/`, Ubuntu will report a `root not found` error. You can format certain drive by clicking `change` button.

You may choose to set a small *swap* driver based on Ubuntu's recommandation.

You just need to format this drive to `linux-swap`.

##Step 7

After finish installation, make sure you adjust BIOS boot priority. `USB storage` should be have highest priority

#Configuration Process: Ubuntu14/Linux Mint Cinam Example

##Node.js & Hexo & Heroku & Github

Install Node.js: `sudo apt-get install nodejs`

Install npm: `sudo apt-get install npm`

Check version: `nodejs -v` | `npm -v`

Install Hexo: `sudo npm install hexo -g`

Install Git: `sudo apt-get install git`

You can download `Heroku Toolbel` from Heroku website and install it.

Clone proejct from Heroku (Please check Heroku website if you need to create project): `heroku git:clone -a app_name`

Get into your project folder and do `sudo npm install`. *You may encounter error message for node-sass: node not found. Solution is to do* `sudo apt-get install nodejs-legacy`.

Now you can test Hexo. Get into project folder and try `hexo clean`, `hexo generate` and `hexo server`. They should all works fine.

To re-add Github `origin master` branch, do `git remote add origin your_git_repo_address.git`. Please refer Github website if you want to create a new repository.

You can check your existing git remote for current folder by doing `git remove -v`.

##Ruby & Jekyll

Install rvm: `sudo apt-get install curl` -> `\curl -L https://get.rvm.io | bash -s stable`. *Please check the message in terminal after this process. You may need to download signature*.

Read message in terminal and run `source /home/pshan/.rvm/scripts/rvm`

Install necessary dependencies: `rvm requirements`

Install Ruby: `rvm install ruby`

Use Ruby: `rvm use ruby --default`

Use RubyGem: `rvm rubygems current`

Install Jekyll: `gem install jekyll`

##Java JDK & Eclipse

Download JDK file from Oracle's website

`cd /usr/local`

`sudo tax xzf Path_to_JDK_File`

`export JAVA_HOME=/usr/local/jdk1._x.0xx`

`export PATH=$PATH:$JAV_HOME/bin`

Dowload `Eclipse` from Oracle wbesite and Extract folder

You may want to choose `window`->`preference` to change your default JRE path to your preferred JDK. Ubuntu or LinuxMint use OpenJDK as defautl JDK

To add server support, First download and extract tomact from Apache website. Then select `File` -> `New` -> `Server`, choose tomcat server in list. You can configure tomcat here.

##Reference: My List of Necessary Apps on Ubuntu

`Okular`: pdf annotation

`Chrome` | `Firefox`

`Dropbox`

`Sublime Text`: Only Sublime Text *3* has `.deb` version

`MySQL Server` & `MySQL Workbench`: can be installed by `apt-get`