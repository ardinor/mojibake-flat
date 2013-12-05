title: Revisiting the auth.log
date: 2013-12-03 01:43:24
tags: SSH, fail2ban
category: IT
lang: en

After about a month since my last update let's check our logs and see how the slightly stricter security measures are holding up.

    Dec  2 11:28:43 defestri sshd[26001]: Invalid user administraator from 217.153.86.163
    Dec  2 11:28:43 defestri sshd[26003]: Invalid user administrador from 217.153.86.163
    Dec  2 11:28:44 defestri sshd[26005]: Invalid user administranto from 217.153.86.163
    Dec  2 11:28:44 defestri sshd[26007]: Invalid user administrate from 217.153.86.163
    Dec  2 11:28:45 defestri sshd[26009]: Invalid user administrateur from 217.153.86.163
    Dec  2 20:31:43 defestri sshd[26261]: Invalid user lukas from 198.61.179.140
    Dec  2 20:31:44 defestri sshd[26263]: Invalid user ottomar from 198.61.179.140
    Dec  2 20:31:45 defestri sshd[26265]: Invalid user pankraz from 198.61.179.140
    Dec  2 20:31:46 defestri sshd[26267]: Invalid user lucas from 198.61.179.140
    Dec  2 20:56:05 defestri sshd[27794]: Invalid user pomelnic from 184.106.189.106
    Dec  2 20:56:51 defestri sshd[27854]: Invalid user ram from 184.106.189.106
    Dec  2 20:56:52 defestri sshd[27856]: Invalid user jake from 184.106.189.106
    Dec  2 21:09:22 defestri sshd[27868]: Invalid user admin from 64.235.53.4

As we can see there's still plenty of log in attempts coming in, although slightly less than last time. We can see how fail2ban is going by having a quick look at it's log.

    2013-12-02 11:28:45,147 fail2ban.actions: WARNING [ssh] Ban 217.153.86.163
    2013-12-02 20:31:46,725 fail2ban.actions: WARNING [ssh] Ban 198.61.179.140
    2013-12-02 20:56:53,357 fail2ban.actions: WARNING [ssh] Ban 184.106.189.106

So we can see it has successfully banned the three IPs that have attempted to break in three or more times in the log.
