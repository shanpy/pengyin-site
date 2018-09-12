.. title: Use Amazon EC2 to Host IPython Notebook
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Data Science
.. tags: Amazon EC2, Python
.. slug: use-amazon-ec2-to-host-ipython-notebook
.. authors: Pengyin Shan
.. description: This post is trannsferred from my <a href="shanpy.github.io/techblog">old blog site</a>, about using Amazon EC2 to host IPython Notebook.

Recentely I read a great article about <a href="https://gist.github.com/iamatypeofwalrus/5183133">Hosting IPython Notebook on Amazon AWS Free Tier from Scratch</a>. This tutorial explains the way to host IPython Notebook using a Amazon EC2 Micro Instance.

I followed this tutorial and successfully hosted an IPython notebook on a Ubuntu 14 Guest AMI. I want to record some of important steps I took while following this tutorial:

Note: You can use **nano** to edit `ipython_notebook_config.py` file. It is located at `~/.ipython/profile_nbserver/`.

##Security Group

When you set up rules for *Security Groups*, make sure you include `SSH`, `HTTPS` and `8888` all of these. Lack of one can make your IPython Notebook fail. If you forget to do so when you set up the machine, you can set up later in your EC2 management console.

##Elastic Ip

The tutorial suggest you link an **Elastic IP** to your instance so that everytime you try to access your instance in browser, you can type new ip address instead of long public DNS.

To do this, click **Elastic IPs** option in you EC2 Dashboard menu, which is in **NETWORK & SECURITY** section. On right panel, click **Allocate New Address** button. Then click **Yes** in the pop-up window.

Now a IP address should be generated. Rememeber to *associate* your instance with this IP address. Select this IP address, then click **Associate Address** button. A pop-up window will appear. Click **Instance** then select your instance in drop-dowm menu. You can also do other setting here. Click **Associate** to associate your instance to this IP.

Now you just need to type: `https://your_elastic_ip:port_number` to your IPython Notebook.

##Make IPython Run as Service

You may want you IPython notebook still works after you shutdown your terminal/SSH. I got solution from this <a href="http://stackoverflow.com/questions/16418477/how-to-keep-server-running-on-ec2-after-ssh-is-terminated">StackOverflow post</a>. I got **screen** by typing `sudo apt-get install screen`, then do `ipython server &`.

If this not work for you, try `screen ipython s` instead