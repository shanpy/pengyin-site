.. title: Setting up RoR/Hydra Environment - Problems and Solutions
.. date: 2015-08-12
.. category: Web Development Tips
.. tags: Linux, Ubuntu, Ruby on Rails, Hydra
.. slug: setting-up-ror-hydra-environment-problems-and-solutions
.. authors: Pengyin Shan
.. description: Recently I tried to install Ruby on Rails/Hydra development environment in different machine, and I got some interesting problems. I want to post solutions in this blog for future usage.

##Ubuntu 15.10

If you want to setup your RoR environment on Ubuntu 14/15, <a href="https://gorails.com/setup/ubuntu/15.04">this post</a> is the best choice for you. I used `rvm` to install Ruby on my two Ubuntu 15.10 machine, and it worked like a charm.

###Problem

When I tried to run `\curl -L https://get.rvm.io | bash -s stable --ruby` in terminal to install both RVM and Ruby, I got following error message:

	:::command
	Error running 'requirements_debian_update_system ruby-2.2.1',
	showing last 15 lines of /usr/local/rvm/log/1439385591_ruby-2.2.1/update_system.log
	++ /scripts/functions/logging : rvm_pretty_print()  78 > case "${TERM:-dumb}" in
	++ /scripts/functions/logging : rvm_pretty_print()  81 > case "$1" in
	++ /scripts/functions/logging : rvm_pretty_print()  83 > [[ -t 2 ]]
	++ /scripts/functions/logging : rvm_pretty_print()  83 > return 1
	++ /scripts/functions/logging : rvm_error()  117 > printf %b 'There has been error while updating '\''apt-get'\'', please give it some time and try again later.
	404 errors should be fixed for rvm to proceed. Check your sources configured in:
	    /etc/apt/sources.list
	    /etc/apt/sources.list.d/*.list
	\n'
	There has been error while updating 'apt-get', please give it some time and try again later.
	404 errors should be fixed for rvm to proceed. Check your sources configured in:
	    /etc/apt/sources.list
	    /etc/apt/sources.list.d/*.list
	++ /scripts/functions/requirements/ubuntu : requirements_debian_update_system()  53 > return 100
	Requirements installation failed with status: 100.

The reason of this error is because RVM will bring error if my Ubuntu machine's `apt-get update` has error in it. I used to install Ninja-IDE through `apt-get` and I had PPA error when I do `apt-get update`. You can view <a href="http://stackoverflow.com/questions/23650992/ruby-rvm-apt-get-update-error">this stackoverflow post</a>.

###Solution

A user **Avinash Raj** posted a great solution in <a href="http://askubuntu.com/questions/65911/how-can-i-fix-a-404-error-when-using-a-ppa-or-updating-my-package-lists">Ubuntu community</a> for removing PPA with errors.

The detail of solution is: create a file called `ppa-remove` (no `.sh` extension) as following:

    :::Bash shell scripts
    #!/bin/bash
    sudo rm /tmp/update.txt; tput setaf 6; echo "Initializing.. Please Wait"
    sudo apt-get update >> /tmp/update.txt 2>&1; awk '( /W:/ && /launchpad/ && /404/ ) { print substr($5,26) }' /tmp/update.txt > /tmp/awk.txt; awk -F '/' '{ print $1"/"$2 }' /tmp/awk.txt > /tmp/awk1.txt; sort -u /tmp/awk1.txt > /tmp/awk2.txt
    tput sgr0
    if [ -s /tmp/awk2.txt ]
    then
      tput setaf 1
      printf "PPA's going to be removed\n%s\n" "$(cat /tmp/awk2.txt)"
      tput sgr0
      while read -r line; do echo "sudo add-apt-repository -r ppa:$line"; done < /tmp/awk2.txt > out
      bash out
    else
      tput setaf 1
      echo "No PPA's to be removed"
      tput sgr0
    fi

Run `sudo chmod +x ppa-remove` after you create this file, then move this file to `/usr/bin`. Run `sudo ppa-remove`. Your PPA with errors will be removed and you can then re-run `\curl -L https://get.rvm.io | bash -s stable` or `\curl -L https://get.rvm.io | bash -s stable --ruby` to install RVM.

*Note: Till Aug 2015, If you run `\curl -L https://get.rvm.io | bash -s stable --ruby`, you will automatically get Ruby 2.2.1 installed. If you run `\curl -L https://get.rvm.io | bash -s stable` then install Ruby, you can choose Ruby 2.2.2. These two versions do not have conflict.*

##Mac OS Yoemite

RoR installation process for Mac OS Yosemite is almost the same as Ubuntu. Make sure you have `xcode` and `Homebrew` installed first. This <a href="http://railsapps.github.io/installrubyonrails-mac.html">post</a> has very detailed description that you can follow.

##Project Hydra

I had a <a href="http://pengyin-shan.com/blog/dive-into-hydra-and-my-thoughts">post</a> describing my thoughts about Hydra. In this post I will include detail of installation part.

After you finish RoR setting (make sure you have `Bundle` installed by `RubyGem`), you want to generate a basic rails app, then add `gem 'hydra', '9.1.0.rc1'` to your `Gemfile`. you can re-run `Bundle install` to install all necessary ruby gems for Hydra.

>If you are creating Hydra head for the first time, run `rails generate hydra:install` to use Hydra generator. If you done this once and you want to setup this project in a new machine, you should skip this step because your old blacklight files will be overwritten.

You can use same Gemfile to set up Hydra environment in different machines, but **make sure you run `rake jetty:config` and `rake db:migrate`** to prevent possible problem.

You can run `Rails.env` in rails console to check your current environment.

###Problem: Data Immigration for Existing Project

How to transfer previous data (Fedora files, Solr documents and indexes) to your new environment?

###Solution

Well, I'm working on solution now :) To figure out a way I did lots of experiments (and made a big mess) in my Hydra project. I started a new post about it <a href="http://pengyin-shan.com/blog/play-with-hydra-data">here</a>.